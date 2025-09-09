import streamlit as st
import google.generativeai as genai
import json
import os
import shutil
from dotenv import load_dotenv
import numpy as np
import time
from pydub import AudioSegment
from streamlit_option_menu import option_menu
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase
import av
from datetime import datetime

# Import custom utility functions from other files
from ui_utils import local_css
from gemini_utils import generate_medical_script, transcribe_audio_only, extract_prescription_from_text
from diff_utils import generate_diff_html
from audio_utils import add_noise_to_audio
from cloudinary_utils import upload_audio_to_cloudinary
from mongodb_utils import upload_prescription_to_mongodb

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
# Set up the basic configuration for the Streamlit page.
st.set_page_config(
    page_title="Medoc Voice",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# API AND ENVIRONMENT VARIABLE SETUP
# -----------------------------------------------------------------------------
# Try to load API keys from Streamlit's secret management first (for deployment).
try:
    GEMINI_API_KEY = st.secrets["GOOGLE_API_KEY"]
    MONGO_URI = st.secrets["MONGO_URI"]
    CLOUDINARY_URL = st.secrets["CLOUDINARY_URL"]
# If Streamlit secrets are not found, fall back to a local .env file (for development).
except (KeyError, FileNotFoundError):
    from dotenv import load_dotenv
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    MONGO_URI = os.getenv("MONGO_URI")
    CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

# Configure the Gemini API and set a flag to indicate its availability.
GEMINI_AVAILABLE = False
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        GEMINI_AVAILABLE = True
    except Exception as e:
        st.error(f"Failed to configure Gemini API: {e}")
else:
    st.error("Google API Key not found. Please set it in Streamlit secrets or a local .env file.")


# -----------------------------------------------------------------------------
# STYLING
# -----------------------------------------------------------------------------
# Apply local CSS for custom styling.
local_css()

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION AND FEEDBACK FORM
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("🩺 Medoc Voice")
    st.info("Your data is being stored for improving the application")
    
    # Create the main navigation menu.
    selected = option_menu(
        menu_title=None,
        options=["Home", "Transcription", "Settings"],
        icons=["house", "mic", "gear"],
        menu_icon="cast",
        default_index=1,
    )
    
    st.divider()

    # Create a feedback form in the sidebar.
    with st.form("Feedback_form"):
        st.subheader("Feedback")
        feedback_rating = st.selectbox(
            "Rate your experience:",
            ["", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
            label_visibility="collapsed",
            placeholder="Rate your experience",
        )
        feedback_text = st.text_area("Your feedback:", placeholder="Tell us what you think...", key="feedback_text_area")
        submitted = st.form_submit_button("Submit")
        
        # Handle feedback form submission.
        if submitted:
            if feedback_rating and feedback_text:
                st.success("Thank you for your feedback!")
                time.sleep(2) # Display success message briefly.
            else:
                st.warning("Please fill out both fields.")


# -----------------------------------------------------------------------------
# MAIN PAGE CONTENT
# -----------------------------------------------------------------------------
# Display content based on the sidebar navigation selection.
if selected == "Transcription":
    st.header("✨ Audio to Prescription Transcription")

    # --- Initialize Session State Variables ---
    # These variables persist across reruns to maintain the app's state.
    if "recorder_key" not in st.session_state:
        st.session_state.recorder_key = 0
    if "mic_active" not in st.session_state:
        st.session_state.mic_active = False
    if "prev_webrtc_state_playing" not in st.session_state:
        st.session_state.prev_webrtc_state_playing = False

    # --- User Input Options ---
    # Create two columns for user selections.
    col_a, col_b = st.columns(2)
    with col_a:
        is_healhcare_industry = st.radio("Related to Healthcare Industry?", ["Yes", "No"], key="is_healthcare", horizontal=True)
    with col_b:
        dictation_type = st.radio(
            "Select Dictation Type",
            ["Doctor Dictation", "Doctor-Patient Conversation"],
            key="dictation_type_selection",
            horizontal=True,
        )
    st.markdown("---")

    # --- Main Layout: Script and Recorder Columns ---
    script_col, recorder_col = st.columns(2)

    # --- SCRIPT COLUMN: For generating and displaying a medical script ---
    with script_col:
        st.markdown("### 📜 Script")
        st.markdown("Generate a script to read, then record it in the panel on the right.")
        
        # Button to generate a new script using the Gemini API.
        if st.button("Generate New Dictation Script", use_container_width=True):
            if GEMINI_AVAILABLE:
                # Call the function to generate script and store it in session state.
                st.session_state.script = generate_medical_script(st.session_state.dictation_type_selection)
                st.session_state.script_json=extract_prescription_from_text(st.session_state.script)
            else:
                st.error("Gemini API is not available to generate a script.")

        # Display the generated script in a disabled text area if it exists.
        if "script" in st.session_state:
            st.text_area(
                "Your Script",
                value=st.session_state.script,
                height=300,
                disabled=True,
                key="script_display_box",
            )

    # --- RECORDER COLUMN: Handles live audio recording ---
    with recorder_col:
        st.markdown("### 🎙️ Record Live Audio")
        st.markdown("Click 'Start' to begin recording. Click 'Stop' when finished.")
        webrtc_ctx = None # Initialize context for the WebRTC component.

        # If microphone is not active, show a button to open it.
        if not st.session_state.mic_active:
            if st.button("🎙️ Open Microphone to Record", use_container_width=True):
                # --- Cleanup logic for starting a new recording ---
                record_dir = "temp_recordings"
                recorded_audio_path = os.path.join(record_dir, "recording.wav")
                noisy_recording_path = os.path.join(record_dir, "noisy_recording.wav")

                # Remove any leftover audio files from previous sessions.
                if os.path.exists(recorded_audio_path):
                    os.remove(recorded_audio_path)
                if os.path.exists(noisy_recording_path):
                    os.remove(noisy_recording_path)
                
                # Clear all relevant state variables to ensure a fresh start.
                keys_to_clear = ["transcription", "result", "cloudinary_url", "cloudinary_public_id", "upload_complete", "needs_transcription", "needs_prescription_generation"]
                for key in keys_to_clear:
                    st.session_state.pop(key, None)

                # Set mic to active and rerun the app to show the recorder.
                st.session_state.mic_active = True
                st.rerun()
        
        # If microphone is active, display the WebRTC streamer component.
        else:
            record_dir = "temp_recordings"
            if not os.path.exists(record_dir):
                os.makedirs(record_dir)

            # Define a class to process audio frames from the WebRTC component.
            class AudioRecorder(AudioProcessorBase):
                def __init__(self) -> None:
                    self.frames_buffer = []
                    self.recording_path = os.path.join(record_dir, "recording.wav")
                    self.sample_rate = None
                    self.channels = None

                # This method receives audio frames from the browser.
                def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
                    if self.sample_rate is None: self.sample_rate = frame.sample_rate
                    if self.channels is None: self.channels = len(frame.layout.channels)
                    self.frames_buffer.append(frame.to_ndarray())
                    return frame

                # This method is called when the recording is stopped.
                def on_ended(self):
                    if not self.frames_buffer or self.sample_rate is None: return
                    # Concatenate all audio frames into a single NumPy array.
                    sound = np.concatenate(self.frames_buffer, axis=1)
                    # Convert the NumPy array to a Pydub AudioSegment.
                    audio_segment = AudioSegment(
                        data=sound.tobytes(),
                        sample_width=sound.dtype.itemsize,
                        frame_rate=self.sample_rate,
                        channels=self.channels,
                    )
                    # Ensure audio is mono.
                    if audio_segment.channels > 1:
                        audio_segment = audio_segment.set_channels(1)
                    # Export the final audio to a .wav file.
                    audio_segment.export(self.recording_path, format="wav")
                    # Clear buffers for the next recording.
                    self.frames_buffer.clear()
                    self.sample_rate = None
                    self.channels = None

            # Instantiate the WebRTC streamer UI component.
            webrtc_ctx = webrtc_streamer(
                key=f"audio-recorder-{st.session_state.recorder_key}",
                mode=WebRtcMode.SENDONLY,
                audio_processor_factory=AudioRecorder,
                media_stream_constraints={
                    "video": False,
                    "audio": {"echoCancellation": True, "noiseSuppression": True, "autoGainControl": True},
                },
            )

            # --- Detect when recording stops ---
            # Check if the recording state changed from playing to not playing.
            just_stopped = st.session_state.prev_webrtc_state_playing and webrtc_ctx and not webrtc_ctx.state.playing
            if webrtc_ctx:
                st.session_state.prev_webrtc_state_playing = webrtc_ctx.state.playing
            if just_stopped:
                time.sleep(0.5) # Wait briefly for the file to be written.
                st.rerun() # Rerun to process the saved audio file.

    # --- REVIEW RECORDING SECTION: Displayed after a recording is finished ---
    record_dir = "temp_recordings"
    recorded_audio_path = os.path.join(record_dir, "recording.wav")
    
    # This block executes only after the recorder has stopped and the .wav file exists.
    if webrtc_ctx and not webrtc_ctx.state.playing and os.path.exists(recorded_audio_path):
        with recorder_col:
            st.divider()
            st.subheader("Review Your Recording")
            st.audio(recorded_audio_path)

            # --- Automatic Upload and Processing ---
            # This logic runs only once per recording to prevent re-uploads.
            if 'upload_complete' not in st.session_state:
                final_recording_path = recorded_audio_path
                noisy_recording_path = os.path.join(record_dir, "noisy_recording.wav")
                
                # <<< FIX START: LIVE RECORDING >>>
                # Attempt to create a noisy version of the recording.
                add_noise_to_audio(recorded_audio_path, noisy_recording_path)

                # Check if the noisy file was successfully created and use it for the upload if it exists.
                if os.path.exists(noisy_recording_path):
                    final_recording_path = noisy_recording_path
                # <<< FIX END: LIVE RECORDING >>>

                with st.spinner("Uploading audio..."):
                    # Generate a unique filename for Cloudinary using a timestamp.
                    unique_filename = f"live_recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    result = upload_audio_to_cloudinary(final_recording_path, public_id=unique_filename)
                
                # If upload is successful, store URLs and set flags for the next steps.
                if "url" in result:
                    st.session_state.cloudinary_url = result["url"]
                    st.session_state.cloudinary_public_id = result["public_id"]
                    st.session_state.upload_complete = True # Flag to prevent re-upload.
                    st.session_state.needs_transcription = True # Flag to trigger auto-transcription.
                    st.rerun() # Rerun to trigger the transcription process.
                else:
                    st.error(result.get("error", "Upload failed"))
            
            # --- Display Processed Audio and URL ---
            noisy_recording_path = os.path.join(record_dir, "noisy_recording.wav")
            if os.path.exists(noisy_recording_path):
                st.write("Noisy Version:")
                st.audio(noisy_recording_path)
            # if 'cloudinary_url' in st.session_state:
            #     st.write("Cloudinary URL:", st.session_state.cloudinary_url)
            
            # --- Auto-Transcription Logic ---
            # This block runs if the `needs_transcription` flag is set.
            if st.session_state.get("needs_transcription"):
                with st.spinner("Auto-transcribing audio..."):
                    if GEMINI_AVAILABLE:
                        # Prioritize the noisy version for transcription if it exists.
                        noisy_path = os.path.join(record_dir, "noisy_recording.wav")
                        clean_path = os.path.join(record_dir, "recording.wav")
                        path_to_transcribe = noisy_path if os.path.exists(noisy_path) else clean_path
                        
                        transcription = transcribe_audio_only(path_to_transcribe)
                        if isinstance(transcription, dict) and "error" in transcription:
                            st.error(transcription["error"])
                        else:
                            st.success("Transcription successful!")
                            st.session_state.transcription = transcription
                            # Set the flag for the next automatic step: prescription generation.
                            st.session_state.needs_prescription_generation = True
                    else:
                        st.error("Gemini API is not available.")
                    # Remove the flag after attempting transcription.
                    st.session_state.pop("needs_transcription", None)

            st.divider()
            
            # --- Manual Control Buttons ---
            b_col1, b_col2 = st.columns(2)
            with b_col1:
                # Manual button to re-run transcription.
                if st.button("Transcribe Recording", use_container_width=True):
                    if "result" in st.session_state: del st.session_state["result"]
                    if GEMINI_AVAILABLE:
                        noisy_path = os.path.join(record_dir, "noisy_recording.wav")
                        clean_path = os.path.join(record_dir, "recording.wav")
                        path_to_transcribe = noisy_path if os.path.exists(noisy_path) else clean_path
                        
                        with st.spinner("Re-transcribing..."):
                            transcription = transcribe_audio_only(path_to_transcribe)
                        if isinstance(transcription, dict) and "error" in transcription:
                            st.error(transcription["error"])
                        else:
                            st.success("Re-transcription successful!")
                            st.session_state.transcription = transcription
                            st.session_state.needs_prescription_generation = True
                            st.rerun()
                    else:
                        st.error("Gemini API is not available.")
            with b_col2:
                # Button to delete the current recording and start over.
                if st.button("New Recording", use_container_width=True, type="primary"):
                    # Delete local audio files.
                    for path in [recorded_audio_path, noisy_recording_path]:
                        if os.path.exists(path):
                            os.remove(path)
                    
                    # Clear all relevant session state keys.
                    keys_to_clear = ["transcription", "result", "script", "upload_complete", "cloudinary_url", "cloudinary_public_id", "needs_transcription", "needs_prescription_generation"]
                    for key in keys_to_clear:
                        st.session_state.pop(key, None)

                    # Reset the recorder and UI.
                    st.session_state.recorder_key += 1
                    st.session_state.mic_active = False
                    st.success("New recording session started.")
                    st.rerun()
            
    st.divider()

    # -------------------------------------------------------------------------
    # FILE UPLOADER SECTION
    # -------------------------------------------------------------------------
    with st.expander("📁 Or Upload an Existing Audio File..."):
        uploaded_file = st.file_uploader("Upload Audio File", type=["wav"], key="file_uploader")
        
        # --- New File Detection and State Reset ---
        if uploaded_file is not None:
            # Use a tuple of name and size to uniquely identify the uploaded file.
            current_file_id = (uploaded_file.name, uploaded_file.size)
            # If a new file is uploaded, reset the entire state to start fresh.
            if st.session_state.get('last_uploaded_file_id') != current_file_id:
                keys_to_clear = ["transcription", "result", "script", "upload_complete", "cloudinary_url", "cloudinary_public_id", "upload_dir", "needs_transcription", "needs_prescription_generation"]
                for key in keys_to_clear:
                    st.session_state.pop(key, None)
                # Store the ID of the new file to prevent resetting on subsequent reruns.
                st.session_state.last_uploaded_file_id = current_file_id

        # --- Process the Uploaded File ---
        if uploaded_file is not None:
            # This block runs only once per uploaded file.
            if 'upload_complete' not in st.session_state:
                # Create a unique temporary directory for the uploaded file.
                if 'upload_dir' not in st.session_state:
                    st.session_state.upload_dir = "temp_audio_" + datetime.now().strftime("%Y%m%d_%H%M%S")
                
                temp_dir = st.session_state.upload_dir
                if not os.path.exists(temp_dir): os.makedirs(temp_dir)
                
                # Save the uploaded file to the temporary directory.
                original_path = os.path.join(temp_dir, "original.wav")
                with open(original_path, "wb") as f: f.write(uploaded_file.getbuffer())

                # <<< FIX START: FILE UPLOAD >>>
                # Add noise and prepare for upload.
                final_audio_path = original_path
                noisy_path = os.path.join(temp_dir, "noisy.wav")
                
                # Try to create a noisy version of the uploaded file.
                add_noise_to_audio(original_path, noisy_path)

                # Check if the noisy file was successfully created and use it for the upload.
                if os.path.exists(noisy_path):
                    final_audio_path = noisy_path
                # <<< FIX END: FILE UPLOAD >>>

                # Upload the processed file to Cloudinary.
                with st.spinner("Uploading audio..."):
                    original_filename = os.path.splitext(uploaded_file.name)[0]
                    unique_filename = f"uploaded_{original_filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    result = upload_audio_to_cloudinary(final_audio_path, public_id=unique_filename)

                # Handle upload result.
                if "url" in result:
                    st.success("Audio uploaded to Cloudinary!")
                    st.session_state.cloudinary_url = result["url"]
                    st.session_state.cloudinary_public_id = result["public_id"]
                    st.session_state.upload_complete = True
                    st.session_state.needs_transcription = True 
                    st.rerun() # Rerun to trigger automatic transcription.
                else:
                    st.error(result.get("error", "Upload failed"))
            
            # --- Auto-Transcribe Uploaded File ---
            if st.session_state.get("needs_transcription"):
                with st.spinner("Auto-transcribing audio..."):
                    if GEMINI_AVAILABLE and 'upload_dir' in st.session_state:
                        temp_dir = st.session_state.upload_dir
                        original_path = os.path.join(temp_dir, "original.wav")
                        noisy_path = os.path.join(temp_dir, "noisy.wav")
                        final_audio_path = noisy_path if os.path.exists(noisy_path) else original_path
                        
                        transcription = transcribe_audio_only(final_audio_path)
                        if isinstance(transcription, dict) and "error" in transcription:
                            st.error(transcription["error"])
                        else:
                            st.success("Transcription successful!")
                            st.session_state.transcription = transcription
                            st.session_state.needs_prescription_generation = True
                        
                        # Clean up and trigger next step.
                        st.session_state.pop("needs_transcription", None) 
                        st.rerun() 
                    else:
                        st.error("Gemini API not available or file path not found.")
                        st.session_state.pop("needs_transcription", None)

            # --- Display Uploaded Audio Files ---
            if 'upload_dir' in st.session_state:
                temp_dir = st.session_state.upload_dir
                original_path = os.path.join(temp_dir, "original.wav")
                noisy_path = os.path.join(temp_dir, "noisy.wav")

                st.audio(original_path, format="audio/wav")
                if os.path.exists(noisy_path):
                    st.info("Noise added.")
                    st.audio(noisy_path, format="audio/wav")

            # if "cloudinary_url" in st.session_state:
            #     st.write("Cloudinary URL:", st.session_state.cloudinary_url)
            
            # --- Manual Transcription Button for Uploaded File ---
            if st.button("Transcribe Uploaded File", use_container_width=True):
                if GEMINI_AVAILABLE and 'upload_dir' in st.session_state:
                    temp_dir = st.session_state.upload_dir
                    original_path = os.path.join(temp_dir, "original.wav")
                    noisy_path = os.path.join(temp_dir, "noisy.wav")
                    final_audio_path = noisy_path if os.path.exists(noisy_path) else original_path

                    transcription = transcribe_audio_only(final_audio_path)
                    if isinstance(transcription, dict) and "error" in transcription:
                        st.error(transcription["error"])
                    else:
                        st.success("Transcription successful!")
                        st.session_state.transcription = transcription
                        st.session_state.needs_prescription_generation = True
                        # Clean up the temporary directory after processing.
                        if os.path.exists(temp_dir):
                            shutil.rmtree(temp_dir)
                        st.session_state.pop('upload_dir', None)
                        st.rerun()
                else:
                    st.error("Gemini API is not available or file path not found.")


    # -------------------------------------------------------------------------
    # TRANSCRIPTION DISPLAY AND PRESCRIPTION GENERATION
    # -------------------------------------------------------------------------
    # This section is displayed only after a transcription is available.
    if "transcription" in st.session_state:
        st.divider()
        st.header("Review Transcription & Generate Prescription")

        # --- Automatic Prescription Generation ---
        if st.session_state.get("needs_prescription_generation"):
            with st.spinner("Auto-generating prescription..."):
                if GEMINI_AVAILABLE:
                    result = extract_prescription_from_text(st.session_state.transcription)
                    if isinstance(result, dict) and "error" in result:
                        st.error(result["error"])
                    else:
                        st.balloons()
                        st.success("Prescription data extracted successfully!")
                        st.session_state.result = result
                        
                        # --- Save to Database ---
                        audio_url = st.session_state.get("cloudinary_url")
                        if audio_url:
                            with st.spinner("Saving prescription to database..."):
                                
                                mongo_result = upload_prescription_to_mongodb(
                                    st.session_state.result, 
                                    audio_url,
                                    st.session_state.get("script", ""),
                                    st.session_state.script_json,
                                    st.session_state.transcription,
                                    feedback_rating,
                                    feedback_text
                                )
                            if "inserted_id" in mongo_result:
                                st.info(f"Prescription saved to MongoDB")
                            else:
                                st.error(f"MongoDB upload error: {mongo_result.get('error', 'Unknown error')}")
                        else:
                            st.warning("Could not save to database: Cloudinary URL not found.")
                else:
                    st.error("Gemini API is not available.")
                st.session_state.pop("needs_prescription_generation", None)
                # st.rerun()

        # --- Display Transcription and Diff View ---
        # If a script was generated, show a side-by-side comparison.
        if "script" in st.session_state and st.session_state.script:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Script")
                diff_html = generate_diff_html(st.session_state.script, st.session_state.transcription)
                st.markdown(
                    f'<div style="border: 1px solid #1E88E5; border-radius: 5px; padding: 10px; height: 275px; overflow-y: scroll;">{diff_html}</div>',
                    unsafe_allow_html=True,
                )
            with col2:
                st.subheader("Generated Transcription")
                st.text_area("Transcription Text", st.session_state.transcription, height=275, key="transcription_display")
        # Otherwise, just show the transcription.
        else:
            st.subheader("Generated Transcription")
            st.text_area("Transcription Text", st.session_state.transcription, height=200, key="transcription_display")
        
        # Manual button to re-generate the prescription.
        if st.button("Generate Prescription from Transcription", use_container_width=True):
            st.session_state.needs_prescription_generation = True
            st.rerun()

    # --- RESULTS DISPLAY SECTION ---
    # Show the extracted JSON data if it exists.
    if "result" in st.session_state:
        st.divider()
        st.header("View Extracted Data")
        st.json(st.session_state.result)


# -----------------------------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------------------------
elif selected == "Home":
    st.title("Welcome to Medoc Voice 🩺")
    st.subheader("""
            \n-This application is for testing and demonstration purposes only 
             1. Model- Gemini 2.0 Flash Lite \n
             2. Input File - .wav file \n
             3. Output - JSON Prescription""")
    st.markdown("---")
    st.subheader("""
        \nHow to Use This Application->
    **Generate a Script**: On the 'Transcription' page, select the dictation type and generate a medical script to read.
    **Record Audio**: Use the built-in recorder to read the script aloud, or upload an existing .wav audio file.""")
# -----------------------------------------------------------------------------
# SETTINGS PAGE
# -----------------------------------------------------------------------------
elif selected == "Settings":
    st.title("Settings")

    st.info("Application settings and configuration options will be available here in a future version.")
    st.info("Application settings and configuration options will be available here in a future version.")



