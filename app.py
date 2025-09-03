import streamlit as st
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
import numpy as np
import time
from pydub import AudioSegment
from streamlit_option_menu import option_menu
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase
import av

# Import functions 
from ui_utils import local_css
from gemini_utils import generate_medical_script, transcribe_audio_only, extract_prescription_from_text
from diff_utils import generate_diff_html
from audio_utils import add_noise_to_audio

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Medoc Voice",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# LOAD ENVIRONMENT VARIABLES
load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

# GEMINI API SETUP
GEMINI_AVAILABLE = False
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        GEMINI_AVAILABLE = True
    except Exception as e:
        st.error(f"Failed to configure Gemini API: {e}")
else:
    st.error("Google API Key not found. Please set it in your .env file.")

# STYLING
local_css()

# SIDEBAR
with st.sidebar:
    st.title("🩺 Medoc Voice")
    selected = option_menu(
        menu_title=None,
        options=["Home", "Transcription", "Settings"],
        icons=["house", "mic", "gear"],
        menu_icon="cast",
        default_index=1,
    )
    st.divider()
    with st.form("Feedback_form"):
        st.subheader("Feedback")
        feedback_rating = st.selectbox(
            "Rate your experience:",
            ["", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
            label_visibility="collapsed",
            placeholder="Rate your experience",
        )
        feedback_text = st.text_area("Your feedback:", placeholder="Tell us what you think...")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if feedback_rating and feedback_text:
                st.success("Thank you for your feedback!")
                time.sleep(2)
            else:
                st.warning("Please fill out both fields.")


# MAIN PAGE CONTENT
if selected == "Transcription":
    st.header("✨ Audio to Prescription Transcription")

    # Initialize session state variables
    if "recorder_key" not in st.session_state:
        st.session_state.recorder_key = 0
    if "mic_active" not in st.session_state:
        st.session_state.mic_active = False
    if "prev_webrtc_state_playing" not in st.session_state:
        st.session_state.prev_webrtc_state_playing = False

    col_a, col_b = st.columns(2)
    with col_a:
        st.radio("Related to Healthcare Industry?", ["Yes", "No"], key="is_healthcare", horizontal=True)
    with col_b:
        dictation_type = st.radio(
            "Select Dictation Type",
            ["Doctor Dictation", "Doctor-Patient Conversation"],
            key="dictation_type_selection",
            horizontal=True,
        )
    st.markdown("---")

    script_col, recorder_col = st.columns(2)

    # --- SCRIPT COLUMN ---
    with script_col:
        st.markdown("### 📜 Script")
        st.markdown("Generate a script to read, then record it in the panel on the right.")
        if st.button("Generate New Dictation Script", use_container_width=True):
            if GEMINI_AVAILABLE:
                st.session_state.script = generate_medical_script(st.session_state.dictation_type_selection)
            else:
                st.error("Gemini API is not available to generate a script.")

        if "script" in st.session_state:
            st.text_area(
                "Your Script",
                value=st.session_state.script,
                height=300,
                disabled=True,
                key="script_display_box",
            )

    # --- RECORDER COLUMN ---
    with recorder_col:
        st.markdown("### 🎙️ Record Live Audio")
        st.markdown("Click 'Start' to begin recording. Click 'Stop' when finished.")
        webrtc_ctx = None
        if not st.session_state.mic_active:
            if st.button("🎙️ Open Microphone to Record", use_container_width=True):
                st.session_state.mic_active = True
                st.rerun()
        else:
            record_dir = "temp_recordings"
            if not os.path.exists(record_dir):
                os.makedirs(record_dir)

            class AudioRecorder(AudioProcessorBase):
                def __init__(self) -> None:
                    self.frames_buffer = []
                    self.recording_path = os.path.join(record_dir, "recording.wav")
                    self.sample_rate = None
                    self.channels = None

                def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
                    if self.sample_rate is None: self.sample_rate = frame.sample_rate
                    if self.channels is None: self.channels = len(frame.layout.channels)
                    self.frames_buffer.append(frame.to_ndarray())
                    return frame

                def on_ended(self):
                    if not self.frames_buffer or self.sample_rate is None: return
                    sound = np.concatenate(self.frames_buffer, axis=1)
                    audio_segment = AudioSegment(
                        data=sound.tobytes(),
                        sample_width=sound.dtype.itemsize,
                        frame_rate=self.sample_rate,
                        channels=self.channels,
                    )
                    if audio_segment.channels > 1:
                        audio_segment = audio_segment.set_channels(1)
                    audio_segment.export(self.recording_path, format="wav")
                    self.frames_buffer.clear()
                    self.sample_rate = None
                    self.channels = None

            webrtc_ctx = webrtc_streamer(
                key=f"audio-recorder-{st.session_state.recorder_key}",
                mode=WebRtcMode.SENDONLY,
                audio_processor_factory=AudioRecorder,
                media_stream_constraints={
                    "video": False,
                    "audio": {"echoCancellation": True, "noiseSuppression": True, "autoGainControl": True},
                },
            )

            just_stopped = st.session_state.prev_webrtc_state_playing and webrtc_ctx and not webrtc_ctx.state.playing
            if webrtc_ctx:
                st.session_state.prev_webrtc_state_playing = webrtc_ctx.state.playing
            if just_stopped:
                time.sleep(0.5)
                st.rerun()

    # REVIEW RECORDING SECTION (appears in recorder column)
    record_dir = "temp_recordings"
    recorded_audio_path = os.path.join(record_dir, "recording.wav")
    if webrtc_ctx and not webrtc_ctx.state.playing and os.path.exists(recorded_audio_path):
        with recorder_col:
            st.divider()
            st.subheader("Review Your Recording")
            st.audio(recorded_audio_path)

            final_recording_path = recorded_audio_path
            noisy_recording_path = os.path.join(record_dir, "noisy_recording.wav")
            if add_noise_to_audio(recorded_audio_path, noisy_recording_path):
                st.write("Noisy Version:")
                st.audio(noisy_recording_path)
                final_recording_path = noisy_recording_path

            st.divider()
            b_col1, b_col2 = st.columns(2)
            with b_col1:
                if st.button("Transcribe Recording", use_container_width=True):
                    if "result" in st.session_state: del st.session_state["result"]
                    if GEMINI_AVAILABLE:
                        transcription = transcribe_audio_only(final_recording_path)
                        if isinstance(transcription, dict) and "error" in transcription:
                            st.error(transcription["error"])
                        else:
                            st.success("Transcription successful!")
                            st.session_state.transcription = transcription
                    else:
                        st.error("Gemini API is not available.")
            with b_col2:
                if st.button("Delete Recording", use_container_width=True, type="primary"):
                    for path in [recorded_audio_path, noisy_recording_path]:
                        if os.path.exists(path):
                            os.remove(path)
                    for key in ["transcription", "result", "script"]:
                        st.session_state.pop(key, None)
                    st.session_state.recorder_key += 1
                    st.session_state.mic_active = False
                    st.success("Recording deleted.")
                    st.rerun()

    st.divider()

    #FILE UPLOADER SECTION
    with st.expander("📁 Or Upload an Existing Audio File..."):
        uploaded_file = st.file_uploader("Upload Audio File", type=["wav"], key="file_uploader")
        if uploaded_file:
            for key in ["transcription", "result", "script"]:
                st.session_state.pop(key, None)

        if uploaded_file is not None:
            temp_dir = "temp_audio"
            if not os.path.exists(temp_dir): os.makedirs(temp_dir)
            original_path = os.path.join(temp_dir, "original.wav")
            with open(original_path, "wb") as f: f.write(uploaded_file.getbuffer())
            st.audio(original_path, format="audio/wav")

            final_audio_path = original_path
            noisy_path = os.path.join(temp_dir, "noisy.wav")
            if add_noise_to_audio(original_path, noisy_path):
                st.info("Noise added.")
                st.audio(noisy_path, format="audio/wav")
                final_audio_path = noisy_path

            if st.button("Transcribe Uploaded File", use_container_width=True):
                if GEMINI_AVAILABLE:
                    transcription = transcribe_audio_only(final_audio_path)
                    if isinstance(transcription, dict) and "error" in transcription:
                        st.error(transcription["error"])
                    else:
                        st.success("Transcription successful!")
                        st.session_state.transcription = transcription
                else:
                    st.error("Gemini API is not available.")


    #Transcription Display and Prescription Generation)
    if "transcription" in st.session_state:
        st.divider()
        st.header("Review Transcription & Generate Prescription")
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
        else:
            st.subheader("Generated Transcription")
            st.text_area("Transcription Text", st.session_state.transcription, height=200, key="transcription_display")

        if st.button("Generate Prescription from Transcription", use_container_width=True):
            if GEMINI_AVAILABLE:
                result = extract_prescription_from_text(st.session_state.transcription)
                if isinstance(result, dict) and "error" in result:
                    st.error(result["error"])
                else:
                    st.balloons()
                    st.success("Prescription data extracted successfully!")
                    st.session_state.result = result
            else:
                st.error("Gemini API is not available.")

    # RESULTS DISPLAY SECTION
    if "result" in st.session_state:
        st.divider()
        st.header("View Extracted Data")
        st.json(st.session_state.result)


elif selected == "Home":
    st.title("Welcome to Medoc Voice 🩺")
    st.markdown("### Revolutionizing Medical Documentation with AI")
    st.markdown("##### This application is for testing and demonstration purposes only- Your Audio is stored locally and not shared.")
    st.write("1. Model- Gemini 2.0 Flash Lite")
    st.write("2. Input File - .wav file")


elif selected == "Settings":
    st.title("Settings")
    st.info("Application settings and configuration options will be available here in a future version.")
