from django.core.management.base import BaseCommand
from quiz_app.models import Quiz, Question, Answer

# First batch of questions
BATCH_1 = [
    {"question": "Who was the first person to accept Islam?", "options": ["A. Abu Bakr", "B. Ali ibn Abi Talib", "C. Khadijah bint Khuwaylid", "D. Zaid ibn Harithah"], "correct": "C. Khadijah bint Khuwaylid"},
    {"question": "How many daily prayers are obligatory in Islam?", "options": ["A. 3", "B. 5", "C. 4", "D. 6"], "correct": "B. 5"},
    {"question": "What is the Islamic term for fasting?", "options": ["A. Zakat", "B. Hajj", "C. Sawm", "D. Salah"], "correct": "C. Sawm"}
]

# Second batch of questions
BATCH_2 = [
    {"question": "Which month is considered the holiest in Islam?", "options": ["A. Shawwal", "B. Muharram", "C. Ramadan", "D. Rajab"], "correct": "C. Ramadan"},
    {"question": "Which Prophet is known as 'Kalimullah'?", "options": ["A. Musa", "B. Isa", "C. Ibrahim", "D. Nuh"], "correct": "A. Musa"},
    {"question": "What is the name of the Islamic pilgrimage to Makkah?", "options": ["A. Umrah", "B. Hajj", "C. Salah", "D. Zakat"], "correct": "B. Hajj"}
]

# Third batch of questions
BATCH_3 = [
    {"question": "What does 'Zakat' mean in Islam?", "options": ["A. Charity", "B. Prayer", "C. Fasting", "D. Pilgrimage"], "correct": "A. Charity"},
    {"question": "Which Surah is recited in every Rak'ah of prayer?", "options": ["A. Surah Al-Baqarah", "B. Surah Al-Fatiha", "C. Surah Al-Ikhlas", "D. Surah Yasin"], "correct": "B. Surah Al-Fatiha"},
    {"question": "What direction do Muslims face in prayer?", "options": ["A. Jerusalem", "B. Kaaba in Makkah", "C. Medina", "D. Mount Sinai"], "correct": "B. Kaaba in Makkah"}
]

# Fourth batch of questions
BATCH_4 = [
    {"question": "Who was the first Caliph after the Prophet Muhammad ﷺ?", "options": ["A. Abu Bakr", "B. Umar", "C. Uthman", "D. Ali"], "correct": "A. Abu Bakr"},
    {"question": "What does 'Shahadah' mean?", "options": ["A. Charity", "B. Prayer", "C. Declaration of faith", "D. Fasting"], "correct": "C. Declaration of faith"},
    {"question": "Which Surah is the longest in the Qur'an?", "options": ["A. Surah Al-Baqarah", "B. Surah Al-Imran", "C. Surah Al-Fatiha", "D. Surah Al-Nisa"], "correct": "A. Surah Al-Baqarah"}
]

# Fifth batch of questions
BATCH_5 = [
    {"question": "Which animal spoke in the Quran?", "options": ["A. Camel", "B. Ant (Surah An-Naml)", "C. Dog", "D. Horse"], "correct": "B. Ant (Surah An-Naml)"},
    {"question": "How many times is the name 'Muhammad' mentioned in the Qur'an?", "options": ["A. 1", "B. 2", "C. 10", "D. 4"], "correct": "D. 4"},
    {"question": "What is the name of the night when the Qur'an was first revealed?", "options": ["A. Laylat al-Qadr", "B. Isra and Mi'raj", "C. Hijrah", "D. Arafah"], "correct": "A. Laylat al-Qadr"}
]

# Sixth batch of questions
BATCH_6 = [
    {"question": "What is the Islamic ruling on interest (Riba)?", "options": ["A. Permissible", "B. Recommended", "C. Prohibited", "D. Makruh"], "correct": "C. Prohibited"},
    {"question": "How many Makki Surahs are in the Qur'an?", "options": ["A. 28", "B. 86", "C. 114", "D. 29"], "correct": "B. 86"},
    {"question": "Who led the compilation of the Qur'an into one book?", "options": ["A. Abu Bakr", "B. Uthman ibn Affan", "C. Ali", "D. Umar"], "correct": "B. Uthman ibn Affan"}
]

# Seventh batch of questions
BATCH_7 = [
    {"question": "Which Prophet built the Kaaba with his son?", "options": ["A. Musa", "B. Isa", "C. Ibrahim", "D. Nuh"], "correct": "C. Ibrahim"},
    {"question": "Who is known as the 'Friend of Allah' (Khalilullah)?", "options": ["A. Ibrahim", "B. Musa", "C. Isa", "D. Nuh"], "correct": "A. Ibrahim"},
    {"question": "What is the meaning of 'Islam'?", "options": ["A. Peace", "B. Prayer", "C. Charity", "D. Submission"], "correct": "D. Submission"}
]

# Eighth batch of questions
BATCH_8 = [
    {"question": "What is the name of the Islamic law derived from the Qur'an and Sunnah?", "options": ["A. Fiqh", "B. Sharia", "C. Hadith", "D. Ijma"], "correct": "B. Sharia"},
    {"question": "What are Hadiths?", "options": ["A. Sayings of the Prophet Muhammad ﷺ", "B. Verses of the Qur'an", "C. Stories of the Companions", "D. Islamic Laws"], "correct": "A. Sayings of the Prophet Muhammad ﷺ"},
    {"question": "Who is the mother of Prophet Isa (Jesus)?", "options": ["A. Aisha", "B. Fatimah", "C. Maryam", "D. Khadijah"], "correct": "C. Maryam"}
]

# Ninth batch of questions
BATCH_9 = [
    {"question": "What is the smallest Surah in the Qur'an?", "options": ["A. Surah Al-Kawthar", "B. Surah Al-Fatiha", "C. Surah Al-Ikhlas", "D. Surah Al-Asr"], "correct": "A. Surah Al-Kawthar"},
    {"question": "What is the Arabic word for the Day of Judgment?", "options": ["A. Yawm al-Deen", "B. Yawm al-Hisab", "C. Yawm al-Fasl", "D. Yawm al-Qiyamah"], "correct": "D. Yawm al-Qiyamah"},
    {"question": "Who was the wife of the Prophet ﷺ known as 'Mother of the Believers'?", "options": ["A. Khadijah", "B. Aisha", "C. Hafsa", "D. Umm Salamah"], "correct": "A. Khadijah"}
]

# Tenth batch of questions
BATCH_10 = [
    {"question": "Which angel is responsible for blowing the trumpet?", "options": ["A. Jibreel", "B. Mika'il", "C. Israfil", "D. Malik"], "correct": "C. Israfil"},
    {"question": "What is 'Sunnah'?", "options": ["A. Verses of the Qur'an", "B. The practices of the Prophet Muhammad ﷺ", "C. Islamic Law", "D. Stories of Prophets"], "correct": "B. The practices of the Prophet Muhammad ﷺ"},
    {"question": "What does 'Hijrah' refer to?", "options": ["A. Migration to Madinah", "B. Night Journey", "C. Battle of Badr", "D. Treaty of Hudaybiyyah"], "correct": "A. Migration to Madinah"}
]

# Eleventh batch of questions
BATCH_11 = [
    {"question": "Which Sahabi compiled the Qur'an in the order we have today under Caliph Uthman?", "options": ["A. Ali ibn Abi Talib", "B. Abdullah ibn Mas'ud", "C. Zaid ibn Thabit", "D. Abu Hurairah"], "correct": "C. Zaid ibn Thabit"},
    {"question": "What does the term 'Tafsir' mean?", "options": ["A. Recitation", "B. Explanation of the Qur'an", "C. Translation", "D. Memorization"], "correct": "B. Explanation of the Qur'an"},
    {"question": "What is 'Naskh' in Islamic jurisprudence?", "options": ["A. Ijtihad", "B. Abrogation of rulings", "C. Revelation", "D. Consensus"], "correct": "B. Abrogation of rulings"}
]

# Twelfth batch of questions
BATCH_12 = [
    {"question": "Which Prophet spoke as a baby?", "options": ["A. Yusuf", "B. Isa", "C. Musa", "D. Ibrahim"], "correct": "B. Isa"},
    {"question": "How many categories of Tawheed are there in Islamic theology?", "options": ["A. 3", "B. 2", "C. 4", "D. 5"], "correct": "A. 3"},
    {"question": "What does 'Fiqh' mean?", "options": ["A. Deep understanding of Islamic rulings", "B. Belief", "C. Prayer", "D. Fasting"], "correct": "A. Deep understanding of Islamic rulings"}
]

# Thirteenth batch of questions
BATCH_13 = [
    {"question": "Which Surah contains the greatest verse in the Qur'an (Ayat al-Kursi)?", "options": ["A. Al-Baqarah", "B. Al-Imran", "C. Al-Fatiha", "D. Al-Nisa"], "correct": "A. Al-Baqarah"},
    {"question": "What is the punishment for false accusation (Qadhf) in Islam?", "options": ["A. 80 lashes", "B. 50 lashes", "C. Death", "D. 100 lashes"], "correct": "A. 80 lashes"},
    {"question": "Who is the only woman mentioned by name in the Qur'an?", "options": ["A. Maryam", "B. Asiya", "C. Khadijah", "D. Fatimah"], "correct": "A. Maryam"}
]

# Fourteenth batch of questions
BATCH_14 = [
    {"question": "Which angel is in charge of rainfall and provision?", "options": ["A. Israfil", "B. Mika'il", "C. Jibreel", "D. Malik"], "correct": "B. Mika'il"},
    {"question": "How many levels are there in Jannah (Paradise) according to Hadith?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "correct": "C. 7"},
    {"question": "What is the Arabic term for analogy in Islamic law?", "options": ["A. Ijma", "B. Qiyas", "C. Naskh", "D. Fard"], "correct": "B. Qiyas"}
]

# Fifteenth batch of questions
BATCH_15 = [
    {"question": "Who are the 'Ahl al-Kitab' in the Qur'an?", "options": ["A. Jews and Christians", "B. Muslims and Hindus", "C. Disbelievers", "D. Angels and Jinn"], "correct": "A. Jews and Christians"},
    {"question": "What is the term for consensus among scholars in Islamic jurisprudence?", "options": ["A. Qiyas", "B. Ijma", "C. Ijtihad", "D. Hadith"], "correct": "B. Ijma"},
    {"question": "Which Surah was revealed entirely at once?", "options": ["A. Al-Ma'idah", "B. Al-An'am", "C. Al-Baqarah", "D. Al-Furqan"], "correct": "B. Al-An'am"}
]

# Sixteenth batch of questions
BATCH_16 = [
    {"question": "What does 'Makruh' mean in Islamic rulings?", "options": ["A. Disliked but not sinful", "B. Obligatory", "C. Permissible", "D. Forbidden"], "correct": "A. Disliked but not sinful"},
    {"question": "What is the 'Bayt al-Ma'mur' in Islamic tradition?", "options": ["A. The celestial Kaaba", "B. Angelic palace", "C. Grave", "D. Garden of Paradise"], "correct": "A. The celestial Kaaba"},
    {"question": "Which Surah has two Bismillah?", "options": ["A. Al-Tawbah", "B. Al-Naml", "C. Al-Fatiha", "D. Al-Kahf"], "correct": "B. Al-Naml"}
]

# Seventeenth batch of questions
BATCH_17 = [
    {"question": "Which battle is mentioned in Surah Al-Imran?", "options": ["A. Battle of Uhud", "B. Badr", "C. Hunayn", "D. Tabuk"], "correct": "A. Battle of Uhud"},
    {"question": "What is the term for minor ritual impurity?", "options": ["A. Hadath Asghar", "B. Hadath Akbar", "C. Ghusl", "D. Janabah"], "correct": "A. Hadath Asghar"},
    {"question": "Who was the Prophet ﷺ referring to as the 'trustworthy of this ummah'?", "options": ["A. Abu Ubaidah ibn al-Jarrah", "B. Abu Bakr", "C. Umar", "D. Uthman"], "correct": "A. Abu Ubaidah ibn al-Jarrah"}
]

# Eighteenth batch of questions
BATCH_18 = [
    {"question": "What is the name of the book by Imam Bukhari on Hadith?", "options": ["A. Sahih al-Bukhari", "B. Musnad Ahmad", "C. Muwatta Malik", "D. Sahih Muslim"], "correct": "A. Sahih al-Bukhari"},
    {"question": "How many categories are there in Hadith classification?", "options": ["A. 2", "B. 5", "C. 4", "D. 3"], "correct": "B. 5"},
    {"question": "What is 'Taqwa'?", "options": ["A. God-consciousness", "B. Knowledge", "C. Generosity", "D. Prayer"], "correct": "A. God-consciousness"}
]

# Nineteenth batch of questions
BATCH_19 = [
    {"question": "Which Prophet's nation built homes in mountains?", "options": ["A. Nuh", "B. Salih", "C. Hud", "D. Musa"], "correct": "B. Salih"},
    {"question": "Who was given the Zabur?", "options": ["A. Musa", "B. Dawud", "C. Isa", "D. Ibrahim"], "correct": "B. Dawud"},
    {"question": "Which verse is called the verse of Mubahala?", "options": ["A. Surah Al-Imran, 3:61", "B. Surah Baqarah, 2:255", "C. Surah Nisa, 4:34", "D. Surah An-Nur, 24:2"], "correct": "A. Surah Al-Imran, 3:61"}
]

# Twentieth batch of questions
BATCH_20 = [
    {"question": "What does 'Kufr' mean in Islamic terminology?", "options": ["A. Hypocrisy", "B. Disbelief", "C. Ignorance", "D. Pride"], "correct": "B. Disbelief"},
    {"question": "What is 'I'tikaf'?", "options": ["A. Seclusion in mosque for worship", "B. Eid prayer", "C. Dry ablution", "D. Friday sermon"], "correct": "A. Seclusion in mosque for worship"},
    {"question": "Who was Dhu'l Qarnayn according to Qur'an?", "options": ["A. A righteous ruler", "B. A Prophet", "C. A tyrant", "D. A Sahabi"], "correct": "A. A righteous ruler"}
]

# Twenty-first batch of questions
BATCH_21 = [
    {"question": "Who is mentioned by name in Surah Al-Tahrim?", "options": ["A. Maryam", "B. Fatimah", "C. Aisha", "D. Zainab"], "correct": "A. Maryam"},
    {"question": "Which Prophet had a kingdom and ruled over humans, jinn and birds?", "options": ["A. Isa", "B. Dawud", "C. Sulaiman", "D. Yusuf"], "correct": "C. Sulaiman"},
    {"question": "Which Surah has the longest verse in the Qur'an?", "options": ["A. Surah Al-Baqarah", "B. Al-Imran", "C. Al-Nisa", "D. Al-Ma'idah"], "correct": "A. Surah Al-Baqarah"}
]

# Twenty-second batch of questions
BATCH_22 = [
    {"question": "What is the punishment for theft in Islamic law (if conditions are met)?", "options": ["A. 100 lashes", "B. Hand cutting", "C. Death", "D. Fines"], "correct": "B. Hand cutting"},
    {"question": "What is the meaning of 'Islam' linguistically?", "options": ["A. Prayer", "B. Submission", "C. Peace", "D. Worship"], "correct": "B. Submission"},
    {"question": "Who is the only Prophet mentioned as a Khalifah in Qur'an?", "options": ["A. Dawud", "B. Musa", "C. Yusuf", "D. Isa"], "correct": "A. Dawud"}
]

# Twenty-third batch of questions
BATCH_23 = [
    {"question": "Which Surah begins with the letter 'Qaf'?", "options": ["A. Surah Qaf", "B. Surah Taha", "C. Surah Rahman", "D. Surah Zumar"], "correct": "A. Surah Qaf"},
    {"question": "How many categories of major sins are there according to Ibn Taymiyyah?", "options": ["A. 3", "B. 5", "C. 7", "D. 70"], "correct": "C. 7"},
    {"question": "Which Prophet is associated with the whale?", "options": ["A. Yunus", "B. Nuh", "C. Musa", "D. Shu'ayb"], "correct": "A. Yunus"}
]

# Twenty-fourth batch of questions
BATCH_24 = [
    {"question": "What is the name of the Islamic eschatological figure who will defeat Dajjal?", "options": ["A. Mahdi", "B. Isa", "C. Khidr", "D. Jibril"], "correct": "B. Isa"},
    {"question": "Which Prophet was thrown into a fire?", "options": ["A. Ibrahim", "B. Yusuf", "C. Nuh", "D. Musa"], "correct": "A. Ibrahim"},
    {"question": "What is the term for a ruling based on benefit and harm analysis?", "options": ["A. Istihsan", "B. Maslahah Mursalah", "C. Qiyas", "D. Ijma"], "correct": "B. Maslahah Mursalah"}
]

# Twenty-fifth batch of questions
BATCH_25 = [
    {"question": "What does 'Bid'ah' mean in Islamic terms?", "options": ["A. Innovation in religion", "B. Prayer", "C. Charity", "D. Backbiting"], "correct": "A. Innovation in religion"},
    {"question": "Which Prophet made du'a to protect his children from Shirk?", "options": ["A. Isa", "B. Ibrahim", "C. Musa", "D. Adam"], "correct": "B. Ibrahim"},
    {"question": "What is the rule of Salah behind an imam?", "options": ["A. Must pray loudly", "B. Must follow exactly", "C. Must recite Fatiha independently", "D. Is invalid"], "correct": "B. Must follow exactly"}
]

# Twenty-sixth batch of questions
BATCH_26 = [
    {"question": "How many authentic Hadith books are in Kutub al-Sittah?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "correct": "B. 6"},
    {"question": "What is the ruling of using gold and silk for men in Islam?", "options": ["A. Permissible", "B. Forbidden", "C. Makruh", "D. Sunnah"], "correct": "B. Forbidden"},
    {"question": "Who were Al-Ashab al-Suffah?", "options": ["A. Poor companions living in Prophet's mosque", "B. Army generals", "C. Tribal leaders", "D. Writers of Hadith"], "correct": "A. Poor companions living in Prophet's mosque"}
]

# Twenty-seventh batch of questions
BATCH_27 = [
    {"question": "Which Surah is equivalent to one-third of the Qur'an?", "options": ["A. Al-Baqarah", "B. Al-Ikhlas", "C. Al-Fatiha", "D. Al-Kahf"], "correct": "B. Al-Ikhlas"},
    {"question": "Which Prophet's people were destroyed by a sound wave?", "options": ["A. Thamud", "B. Madyan", "C. Aad", "D. Banu Israel"], "correct": "A. Thamud"}
]

# Twenty-eighth batch of questions
BATCH_28 = [
    {"question": "What is the term for the legal ruling that allows flexibility in certain circumstances in Islamic law?", "options": ["A. Ijma", "B. Istihsan", "C. Qiyas", "D. Ijtihad"], "correct": "B. Istihsan"},
    {"question": "Which of the following is a legitimate source of Islamic law?", "options": ["A. The opinions of kings", "B. Consensus of philosophers", "C. Consensus of scholars", "D. Individual reasoning"], "correct": "C. Consensus of scholars"},
    {"question": "In which battle did the Muslims lose due to disobedience to the Prophet ﷺ?", "options": ["A. Battle of Badr", "B. Battle of Uhud", "C. Battle of Khandaq", "D. Battle of Hunayn"], "correct": "B. Battle of Uhud"},
    {"question": "Which Prophet was known for his patience through trials and hardship?", "options": ["A. Ayub (Job)", "B. Musa", "C. Ibrahim", "D. Yusuf"], "correct": "A. Ayub (Job)"},
    {"question": "Which companion of the Prophet ﷺ is known for his profound knowledge and was called 'Al-Faruq'?", "options": ["A. Umar ibn al-Khattab", "B. Abu Bakr", "C. Ali ibn Abi Talib", "D. Uthman ibn Affan"], "correct": "A. Umar ibn al-Khattab"},
    {"question": "Who was the first woman to accept Islam?", "options": ["A. Khadijah bint Khuwaylid", "B. Fatimah bint Muhammad", "C. Aisha bint Abi Bakr", "D. Umm Salamah"], "correct": "A. Khadijah bint Khuwaylid"},
    {"question": "What does the word 'Sharia' literally mean?", "options": ["A. Path to the water", "B. Book of laws", "C. Light of Islam", "D. Faithful guidance"], "correct": "A. Path to the water"},
    {"question": "Which companion was the first to be martyred in the Battle of Uhud?", "options": ["A. Abu Bakr", "B. Umar ibn al-Khattab", "C. Mus'ab ibn Umair", "D. Zayd ibn Harithah"], "correct": "C. Mus'ab ibn Umair"},
    {"question": "Which Surah contains the longest verse in the Qur'an?", "options": ["A. Surah Al-Fatiha", "B. Surah Al-Baqarah", "C. Surah Al-Baqarah, Verse 282", "D. Surah Al-Nisa"], "correct": "C. Surah Al-Baqarah, Verse 282"},
    {"question": "What is the name of the angel who blew the trumpet to announce the Day of Judgment?", "options": ["A. Jibril", "B. Mikail", "C. Israfil", "D. Malik"], "correct": "C. Israfil"},
    {"question": "Which Prophet is known for his ability to interpret dreams?", "options": ["A. Yusuf", "B. Ibrahim", "C. Musa", "D. Dawud"], "correct": "A. Yusuf"},
    {"question": "Which Islamic month is considered the holiest after Ramadan?", "options": ["A. Shawwal", "B. Muharram", "C. Dhul-Hijjah", "D. Safar"], "correct": "C. Dhul-Hijjah"},
    {"question": "Who was the first caliph of Islam?", "options": ["A. Abu Bakr", "B. Umar ibn al-Khattab", "C. Uthman ibn Affan", "D. Ali ibn Abi Talib"], "correct": "A. Abu Bakr"},
    {"question": "What was the name of the Prophet's ﷺ sword?", "options": ["A. Zulfiqar", "B. Al-Battar", "C. Al-Miqdadi", "D. Al-Shaheed"], "correct": "D. Al-Shaheed"},
    {"question": "What is the Arabic word for 'a person who opposes the truth intentionally'?", "options": ["A. Kafir", "B. Munafiq", "C. Murtad", "D. Dhimmi"], "correct": "A. Kafir"},
    {"question": "What is the name of the book written by Imam Malik?", "options": ["A. Sahih al-Bukhari", "B. Sahih Muslim", "C. Muwatta", "D. Muwatta Malik"], "correct": "D. Muwatta Malik"},
    {"question": "What is the name of the Prophet's ﷺ grandfather?", "options": ["A. Abdul Muttalib", "B. Abu Talib", "C. Al-Harith", "D. Uthman"], "correct": "A. Abdul Muttalib"},
    {"question": "What is the term for a religious ruling based on consensus?", "options": ["A. Qiyas", "B. Ijma", "C. Istihsan", "D. Ijtihad"], "correct": "B. Ijma"},
    {"question": "Who was the first person to establish a state based on the Islamic laws after the death of Prophet ﷺ?", "options": ["A. Umar ibn al-Khattab", "B. Uthman ibn Affan", "C. Abu Bakr", "D. Ali ibn Abi Talib"], "correct": "C. Abu Bakr"},
    {"question": "What does the word 'Jihad' primarily mean in Islam?", "options": ["A. Struggle", "B. War", "C. Striving in the way of Allah", "D. Conquest"], "correct": "C. Striving in the way of Allah"},
    {"question": "Which of the following is a type of Islamic charity?", "options": ["A. Khums", "B. Zakat", "C. Fitra", "D. All of the above"], "correct": "D. All of the above"},
    {"question": "Which Surah is known as the Surah of the Hypocrites?", "options": ["A. Surah Al-Munafiqun", "B. Surah Al-Nisa", "C. Surah Al-Munafiqun", "D. Surah Al-Baqarah"], "correct": "C. Surah Al-Munafiqun"},
    {"question": "Who was the companion that was called 'the Sword of Allah'?", "options": ["A. Abu Bakr", "B. Umar ibn al-Khattab", "C. Khalid ibn al-Walid", "D. Ali ibn Abi Talib"], "correct": "C. Khalid ibn al-Walid"},
    {"question": "Which Surah mentions the story of the people of the cave (Ashab al-Kahf)?", "options": ["A. Surah Al-Araf", "B. Surah Al-Kahf", "C. Surah Al-Imran", "D. Surah Maryam"], "correct": "B. Surah Al-Kahf"},
    {"question": "Which Prophet built the Kaaba along with his son Ismail?", "options": ["A. Ibrahim", "B. Musa", "C. Dawud", "D. Ibrahim"], "correct": "D. Ibrahim"},
    {"question": "What is the name of the woman who nursed Prophet Muhammad ﷺ?", "options": ["A. Amina", "B. Fatima", "C. Halimah al-Sa'diyah", "D. Khadijah"], "correct": "C. Halimah al-Sa'diyah"},
    {"question": "What is the term for the agreement made with the People of the Book (Jews and Christians) to live under Muslim rule?", "options": ["A. Jizyah", "B. Dhimmi", "C. Ummah", "D. Ahl al-Dhimma"], "correct": "D. Ahl al-Dhimma"},
    {"question": "What is the name of the treaty signed by the Prophet ﷺ and the Quraysh at Hudaybiyyah?", "options": ["A. Treaty of Makkah", "B. Treaty of Uhud", "C. Treaty of Hudaybiyyah", "D. Treaty of Badr"], "correct": "C. Treaty of Hudaybiyyah"},
    {"question": "Which Prophet was swallowed by a fish as punishment?", "options": ["A. Musa", "B. Yunus", "C. Yusuf", "D. Isa"], "correct": "B. Yunus"},
    {"question": "Which of the following is NOT a form of Ibadah (worship)?", "options": ["A. Salah", "B. Zakat", "C. Fasting", "D. Materialism"], "correct": "D. Materialism"},
    {"question": "Which of the following is the last Surah revealed to the Prophet ﷺ?", "options": ["A. Al-Nas", "B. Al-Alaq", "C. Al-Nasr", "D. Al-Baqarah"], "correct": "C. Al-Nasr"},
    {"question": "Which of the following angels is responsible for taking the souls of the deceased?", "options": ["A. Israfil", "B. Jibreel", "C. Malak al-Mawt", "D. Mika'il"], "correct": "C. Malak al-Mawt"},
    {"question": "What is the significance of the 'Night of Ascension' (Isra and Mi'raj)?", "options": ["A. The first revelation", "B. The Prophet ﷺ's ascent to the heavens", "C. The victory at Badr", "D. The conquest of Makkah"], "correct": "B. The Prophet ﷺ's ascent to the heavens"},
    {"question": "Which of the following was the Prophet ﷺ's favorite food?", "options": ["A. Dates", "B. Lamb", "C. Barley bread", "D. Fish"], "correct": "C. Barley bread"},
    {"question": "What was the name of the first mosque built in Madinah?", "options": ["A. Masjid al-Haram", "B. Masjid al-Aqsa", "C. Masjid Quba", "D. Masjid al-Nabawi"], "correct": "C. Masjid Quba"},
    {"question": "Who was the last prophet to be sent to a specific nation?", "options": ["A. Isa", "B. Musa", "C. Muhammad ﷺ", "D. Ibrahim"], "correct": "C. Muhammad ﷺ"},
    {"question": "Which Surah has the verse 'This day have I perfected your religion for you'?", "options": ["A. Al-Fatiha", "B. Al-Baqarah", "C. Al-Ma'idah", "D. Al-Ahzab"], "correct": "C. Al-Ma'idah"},
    {"question": "What is the purpose of the Hijrah (migration) from Makkah to Madinah?", "options": ["A. To seek wealth", "B. To escape persecution and establish a community", "C. To spread the message of Islam", "D. To gain political power"], "correct": "B. To escape persecution and establish a community"},
    {"question": "Which of the following events happened first?", "options": ["A. Battle of Uhud", "B. Treaty of Hudaybiyyah", "C. Battle of Badr", "D. Conquest of Makkah"], "correct": "C. Battle of Badr"},
    {"question": "What is the name of the Prophet's ﷺ horse that he rode during the Battle of Badr?", "options": ["A. Al-Buraq", "B. Al-Qaswa", "C. Al-Murtaja", "D. Al-Dulul"], "correct": "C. Al-Murtaja"},
    {"question": "What was the primary objective of the Battle of Uhud?", "options": ["A. To defend Madinah", "B. To defend Islam and Prophet ﷺ", "C. To conquer Makkah", "D. To stop the Quraysh's economic trade"], "correct": "B. To defend Islam and Prophet ﷺ"},
    {"question": "Which of the following hadith books is considered the most authentic after Sahih al-Bukhari?", "options": ["A. Sahih Muslim", "B. Sunan Abu Dawood", "C. Sahih Muslim", "D. Jami' at-Tirmidhi"], "correct": "C. Sahih Muslim"},
    {"question": "Who was the Prophet's ﷺ first scribe of revelation?", "options": ["A. Uthman ibn Affan", "B. Zaid ibn Thabit", "C. Ali ibn Abi Talib", "D. Umar ibn al-Khattab"], "correct": "B. Zaid ibn Thabit"},
    {"question": "Which month is considered the most sacred in Islam?", "options": ["A. Ramadan", "B. Dhul-Hijjah", "C. Muharram", "D. Shawwal"], "correct": "C. Muharram"},
    {"question": "What is the name of the river in Paradise?", "options": ["A. Nile", "B. Euphrates", "C. Al-Kawthar", "D. Tigris"], "correct": "C. Al-Kawthar"},
    {"question": "Who was the first martyr in Islam?", "options": ["A. Umar ibn al-Khattab", "B. Sumayyah bint Khayyat", "C. Ali ibn Abi Talib", "D. Uthman ibn Affan"], "correct": "B. Sumayyah bint Khayyat"},
    {"question": "Which surah is named after a woman?", "options": ["A. Al-Tahrim", "B. Maryam", "C. Nisa", "D. Fatimah"], "correct": "B. Maryam"},
    {"question": "What is the first step in the process of Ijtihad?", "options": ["A. Consultation", "B. Research", "C. Knowledge of the Qur'an and Hadith", "D. Consensus"], "correct": "C. Knowledge of the Qur'an and Hadith"},
    {"question": "Who was the first Muslim scholar to systematically compile the Hadiths?", "options": ["A. Ibn Qayyim", "B. Imam Bukhari", "C. Imam Malik", "D. Imam Shafi'i"], "correct": "B. Imam Bukhari"},
    {"question": "Which of the following is prohibited for Muslims during the Hajj pilgrimage?", "options": ["A. Shaving the head", "B. Cutting nails", "C. Fasting", "D. Offering sacrifices"], "correct": "B. Cutting nails"}
]

class Command(BaseCommand):
    help = "Populate the database with Islamic quiz questions"

    def add_questions(self, quiz, questions):
        for mcq in questions:
            question = Question.objects.create(
                quiz=quiz,
                text=mcq["question"]
            )
            for option in mcq["options"]:
                Answer.objects.create(
                    question=question,
                    text=option,
                    is_correct=(option == mcq["correct"])
                )

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating quiz...")
        
        # Create the quiz
        quiz = Quiz.objects.create(
            title="Islamic Knowledge Quiz",
            description="Test your knowledge of Islamic teachings and history"
        )
        
        # Add questions in batches
        for i, batch in enumerate([BATCH_1, BATCH_2, BATCH_3, BATCH_4, BATCH_5, 
                                 BATCH_6, BATCH_7, BATCH_8, BATCH_9, BATCH_10,
                                 BATCH_11, BATCH_12, BATCH_13, BATCH_14, BATCH_15,
                                 BATCH_16, BATCH_17, BATCH_18, BATCH_19, BATCH_20,
                                 BATCH_21, BATCH_22, BATCH_23, BATCH_24, BATCH_25,
                                 BATCH_26, BATCH_27, BATCH_28], 1):
            self.stdout.write(f"Adding batch {i} of questions...")
            self.add_questions(quiz, batch)
        
        total_questions = sum(len(batch) for batch in [BATCH_1, BATCH_2, BATCH_3, BATCH_4, BATCH_5,
                                                      BATCH_6, BATCH_7, BATCH_8, BATCH_9, BATCH_10,
                                                      BATCH_11, BATCH_12, BATCH_13, BATCH_14, BATCH_15,
                                                      BATCH_16, BATCH_17, BATCH_18, BATCH_19, BATCH_20,
                                                      BATCH_21, BATCH_22, BATCH_23, BATCH_24, BATCH_25,
                                                      BATCH_26, BATCH_27, BATCH_28])
        self.stdout.write(self.style.SUCCESS(f"Successfully created quiz with {total_questions} questions")) 