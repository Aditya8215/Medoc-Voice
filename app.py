import streamlit as st
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
import time
from pydub import AudioSegment
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase
import av

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Medoc Voice",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- LOAD ENVIRONMENT VARIABLES ---
load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- GEMINI API SETUP ---
GEMINI_AVAILABLE = False
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        GEMINI_AVAILABLE = True
    except Exception as e:
        st.error(f"Failed to configure Gemini API: {e}")
else:
    st.error("Google API Key not found. Please set it in your .env file.")

# --- STYLING ---
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

# --- HELPER FUNCTIONS ---
def generate_medical_script():
    """Calls Gemini to generate a medical dictation script."""
    if not GEMINI_AVAILABLE:
        return "Gemini API is not available. Cannot generate script."
    try:
        with st.spinner("Generating new medical script..."):
            model = genai.GenerativeModel('models/gemini-2.5-flash-lite')
            system_prompt = """
            System Prompt for Generating Test Scripts (Minimal Output)
            You are MedScribe Simulator. Your task is to generate India-specific, realistic medical dictation scripts for QA testers to read aloud when testing an AI medical scribe.
            Guidelines:
            - Output only the dictation script text, no titles, no formatting, no explanations.
            - The script must sound like spoken dictation a doctor would give.
            - Cover: patient intro, symptoms, exam findings, impression/diagnosis, treatment plan, and prescription.
            - Use Indian medical context and safe, generic prescriptions.
            - Script length: 150–450 words.
            Output rule:
            Return only the dictation script text as if spoken by the doctor.
            """
            response = model.generate_content(system_prompt)
            return response.text.strip()
    except Exception as e:
        st.error(f"Error generating script: {e}")
        return "Failed to generate script."

def add_noise_to_audio(input_path, output_path, noise_level=0.05):
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
    if not GEMINI_AVAILABLE: return {"error": "Gemini API is not available."}
    if not os.path.exists(audio_path): return {"error": f"Audio file not found at {audio_path}"}
    try:
        with st.spinner('Uploading file for transcription...'):
            audio_file = genai.upload_file(path=audio_path)
        with st.spinner('Transcribing audio... This may take a moment.'):
            model = genai.GenerativeModel('models/gemini-2.5-flash-lite')
            prompt = "Please transcribe the following audio file accurately. Provide only the raw text of the conversation."
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

# --- SIDEBAR ---
with st.sidebar:
    st.title("🩺 Medoc Voice")
    selected = option_menu(menu_title=None, options=["Home", "Transcription", "Settings"], icons=["house", "mic", "gear"], menu_icon="cast", default_index=1)

# --- MAIN PAGE CONTENT ---
if selected == "Transcription":
    st.header("✨ Audio to Prescription Transcription")

    if 'recorder_key' not in st.session_state:
        st.session_state.recorder_key = 0

    st.markdown("### 🎙️ Record Live Audio")
    st.markdown("Generate a script to read, or simply start recording your own dictation.")

    if st.button("Generate New Dictation Script", use_container_width=True):
        st.session_state.script = generate_medical_script()

    if 'script' in st.session_state:
        st.markdown("---")
        st.subheader("Your Script")
        st.markdown(st.session_state.script)
        st.markdown("---")

    st.write("Click 'Start' to begin recording. Click 'Stop' when finished.")

    record_dir = "temp_recordings"
    if not os.path.exists(record_dir): os.makedirs(record_dir)
    
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
    
    recorded_audio_path = os.path.join(record_dir, "recording.wav")
    if not webrtc_ctx.state.playing and os.path.exists(recorded_audio_path):
        st.divider()
        st.subheader("Step 1: Review Your Recording")
        st.write("Listen to your recording. You can add noise for testing, then transcribe it.")
        st.audio(recorded_audio_path)
        
        add_noise_record = st.checkbox("Add Noise to Recorded Audio", key="record_add_noise")
        noise_level_record = st.slider("Noise Level", 0.0, 1.0, 0.05, 0.01, disabled=not add_noise_record, key="record_noise_level", help="Controls the intensity of the generated white noise.")
        
        final_recording_path = recorded_audio_path
        noisy_recording_path = os.path.join(record_dir, "noisy_recording.wav")

        if add_noise_record:
            if add_noise_to_audio(recorded_audio_path, noisy_recording_path, noise_level_record):
                st.write("Noisy Version:")
                st.audio(noisy_recording_path)
                final_recording_path = noisy_recording_path
        
        st.divider()
        b_col1, b_col2 = st.columns(2)
        with b_col1:
            if st.button("Transcribe Recording", use_container_width=True):
                if 'result' in st.session_state: del st.session_state.result
                transcription = transcribe_audio_only(final_recording_path)
                if isinstance(transcription, dict) and "error" in transcription:
                    st.error(transcription["error"])
                else:
                    st.success("Transcription successful!")
                    st.session_state.transcription = transcription
        with b_col2:
            if st.button("Delete Recording", use_container_width=True, type="primary"):
                if os.path.exists(recorded_audio_path): os.remove(recorded_audio_path)
                if os.path.exists(noisy_recording_path): os.remove(noisy_recording_path)
                if 'transcription' in st.session_state: del st.session_state.transcription
                if 'result' in st.session_state: del st.session_state.result
                st.session_state.recorder_key += 1
                st.success("Recording deleted. You can now record again.")
                time.sleep(1)
                st.rerun()

    st.divider()

    with st.expander("📁 Or Upload an Existing Audio File..."):
        st.markdown("Upload a medical consultation audio file (`.wav`) for transcription and analysis.")
        uploaded_file = st.file_uploader("Upload Audio File", type=['wav'], key="file_uploader")
        if uploaded_file:
            if 'transcription' in st.session_state: del st.session_state.transcription
            if 'result' in st.session_state: del st.session_state.result
        add_noise_upload = st.checkbox("Add Noise to Uploaded Audio for Testing", key="upload_add_noise")
        noise_level_upload = st.slider("Noise Level ", 0.0, 1.0, 0.05, 0.01, disabled=not add_noise_upload, key="upload_noise_level", help="Controls the intensity of the generated white noise.")
        if uploaded_file is not None:
            temp_dir = "temp_audio"
            if not os.path.exists(temp_dir): os.makedirs(temp_dir)
            original_path = os.path.join(temp_dir, "original.wav")
            with open(original_path, "wb") as f: f.write(uploaded_file.getbuffer())
            st.audio(original_path, format='audio/wav')
            final_audio_path = original_path
            if add_noise_upload:
                noisy_path = os.path.join(temp_dir, "noisy.wav")
                if add_noise_to_audio(original_path, noisy_path, noise_level_upload):
                    st.info("Noise added to the uploaded file for processing.")
                    st.audio(noisy_path, format='audio/wav')
                    final_audio_path = noisy_path
            if st.button("Transcribe Uploaded File", use_container_width=True):
                transcription = transcribe_audio_only(final_audio_path)
                if isinstance(transcription, dict) and "error" in transcription:
                    st.error(transcription["error"])
                else:
                    st.success("Transcription successful!")
                    st.session_state.transcription = transcription

    # --- SHARED WORKFLOW & DISPLAY ---
    if 'transcription' in st.session_state:
        st.divider()
        st.header("Step 2: Review Transcription & Generate Prescription")
        st.text_area("Transcription Text", st.session_state.transcription, height=200, key="transcription_display")
        if st.button("Generate Prescription from Transcription", use_container_width=True):
            result = extract_prescription_from_text(st.session_state.transcription)
            if "error" in result: st.error(result["error"])
            else:
                st.balloons()
                st.success("Prescription data extracted successfully!")
                st.session_state.result = result

    if 'result' in st.session_state:
        st.divider()
        st.header("Step 3: View Extracted Data")
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
        if not medications or not medications[0].get('name'): st.info("No medication details were extracted.")
        else:
            for i, med in enumerate(medications):
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
        if not tests or not tests[0].get('name'): st.info("No recommended tests were extracted.")
        else:
            for i, test in enumerate(tests):
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
    st.write("...") # Home page content
elif selected == "Settings":
    st.title("Settings")
    st.info("Application settings and configuration options will be available here in a future version.")

