🤖 Emotion-Aware & Content-Based Recommendation Chatbot

📌 Project Overview

The Emotion-Aware and Content-Based Recommendation Chatbot is an interactive application that recommends songs based on user input such as song name, mood keywords, or emojis.  
The system infers user mood using rule-based logic derived from song metadata (genre and popularity) and emoji mapping, and generates recommendations using content-based filtering techniques.

This project demonstrates the implementation of a content-based recommendation system, basic mood inference, and chatbot-style interaction deployed using Streamlit.

🎯 Objectives
- Infer user mood using rule-based logic based on song metadata and emoji input  
- Generate relevant song recommendations using content-based filtering  
- Build an interactive chatbot-style interface for real-time recommendations

---

🛠️ Technologies Used
Programming Language: Python  

Libraries & Tools:
- TF-IDF
- Cosine Similarity
- Scikit-learn 
- Pandas  

Web / Application Framework:
- Streamlit(for chatbot deployment)

Development Tools:
- VS Code  

---

🧠 System Architecture
- Input Layer: User enters a song name, mood keyword, or emoji through the Streamlit interface  
- Mood Detection Module: Rule-based mood inference using song genre, popularity scores, and emoji mapping  
- Recommendation Engine: Content-based filtering using TF-IDF vectorization and cosine similarity  
- Response Layer: Displays recommended songs with track name and artist in real time


---

⚙️ Project Workflow
1. Dataset loading and preprocessing using Pandas  
2. Feature engineering by combining song metadata (track name, artist, genre)  
3. Rule-based mood detection using genre keywords, popularity scores, and emoji mapping  
4. Text vectorization using TF-IDF  
5. Content-based recommendation using cosine similarity  
6. Chatbot-style response generation  
7. Deployment using Streamlit


---

🚀 Features
- Mood-based song recommendations  
- Content-based filtering using TF-IDF and cosine similarity  
- Interactive user interface using Streamlit  
- Emoji-supported user input  
- Real-time recommendation generation


---

📈 Output
- Classifies songs into moods such as happy, sad, energetic, and chill  
- Generates relevant song recommendations based on song similarity, mood, or emoji input  
- Displays recommended songs with track name and artist in real time  
- Improves user engagement through an interactive Streamlit interface


---

📌 Future Enhancements
- Voice-based chatbot interaction  
- Multi-language support  
- Integration with real-time APIs  
- Use deep learning models for improved emotion accuracy  

---

👩‍💻 Author
Geetha Valluri
