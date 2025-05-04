from django.core.management.base import BaseCommand
from quiz_app.models import Quiz, Question, Answer

ISLAMIC_MCQ_POOL = [
    {"question": "Who was the first person to accept Islam?", "options": ["A. Abu Bakr", "B. Ali ibn Abi Talib", "C. Khadijah bint Khuwaylid", "D. Zaid ibn Harithah"], "correct": "C. Khadijah bint Khuwaylid"},
    {"question": "How many daily prayers are obligatory in Islam?", "options": ["A. 3", "B. 5", "C. 4", "D. 6"], "correct": "B. 5"},
    {"question": "What is the Islamic term for fasting?", "options": ["A. Zakat", "B. Hajj", "C. Sawm", "D. Salah"], "correct": "C. Sawm"},
    {"question": "Which month is considered the holiest in Islam?", "options": ["A. Shawwal", "B. Muharram", "C. Ramadan", "D. Rajab"], "correct": "C. Ramadan"},
    {"question": "Which Prophet is known as 'Kalimullah'?", "options": ["A. Musa", "B. Isa", "C. Ibrahim", "D. Nuh"], "correct": "A. Musa"},
    {"question": "What is the name of the Islamic pilgrimage to Makkah?", "options": ["A. Umrah", "B. Hajj", "C. Salah", "D. Zakat"], "correct": "B. Hajj"},
    {"question": "What does 'Zakat' mean in Islam?", "options": ["A. Charity", "B. Prayer", "C. Fasting", "D. Pilgrimage"], "correct": "A. Charity"},
    {"question": "Which Surah is recited in every Rak'ah of prayer?", "options": ["A. Surah Al-Baqarah", "B. Surah Al-Fatiha", "C. Surah Al-Ikhlas", "D. Surah Yasin"], "correct": "B. Surah Al-Fatiha"},
    {"question": "What direction do Muslims face in prayer?", "options": ["A. Jerusalem", "B. Kaaba in Makkah", "C. Medina", "D. Mount Sinai"], "correct": "B. Kaaba in Makkah"},
    {"question": "Who was the first Caliph after the Prophet Muhammad ﷺ?", "options": ["A. Abu Bakr", "B. Umar", "C. Uthman", "D. Ali"], "correct": "A. Abu Bakr"},
    {"question": "What does 'Shahadah' mean?", "options": ["A. Charity", "B. Prayer", "C. Declaration of faith", "D. Fasting"], "correct": "C. Declaration of faith"},
    {"question": "Which Surah is the longest in the Qur'an?", "options": ["A. Surah Al-Baqarah", "B. Surah Al-Imran", "C. Surah Al-Fatiha", "D. Surah Al-Nisa"], "correct": "A. Surah Al-Baqarah"},
    {"question": "Which animal spoke in the Quran?", "options": ["A. Camel", "B. Ant (Surah An-Naml)", "C. Dog", "D. Horse"], "correct": "B. Ant (Surah An-Naml)"},
    {"question": "How many times is the name 'Muhammad' mentioned in the Qur'an?", "options": ["A. 1", "B. 2", "C. 10", "D. 4"], "correct": "D. 4"},
    {"question": "What is the name of the night when the Qur'an was first revealed?", "options": ["A. Laylat al-Qadr", "B. Isra and Mi'raj", "C. Hijrah", "D. Arafah"], "correct": "A. Laylat al-Qadr"},
    {"question": "What is the Islamic ruling on interest (Riba)?", "options": ["A. Permissible", "B. Recommended", "C. Prohibited", "D. Makruh"], "correct": "C. Prohibited"},
    {"question": "How many Makki Surahs are in the Qur'an?", "options": ["A. 28", "B. 86", "C. 114", "D. 29"], "correct": "B. 86"},
    {"question": "Who led the compilation of the Qur'an into one book?", "options": ["A. Abu Bakr", "B. Uthman ibn Affan", "C. Ali", "D. Umar"], "correct": "B. Uthman ibn Affan"},
    {"question": "Which Prophet built the Kaaba with his son?", "options": ["A. Musa", "B. Isa", "C. Ibrahim", "D. Nuh"], "correct": "C. Ibrahim"},
    {"question": "Who is known as the 'Friend of Allah' (Khalilullah)?", "options": ["A. Ibrahim", "B. Musa", "C. Isa", "D. Nuh"], "correct": "A. Ibrahim"},
    {"question": "What is the meaning of 'Islam'?", "options": ["A. Peace", "B. Prayer", "C. Charity", "D. Submission"], "correct": "D. Submission"},
    {"question": "What is the name of the Islamic law derived from the Qur'an and Sunnah?", "options": ["A. Fiqh", "B. Sharia", "C. Hadith", "D. Ijma"], "correct": "B. Sharia"},
    {"question": "What are Hadiths?", "options": ["A. Sayings of the Prophet Muhammad ﷺ", "B. Verses of the Qur'an", "C. Stories of the Companions", "D. Islamic Laws"], "correct": "A. Sayings of the Prophet Muhammad ﷺ"},
    {"question": "Who is the mother of Prophet Isa (Jesus)?", "options": ["A. Aisha", "B. Fatimah", "C. Maryam", "D. Khadijah"], "correct": "C. Maryam"},
    {"question": "What is the smallest Surah in the Qur'an?", "options": ["A. Surah Al-Kawthar", "B. Surah Al-Fatiha", "C. Surah Al-Ikhlas", "D. Surah Al-Asr"], "correct": "A. Surah Al-Kawthar"},
    {"question": "What is the Arabic word for the Day of Judgment?", "options": ["A. Yawm al-Deen", "B. Yawm al-Hisab", "C. Yawm al-Fasl", "D. Yawm al-Qiyamah"], "correct": "D. Yawm al-Qiyamah"},
    {"question": "Who was the wife of the Prophet ﷺ known as 'Mother of the Believers'?", "options": ["A. Khadijah", "B. Aisha", "C. Hafsa", "D. Umm Salamah"], "correct": "A. Khadijah"},
    {"question": "Which angel is responsible for blowing the trumpet?", "options": ["A. Jibreel", "B. Mika'il", "C. Israfil", "D. Malik"], "correct": "C. Israfil"},
    {"question": "What is 'Sunnah'?", "options": ["A. Verses of the Qur'an", "B. The practices of the Prophet Muhammad ﷺ", "C. Islamic Law", "D. Stories of Prophets"], "correct": "B. The practices of the Prophet Muhammad ﷺ"},
    {"question": "What does 'Hijrah' refer to?", "options": ["A. Migration to Madinah", "B. Night Journey", "C. Battle of Badr", "D. Treaty of Hudaybiyyah"], "correct": "A. Migration to Madinah"},
    {"question": "Which Sahabi compiled the Qur'an in the order we have today under Caliph Uthman?", "options": ["A. Ali ibn Abi Talib", "B. Abdullah ibn Mas'ud", "C. Zaid ibn Thabit", "D. Abu Hurairah"], "correct": "C. Zaid ibn Thabit"},
    {"question": "What does the term 'Tafsir' mean?", "options": ["A. Recitation", "B. Explanation of the Qur'an", "C. Translation", "D. Memorization"], "correct": "B. Explanation of the Qur'an"},
    {"question": "What is 'Naskh' in Islamic jurisprudence?", "options": ["A. Ijtihad", "B. Abrogation of rulings", "C. Revelation", "D. Consensus"], "correct": "B. Abrogation of rulings"},
    {"question": "Which Prophet spoke as a baby?", "options": ["A. Yusuf", "B. Isa", "C. Musa", "D. Ibrahim"], "correct": "B. Isa"},
    {"question": "How many categories of Tawheed are there in Islamic theology?", "options": ["A. 3", "B. 2", "C. 4", "D. 5"], "correct": "A. 3"},
    {"question": "What does 'Fiqh' mean?", "options": ["A. Deep understanding of Islamic rulings", "B. Belief", "C. Prayer", "D. Fasting"], "correct": "A. Deep understanding of Islamic rulings"},
    {"question": "Which Surah contains the greatest verse in the Qur'an (Ayat al-Kursi)?", "options": ["A. Al-Baqarah", "B. Al-Imran", "C. Al-Fatiha", "D. Al-Nisa"], "correct": "A. Al-Baqarah"},
    {"question": "What is the punishment for false accusation (Qadhf) in Islam?", "options": ["A. 80 lashes", "B. 50 lashes", "C. Death", "D. 100 lashes"], "correct": "A. 80 lashes"},
    {"question": "Who is the only woman mentioned by name in the Qur'an?", "options": ["A. Maryam", "B. Asiya", "C. Khadijah", "D. Fatimah"], "correct": "A. Maryam"},
    {"question": "Which angel is in charge of rainfall and provision?", "options": ["A. Israfil", "B. Mika'il", "C. Jibreel", "D. Malik"], "correct": "B. Mika'il"},
    {"question": "How many levels are there in Jannah (Paradise) according to Hadith?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "correct": "C. 7"},
    {"question": "What is the Arabic term for analogy in Islamic law?", "options": ["A. Ijma", "B. Qiyas", "C. Naskh", "D. Fard"], "correct": "B. Qiyas"},
    {"question": "Who are the "Ahl al-Kitab" in the Qur'an?", "options": ["A. Jews and Christians", "B. Muslims and Hindus", "C. Disbelievers", "D. Angels and Jinn"], "correct": "A. Jews and Christians"},
    {"question": "What is the term for consensus among scholars in Islamic jurisprudence?", "options": ["A. Qiyas", "B. Ijma", "C. Ijtihad", "D. Hadith"], "correct": "B. Ijma"},
    {"question": "Which Surah was revealed entirely at once?", "options": ["A. Al-Ma'idah", "B. Al-An'am", "C. Al-Baqarah", "D. Al-Furqan"], "correct": "B. Al-An'am"},
    {"question": "What does "Makruh" mean in Islamic rulings?", "options": ["A. Disliked but not sinful", "B. Obligatory", "C. Permissible", "D. Forbidden"], "correct": "A. Disliked but not sinful"},
    {"question": "What is the 'Bayt al-Ma'mur' in Islamic tradition?", "options": ["A. The celestial Kaaba", "B. Angelic palace", "C. Grave", "D. Garden of Paradise"], "correct": "A. The celestial Kaaba"},
    {"question": "Which Surah has two Bismillah?", "options": ["A. Al-Tawbah", "B. Al-Naml", "C. Al-Fatiha", "D. Al-Kahf"], "correct": "B. Al-Naml"},
    {"question": "Which battle is mentioned in Surah Al-Imran?", "options": ["A. Battle of Uhud", "B. Badr", "C. Hunayn", "D. Tabuk"], "correct": "A. Battle of Uhud"},
    {"question": "What is the term for minor ritual impurity?", "options": ["A. Hadath Asghar", "B. Hadath Akbar", "C. Ghusl", "D. Janabah"], "correct": "A. Hadath Asghar"},
    {"question": "Who was the Prophet ﷺ referring to as the "trustworthy of this ummah"?", "options": ["A. Abu Ubaidah ibn al-Jarrah", "B. Abu Bakr", "C. Umar", "D. Uthman"], "correct": "A. Abu Ubaidah ibn al-Jarrah"},
    {"question": "What is the name of the book by Imam Bukhari on Hadith?", "options": ["A. Sahih al-Bukhari", "B. Musnad Ahmad", "C. Muwatta Malik", "D. Sahih Muslim"], "correct": "A. Sahih al-Bukhari"},
    {"question": "How many categories are there in Hadith classification?", "options": ["A. 2", "B. 5", "C. 4", "D. 3"], "correct": "B. 5"},
    {"question": "What is 'Taqwa'?", "options": ["A. God-consciousness", "B. Knowledge", "C. Generosity", "D. Prayer"], "correct": "A. God-consciousness"},
    {"question": "Which Prophet's nation built homes in mountains?", "options": ["A. Nuh", "B. Salih", "C. Hud", "D. Musa"], "correct": "B. Salih"},
    {"question": "Who was given the Zabur?", "options": ["A. Musa", "B. Dawud", "C. Isa", "D. Ibrahim"], "correct": "B. Dawud"},
    {"question": "Which verse is called the verse of Mubahala?", "options": ["A. Surah Al-Imran, 3:61", "B. Surah Baqarah, 2:255", "C. Surah Nisa, 4:34", "D. Surah An-Nur, 24:2"], "correct": "A. Surah Al-Imran, 3:61"},
    {"question": "What does 'Kufr' mean in Islamic terminology?", "options": ["A. Hypocrisy", "B. Disbelief", "C. Ignorance", "D. Pride"], "correct": "B. Disbelief"},
    {"question": "What is 'I'tikaf'?", "options": ["A. Seclusion in mosque for worship", "B. Eid prayer", "C. Dry ablution", "D. Friday sermon"], "correct": "A. Seclusion in mosque for worship"},
    {"question": "Who was Dhu'l Qarnayn according to Qur'an?", "options": ["A. A righteous ruler", "B. A Prophet", "C. A tyrant", "D. A Sahabi"], "correct": "A. A righteous ruler"},
    {"question": "Who is mentioned by name in Surah Al-Tahrim?", "options": ["A. Maryam", "B. Fatimah", "C. Aisha", "D. Zainab"], "correct": "A. Maryam"},
    {"question": "Which Prophet had a kingdom and ruled over humans, jinn and birds?", "options": ["A. Isa", "B. Dawud", "C. Sulaiman", "D. Yusuf"], "correct": "C. Sulaiman"},
    {"question": "Which Surah has the longest verse in the Qur'an?", "options": ["A. Surah Al-Baqarah", "B. Al-Imran", "C. Al-Nisa", "D. Al-Ma'idah"], "correct": "A. Surah Al-Baqarah"},
    {"question": "What is the punishment for theft in Islamic law (if conditions are met)?", "options": ["A. 100 lashes", "B. Hand cutting", "C. Death", "D. Fines"], "correct": "B. Hand cutting"},
    {"question": "What is the meaning of 'Islam' linguistically?", "options": ["A. Prayer", "B. Submission", "C. Peace", "D. Worship"], "correct": "B. Submission"},
    {"question": "Who is the only Prophet mentioned as a Khalifah in Qur'an?", "options": ["A. Dawud", "B. Musa", "C. Yusuf", "D. Isa"], "correct": "A. Dawud"},
    {"question": "Which Surah begins with the letter "Qaf"?", "options": ["A. Surah Qaf", "B. Surah Taha", "C. Surah Rahman", "D. Surah Zumar"], "correct": "A. Surah Qaf"},
    {"question": "How many categories of major sins are there according to Ibn Taymiyyah?", "options": ["A. 3", "B. 5", "C. 7", "D. 70"], "correct": "C. 7"},
    {"question": "Which Prophet is associated with the whale?", "options": ["A. Yunus", "B. Nuh", "C. Musa", "D. Shu'ayb"], "correct": "A. Yunus"},
    {"question": "What is the name of the Islamic eschatological figure who will defeat Dajjal?", "options": ["A. Mahdi", "B. Isa", "C. Khidr", "D. Jibril"], "correct": "B. Isa"},
    {"question": "Which Prophet was thrown into a fire?", "options": ["A. Ibrahim", "B. Yusuf", "C. Nuh", "D. Musa"], "correct": "A. Ibrahim"},
    {"question": "What is the term for a ruling based on benefit and harm analysis?", "options": ["A. Istihsan", "B. Maslahah Mursalah", "C. Qiyas", "D. Ijma"], "correct": "B. Maslahah Mursalah"},
    {"question": "What does 'Bid'ah' mean in Islamic terms?", "options": ["A. Innovation in religion", "B. Prayer", "C. Charity", "D. Backbiting"], "correct": "A. Innovation in religion"},
    {"question": "Which Prophet made du'a to protect his children from Shirk?", "options": ["A. Isa", "B. Ibrahim", "C. Musa", "D. Adam"], "correct": "B. Ibrahim"},
    {"question": "What is the rule of Salah behind an imam?", "options": ["A. Must pray loudly", "B. Must follow exactly", "C. Must recite Fatiha independently", "D. Is invalid"], "correct": "B. Must follow exactly"},
    {"question": "How many authentic Hadith books are in Kutub al-Sittah?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "correct": "B. 6"},
    {"question": "What is the ruling of using gold and silk for men in Islam?", "options": ["A. Permissible", "B. Forbidden", "C. Makruh", "D. Sunnah"], "correct": "B. Forbidden"},
    {"question": "Who were Al-Ashab al-Suffah?", "options": ["A. Poor companions living in Prophet's mosque", "B. Army generals", "C. Tribal leaders", "D. Writers of Hadith"], "correct": "A. Poor companions living in Prophet's mosque"},
    {"question": "Which Surah is equivalent to one-third of the Qur'an?", "options": ["A. Al-Baqarah", "B. Al-Ikhlas", "C. Al-Fatiha", "D. Al-Kahf"], "correct": "B. Al-Ikhlas"},
    {"question": "Which Prophet's people were destroyed by a sound wave?", "options": ["A. Thamud", "B. Madyan", "C. Aad", "D. Banu Israel"], "correct": "A. Thamud"}
]

class Command(BaseCommand):
    help = "Populate the database with one big Islamic quiz using the provided dataset."

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database with one big Islamic quiz...")
        quiz = Quiz.objects.create(
            title="Comprehensive Islamic Quiz",
            description="A comprehensive set of Islamic MCQs (medium/hard)."
        )
        for q in ISLAMIC_MCQ_POOL:
            question = Question.objects.create(
                quiz=quiz,
                text=q["question"]
            )
            for option in q["options"]:
                is_correct = (option == q["correct"])
                Answer.objects.create(
                    question=question,
                    text=option,
                    is_correct=is_correct
                )
        self.stdout.write(self.style.SUCCESS(f"Successfully populated 1 big Islamic quiz with {len(ISLAMIC_MCQ_POOL)} questions!")) 