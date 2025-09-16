# scripts.py

doctor_dictation = {
    'English': [
        "Patient is Mr. Vikram Singh 65 year old male... chief complaint of chest pain since morning... radiating to the left arm... associated with sweating and shortness of breath... on examination pulse is 110 per minute... BP is 150 by 90... ECG shows ST segment elevation in anterior leads... impression is acute anterior wall myocardial infarction... plan is to admit to the ICU... start thrombolysis... prescription is Injection Streptokinase 1.5 million units IV infusion over one hour... tablet Aspirin 300mg stat... tablet Clopidogrel 300mg stat... followed by 75mg once daily... tablet Atorvastatin 80mg at night... Injection Morphine 2mg IV for pain... Get cardiac enzymes done... Trop T and Trop I... Follow up with cardiology team immediately... let's say on 17 September.",
        "This patient is Rohan a 7 year old boy... brought by his mother with complaints of fever and rash for the last 4 days... the rash started on the face and then spread to the body... it is a maculopapular rash... on examination there is high grade fever... conjunctivitis and Koplik's spots are seen inside the mouth... diagnosis is Measles... treatment is symptomatic... prescribe Syrup Paracetamol 5ml... if fever is high... can be given three times a day... advise plenty of fluids and rest... Vitamin A supplement should be given... one dose today and one tomorrow... Isolation is important to prevent spread... follow up after five days or if symptoms worsen... lets say 22 September... no antibiotics needed for now.",
        "Patient's name is Sameer... age 25... complaint of watery diarrhea and vomiting since last night... about 8 to 10 episodes of loose stools... On examination the patient looks dehydrated... tongue is dry... BP is low 90 by 60... Diagnosis is acute gastroenteritis with moderate dehydration... plan is to admit and start IV fluids... prescribe Injection Ringer's Lactate... 1 litre stat... then 1 litre over 4 hours... Injection Ondansetron 4mg IV for vomiting... Give ORS solution to drink frequently... once he starts tolerating orally... Start antibiotic... Tablet Ofloxacin and Ornidazole... one tablet twice a day for five days... monitor intake output chart... check electrolytes... CBC."
    ],
    'Hindi': [
        "ये पेशेंट हैं श्रीमती कमला देवी... उम्र 50 साल... इनको दो दिन से पेट में दाहिनी तरफ बहुत तेज दर्द हो रहा है... साथ में उल्टी और बुखार भी है... जांच करने पर मर्फी साइन पॉजिटिव है... पेट का अल्ट्रासाउंड करवाया है... उसमें गॉल ब्लैडर में स्टोन और सूजन है... तो डायग्नोसिस है एक्यूट कैलकुलस कोलीसिस्टाइटिस... अभी इनको भर्ती करना है... सर्जरी की जरूरत पड़ेगी... इनको अभी दर्द और इन्फेक्शन के लिए दवाइयां शुरू करो... इंजेक्शन Tramadol 50mg IV... जब दर्द हो तब... इंजेक्शन Ceftriaxone 1 gram IV दिन में दो बार... इंजेक्शन Metronidazole 500mg IV दिन में तीन बार... और इनको NBM रखो... मतलब मुंह से कुछ नहीं देना है... IV fluids Dextrose Normal Saline... 1 litre 8 hourly... सर्जन को तुरंत बुलाओ... टेस्ट में CBC LFT KFT करवा लो.",
        "रोगी का नाम है आशा कुमारी... उम्र 28 वर्ष... यह तीन महीने की गर्भवती है... रेगुलर चेकअप के लिए आई है... इनको सुबह के समय बहुत उल्टी आती है... और कमजोरी महसूस होती है... जांच में इनका ब्लड प्रेशर ठीक है... वजन भी ठीक है... डायग्नोसिस है मॉर्निंग सिकनेस... इनको दवा देनी है और कुछ सलाह देनी है... Tablet Doxylamine and Pyridoxine... एक गोली रात को सोने से पहले... और एक सुबह... अगर जरूरत पड़े तो... Capsule Folic acid 5mg... रोज दोपहर में एक... इनको छोटे और बार-बार भोजन करने की सलाह दें... ज्यादा तेल वाला खाना न खाएं... टेस्ट में हीमोग्लोबिन और ब्लड ग्रुप करवा लें... अगले महीने फॉलो अप के लिए आएं... 15 अक्टूबर को.",
        "यह बच्चा है... राहुल... उम्र 5 साल... इसकी माँ इसे लेकर आई है... शिकायत है कि इसके पेट में कीड़े हैं... और यह रात को दांत पीसता है... भूख भी कम लगती है... जांच में कुछ खास नहीं मिला... वजन ठीक है... डायग्नोसिस है... वर्म इन्फेस्टेशन... पेट के कीड़े... इसको कीड़े की दवा देनी है... Syrup Albendazole... 5 ml... नहीं... 10 ml की पूरी बोतल एक बार में देनी है... रात को सोने से पहले... और दो हफ्ते बाद एक और डोज़ देनी है... घर के सभी सदस्यों को यह दवा लेने की सलाह दें... और... बस."
    ],
    'Marathi': [
        "ही पेशंट आहे... सुनीता पाटील वय ४० वर्षे... गेल्या दोन महिन्यांपासून खूप कोरडा खोकला येतो आहे... रात्री जास्त होतो... दम पण लागतो... तपासणी केली असता छातीत घरघर आवाज येतोय... बायलॅटरल व्हीज आहे... इम्प्रेशन आहे ब्रॉन्कियल अस्थमा... प्लॅन आहे की यांना इन्हेलर आणि काही गोळ्या सुरू करायच्या... लिहून घ्या... Seroflo Inhaler 250... दोन पफ सकाळी आणि दोन पफ रात्री घ्यायचे... टॅब्लेट Montelukast Levocetirizine रात्री एक... पंधरा दिवसांसाठी... गरज पडल्यास Asthalin Inhaler वापरा... यांना स्पायरोमेट्री टेस्ट करायला सांगा... आणि दोन आठवड्यांनी फॉलो अप साठी यायला सांगा... 29 सप्टेंबरला.",
        "हा रुग्ण आहे... प्रकाश जोशी वय ६५... यांना चालताना दोन्ही पायांच्या पोटऱ्यांमध्ये दुखतं... थोडं चालल्यावर थांबावं लागतं... तपासणी केली असता पायांच्या नाड्या... डॉर्सेलिस पेडिस आर्टरी... खूप कमी जाणवत आहेत... इम्प्रेशन आहे पेरिफेरल आर्टेरियल डिसीज... यांना कलर डॉप्लर स्टडी करायला सांगा... दोन्ही पायांचा... औषधं लिहून घ्या... Tablet Clopidogrel 75mg... रोज दुपारी एक... Tablet Cilostazol 50mg... दिवसातून दोन वेळा... आणि स्टॅटिन द्या... Atorvastatin 20mg रात्री एक... यांना स्मोकिंग पूर्णपणे बंद करायला सांगा... आणि रोज थोडं चालायला सांगा... रिपोर्ट घेऊन एका आठवड्याने परत या."
    ],
    'Punjabi': [
        "ਮਰੀਜ਼ ਦਾ ਨਾਮ ਗੁਰਮੀਤ ਸਿੰਘ ਉਮਰ 45 ਸਾਲ... ਮੁੱਖ ਸ਼ਿਕਾਇਤ ਹੈ ਕਿ ਪਿਛਲੇ 3 ਦਿਨਾਂ ਤੋਂ ਪਿਸ਼ਾਬ ਵਿਚ ਜਲਣ ਅਤੇ ਵਾਰ-ਵਾਰ ਪਿਸ਼ਾਬ ਆ ਰਿਹਾ ਹੈ... ਨਾਲ ਹੀ ਬੁਖਾਰ ਵੀ ਹੈ... ਜਾਂਚ ਕਰਨ ਤੇ ਪੇਟ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ਵਿਚ ਦਰਦ ਹੈ... ਡਾਇਗਨੋਸਿਸ ਹੈ ਯੂਰਿਨਰੀ ਟ੍ਰੈਕਟ ਇਨਫੈਕਸ਼ਨ... ਪਲੈਨ ਹੈ ਐਂਟੀਬਾਇਓਟਿਕ ਸ਼ੂਰੂ ਕਰਨ ਦਾ... ਦਵਾਈ ਲਿਖੋ... Tablet Nitrofurantoin 100mg ਦਿਨ ਵਿੱਚ ਦੋ ਵਾਰ... ਸੱਤ ਦਿਨਾਂ ਲਈ... Tablet Paracetamol 500mg ਜੇ ਬੁਖਾਰ ਹੋਵੇ ਤਾਂ... ਮਰੀਜ਼ ਨੂੰ ਬਹੁਤ ਸਾਰਾ ਪਾਣੀ ਪੀਣ ਲਈ ਕਹੋ... Urine routine and culture test ਕਰਵਾਓ... ਰਿਪੋਰਟਾਂ ਲੈ ਕੇ ਤਿੰਨ ਦਿਨ ਬਾਅਦ ਦੁਬਾਰਾ ਆਉਣਾ ਹੈ... 20 ਸਤੰਬਰ ਨੂੰ.",
        "ਇਹ ਮਰੀਜ਼ ਹੈ ਬਲਜੀਤ ਕੌਰ... 62 ਸਾਲ ਦੀ ਔਰਤ... ਸ਼ੂਗਰ ਅਤੇ ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ ਦੀ ਪੁਰਾਣੀ ਮਰੀਜ਼... ਅੱਜ ਸਵੇਰੇ ਅਚਾਨਕ ਬੋਲਣ ਵਿੱਚ ਤਕਲੀਫ ਹੋਈ... ਅਤੇ ਸਰੀਰ ਦਾ ਸੱਜਾ ਪਾਸਾ ਕਮਜ਼ੋਰ ਹੋ ਗਿਆ... ਓਨ ਐਗਜ਼ਾਮੀਨੇਸ਼ਨ... ਪਾਵਰ... ਨਹੀਂ... ਸੱਜੇ ਪਾਸੇ ਦੀ ਪਾਵਰ 2/5 ਹੈ... ਫੇਸ਼ੀਅਲ ਡੀਵੀਏਸ਼ਨ ਵੀ ਹੈ... ਡਾਇਗਨੋਸਿਸ ਹੈ... ਸੇਰੇਬਰੋਵੈਸਕੁਲਰ ਐਕਸੀਡੈਂਟ... ਮਤਲਬ ਸਟ੍ਰੋਕ... ਇਹਨਾਂ ਨੂੰ ਤੁਰੰਤ ਦਾਖਲ ਕਰੋ... CT scan brain ਕਰਵਾਓ... ਇਹਨਾਂ ਦੀ ਸ਼ੂਗਰ ਅਤੇ ਬੀਪੀ ਕੰਟਰੋਲ ਕਰੋ... ਦਵਾਈ ਸ਼ੁਰੂ ਕਰੋ... Injection Mannitol 100ml IV... 8 ਘੰਟੇ ਬਾਅਦ... Tablet Aspirin Clopidogrel combination... ਇੱਕ ਗੋਲੀ ਰੋਜ਼ਾਨਾ... Atorvastatin 40mg ਰਾਤ ਨੂੰ... ਨਿਊਰੋਲੋਜਿਸਟ ਨੂੰ consult ਕਰੋ..."
    ]
}

doctor_patient_dictation = {
    'English': [
        """Doctor: Good morning Mr. Sharma, please have a seat. What brings you in today?
Patient: Good morning, doctor. I've been having this chest pain for the past two days. It feels heavy, right in the center.
Doctor: I see. Does the pain go anywhere else? Like your arm or jaw?
Patient: Yes, it sometimes goes to my left arm. I also feel a bit breathless when it happens.
Doctor: And when do you feel this pain? Is it during rest or while walking?
Patient: Mostly when I walk a little fast or climb the stairs. I feel better when I rest.
Doctor: Okay. Do you have a history of high blood pressure or diabetes?
Patient: Yes, doctor. I have had high blood pressure for the last five years.
Doctor: Alright. Based on your symptoms, it could be angina. We need to run some tests to be sure. I'll order an ECG and a stress test for you. For now, I am prescribing Tablet Sorbitrate 5mg to be kept under your tongue if you get the pain. And Tablet Aspirin 75mg once daily after food. Please get the tests done and see me with the reports.
Patient: Okay doctor, thank you.""",
        """Doctor: Hello, please bring the child here. What is the problem?
Patient: Doctor, my son Rahul has had a high fever and a bad cough for three days. He is not eating anything.
Doctor: Okay, let me check him. Does he have a runny nose as well?
Patient: Yes, a little bit. He also complains of a headache.
Doctor: I'm checking his chest... there is some congestion. It seems like a viral infection, which is very common in this weather.
Patient: Is it serious, doctor?
Doctor: No, not at all. We just need to manage the symptoms. I am prescribing Syrup Paracetamol, 5 ml, three times a day for the fever. For the cough, give him Syrup Ambroxol, 2.5 ml twice a day.
Patient: Okay, doctor.
Doctor: Make sure he drinks plenty of fluids, like water and juice. Give him light food like khichdi. If the fever doesn't go down in two days or if he has trouble breathing, bring him back immediately.
Patient: Thank you so much, doctor.""",
        """Doctor: Hello Mrs. Gupta. You said you've been feeling breathless?
Patient: Yes doctor. For the past month, I get breathless even with a little bit of work. And I have a dry cough, especially at night.
Doctor: Do you hear any whistling sound from your chest while breathing?
Patient: Yes, sometimes I do. It gets very scary.
Doctor: I understand. Do you have any allergies? Or a family history of asthma?
Patient: My father had asthma.
Doctor: Okay. Your symptoms are suggestive of bronchial asthma. We need to do a test called Spirometry or a Pulmonary Function Test to confirm it.
Patient: Okay doctor.
Doctor: In the meantime, I am prescribing an inhaler. Seroflo Inhaler 250, you need to take two puffs in the morning and two at night. I will show you how to use it correctly. I'm also giving you a tablet, Montelukast 10mg, one tablet at bedtime.
Patient: Will I have to take this for life?
Doctor: Not necessarily. We will adjust the dose based on your response. Get the test done and see me in two weeks.
Patient: Thank you, doctor."""
    ],
    'Hindi': [
        """Doctor: नमस्ते, आइए बैठिए। बताइए क्या तकलीफ है?
Patient: नमस्ते डॉक्टर साहब। मेरे पेट में दो-तीन दिन से बहुत जलन हो रही है। खट्टी डकारें भी आती हैं।
Doctor: अच्छा, ये जलन खाने से पहले होती है या बाद में?
Patient: खाने के बाद ज़्यादा होती है डॉक्टर, और रात में सोते समय भी।
Doctor: क्या आपको मसालेदार या तला हुआ खाना पसंद है?
Patient: हाँ डॉक्टर, मैं बाहर का खाना काफी खाता हूँ।
Doctor: हम्म, यह एसिडिटी और शायद GERD की समस्या लग रही है। आपको अपनी जीवनशैली में कुछ बदलाव करने होंगे।
Patient: जी डॉक्टर।
Doctor: मैं आपको कुछ दवाइयां लिख रहा हूँ। Capsule Pantoprazole 40mg, रोज़ सुबह खाली पेट एक लेना है। और एक सिरप है, Sucralfate, दो चम्मच दिन में तीन बार खाने से पहले।
Patient: ठीक है डॉक्टर साहब।
Doctor: और हाँ, मसालेदार खाना, चाय, कॉफ़ी अभी कुछ दिन के लिए बंद कर दें। रात का खाना सोने से कम से कम दो घंटे पहले खाएं। एक हफ्ते बाद फिर दिखाइए।
Patient: जी, धन्यवाद डॉक्टर।""",
        """Doctor: नमस्ते, क्या हुआ?
Patient: डॉक्टर, मेरे गले में बहुत दर्द है और कुछ भी निगलने में परेशानी हो रही है।
Doctor: कब से है यह दिक्कत?
Patient: कल रात से है। और आज सुबह से कान में भी हल्का दर्द शुरू हो गया है।
Doctor: ठीक है, मुँह खोलिए... आआआ करें। हाँ, आपके टॉन्सिल में सूजन है। यह एक बैक्टीरियल इन्फेक्शन लग रहा है।
Patient: जी।
Doctor: आपको बुखार भी है?
Patient: हाँ, हल्का सा लग रहा है।
Doctor: मैं आपको एक एंटीबायोटिक दे रहा हूँ। Tablet Amoxicillin 625mg, दिन में दो बार, खाने के बाद। इसे पाँच दिन तक लेना है, कोर्स पूरा करना।
Patient: ठीक है डॉक्टर।
Doctor: दर्द के लिए Tablet Paracetamol ले सकते हैं। और गरारे करें, गर्म पानी में नमक डालकर दिन में तीन-चार बार।
Patient: जी।
Doctor: ठंडा पानी और ठंडी चीजें बिल्कुल न खाएं। दो दिन में आराम मिल जाएगा।
Patient: धन्यवाद डॉक्टर साहब।"""
    ],
    'Marathi': [
        """Doctor: नमस्कार काकू, या बसा. काय त्रास होतोय?
Patient: नमस्कार डॉक्टर. माझा हा उजवा गुडघा खूप दुखतोय गेल्या महिन्यापासून. चालताना आणि जिने चढताना खूप त्रास होतो.
Doctor: बरं. गुडघ्यावर सूज वगैरे आहे का? किंवा सकाळी उठल्यावर गुडघा आखडल्यासारखा वाटतो का?
Patient: हो डॉक्टर, सकाळी जास्त दुखतो आणि थोडी सूज पण वाटते.
Doctor: ठीक आहे. तुमचं वय किती आहे?
Patient: मी ६२ वर्षांची आहे.
Doctor: या वयात गुडघेदुखी सामान्य आहे. हा संधिवाताचा प्रकार असू शकतो. मी तुमचा गुडघा तपासतो.
Patient: हो डॉक्टर.
Doctor: वेदना आहेत. मी तुम्हाला गुडघ्याचा एक्स-रे काढायला सांगतो. तोपर्यंत काही औषधं देतो. Tablet Etoricoxib 60mg, दिवसातून एकदा जेवणानंतर घ्या. आणि लावण्यासाठी एक मलम देतोय.
Patient: बरं डॉक्टर.
Doctor: जास्त वेळ उभे राहू नका आणि जमिनीवर बसणे टाळा. एक्स-रे रिपोर्ट घेऊन पुढच्या आठवड्यात या.
Patient: ठीक आहे डॉक्टर.""",
        """Doctor: या, बसा. बोला, काय होत आहे?
Patient: डॉक्टर, माझी डोकेदुखी अजिबात कमी होत नाहीये. जवळजवळ दहा दिवसांपासून डोकं दुखतंय.
Doctor: डोकं कोणत्या बाजूला जास्त दुखतं? की संपूर्ण डोकं दुखतं?
Patient: बहुतेक वेळा डाव्या बाजूला दुखतं आणि कधीकधी डोळ्यांवर पण दाब येतो.
Doctor: तुम्हाला यासोबत मळमळ किंवा उलटीसारखं होतं का?
Patient: हो, कधीकधी मळमळतं.
Doctor: तुम्हाला प्रकाशाचा किंवा आवाजाचा त्रास होतो का डोकेदुखीच्या वेळी?
Patient: हो डॉक्टर, खूप होतो. अंधार्या खोलीत बरं वाटतं.
Doctor: ठीक आहे. ही लक्षणं मायग्रेनची आहेत. तुम्हाला काही गोष्टी टाळाव्या लागतील.
Patient: काय डॉक्टर?
Doctor: जास्त वेळ उपाशी राहू नका, झोप पूर्ण घ्या आणि तणावापासून दूर रहा. मी तुम्हाला आता काही औषधं देतो. Tablet Naproxen 500mg, जेव्हा डोकेदुखी सुरू होईल तेव्हा एक घ्या. आणि Tablet Propranolol 20mg, रोज रात्री एक.
Patient: बरं डॉक्टर.
Doctor: पंधरा दिवसांनी परत येऊन दाखवा.
Patient: हो, नक्की. धन्यवाद.""",
        """Doctor: नमस्ते पाटील साहब, कैसे हैं? शुगर कैसी चल रही है?
Patient: नमस्ते डॉक्टर, ठीक है। मैंने कल ही जाँची थी, खाने के बाद 180 थी।
Doctor: हम्म, थोड़ी ज़्यादा है। दवाइयाँ समय पर ले रहे हैं?
Patient: हाँ डॉक्टर, दवा तो रोज़ लेता हूँ। पर कभी-कभी मीठा खाने का मन कर जाता है।
Doctor: वही तो कंट्रोल करना है पाटील साहब। क्या आप सैर करने जाते हैं?
Patient: नहीं डॉक्टर, आजकल काम की वजह से समय नहीं मिलता।
Doctor: देखिये, सिर्फ दवा से शुगर कंट्रोल नहीं होगी। आपको रोज़ कम से कम 30 मिनट तेज़ चलना होगा और खाने-पीने का परहेज़ करना होगा।
Patient: जी डॉक्टर, मैं कोशिश करूंगा।
Doctor: मैं आपकी दवा में थोड़ा बदलाव कर रहा हूँ। Tablet Metformin 500mg, दिन में दो बार चलती रहेगी। इसके साथ Tablet Glimepiride 1mg, नाश्ते से पहले एक गोली शुरू कर रहा हूँ।
Patient: ठीक है डॉक्टर साहब।
Doctor: एक महीने बाद फिर से fasting और PP शुगर की जाँच करवा के रिपोर्ट लेकर आइए।
Patient: जी, ज़रूर। धन्यवाद डॉक्टर"""
    ],
    'Punjabi': [
        """Doctor: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਜੀ, ਬੈਠੋ। ਦੱਸੋ, ਕੀ ਸਮੱਸਿਆ ਹੈ?
Patient: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਡਾਕਟਰ ਸਾਹਿਬ। ਮੇਰੇ ਚਿਹਰੇ 'ਤੇ ਪਿਛਲੇ ਹਫ਼ਤੇ ਤੋਂ ਛੋਟੇ-ਛੋਟੇ ਲਾਲ ਦਾਣੇ ਹੋ ਗਏ ਨੇ ਤੇ ਖਾਰਿਸ਼ ਬਹੁਤ ਹੁੰਦੀ ਹੈ।
Doctor: ਅੱਛਾ, ਕੀ ਤੁਸੀਂ ਕੋਈ ਨਵੀਂ ਕਰੀਮ ਜਾਂ ਸਾਬਣ ਵਰਤਣਾ ਸ਼ੁਰੂ ਕੀਤਾ ਹੈ?
Patient: ਹਾਂਜੀ, ਮੈਂ ਇੱਕ ਨਵਾਂ ਫੇਸ ਵਾਸ਼ ਲਿਆਂਦਾ ਸੀ।
Doctor: ਹੋ ਸਕਦਾ ਹੈ ਤੁਹਾਨੂੰ ਉਸ ਤੋਂ ਐਲਰਜੀ ਹੋ ਗਈ ਹੋਵੇ। ਇਹ ਦਾਣੇ ਸਿਰਫ ਚਿਹਰੇ 'ਤੇ ਹੀ ਹਨ ਜਾਂ ਸਰੀਰ 'ਤੇ ਹੋਰ ਕਿਤੇ ਵੀ?
Patient: ਨਹੀਂ ਜੀ, ਬੱਸ ਚਿਹਰੇ 'ਤੇ ਹੀ ਨੇ।
Doctor: ਠੀਕ ਹੈ। ਫਿਕਰ ਵਾਲੀ ਕੋਈ ਗੱਲ ਨਹੀਂ ਹੈ। ਪਹਿਲਾਂ ਤਾਂ ਉਹ ਨਵਾਂ ਫੇਸ ਵਾਸ਼ ਵਰਤਣਾ ਬੰਦ ਕਰ ਦਿਓ।
Patient: ਠੀਕ ਹੈ ਜੀ।
Doctor: ਮੈਂ ਤੁਹਾਨੂੰ ਇੱਕ ਗੋਲੀ ਤੇ ਇੱਕ ਲਗਾਉਣ ਵਾਲੀ ਕਰੀਮ ਦੇ ਰਿਹਾ ਹਾਂ। Tablet Levocetirizine 5mg, ਰਾਤ ਨੂੰ ਸੌਣ ਵੇਲੇ ਇੱਕ ਲੈਣੀ ਹੈ। ਅਤੇ Hydrocortisone cream, ਦਿਨ ਵਿੱਚ ਦੋ ਵਾਰ ਦਾਣਿਆਂ 'ਤੇ ਹਲਕੀ-ਹਲਕੀ ਲਗਾਉਣੀ ਹੈ।
Patient: ਠੀਕ ਹੈ ਡਾਕਟਰ ਸਾਹਿਬ।
Doctor: ਧੁੱਪ ਤੋਂ ਬਚਾਅ ਰੱਖੋ। ਜੇ ਪੰਜ ਦਿਨਾਂ ਵਿੱਚ ਆਰਾਮ ਨਾ ਆਇਆ ਤਾਂ ਦੁਬਾਰਾ ਆ ਕੇ ਮਿਲਣਾ।
Patient: ਬਹੁਤ ਮਿਹਰਬਾਨੀ ਡਾਕਟਰ ਸਾਹਿਬ।""",
        """Doctor: ਆਓ ਜੀ, ਕੀ ਹਾਲ ਹੈ?
Patient: ਡਾਕਟਰ ਸਾਹਿਬ, ਸਰੀਰ ਵਿੱਚ ਬਹੁਤ ਕਮਜ਼ੋਰੀ ਰਹਿੰਦੀ ਹੈ। ਕੋਈ ਵੀ ਕੰਮ ਕਰਨ ਨੂੰ ਦਿਲ ਨਹੀਂ ਕਰਦਾ।
Doctor: ਇਹ ਕਦੋਂ ਤੋਂ ਹੋ ਰਿਹਾ ਹੈ?
Patient: ਲਗਭਗ ਦੋ-ਤਿੰਨ ਮਹੀਨੇ ਹੋ ਗਏ। ਥਕਾਵਟ ਬਹੁਤ ਜਲਦੀ ਹੋ ਜਾਂਦੀ ਹੈ।
Doctor: ਖਾਣਾ-ਪੀਣਾ ਠੀਕ ਹੈ ਤੁਹਾਡਾ? ਭੁੱਖ ਲੱਗਦੀ ਹੈ?
Patient: ਭੁੱਖ ਤਾਂ ਠੀਕ ਲੱਗਦੀ ਹੈ, ਪਰ ਖਾਣ ਤੋਂ ਬਾਅਦ ਵੀ ਤਾਕਤ ਨਹੀਂ ਮਹਿਸੂਸ ਹੁੰਦੀ।
Doctor: ਨੀਂਦ ਪੂਰੀ ਆਉਂਦੀ ਹੈ ਰਾਤ ਨੂੰ?
Patient: ਹਾਂਜੀ, ਨੀਂਦ ਤਾਂ ਆ ਜਾਂਦੀ ਹੈ।
Doctor: ਠੀਕ ਹੈ। ਕਈ ਵਾਰ ਸਰੀਰ ਵਿੱਚ ਖੂਨ ਦੀ ਜਾਂ ਵਿਟਾਮਿਨ ਦੀ ਕਮੀ ਨਾਲ ਇੱਦਾਂ ਹੁੰਦਾ ਹੈ। ਸਾਨੂੰ ਕੁਝ ਖੂਨ ਦੇ ਟੈਸਟ ਕਰਵਾਉਣੇ ਪੈਣਗੇ।
Patient: ਠੀਕ ਹੈ ਜੀ।
Doctor: ਮੈਂ ਇੱਕ ਕੰਪਲੀਟ ਬਲੱਡ ਕਾਊਂਟ (CBC) ਅਤੇ ਵਿਟਾਮਿਨ B12 ਤੇ D3 ਦਾ ਟੈਸਟ ਲਿਖ ਰਿਹਾ ਹਾਂ। ਰਿਪੋਰਟਾਂ ਆਉਣ ਤੱਕ, ਤੁਸੀਂ ਇੱਕ ਮਲਟੀਵਿਟਾਮਿਨ ਕੈਪਸੂਲ ਰੋਜ਼ਾਨਾ ਇੱਕ ਲੈਣਾ ਸ਼ੁਰੂ ਕਰੋ।
Patient: ਠੀਕ ਹੈ ਡਾਕਟਰ ਸਾਹਿਬ।
Doctor: ਆਪਣੀ ਖੁਰਾਕ ਵਿੱਚ ਹਰੀਆਂ ਸਬਜ਼ੀਆਂ, ਫਲ ਅਤੇ ਦੁੱਧ-ਦਹੀਂ ਸ਼ਾਮਲ ਕਰੋ। ਰਿਪੋਰਟਾਂ ਲੈ ਕੇ ਅਗਲੇ ਹਫ਼ਤੇ ਆਉਣਾ।
Patient: ਜੀ, ਬਹੁਤ ਧੰਨਵਾਦ।"""
    ]
}