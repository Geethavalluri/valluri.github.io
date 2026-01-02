import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("spotify_dataset.csv")
df = df[['Track Name', 'Artist(s)', 'Genre', 'Popularity']]
df = df.dropna()
df.reset_index(drop=True, inplace=True)

# Normalize track names
df['track_lower'] = df['Track Name'].str.lower().str.strip()

# -------------------------------
# Mood Detection Logic
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
# Content-Based Recommendation Setup
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
# Emoji to Mood Mapping
# -------------------------------
emoji_mood_map = {
    "😊": "happy", "😄": "happy", "😃": "happy",
    "😢": "sad", "😭": "sad", "😔": "sad",
    "🔥": "energetic", "⚡": "energetic", "💃": "energetic",
    "😌": "chill", "🌙": "chill", "☁️": "chill"
}

# -------------------------------
# Recommendation Functions
# -------------------------------
def recommend_by_song(song_name, top_n=5):
    song_name = song_name.lower().strip()

    if song_name not in df['track_lower'].values:
        return None

    idx = df[df['track_lower'] == song_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    song_indices = [i[0] for i in sim_scores[1:top_n+1]]

    return [
        f"{df.iloc[i]['Track Name']} - {df.iloc[i]['Artist(s)']}"
        for i in song_indices
    ]

def recommend_by_mood(mood, top_n=5):
    mood = mood.lower().strip()
    mood_songs = df[df['mood'] == mood]

    if mood_songs.empty:
        return None

    sample = mood_songs.sample(min(top_n, len(mood_songs)))
    return [
        f"{row['Track Name']} - {row['Artist(s)']}"
        for _, row in sample.iterrows()
    ]

# -------------------------------
# Chatbot Interface
# -------------------------------
print("🎵🤖 Spotify Chatbot Recommender 🤖🎵")
print("You can enter:")
print("• A song name (e.g., Sahiba)")
print("• A mood word (happy, sad, energetic, chill)")
print("• An emoji 😊 😢 🔥 😌")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Your input: ").strip()

    if user_input.lower() == "exit":
        print("👋 Enjoy your music!")
        break

    # Emoji input
    if user_input in emoji_mood_map:
        mood = emoji_mood_map[user_input]
        results = recommend_by_mood(mood)

    # Mood word input
    elif user_input.lower() in ["happy", "sad", "energetic", "chill"]:
        results = recommend_by_mood(user_input.lower())

    # Song name input
    else:
        results = recommend_by_song(user_input)

    if not results:
        print("❌ No results found. Try another song or mood.\n")
        continue

    print("\n🎧 Recommended Songs:")
    for song in results:
        print("•", song)
    print()
