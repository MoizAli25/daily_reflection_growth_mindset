import streamlit as st
import pandas as pd
import random
from datetime import datetime
import os

QUOTES = [
    "Do the best you can until you know better. Then when you know better, do better. - Maya Angelou",

    "There is nothing noble in being superior to your fellow man; true nobility is being superior to your former self. - Ernest Hemingway",

    "Stay afraid, but do it anyway. What's important is the action. You don't have to wait to be confident. Just do it and eventually the confidence will follow. - Carrie Fisher",

    "One can choose to go back toward safety or forward toward growth. Growth must be chosen again and again; fear must be overcome again and again. - Abraham Maslow",

    "We can't become what we need to be by remaining what we are. - Oprah Winfrey",

    "When we're growing up there are all sorts of people telling us what to do when really what we need is space to work out who to be. - Elliot Page",

    "If there is no struggle, there is no progress. - Frederick Douglass",

    "Permit yourself to change your mind when something is no longer working for you. - Nedra Glover Tawwab",

    "Be not afraid of growing slowly; be afraid only of standing still. - Chinese Proverb",

    "Though no one can go back and make a brand new start, anyone can start from now and make a brand new ending. - Carl Bard"
]

def main():
    st.title("🌱 Growth Mindset Daily Journal")
    st.write("Welcome to your personal space to reflect and grow!")

    user_name = st.text_input("Enter your name to begin:")

    if user_name:
        st.subheader(f"Hello, {user_name}! Let's reflect on your day.")

        learned = st.text_area("1. What did you learn today?")
        challenge = st.text_area("2. What challenge did you face and how did you respond?")
        tomorrow = st.text_area("3. What would you do differently tomorrow?")
        gratitude = st.text_area("List 3 things you're grateful for today:")

        if st.button("Save My Reflection"):
            entry = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": user_name,
                "Learned": learned,
                "Challenge": challenge,
                "Tomorrow": tomorrow,
                "Gratitude": gratitude
            }

            df = pd.DataFrame([entry])

            file_path = "growth_journal.csv"

            # 🛠 Check if file exists
            if os.path.exists(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, mode='w', header=True, index=False)

            st.success("Your reflection has been saved. Keep it up! 💪")

        st.subheader("🌟 Quote of the Day")
        st.info(random.choice(QUOTES))

if __name__ == "__main__":
    main()
