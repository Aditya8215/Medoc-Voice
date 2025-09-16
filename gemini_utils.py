import streamlit as st
import google.generativeai as genai
import json
import os
import random
from scripts import doctor_dictation, doctor_patient_dictation

# Updated function to use local scripts
def generate_medical_script(dictation_type, language):
    """
    Selects a random medical script from pre-defined dictionaries based on the
    dictation type and language.
    """
    try:
        script_source = None
        if dictation_type == "Doctor Dictation":
            script_source = doctor_dictation
        elif dictation_type == "Doctor-Patient Conversation":
            script_source = doctor_patient_dictation

        if script_source and language in script_source and script_source[language]:
            return random.choice(script_source[language])
        else:
            return f"Error: No '{dictation_type}' scripts found for the selected language '{language}'."

    except Exception as e:
        st.error(f"An error occurred while selecting a script: {e}")
        return "Error: Failed to generate a script due to an unexpected error."


def transcribe_audio_only(audio_path):
    if not os.path.exists(audio_path):
        return {"error": f"Audio file not found at {audio_path}"}
    try:
        with st.spinner('Uploading file for transcription---'):
            audio_file = genai.upload_file(path=audio_path)
        with st.spinner('Transcribing audio... This may take a moment.'):
            model = genai.GenerativeModel('models/gemini-2.5-flash')
            prompt = """
            #*IF a single speaker- Doctor dictation, transcribe as-is*.
            You are a specialized audio-to-text converter for doctor-patient conversations. Your task is to transcribe noisy phone audio recordings into clean, diarized text output with maximum speaker identification accuracy.
            ## CORE MISSION
            Convert audio input into structured dialogue format using only two speaker labels: DOCTOR: and PATIENT:

            ## AUDIO CONTEXT AWARENESS
            - Input: Noisy phone recordings with distant microphone placement
            - Expect: Background noise, potential speech overlap, varying audio quality
            - Challenge: Distinguish between two speakers in suboptimal conditions

            ## PROCESSING PROTOCOL

            ### 1. AUDIO ANALYSIS FIRST
            - Identify distinct vocal characteristics (pitch, pace, speech patterns)
            - Map higher/lower frequency ranges to likely speaker types
            - Note conversation flow patterns (questions vs responses, medical terminology usage)

            ### 2. SPEAKER IDENTIFICATION STRATEGY
            - DOCTOR typically: Uses medical terminology, asks diagnostic questions, provides instructions/explanations
            - PATIENT typically: Describes symptoms, asks clarifying questions, responds to medical queries
            - When uncertain: Use contextual clues from conversation content rather than guessing

            ### 3. TRANSCRIPTION RULES
            - **CRITICAL:** Pay extremely close attention to negations and qualifications (e.g., "not," "don't," "can't," "I'm not," "a little," "sometimes"). A missed "not" can completely invert the clinical meaning. Transcribe these words with high fidelity.
            - Format every line as either "DOCTOR: [speech]" or "PATIENT: [speech]"
            - Maintain natural conversation flow and timing
            - Include hesitations, partial words only if they affect meaning
            - Mark unclear audio as [UNCLEAR] rather than guessing
            - Use [OVERLAPPING] when both speakers talk simultaneously

            ### 4. MEDICAL CONTEXT HANDLING
            - Preserve all medical terms accurately
            - Maintain patient privacy (don't add identifying details not in audio)
            - Keep symptom descriptions verbatim
            - Preserve medication names and dosages exactly as spoken

            ### 5. QUALITY ASSURANCE
            - Cross-reference speaker assignments with conversation logic
            - Verify medical terminology context matches speaker role
            - Flag inconsistent speaker patterns with [SPEAKER_UNCERTAIN] tag
            - Prioritize accuracy over perfection - mark uncertainties rather than guess

            ## OUTPUT FORMAT

            Doctor: [First speaker's words]
            Patient: [Second speaker's words]
            Doctor: [Continuing dialogue]
            [UNCLEAR] [when audio is unintelligible]
            [OVERLAPPING] Doctor: [speech] / Patient: [speech]


            ## ERROR HANDLING
            When speaker identification confidence is low:
            - Use context clues from medical conversation patterns
            - Mark uncertainty with [SPEAKER_UNCERTAIN] before the line
            - Never leave speech unattributed - assign to most likely speaker
            # *AUTODETECT Language and provide transcription in same language*
            EXECUTE: Process the provided audio and return clean diarized transcript following this protocol.
            
            """
            response = model.generate_content([prompt, audio_file], request_options={"timeout": 600})
            return response.text
    except Exception as e:
        return {"error": f"An error occurred during transcription: {e}"}


def extract_prescription_from_text(transcription_text):
    try:
        with st.spinner('Generating prescription from transcription...'):
            model = genai.GenerativeModel('models/gemini-2.5-flash')
            prompt = f"""
            #You are a medical data extraction system. From a given doctor_dictation/doctor-patient transcription, extract key information and return a single valid JSON object.

#*Rules*
Empty fields → use ""; empty lists → use []. Never use null.
Expand all standard medical abbreviations.- mg- milligram
Never use any stopwards or anything else. 
Medical History → capture past/current conditions (expand abbreviations). Example: "HTN" → "Hypertension". If none, use [].
Medications:
dose: in mg.
dosage: morning-afternoon-night format (e.g., 1-0-1). If 0-x, convert to 1-0-0.
class: Tablet, Capsule, Injection, Syrup, Drops, Ointment, Inhaler, Powder, Cream, Lotion, Suppository, Patch.
route: expand (e.g., po → oral, iv → intravenous).
freq: use predefined values only (once a day, twice a day, three times a day, Daily, Alternate Days, Sos, Weekly, Weekly twice, Weekly thrice, Stat).
when: use predefined values only (Before food, After food, After Lunch, After Breakfast, After Dinner, Before Dinner, Before Lunch, Before Breakfast, Empty Stomach, Bed Time, Sos).
Notes → capture any doctor’s free instructions for medication.
Clinical Note → extra instructions not fitting elsewhere.
Follow-up: if doctor says "after X days/weeks", calculate and format as dd-mm-yyyy from prescription date.
Systematic Examinations, Nursing, Discharge, Tests, Referrals → fill if mentioned, else empty.


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
            response = model.generate_content([prompt, transcription_text], generation_config={"response_mime_type": "application/json"})
            parsed_json = json.loads(response.text.strip())
            return parsed_json
    except Exception as e:
        return {"error": f"An error occurred while generating the prescription: {e}"}