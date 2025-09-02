import streamlit as st
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
import time
from pydub import AudioSegment  # For adding noise to recordings
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase  # For handling real-time audio recording
import av  # handles audio frames
import diff_match_patch as dmp_module # For text comparison
import re # For splitting text into words

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
def local_css():
    st.markdown("""
        <style>
        /* Main theme colors */
        .stApp {
            background-color: #0E1117; /* Black */
            color: #FAFAFA;
        }
        .st-emotion-cache-18ni7ap, .st-emotion-cache-z5fcl4 {
            background-color: #161A25; /* Slightly lighter black for sidebar/main content */
        }
        .stButton>button {
            border: 2px solid #1E88E5; /* Blue */
            background-color: transparent;
            color: #1E88E5;
            padding: 0.5em 1em;
            border-radius: 0.5em;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #1E88E5;
            color: white;
        }
        /* Style for the delete button */
        .stButton>button[kind="primary"] {
            border: 2px solid #D32F2F;
            background-color: #D32F2F;
            color: white;
        }
        .stButton>button[kind="primary"]:hover {
            background-color: #B71C1C;
            border-color: #B71C1C;
        }
        .st-emotion-cache-1v0mbdj, .st-emotion-cache-1xarl3l {
            border: 1px solid #1E88E5;
        }
        h1, h2, h3 {
            color: #1E88E5;
        }
        .st-emotion-cache-16txtl3 {
            padding: 2rem 1rem 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

local_css()

# HELPER FUNCTIONS
def generate_medical_script(dictation_type="Doctor Dictation"):
    if not GEMINI_AVAILABLE:
        return "Gemini API is not available. Cannot generate script."
    try:
        with st.spinner(f"Generating new {dictation_type.lower()} script..."):
            model = genai.GenerativeModel('models/gemini-2.5-flash-lite')

            if dictation_type == "Doctor Dictation":
                system_prompt = """
                System Prompt for Generating Test Scripts (Minimal Output)
                You are MedScribe Simulator. Your task is to generate India-specific, realistic medical dictation scripts for QA testers to read aloud when testing an AI medical scribe.
                Guidelines:
                - Output only the dictation script text, no titles, no formatting, no explanations.
                - The script must sound like spoken dictation a doctor would give.
                - Cover: patient intro, symptoms, exam findings, impression/diagnosis, treatment plan, and prescription.
                - Use Indian medical context and safe, generic prescriptions.
                - Script length: 150–450 words,1–3 minutes reading time
                -Vary specialty, severity, and dictation style across scripts.
                -Include edge cases in some scripts (unclear speech, mid-sentence correction, abrupt stop).
                Output rule:
                Return only the dictation script text as if spoken by the doctor.
                """
            else: # Doctor-Patient Conversation
                system_prompt = """
                Doctor–Patient Conversation → Verbatim Diarized Transcript
                You are Intent Translator MAX, tasked with converting raw audio of a doctor–patient consultation into a verbatim, India-specific transcript.
                MISSION
                Perform speech recognition and speaker diarization.
                Handle imperfect audio (phone microphones, background noise, echo, distant voices).
                Output a plain text transcript formatted with strict speaker labels:
                Doctor: ...
                Patient: ...
                PROTOCOL
                Transcription Rules
                Transcribe verbatim (include hesitations, repetitions).
                Do not remove fillers unless they are pure non-speech noise.
                Maintain maximum medical term accuracy.
                Diarization Rules
                Always label as Doctor or Patient (never Speaker 1/2).
                Use context (greetings, questions vs. answers, medical authority) to assign correctly.
                If unsure, insert [unclear speaker] but minimize such cases.
                Noise Handling Rules
                Adapt to phone-quality audio, background chatter, and echo.
                If part of the speech is unintelligible, insert [inaudible] or [unclear].

                Never guess medical terms—mark them [unclear] if indistinct
                Output Rules
                Plain text only, no timestamps, no JSON, no metadata.
                Each speaker turn starts on a new line.
                Example format:
                Doctor: Good morning. What brings you in today?
                Patient: Good morning doctor. I have been having a cough and [unclear] fever for the past three days.
                Doctor: Any other symptoms like shortness of breath or chest pain?
                Patient: Yes, a little shortness of breath especially at night.

                SUCCESS CRITERIA
                Faithful capture of every spoken word (except non-speech noise).
                Accurate identification of Doctor vs. Patient.
                Robust handling of Indian English, regional accents, and noisy clinic/phone environments.
                """

            response = model.generate_content(system_prompt)
            return response.text.strip()
    except Exception as e:
        st.error(f"Error generating script: {e}")
        return "Failed to generate script."
def add_noise_to_audio(input_path, output_path, noise_level=0.005):
    try:
        sound = AudioSegment.from_wav(input_path)
        samples = np.array(sound.get_array_of_samples())
        noise = np.random.normal(0, sound.max * noise_level, len(samples))
        noisy_samples = samples + noise
        noisy_samples = np.clip(noisy_samples, -sound.max, sound.max).astype(samples.dtype)
        noisy_sound = sound._spawn(noisy_samples.tobytes())
        noisy_sound.export(output_path, format="wav")
        return True
    except Exception as e:
        st.error(f"Error adding noise: {e}")
        return False

def transcribe_audio_only(audio_path):
    if not GEMINI_AVAILABLE:
        return {"error": "Gemini API is not available."}
    if not os.path.exists(audio_path):
        return {"error": f"Audio file not found at {audio_path}"}
    try:
        with st.spinner('Uploading file for transcription---'):
            audio_file = genai.upload_file(path=audio_path)
        with st.spinner('Transcribing audio... This may take a moment.'):
            model = genai.GenerativeModel('models/gemini-2.5-flash-lite')
            prompt = """
            Your primary task is to accurately transcribe the provided audio.
            - The very first line of your output MUST begin with a speaker label (e.g., "Doctor:" or "Patient:").
            - For conversations, every change in speaker must start on a new line with the correct label ("Doctor:" or "Patient:").
            - Transcribe the content verbatim.
            - Ensure high accuracy for medical terms and drug names.
            - Provide only the raw transcription text as the output.
            The problem here is while transcription if speaker takes gaps, tap their previous audio and convert accordingly
            """
            response = model.generate_content([prompt, audio_file], request_options={"timeout": 600})
            return response.text
    except Exception as e:
        return {"error": f"An error occurred during transcription: {e}"}

def extract_prescription_from_text(transcription_text):
    if not GEMINI_AVAILABLE: return {"error": "Gemini API is not available."}
    try:
        with st.spinner('Generating prescription from transcription...'):
            model = genai.GenerativeModel('models/gemini-2.5-flash-lite')
            prompt = f"""
            You are a highly intelligent medical data extraction system. You are given a text transcription of a doctor-patient consultation.
            Your task is to extract key medical information from this text and format it into a single, valid JSON object according to the rules and structure below.
            ### TRANSCRIPTION TEXT ###
            {transcription_text}
            ### RULES & JSON STRUCTURE ###
            # JSON OUTPUT STRUCTURE
            {{
                "name": "", "date": "", "time": "", "doctorUsername": "", "patientUsername": "", "hospitalName": "", "hospitalId": "", "clinicalNote": "", "diagnosis": [], "complaints": [], "notes": [],
                "medication": [{{"name": "", "medicationDetails": [{{"dose": "","dosage": "","route": "","freq": "","dur": "","class": "","when": ""}}]}}],
                "test": [{{"name": "","instruction": "","date": ""}}], "followup": {{"date": "","reason": ""}},
                "vitals": {{"BP": "","Heartrate": "","RespiratoryRate": "","temp": "","spO2": "","weight": "","height": "","BMI": "","waist_hips": ""}},
                "nursing": [{{"instruction": "","priority": ""}}], "discharge": {{"planned_date": "","instruction": "","Home_Care": "","Recommendations": ""}},
                "icdCode": [], "medicalHistory": [], "labScanPdf": [], "systematicExamination": {{"General": [],"CVS": [],"RS": [],"CNS": [],"PA": [],"ENT": []}},
                "assessmentPlan": "", "nutritionAssessment": [],
                "referredTo": {{"doctorName": "","doctorUsername": "","phoneNumber": "","email": "","hospitalId": "","hospitalName": "","speciality": ""}},
                "scribePrescription": {{"scribeId": "","imageUrl": "","publicId": "","date": ""}}
            }}
            """
            response = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
            parsed_json = json.loads(response.text.strip())
            return parsed_json
    except Exception as e:
        return {"error": f"An error occurred while generating the prescription: {e}"}

def generate_diff_html(text1, text2):
    """Generates an HTML string to visualize the word-level differences."""
    dmp = dmp_module.diff_match_patch()

    def words_to_chars(text):
        word_array, word_hash = [], {}
        words = re.split(r'(\s+)', text)
        for word in words:
            if word not in word_hash:
                word_hash[word] = len(word_array)
                word_array.append(word)
        return word_array, word_hash

    word_array_1, word_hash_1 = words_to_chars(text1)
    word_array_2, word_hash_2 = words_to_chars(text2)

    chars1 = "".join([chr(word_hash_1[word]) for word in re.split(r'(\s+)', text1)])
    chars2 = "".join([chr(word_hash_2[word]) for word in re.split(r'(\s+)', text2)])

    diffs = dmp.diff_main(chars1, chars2, False)
    dmp.diff_cleanupSemantic(diffs)

    html = ""
    for op, data in diffs:
        words = "".join([word_array_1[ord(char)] for char in data]) if op != dmp.DIFF_INSERT else "".join([word_array_2[ord(char)] for char in data])
        if op == dmp.DIFF_DELETE:
            html += f'<span style="background-color: #993333; color: white; padding: 2px; border-radius: 3px; text-decoration: line-through;">{words}</span>'
        elif op == dmp.DIFF_EQUAL:
            html += words

    return html.replace('\n', '<br>')


# SIDEBAR
with st.sidebar:
    st.title("🩺 Medoc Voice")
    selected = option_menu(menu_title=None, options=["Home", "Transcription", "Settings"], icons=["house", "mic", "gear"], menu_icon="cast", default_index=1)
    st.divider()
    with st.form("Feedback_form"):
        st.subheader("Feedback")
        feedback_rating = st.selectbox("Rate your experience:", ["", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], label_visibility="collapsed", placeholder="Rate your experience")
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

    if 'recorder_key' not in st.session_state:
        st.session_state.recorder_key = 0
    if 'mic_active' not in st.session_state:
        st.session_state.mic_active = False
    # --- CHANGE: ADDED STATE TO DETECT WHEN RECORDING STOPS ---
    if 'prev_webrtc_state_playing' not in st.session_state:
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

    with script_col:
        st.markdown("### 📜 Script")
        st.markdown("Generate a script to read, then record it in the panel on the right.")
        if st.button("Generate New Dictation Script", use_container_width=True):
            st.session_state.script = generate_medical_script(st.session_state.dictation_type_selection)

        if 'script' in st.session_state:
            st.text_area(
                "Your Script",
                value=st.session_state.script,
                height=300,
                disabled=True,
                key="script_display_box"
            )

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
            if not os.path.exists(record_dir): os.makedirs(record_dir)

            class AudioRecorder(AudioProcessorBase):
                def __init__(self) -> None:
                    self.frames_buffer, self.recording_path, self.sample_rate, self.channels = [], os.path.join(record_dir, "recording.wav"), None, None
                def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
                    if self.sample_rate is None: self.sample_rate = frame.sample_rate
                    if self.channels is None: self.channels = len(frame.layout.channels)
                    self.frames_buffer.append(frame.to_ndarray())
                    return frame
                def on_ended(self):
                    if not self.frames_buffer or self.sample_rate is None: return
                    sound = np.concatenate(self.frames_buffer, axis=1)
                    audio_segment = AudioSegment(data=sound.tobytes(), sample_width=sound.dtype.itemsize, frame_rate=self.sample_rate, channels=self.channels)
                    if audio_segment.channels > 1: audio_segment = audio_segment.set_channels(1)
                    audio_segment.export(self.recording_path, format="wav")
                    self.frames_buffer.clear(); self.sample_rate = None; self.channels = None

            webrtc_ctx = webrtc_streamer(
                key=f"audio-recorder-{st.session_state.recorder_key}",
                mode=WebRtcMode.SENDONLY,
                audio_processor_factory=AudioRecorder,
                media_stream_constraints={ "video": False, "audio": { "echoCancellation": True, "noiseSuppression": True, "autoGainControl": True }},
            )

            # --- FIX FOR SINGLE-CLICK STOP ---
            # Detect the transition from playing to stopped
            just_stopped = st.session_state.prev_webrtc_state_playing and webrtc_ctx and not webrtc_ctx.state.playing
            # Update the state for the next run
            if webrtc_ctx:
                st.session_state.prev_webrtc_state_playing = webrtc_ctx.state.playing
            # If we just stopped, wait a moment for the file-write and then rerun the script to show the review section
            if just_stopped:
                time.sleep(0.5)
                st.rerun()

    # REVIEW RECORDING SECTION
    record_dir = "temp_recordings"
    recorded_audio_path = os.path.join(record_dir, "recording.wav")
    if webrtc_ctx and not webrtc_ctx.state.playing and os.path.exists(recorded_audio_path):
        with recorder_col: # Display the review section in the same column
            st.divider()
            st.subheader("Review Your Recording")
            st.audio(recorded_audio_path)

            add_noise_record = st.checkbox("Add Noise to Recorded Audio", key="record_add_noise")
            noise_level_record = st.slider("Noise Level", 0.0, 1.0, 0.05, 0.01, disabled=not add_noise_record, key="record_noise_level", help="Controls the intensity of the generated white noise.")

            final_recording_path, noisy_recording_path = recorded_audio_path, os.path.join(record_dir, "noisy_recording.wav")

            if add_noise_record and add_noise_to_audio(recorded_audio_path, noisy_recording_path, noise_level_record):
                st.write("Noisy Version:"); st.audio(noisy_recording_path); final_recording_path = noisy_recording_path

            st.divider()
            b_col1, b_col2 = st.columns(2)
            with b_col1:
                if st.button("Transcribe Recording", use_container_width=True):
                    if 'result' in st.session_state: del st.session_state.result
                    transcription = transcribe_audio_only(final_recording_path)
                    if isinstance(transcription, dict) and "error" in transcription: st.error(transcription["error"])
                    else: st.success("Transcription successful!"); st.session_state.transcription = transcription
            with b_col2:
                if st.button("Delete Recording", use_container_width=True, type="primary"):
                    if os.path.exists(recorded_audio_path): os.remove(recorded_audio_path)
                    if os.path.exists(noisy_recording_path): os.remove(noisy_recording_path)
                    for key in ['transcription', 'result', 'script']:
                        if key in st.session_state: del st.session_state[key]
                    st.session_state.recorder_key += 1
                    st.session_state.mic_active = False
                    st.success("Recording deleted."); st.rerun()

    st.divider()
    with st.expander("📁 Or Upload an Existing Audio File..."):
        uploaded_file = st.file_uploader("Upload Audio File", type=['wav'], key="file_uploader")
        if uploaded_file:
            for key in ['transcription', 'result', 'script']:
                if key in st.session_state: del st.session_state[key]

        if uploaded_file is not None:
            add_noise_upload = st.checkbox("Add Noise to Uploaded Audio for Testing", key="upload_add_noise")
            noise_level_upload = st.slider("Noise Level ", 0.0, 1.0, 0.05, 0.01, disabled=not add_noise_upload, key="upload_noise_level", help="Controls the intensity of the generated white noise.")

            temp_dir = "temp_audio"
            if not os.path.exists(temp_dir): os.makedirs(temp_dir)
            original_path = os.path.join(temp_dir, "original.wav")
            with open(original_path, "wb") as f: f.write(uploaded_file.getbuffer())
            st.audio(original_path, format='audio/wav')

            final_audio_path = original_path
            if add_noise_upload:
                noisy_path = os.path.join(temp_dir, "noisy.wav")
                if add_noise_to_audio(original_path, noisy_path, noise_level_upload):
                    st.info("Noise added."); st.audio(noisy_path, format='audio/wav'); final_audio_path = noisy_path

            if st.button("Transcribe Uploaded File", use_container_width=True):
                transcription = transcribe_audio_only(final_audio_path)
                if isinstance(transcription, dict) and "error" in transcription: st.error(transcription["error"])
                else: st.success("Transcription successful!"); st.session_state.transcription = transcription

    # SHARED WORKFLOW
    if 'transcription' in st.session_state:
        st.divider()
        st.header("Review Transcription & Generate Prescription")
        if 'script' in st.session_state and st.session_state.script:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Script ")
                diff_html = generate_diff_html(st.session_state.script, st.session_state.transcription)
                st.markdown(f'<div style="border: 1px solid #1E88E5; border-radius: 5px; padding: 10px; height: 275px; overflow-y: scroll;">{diff_html}</div>', unsafe_allow_html=True)
            with col2:
                st.subheader("Generated Transcription")
                st.text_area("Transcription Text", st.session_state.transcription, height=275, key="transcription_display")
        else:
            st.subheader("Generated Transcription")
            st.text_area("Transcription Text", st.session_state.transcription, height=200, key="transcription_display")

        if st.button("Generate Prescription from Transcription", use_container_width=True):
            result = extract_prescription_from_text(st.session_state.transcription)
            if "error" in result: st.error(result["error"])
            else: st.balloons(); st.success("Prescription data extracted successfully!"); st.session_state.result = result

    if 'result' in st.session_state:
        st.divider()
        st.header("View Extracted Data")
        result_data = st.session_state.result
        st.subheader("Patient & Consultation Details")
        p_col1, p_col2, p_col3 = st.columns(3)
        p_col1.text_input("Full Name", value=result_data.get('name', ''), disabled=True, key="patient_name")
        p_col2.text_input("Hospital Name", value=result_data.get('hospitalName', ''), disabled=True, key="hospital_name")
        p_col3.text_input("Date", value=result_data.get('date', ''), disabled=True, key="consult_date")
        st.subheader("Complaints & Medical History")
        ch_col1, ch_col2 = st.columns(2)
        ch_col1.text_area("Chief Complaints", value=", ".join(result_data.get('complaints', [])), disabled=True, key="complaints")
        ch_col2.text_area("Medical History", value=", ".join(result_data.get('medicalHistory', [])), disabled=True, key="medical_history")
        st.subheader("Vitals")
        vitals = result_data.get('vitals', {})
        v_col1, v_col2, v_col3, v_col4, v_col5 = st.columns(5)
        v_col1.text_input("Weight", value=vitals.get('weight', ''), disabled=True, key="vitals_weight")
        v_col2.text_input("Height", value=vitals.get('height', ''), disabled=True, key="vitals_height")
        v_col3.text_input("Blood Pressure", value=vitals.get('BP', ''), disabled=True, key="vitals_bp")
        v_col4.text_input("Temperature", value=vitals.get('temp', ''), disabled=True, key="vitals_temp")
        v_col5.text_input("SpO2", value=vitals.get('spO2', ''), disabled=True, key="vitals_spo2")
        st.subheader("Clinical Assessment & Plan")
        st.text_area("Diagnosis", value=", ".join(result_data.get('diagnosis', [])), disabled=True, key="diagnosis")
        st.text_area("Clinical Note", value=result_data.get('clinicalNote', ''), disabled=True, key="clinical_note")
        st.subheader("Medication")
        medications = result_data.get('medication', [])
        if not medications or not any(med.get('name') for med in medications): st.info("No medication details were extracted.")
        else:
            for i, med in enumerate(medications):
                if med.get('name'):
                    st.text_input("Drug Name", value=med.get('name', ''), disabled=True, key=f"drug_name_{i}")
                    if med.get('medicationDetails') and med['medicationDetails']:
                        details = med['medicationDetails'][0]
                        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                        m_col1.text_input("Dosage", value=details.get('dosage', ''), disabled=True, key=f"dosage_{i}")
                        m_col2.text_input("Frequency", value=details.get('freq', ''), disabled=True, key=f"frequency_{i}")
                        m_col3.text_input("Duration", value=details.get('dur', ''), disabled=True, key=f"duration_{i}")
                        m_col4.text_input("When", value=details.get('when', ''), disabled=True, key=f"when_{i}")
        st.subheader("Recommended Tests")
        tests = result_data.get('test', [])
        if not tests or not any(t.get('name') for t in tests): st.info("No recommended tests were extracted.")
        else:
            for i, test in enumerate(tests):
                if test.get('name'):
                    t_col1, t_col2 = st.columns([1,2])
                    t_col1.text_input("Test Name", value=test.get('name', ''), disabled=True, key=f"test_name_{i}")
                    t_col2.text_input("Instruction", value=test.get('instruction', ''), disabled=True, key=f"test_instruction_{i}")
        st.subheader("Follow-up Plan")
        followup = result_data.get('followup', {})
        f_col1, f_col2 = st.columns(2)
        f_col1.text_input("Follow-up Date", value=followup.get('date', ''), disabled=True, key="followup_date")
        f_col2.text_area("Reason for Follow-up", value=followup.get('reason', ''), disabled=True, key="followup_reason")
        st.divider()
        st.subheader("Full JSON Output")
        st.json(result_data)


elif selected == "Home":
    st.title("Welcome to Medoc Voice 🩺")
    st.markdown("### Revolutionizing Medical Documentation with AI")
    st.markdown("##### This application is for testing and demonstration purposes only- Your Audio is stored locally and not shared.")
    st.write("1. Model- Gemini 2.5 Flash lite")
    st.write("2. Input File - .wav file")

elif selected == "Settings":
    st.title("Settings")
    st.info("Application settings and configuration options will be available here in a future version.")
