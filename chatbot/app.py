import pandas as pd
import random
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# App Title
# -------------------------------
st.set_page_config(page_title="Spotify Song Recommender", page_icon="🎵")
st.title("🎵 Spotify Song Recommender App")
st.write("Recommend songs by **song name, mood, or emoji**")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("spotify_dataset.csv")
    df = df[['Track Name', 'Artist(s)', 'Genre', 'Popularity']]
    df = df.dropna()
    df.reset_index(drop=True, inplace=True)
    return df

df = load_data()

# Normalize track names
df['track_lower'] = df['Track Name'].str.lower().str.strip()

# -------------------------------
# Mood Detection
# -------------------------------
def detect_mood(row):
    genre = row['Genre'].lower()
    popularity = row['Popularity']

    if popularity >= 70:
        return "happy"
    elif any(word in genre for word in ['dance', 'edm', 'pop']):
        return "energetic"
    elif any(word in genre for word in ['romantic', 'melody', 'sad']):
        return "sad"
    else:
        return "chill"

df['mood'] = df.apply(detect_mood, axis=1)

# -------------------------------
# Content-Based Setup
# -------------------------------
df['combined_features'] = (
    df['Track Name'] + " " +
    df['Artist(s)'] + " " +
    df['Genre']
)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# -------------------------------
# Emoji Mapping
# -------------------------------
emoji_mood_map = {
    "😊": "happy", "😄": "happy",
    "😢": "sad", "😭": "sad",
    "🔥": "energetic", "💃": "energetic",
    "😌": "chill", "🌙": "chill"
}

# -------------------------------
# Recommendation Functions
# -------------------------------
def recommend_by_song(song_name, top_n=5):
    song_name = song_name.lower().strip()
    if song_name not in df['track_lower'].values:
        return None

    idx = df[df['track_lower'] == song_name].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    indices = [i[0] for i in scores[1:top_n+1]]

    return [
        f"{df.iloc[i]['Track Name']} - {df.iloc[i]['Artist(s)']}"
        for i in indices
    ]

def recommend_by_mood(mood, top_n=5):
    mood_songs = df[df['mood'] == mood]
    if mood_songs.empty:
        return None

    sample = mood_songs.sample(min(top_n, len(mood_songs)))
    return [
        f"{row['Track Name']} - {row['Artist(s)']}"
        for _, row in sample.iterrows()
    ]

# -------------------------------
# UI Inputs
# -------------------------------
user_input = st.text_input(
    "Enter a song name, mood (happy/sad/energetic/chill), or emoji 😊 😢 🔥 😌"
)

if st.button("Recommend 🎧"):
    if not user_input:
        st.warning("Please enter a song name, mood, or emoji.")
    else:
        # Emoji
        if user_input in emoji_mood_map:
            mood = emoji_mood_map[user_input]
            results = recommend_by_mood(mood)

        # Mood word
        elif user_input.lower() in ["happy", "sad", "energetic", "chill"]:
            results = recommend_by_mood(user_input.lower())

        # Song name
        else:
            results = recommend_by_song(user_input)

        if not results:
            st.error("No recommendations found. Try another input.")
        else:
            st.subheader("🎶 Recommended Songs")
            for song in results:
                st.write("•", song)

