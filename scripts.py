# scripts.py

doctor_dictation = {
    'English': [
        "Patient is Mr. Vikram Singh 65 year old male... chief complaint of chest pain since morning... radiating to the left arm... associated with sweating and shortness of breath... on examination pulse is 110 per minute... BP is 150 by 90... ECG shows ST segment elevation in anterior leads... impression is acute anterior wall myocardial infarction... plan is to admit to the ICU... start thrombolysis... prescription is Injection Streptokinase 1.5 million units IV infusion over one hour... tablet Aspirin 300mg stat... tablet Clopidogrel 300mg stat... followed by 75mg once daily... tablet Atorvastatin 80mg at night... Injection Morphine 2mg IV for pain... Get cardiac enzymes done... Trop T and Trop I... Follow up with cardiology team immediately... let's say on 17 September.",
        "This patient is Rohan a 7 year old boy... brought by his mother with complaints of fever and rash for the last 4 days... the rash started on the face and then spread to the body... it is a maculopapular rash... on examination there is high grade fever... conjunctivitis and Koplik's spots are seen inside the mouth... diagnosis is Measles... treatment is symptomatic... prescribe Syrup Paracetamol 5ml... if fever is high... can be given three times a day... advise plenty of fluids and rest... Vitamin A supplement should be given... one dose today and one tomorrow... Isolation is important to prevent spread... follow up after five days or if symptoms worsen... lets say 22 September... no antibiotics needed for now.",
        "Patient's name is Sameer... age 25... complaint of watery diarrhea and vomiting since last night... about 8 to 10 episodes of loose stools... On examination the patient looks dehydrated... tongue is dry... BP is low 90 by 60... Diagnosis is acute gastroenteritis with moderate dehydration... plan is to admit and start IV fluids... prescribe Injection Ringer's Lactate... 1 litre stat... then 1 litre over 4 hours... Injection Ondansetron 4mg IV for vomiting... Give ORS solution to drink frequently... once he starts tolerating orally... Start antibiotic... Tablet Ofloxacin and Ornidazole... one tablet twice a day for five days... monitor intake output chart... check electrolytes... CBC.",
        "This is a 45-year-old female... Mrs. Anjali Desai... complaining of a persistent dry cough for the last three months... worse at night... associated with occasional wheezing... no history of smoking... Examination reveals bilateral rhonchi on auscultation... Diagnosis is likely adult-onset asthma... Plan is to start inhaled corticosteroids... Prescribe Budesonide and Formoterol inhaler... two puffs twice daily... also Tablet Montelukast 10mg at bedtime... order a pulmonary function test... spirometry... to confirm the diagnosis... follow up in one month.",
        "Patient is a 30-year-old software engineer... Mr. Anand Kumar... presents with neck pain and stiffness for six weeks... pain radiates to the right shoulder... aggravated by long hours of sitting... Examination shows restricted neck movements... and tenderness over the cervical paraspinal muscles... Impression is cervical spondylosis... secondary to poor posture... Plan... physiotherapy for neck strengthening exercises... Prescribe Tablet Aceclofenac and Thiocolchicoside combination... twice daily for five days... and a topical Diclofenac gel for local application... Advise ergonomic adjustments at his workstation.",
        "This is a 58-year-old male... diabetic for 10 years... complaining of burning sensation in both feet... especially at night... On examination... loss of sensation to fine touch and vibration is noted... diagnosis is Diabetic Peripheral Neuropathy... Plan is to manage symptoms and optimize glycemic control... Prescribe Capsule Pregabalin 75mg at bedtime... and Tablet Methylcobalamin once daily... Re-evaluate his current anti-diabetic medication... and advise strict blood sugar monitoring... Follow up with HbA1c report in 3 months.",
        "Patient is a 19-year-old female college student... presenting with multiple painful pimples on her face... for the last six months... On examination... multiple comedones... papules and pustules are seen on the cheeks and forehead... Diagnosis is moderate acne vulgaris... I will prescribe... topical Clindamycin and Nicotinamide gel for morning application... and Adapalene gel for night... also Tablet Doxycycline 100mg once daily for one month... Advise to use a gentle face wash and avoid picking the lesions.",
        "This patient... Mr. Rakesh Verma... age 55... was admitted with high-grade fever and chills... On examination... he has a temperature of 103 Fahrenheit... and splenomegaly... Peripheral smear for malaria is positive for Plasmodium vivax... Diagnosis is Vivax Malaria... Plan is to start antimalarials... Tablet Chloroquine... 1000mg stat... then 500mg after 6 hours... then 500mg daily for two days... followed by Tablet Primaquine... 15mg daily for 14 days to prevent relapse... Monitor for any signs of hemolysis... and advise complete rest."
    ],
    'Hindi': [
        "ये पेशेंट हैं श्रीमती कमला देवी... उम्र 50 साल... इनको दो दिन से पेट में दाहिनी तरफ बहुत तेज दर्द हो रहा है... साथ में उल्टी और बुखार भी है... जांच करने पर मर्फी साइन पॉजिटिव है... पेट का अल्ट्रासाउंड करवाया है... उसमें गॉल ब्लैडर में स्टोन और सूजन है... तो डायग्नोसिस है एक्यूट कैलकुलस कोलीसिस्टाइटिस... अभी इनको भर्ती करना है... सर्जरी की जरूरत पड़ेगी... इनको अभी दर्द और इन्फेक्शन के लिए दवाइयां शुरू करो... इंजेक्शन Tramadol 50mg IV... जब दर्द हो तब... इंजेक्शन Ceftriaxone 1 gram IV दिन में दो बार... इंजेक्शन Metronidazole 500mg IV दिन में तीन बार... और इनको NBM रखो... मतलब मुंह से कुछ नहीं देना है... IV fluids Dextrose Normal Saline... 1 litre 8 hourly... सर्जन को तुरंत बुलाओ... टेस्ट में CBC LFT KFT करवा लो.",
        "रोगी का नाम है आशा कुमारी... उम्र 28 वर्ष... यह तीन महीने की गर्भवती है... रेगुलर चेकअप के लिए आई है... इनको सुबह के समय बहुत उल्टी आती है... और कमजोरी महसूस होती है... जांच में इनका ब्लड प्रेशर ठीक है... वजन भी ठीक है... डायग्नोसिस है मॉर्निंग सिकनेस... इनको दवा देनी है और कुछ सलाह देनी है... Tablet Doxylamine and Pyridoxine... एक गोली रात को सोने से पहले... और एक सुबह... अगर जरूरत पड़े तो... Capsule Folic acid 5mg... रोज दोपहर में एक... इनको छोटे और बार-बार भोजन करने की सलाह दें... ज्यादा तेल वाला खाना न खाएं... टेस्ट में हीमोग्लोबिन और ब्लड ग्रुप करवा लें... अगले महीने फॉलो अप के लिए आएं... 15 अक्टूबर को.",
        "यह बच्चा है... राहुल... उम्र 5 साल... इसकी माँ इसे लेकर आई है... शिकायत है कि इसके पेट में कीड़े हैं... और यह रात को दांत पीसता है... भूख भी कम लगती है... जांच में कुछ खास नहीं मिला... वजन ठीक है... डायग्नोसिस है... वर्म इन्फेस्टेशन... पेट के कीड़े... इसको कीड़े की दवा देनी है... Syrup Albendazole... 5 ml... नहीं... 10 ml की पूरी बोतल एक बार में देनी है... रात को सोने से पहले... और दो हफ्ते बाद एक और डोज़ देनी है... घर के सभी सदस्यों को यह दवा लेने की सलाह दें... और... बस.",
        "पेशेंट का नाम है... सुरेश... उम्र 40 साल... शिकायत है कि तीन दिन से दस्त और उल्टी हो रही है... पेट में मरोड़ भी है... जांच करने पर dehydration के signs हैं... जुबान सूखी है... डायग्नोसिस है एक्यूट गैस्ट्रोएंटेराइटिस... इनको भर्ती करके IV fluid देना होगा... रिंगर्स लैक्टेट... 500ml stat... फिर 8 घंटे में... उल्टी के लिए इंजेक्शन Ondansetron IV दो... और इनको ORS का घोल पिलाते रहो... एंटीबायोटिक में... टैबलेट नॉरफ्लोक्सासिन-टिप्पणी... नहीं... नॉरफ्लोक्सासिन और टिनिडाजोल... दिन में दो बार पांच दिन के लिए... और प्रोबायोटिक सैशे भी दो...",
        "ये मरीज हैं श्रीमती... गीता शर्मा... उम्र 60 साल... इनको घुटनों में दर्द की शिकायत है... खासकर सीढ़ियां चढ़ते हुए... सुबह के समय जकड़न भी रहती है... जांच करने पर घुटनों में crepitus है... एक्स-रे में ऑस्टियोआर्थराइटिस के बदलाव दिख रहे हैं... डायग्नोसिस है ऑस्टियोआर्थराइटिस नी... इनको दवाइयां शुरू करो... टैबलेट Etoricoxib 60mg... रोज एक बार खाने के बाद... और Glucosamine सल्फेट... दिन में एक बार... लगाने के लिए Diclofenac जेल भी दो... फिजियोथेरेपी की सलाह दें... और वजन कम करने के लिए कहें...",
        "रोगी का नाम है... दीपक... उम्र 22 साल... कल शाम को क्रिकेट खेलते हुए टखने में मोच आ गई... बहुत सूजन और दर्द है... On examination... tenderness over the anterior talofibular ligament... एक्स-रे में कोई फ्रैक्चर नहीं है... डायग्नोसिस है Ankle Sprain... Grade 2... प्लान है RICE therapy... मतलब रेस्ट... आइस... कंप्रेशन... और एलिवेशन... दर्द के लिए टैबलेट Zerodol-SP... दिन में दो बार... पांच दिन के लिए... और एक क्रेप बैंडेज बांध दो... दो हफ्ते तक कोई भी स्पोर्ट्स एक्टिविटी नहीं करनी है...",
        "ये पेशेंट हैं... 35 साल की महिला... नाम... संगीता... इनको बार-बार छींकें आती हैं... नाक से पानी बहता है... और आंखों में खुजली होती है... खासकर सुबह के समय... यह लक्षण पिछले कई सालों से हैं... डायग्नोसिस है एलर्जिक राइनाइटिस... इनको एंटी-एलर्जिक दवाइयां देनी हैं... टैबलेट Fexofenadine 120mg... रोज रात को एक... और Fluticasone नेजल स्प्रे... हर नथुने में दो स्प्रे... रोज एक बार... इनको धूल और धुएं से बचने की सलाह दें... फॉलो अप एक महीने बाद...",
        "रोगी का नाम है... अजय सिंह... उम्र 48 साल... इन्हें पिछले 6 महीने से सीने में जलन और खट्टी डकारें आती हैं... रात में लेटने पर दिक्कत बढ़ जाती है... एंडोस्कोपी में ग्रेड ए एसोफैगाइटिस आया है... डायग्नोसिस है गैस्ट्रोएसोफेगल रिफ्लक्स डिजीज... यानी GERD... इनको लाइफस्टाइल मॉडिफिकेशन की सलाह देनी है... और दवा शुरू करनी है... कैप्सूल Esomeprazole 40mg... रोज सुबह खाली पेट... और सिरप Magaldrate and Simethicone... दो चम्मच खाने के बाद... जब जरूरत हो... इनको मसालेदार खाना और चाय-कॉफी कम करने को कहें..."
    ],
    'Marathi': [
        "ही पेशंट आहे... सुनीता पाटील वय ४० वर्षे... गेल्या दोन महिन्यांपासून खूप कोरडा खोकला येतो आहे... रात्री जास्त होतो... दम पण लागतो... तपासणी केली असता छातीत घरघर आवाज येतोय... बायलॅटरल व्हीज आहे... इम्प्रेशन आहे ब्रॉन्कियल अस्थमा... प्लॅन आहे की यांना इन्हेलर आणि काही गोळ्या सुरू करायच्या... लिहून घ्या... Seroflo Inhaler 250... दोन पफ सकाळी आणि दोन पफ रात्री घ्यायचे... टॅब्लेट Montelukast Levocetirizine रात्री एक... पंधरा दिवसांसाठी... गरज पडल्यास Asthalin Inhaler वापरा... यांना स्पायरोमेट्री टेस्ट करायला सांगा... आणि दोन आठवड्यांनी फॉलो अप साठी यायला सांगा... 29 सप्टेंबरला.",
        "हा रुग्ण आहे... प्रकाश जोशी वय ६५... यांना चालताना दोन्ही पायांच्या पोटऱ्यांमध्ये दुखतं... थोडं चालल्यावर थांबावं लागतं... तपासणी केली असता पायांच्या नाड्या... डॉर्सेलिस पेडिस आर्टरी... खूप कमी जाणवत आहेत... इम्प्रेशन आहे पेरिफेरल आर्टेरियल डिसीज... यांना कलर डॉप्लर स्टडी करायला सांगा... दोन्ही पायांचा... औषधं लिहून घ्या... Tablet Clopidogrel 75mg... रोज दुपारी एक... Tablet Cilostazol 50mg... दिवसातून दोन वेळा... आणि स्टॅटिन द्या... Atorvastatin 20mg रात्री एक... यांना स्मोकिंग पूर्णपणे बंद करायला सांगा... आणि रोज थोडं चालायला सांगा... रिपोर्ट घेऊन एका आठवड्याने परत या.",
        "ही पेशंट आहे... सीमा देशमुख... वय ३२ वर्षे... तिला गेल्या आठवड्यापासून ताप... अंगदुखी आणि डोकेदुखी आहे... कालपासून अंगावर पुरळ आले आहेत... तपासणी केली असता... retro-orbital pain आहे... आणि tourniquet test positive आहे... प्लेटलेट काउंट कमी आहे... 70,000... डायग्नोसिस आहे डेंगी फिवर... प्लॅन आहे... तिला ऍडमिट करायचं... आणि symptomatic treatment द्यायची... IV fluids Normal Saline... मॉनिटर करायचं... तापमानासाठी फक्त पॅरासिटामॉल द्या... टॅब्लेट पॅरासिटामॉल 650mg... गरज असेल तेव्हा... आणि भरपूर पाणी प्यायला सांगा... रोज CBC आणि प्लेटलेट काउंट तपासा.",
        "हा रुग्ण... किशोर सावंत... वय 50... दोन दिवसांपासून छातीत जळजळ... आणि आंबट ढेकर येत आहेत... जेवणानंतर त्रास वाढतो... पूर्वी कधीतरी असा त्रास व्हायचा... डायग्नोसिस... ऍसिड पेप्टिक डिसीज... यांना औषधं लिहून द्या... कॅप्सूल Pantoprazole आणि Domperidone... सकाळी उपाशी पोटी एक... आणि अँटासिड सिरप... दोन चमचे जेवणानंतर... तिखट आणि तेलकट पदार्थ टाळायला सांगा... आणि रात्रीचं जेवण झोपण्याच्या दोन तास आधी घ्यायला सांगा... एका आठवड्यानंतर परत बोलवा.",
        "ही 7 वर्षांची मुलगी आहे... रिया... तिला चार दिवसांपासून ताप आणि घसा दुखतोय... तपासणी केली असता... टॉन्सिल्स लाल आणि सुजलेले आहेत... त्यावर पांढरे डाग आहेत... डायग्नोसिस आहे... एक्यूट टॉन्सिलाइटिस... बैक्टीरियल इन्फेक्शन वाटतंय... तिला अँटीबायोटिक सुरू करा... सिरप Amoxicillin-Clavulanic acid... 5 ml दिवसातून दोनदा... पाच दिवसांसाठी... तापासाठी आणि घसादुखीसाठी... सिरप Mefenamic acid द्या... गरज असेल तेव्हा... तिला कोमट पाण्याच्या गुळण्या करायला सांगा... आणि थंड पदार्थ देऊ नका."
    ],
    'Punjabi': [
        "ਮਰੀਜ਼ ਦਾ ਨਾਮ ਗੁਰਮੀਤ ਸਿੰਘ ਉਮਰ 45 ਸਾਲ... ਮੁੱਖ ਸ਼ਿਕਾਇਤ ਹੈ ਕਿ ਪਿਛਲੇ 3 ਦਿਨਾਂ ਤੋਂ ਪਿਸ਼ਾਬ ਵਿਚ ਜਲਣ ਅਤੇ ਵਾਰ-ਵਾਰ ਪਿਸ਼ਾਬ ਆ ਰਿਹਾ ਹੈ... ਨਾਲ ਹੀ ਬੁਖਾਰ ਵੀ ਹੈ... ਜਾਂਚ ਕਰਨ ਤੇ ਪੇਟ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ਵਿਚ ਦਰਦ ਹੈ... ਡਾਇਗਨੋਸਿਸ ਹੈ ਯੂਰਿਨਰੀ ਟ੍ਰੈਕਟ ਇਨਫੈਕਸ਼ਨ... ਪਲੈਨ ਹੈ ਐਂਟੀਬਾਇਓਟਿਕ ਸ਼ੁਰੂ ਕਰਨ ਦਾ... ਦਵਾਈ ਲਿਖੋ... Tablet Nitrofurantoin 100mg ਦਿਨ ਵਿੱਚ ਦੋ ਵਾਰ... ਸੱਤ ਦਿਨਾਂ ਲਈ... Tablet Paracetamol 500mg ਜੇ ਬੁਖਾਰ ਹੋਵੇ ਤਾਂ... ਮਰੀਜ਼ ਨੂੰ ਬਹੁਤ ਸਾਰਾ ਪਾਣੀ ਪੀਣ ਲਈ ਕਹੋ... Urine routine and culture test ਕਰਵਾਓ... ਰਿਪੋਰਟਾਂ ਲੈ ਕੇ ਤਿੰਨ ਦਿਨ ਬਾਅਦ ਦੁਬਾਰਾ ਆਉਣਾ ਹੈ... 20 ਸਤੰਬਰ ਨੂੰ.",
        "ਇਹ ਮਰੀਜ਼ ਹੈ ਬਲਜੀਤ ਕੌਰ... 62 ਸਾਲ ਦੀ ਔਰਤ... ਸ਼ੂਗਰ ਅਤੇ ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ ਦੀ ਪੁਰਾਣੀ ਮਰੀਜ਼... ਅੱਜ ਸਵੇਰੇ ਅਚਾਨਕ ਬੋਲਣ ਵਿੱਚ ਤਕਲੀਫ ਹੋਈ... ਅਤੇ ਸਰੀਰ ਦਾ ਸੱਜਾ ਪਾਸਾ ਕਮਜ਼ੋਰ ਹੋ ਗਿਆ... ਓਨ ਐਗਜ਼ਾਮੀਨੇਸ਼ਨ... ਪਾਵਰ... ਨਹੀਂ... ਸੱਜੇ ਪਾਸੇ ਦੀ ਪਾਵਰ 2/5 ਹੈ... ਫੇਸ਼ੀਅਲ ਡੀਵੀਏਸ਼ਨ ਵੀ ਹੈ... ਡਾਇਗਨੋਸਿਸ ਹੈ... ਸੇਰੇਬਰੋਵੈਸਕੁਲਰ ਐਕਸੀਡੈਂਟ... ਮਤਲਬ ਸਟ੍ਰੋਕ... ਇਹਨਾਂ ਨੂੰ ਤੁਰੰਤ ਦਾਖਲ ਕਰੋ... CT scan brain ਕਰਵਾਓ... ਇਹਨਾਂ ਦੀ ਸ਼ੂਗਰ ਅਤੇ ਬੀਪੀ ਕੰਟਰੋਲ ਕਰੋ... ਦਵਾਈ ਸ਼ੁਰੂ ਕਰੋ... Injection Mannitol 100ml IV... 8 ਘੰਟੇ ਬਾਅਦ... Tablet Aspirin Clopidogrel combination... ਇੱਕ ਗੋਲੀ ਰੋਜ਼ਾਨਾ... Atorvastatin 40mg ਰਾਤ ਨੂੰ... ਨਿਊਰੋਲੋਜਿਸਟ ਨੂੰ consult ਕਰੋ...",
        "ਇਹ ਮਰੀਜ਼ ਹੈ ਜਸਪ੍ਰੀਤ... 25 ਸਾਲ ਦੀ ਕੁੜੀ... ਚਿਹਰੇ 'ਤੇ ਕਿੱਲ ਅਤੇ ਦਾਣਿਆਂ ਦੀ ਸ਼ਿਕਾਇਤ ਲੈ ਕੇ ਆਈ ਹੈ... ਪਿਛਲੇ ਇੱਕ ਸਾਲ ਤੋਂ... ਜਾਂਚ ਕਰਨ 'ਤੇ... oily skin ਅਤੇ blackheads ਹਨ... ਡਾਇਗਨੋਸਿਸ ਹੈ... Acne Vulgaris... ਇਸਨੂੰ ਦਵਾਈ ਲਿਖੋ... ਲਗਾਉਣ ਲਈ... Benzoyl Peroxide gel... ਸਿਰਫ ਦਾਣਿਆਂ 'ਤੇ ਰਾਤ ਨੂੰ... ਅਤੇ ਇੱਕ ਐਂਟੀਬਾਇਓਟਿਕ... Tablet Azithromycin 500mg... ਹਫ਼ਤੇ ਵਿੱਚ ਤਿੰਨ ਦਿਨ... ਇੱਕ ਮਹੀਨੇ ਲਈ... ਇਸਨੂੰ ਤੇਲ ਵਾਲੀਆਂ ਚੀਜ਼ਾਂ ਘੱਟ ਖਾਣ ਲਈ ਕਹੋ... ਅਤੇ ਚਿਹਰਾ ਸਾਫ਼ ਰੱਖਣ ਲਈ ਕਹੋ।",
        "ਮਰੀਜ਼ ਦਾ ਨਾਮ... ਬਲਵਿੰਦਰ ਸਿੰਘ... ਉਮਰ 60 ਸਾਲ... ਪਿਛਲੇ ਕੁਝ ਮਹੀਨਿਆਂ ਤੋਂ... ਖੰਘ ਦੇ ਨਾਲ ਖੂਨ ਆ ਰਿਹਾ ਹੈ... ਭਾਰ ਵੀ ਘੱਟ ਗਿਆ ਹੈ... ਇਹ ਬਹੁਤ ਜ਼ਿਆਦਾ ਸਿਗਰਟ ਪੀਂਦੇ ਸਨ... ਜਾਂਚ ਕਰਨ 'ਤੇ... ਛਾਤੀ ਵਿੱਚ... ਨਹੀਂ... ਛਾਤੀ ਦੇ ਐਕਸ-ਰੇ ਵਿੱਚ ਸੱਜੇ ਫੇਫੜੇ ਵਿੱਚ ਇੱਕ ਸ਼ੱਕੀ ਗੰਢ ਹੈ... ਡਾਇਗਨੋਸਿਸ... ਸ਼ੱਕੀ... Lung malignancy... ਇਹਨਾਂ ਨੂੰ ਦਾਖਲ ਕਰਨਾ ਹੈ... ਅਤੇ CT scan ਛਾਤੀ ਦਾ ਕਰਵਾਉਣਾ ਹੈ... ਬਾਇਓਪਸੀ ਦੀ ਲੋੜ ਪਵੇਗੀ... ਓਨਕੋਲੋਜਿਸਟ ਨੂੰ refer ਕਰੋ... ਅੱਗੇ ਦੀ ਜਾਂਚ ਲਈ।",
        "ਇਹ 5 ਸਾਲ ਦਾ ਬੱਚਾ ਹੈ... ਅਮਨ... ਇਸਨੂੰ ਦੋ ਦਿਨਾਂ ਤੋਂ ਪੇਟ ਦਰਦ ਅਤੇ ਹਰੇ ਰੰਗ ਦੇ ਦਸਤ ਲੱਗੇ ਹੋਏ ਹਨ... ਜਾਂਚ ਕਰਨ 'ਤੇ... dehydration ਦੇ ਲੱਛਣ ਹਨ... ਇਸਨੂੰ ਦਾਖਲ ਕਰੋ... IV fluids ਸ਼ੁਰੂ ਕਰੋ... zinc ਅਤੇ ORS ਦੇ ਘੋਲ ਦੇ ਨਾਲ... ਦਵਾਈ ਵਿੱਚ... Syrup Metronidazole... 5 ml ਦਿਨ ਵਿੱਚ ਤਿੰਨ ਵਾਰ... ਅਤੇ Syrup Zinc... 5 ml ਰੋਜ਼ ਇੱਕ ਵਾਰ... 14 ਦਿਨਾਂ ਲਈ... ਇਸਦੇ ਸਟੂਲ ਦਾ ਸੈਂਪਲ ਜਾਂਚ ਲਈ ਭੇਜੋ..."
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
        """Doctor: Good afternoon, please have a seat. What seems to be the trouble?
Patient: Doctor, I have this very itchy circular rash on my arm for the past week. It seems to be spreading.
Doctor: Let me have a look. Yes, this looks like a classic fungal infection, commonly known as ringworm. Have you been applying any cream on your own?
Patient: I used a regular moisturizing cream, but it didn't help.
Doctor: You should avoid that. It can make it worse. Fungal infections thrive in moisture.
Patient: Oh, I see. What should I do?
Doctor: I am prescribing a cream and a tablet. Apply Clotrimazole cream twice daily on the affected area. Also, take Tablet Fluconazole 150mg once a week, for two weeks.
Patient: Okay, doctor.
Doctor: It's very important to keep the area dry. Wear loose cotton clothes and make sure you dry yourself properly after bathing. Do not share your towel with anyone.
Patient: I will keep that in mind. Thank you, doctor.""",
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
Patient: Thank you, doctor.""",
        """Doctor: Hello, please come in. How may I help you?
Patient: Doctor, my eyes have been red and watery since yesterday morning. There's a lot of itching too.
Doctor: Are both eyes affected?
Patient: It started with one, but now both are red.
Doctor: Is there any sticky discharge, especially after waking up?
Patient: Yes, a little bit of yellowish discharge.
Doctor: Okay, this appears to be a case of infective conjunctivitis. It's quite contagious.
Patient: What should I do to prevent it from spreading?
Doctor: Wash your hands frequently. Do not share your towels or handkerchiefs. And please avoid touching your eyes.
Doctor: I am prescribing an antibiotic eye drop. Moxifloxacin eye drops, put one drop in each eye four times a day for five days.
Patient: Okay, doctor.
Doctor: Also, wear dark glasses if you go out to avoid discomfort from light. It should get better in two to three days.
Patient: Thank you very much, doctor."""
    ],
    'Hindi': [
        """Doctor: नमस्ते, बैठिए। बताइए क्या परेशानी है?
Patient: डॉक्टर साहब, मेरे कान में कल रात से बहुत तेज़ दर्द हो रहा है। ऐसा लग रहा है कुछ बज रहा है अंदर।
Doctor: अच्छा। क्या कान से कोई पानी या पस जैसा कुछ निकल रहा है?
Patient: नहीं, अभी तो सूखा है। पर दर्द बहुत है और हल्का बुखार भी लग रहा है।
Doctor: ठीक है, मैं टॉर्च से देखता हूँ। मुँह खोलिए। गले में खराश है?
Patient: हाँ, थोड़ी सी है।
Doctor: आपके कान के परदे में सूजन और लाली है। यह मिडिल इयर का इन्फेक्शन है, जिसे ओटाइटिस मीडिया कहते हैं।
Patient: यह गंभीर है क्या?
Doctor: नहीं, चिंता मत करिए। मैं आपको कुछ दवाएं दे रहा हूँ। सिप्रोफ्लोक्सासिन इयर ड्रॉप्स, दो बूँदें दिन में तीन बार इसी कान में डालनी हैं। दर्द के लिए टैबलेट आइबूप्रोफेन 400mg दिन में दो बार खाने के बाद ले सकते हैं।
Patient: ठीक है डॉक्टर।
Doctor: कान में पानी न जाने दें। रुई लगाकर नहाएं। तीन दिन में आराम न मिले तो दोबारा आकर दिखाएँ।
Patient: जी, धन्यवाद डॉक्टर साहब।
        """,
        """Doctor: नमस्ते, आइए। क्या हुआ?
Patient: डॉक्टर, मेरे कमर के दाहिनी तरफ से पेट की तरफ बहुत भयंकर दर्द उठ रहा है। लहर जैसा आता है, मैं सीधा नहीं हो पा रहा हूँ।
Doctor: यह दर्द कब से हो रहा है?
Patient: आज सुबह से ही शुरू हुआ है। दर्द के साथ उल्टी जैसा भी लग रहा है।
Doctor: पेशाब करने में कोई जलन या रुकावट? या पेशाब का रंग बदला हुआ लग रहा है?
Patient: हाँ, पेशाब में हल्की जलन है और रंग भी थोड़ा गहरा है।
Doctor: यह लक्षण गुर्दे की पथरी के दर्द के हैं, जिसे रीनल कोलिक कहते हैं।
Patient: अब क्या होगा? दर्द बर्दाश्त नहीं हो रहा।
Doctor: मैं आपको अभी एक दर्द-निवारक इंजेक्शन लगाता हूँ, उससे तुरंत आराम मिलेगा।
Patient: ठीक है डॉक्टर।
Doctor: इसके बाद आप पेट का एक अल्ट्रासाउंड और पेशाब की जाँच करवाइए। उससे पता चल जाएगा कि पथरी कहाँ है और कितनी बड़ी है।
Patient: ठीक है।
Doctor: दिन में कम से कम तीन से चार लीटर पानी ज़रूर पिएँ। जितनी ज़्यादा पेशाब आएगी, छोटी पथरी निकलने की संभावना उतनी बढ़ जाएगी। रिपोर्ट लेकर कल दिखाइए।
Patient: जी डॉक्टर, धन्यवाद।""",
        """Doctor: नमस्ते! बच्चे को क्या हुआ?
Patient: डॉक्टर साहब, इसे कल रात से उल्टी और दस्त लगे हुए हैं। बहुत सुस्त हो गया है।
Doctor: कितनी बार दस्त हुए? पानी जैसा है क्या?
Patient: हाँ, पाँच-छह बार हो गए हैं, बिलकुल पानी जैसे। दो बार उल्टी भी की है। कुछ खा-पी नहीं रहा।
Doctor: देखिए, बच्चों में ऐसे में पानी की कमी होने का डर रहता है। क्या बच्चा पेशाब ठीक से कर रहा है?
Patient: सुबह से बहुत कम किया है।
Doctor: यह चिंता की बात है। यह गैस्ट्रोएन्टराइटिस है। हमें इसे पानी की कमी से बचाना है।
Patient: तो क्या करें?
Doctor: मैं आपको एक ORS का पैकेट दे रहा हूँ। इसे एक लीटर उबले हुए ठंडे पानी में घोलकर हर दस्त के बाद एक कप पिलाइए।
Patient: ठीक है।
Doctor: उल्टी के लिए Domperidone syrup दे रहा हूँ, ढाई ml दिन में तीन बार, खाने से पहले। और एक प्रोबायोटिक सैशे, दिन में एक बार दही या पानी में मिलाकर दें। हल्का खाना जैसे खिचड़ी और केला दें।
Patient: जी डॉक्टर।
Doctor: अगर बच्चा बिलकुल सुस्त हो जाए या दस्त न रुकें, तो तुरंत वापस अस्पताल ले आएँ।
Patient: धन्यवाद डॉक्टर साहब।""",
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
        """Doctor: नमस्कार, या बसा. काय होत आहे?
Patient: डॉक्टर, दोन दिवसांपूर्वी मी एक जड वस्तू उचलली आणि तेव्हापासून माझ्या कमरेत खूप वेदना होत आहेत. मला नीट उभं पण राहता येत नाहीये.
Doctor: बरं. वेदना पायापर्यंत जातात का? किंवा पायाला मुंग्या येतात का?
Patient: नाही, वेदना फक्त कमरेतच आहेत. पण खूप तीव्र आहेत.
Doctor: ठीक आहे. बहुतेक हा स्नायूंचा ताण आहे. मी तुम्हाला तपासतो, जरा उभे रहा. पुढे वाका बघू.
Patient: डॉक्टर, जास्त वाकता येत नाही. खूप दुखतंय.
Doctor: ठीक आहे, बसू शकता. घाबरण्यासारखं काही नाही. हा एक सामान्य स्नायूंचा दुखापत आहे.
Patient: मग आता काय करायचं?
Doctor: मी तुम्हाला काही औषधं देतोय. Tablet Thiocolchicoside, दिवसातून दोनदा जेवणानंतर घ्या. हे स्नायू शिथिल करण्यासाठी आहे. आणि वेदनेसाठी Tablet Aceclofenac घ्या. गरम पाण्याने शेक द्या आणि दोन दिवस पूर्ण आराम करा.
Patient: ठीक आहे डॉक्टर.
Doctor: पुढच्या वेळी जड वस्तू उचलताना काळजी घ्या.
Patient: हो डॉक्टर, धन्यवाद.""",
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
Patient: जी, ज़रूर। धन्यवाद डॉक्टर""",
        """Doctor: नमस्कार, काय होत आहे?
Patient: डॉक्टर, मला काही दिवसांपासून खूप थकवा जाणवत आहे आणि वजन पण वाढल्यासारखं वाटतंय. केस पण खूप गळत आहेत.
Doctor: अच्छा, तुमची झोप पूर्ण होते का?
Patient: हो, झोप तर व्यवस्थित होते, पण सकाळी उठल्यावर ताजेतवानं वाटत नाही.
Doctor: तुम्हाला थंडी जास्त वाजते का हल्ली? आणि त्वचा कोरडी पडली आहे का?
Patient: हो डॉक्टर, दोन्ही गोष्टी होत आहेत.
Doctor: ठीक आहे. ही सर्व लक्षणं थायरॉईडच्या समस्येची असू शकतात, ज्याला हायपोथायरॉईडीझम म्हणतात.
Patient: मग आता काय तपासणी करावी लागेल?
Doctor: आपल्याला रक्ताची तपासणी करावी लागेल. मी तुम्हाला थायरॉईड फंक्शन टेस्ट (TFT) लिहून देतोय. उपाशी पोटी करायची आहे.
Patient: बरं.
Doctor: तोपर्यंत मी तुम्हाला एक मल्टीविटामिनची गोळी देतोय. रोज एक घ्या. रिपोर्ट आल्यावर आपण पुढचं उपचार ठरवू. रिपोर्ट घेऊन पुढच्या आठवड्यात या.
Patient: ठीक आहे डॉक्टर."""
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
        """Doctor: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਸਰਦਾਰ ਜੀ। ਦੱਸੋ ਕੀ ਸੇਵਾ ਕਰੀਏ?
Patient: ਡਾਕਟਰ ਸਾਹਿਬ, ਮੇਰੇ ਢਿੱਡ ਦੇ ਹੇਠਲੇ ਪਾਸੇ, ਸੱਜੇ ਪਾਸੇ ਇੱਕ ਗਿਲਟੀ ਜਿਹੀ ਮਹਿਸੂਸ ਹੁੰਦੀ ਹੈ। ਖੰਘਣ ਵੇਲੇ ਇਹ ਬਾਹਰ ਨੂੰ ਆਉਂਦੀ ਹੈ ਤੇ ਦਰਦ ਵੀ ਕਰਦੀ ਹੈ।
Doctor: ਇਹ ਕਦੋਂ ਤੋਂ ਹੈ?
Patient: ਲਗਭਗ ਦੋ ਮਹੀਨੇ ਹੋ ਗਏ। ਪਹਿਲਾਂ ਛੋਟੀ ਸੀ, ਹੁਣ ਵੱਡੀ ਲੱਗਦੀ ਹੈ।
Doctor: ਠੀਕ ਹੈ, ਇੱਥੇ ਲੇਟ ਜਾਓ। ਮੈਂ ਦੇਖਦਾ ਹਾਂ। ਹੁਣ ਖੰਘੋ ਜ਼ਰਾ। ਹਮਮ... ਇਹ ਇਨਗੁਆਇਨਲ ਹਰਨੀਆ ਹੈ।
Patient: ਇਹ ਕੀ ਹੁੰਦਾ ਹੈ ਜੀ?
Doctor: ਇਸ ਵਿੱਚ ਤੁਹਾਡੀ ਆਂਤੜੀ ਦਾ ਇੱਕ ਛੋਟਾ ਹਿੱਸਾ ਕਮਜ਼ੋਰ ਮਾਸਪੇਸ਼ੀਆਂ ਵਿੱਚੋਂ ਬਾਹਰ ਆ ਜਾਂਦਾ ਹੈ।
Patient: ਕੀ ਇਹ ਦਵਾਈ ਨਾਲ ਠੀਕ ਹੋ ਸਕਦਾ ਹੈ?
Doctor: ਨਹੀਂ, ਇਸਦਾ ਪੱਕਾ ਇਲਾਜ ਸਿਰਫ ਅਪ੍ਰੇਸ਼ਨ ਹੀ ਹੈ। ਦਵਾਈ ਨਾਲ ਸਿਰਫ ਦਰਦ ਘੱਟ ਹੋ ਸਕਦਾ ਹੈ।
Patient: ਅਪ੍ਰੇਸ਼ਨ ਜ਼ਰੂਰੀ ਹੈ?
Doctor: ਹਾਂਜੀ। ਜੇ ਇਸਨੂੰ ਨਾ ਕਰਵਾਇਆ ਜਾਵੇ ਤਾਂ ਇਹ ਫਸ ਸਕਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਗੰਭੀਰ ਸਮੱਸਿਆ ਹੋ ਸਕਦੀ ਹੈ। ਇਹ ਇੱਕ ਛੋਟਾ ਜਿਹਾ ਅਪ੍ਰੇਸ਼ਨ ਹੁੰਦਾ ਹੈ। ਤੁਸੀਂ ਜਦੋਂ ਚਾਹੋ ਦਾਖਲ ਹੋ ਕੇ ਕਰਵਾ ਸਕਦੇ ਹੋ।
Patient: ਠੀਕ ਹੈ ਜੀ, ਮੈਂ ਘਰੇ ਸਲਾਹ ਕਰਕੇ ਦੱਸਦਾ ਹਾਂ।""",
        """Doctor: ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਜੀ, ਆਓ। ਕੀ ਤਕਲੀਫ ਹੈ?
Patient: ਡਾਕਟਰ ਸਾਹਿਬ, ਮੈਨੂੰ ਕੱਲ੍ਹ ਦਾ ਬਹੁਤ ਤੇਜ਼ ਬੁਖਾਰ ਹੈ। ਸਾਰਾ ਸਰੀਰ ਟੁੱਟ ਰਿਹਾ ਹੈ।
Doctor: ਬੁਖਾਰ ਕਿੰਨਾ ਸੀ? ਮਾਪਿਆ ਸੀ?
Patient: ਹਾਂਜੀ, 102 ਸੀ। ਨਾਲੇ ਸਿਰ ਦਰਦ ਤੇ ਗਲ਼ੇ ਵਿੱਚ ਖਰਾਸ਼ ਵੀ ਹੈ।
Doctor: ਖੰਘ ਜਾਂ ਜ਼ੁਕਾਮ ਹੈ?
Patient: ਹਲਕਾ ਜਿਹਾ ਜ਼ੁਕਾਮ ਹੈ।
Doctor: ਠੀਕ ਹੈ। ਅੱਜਕਲ੍ਹ ਮੌਸਮ ਬਦਲ ਰਿਹਾ ਹੈ, ਇਸ ਕਰਕੇ ਵਾਇਰਲ ਬੁਖਾਰ ਬਹੁਤ ਫੈਲਿਆ ਹੋਇਆ ਹੈ। ਇਹ ਉਸਦੇ ਹੀ ਲੱਛਣ ਲੱਗ ਰਹੇ ਨੇ।
Patient: ਕੋਈ ਖਾਸ ਦਵਾਈ?
Doctor: ਇਸ ਵਿੱਚ ਕੋਈ ਐਂਟੀਬਾਇਓਟਿਕ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ। ਤੁਸੀਂ ਸਿਰਫ ਬੁਖਾਰ ਲਈ Tablet Paracetamol 650mg ਲੈ ਸਕਦੇ ਹੋ, ਹਰ ਛੇ ਘੰਟੇ ਬਾਅਦ ਜੇ ਬੁਖਾਰ ਹੋਵੇ ਤਾਂ।
Patient: ਠੀਕ ਹੈ ਜੀ।
Doctor: ਗਰਮ ਪਾਣੀ ਦੇ ਗਰਾਰੇ ਕਰੋ। ਪਾਣੀ, ਜੂਸ ਅਤੇ ਸੂਪ ਵਰਗੀਆਂ ਚੀਜ਼ਾਂ ਵੱਧ ਤੋਂ ਵੱਧ ਪੀਓ। ਦੋ-ਤਿੰਨ ਦਿਨ ਆਰਾਮ ਕਰੋ, ਸਭ ਠੀਕ ਹੋ ਜਾਵੇਗਾ। ਜੇ ਬੁਖਾਰ ਨਾ ਉੱਤਰੇ ਤਾਂ ਦੁਬਾਰਾ ਆਉਣਾ।
Patient: ਬਹੁਤ ਮਿਹਰਬਾਨੀ, ਡਾਕਟਰ ਸਾਹਿਬ।""",
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
