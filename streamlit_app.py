import streamlit as st
import spacy
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# Sample previous year questions for demonstration purposes
previous_year_questions = [
    "What are the main concepts in calculus?",
    "How do you solve differential equations?",
    "Explain the principles of quantum mechanics.",
    "What is the significance of the theory of relativity?",
    "Discuss the applications of artificial intelligence."
]

# Function to preprocess and vectorize text data
def preprocess_text(text):
    doc = nlp(text)
    # Lemmatize and remove stopwords
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)

# Vectorize and preprocess previous year questions
vectorizer = CountVectorizer()
previous_year_questions = [preprocess_text(question) for question in previous_year_questions]
question_vectors = vectorizer.fit_transform(previous_year_questions)

# Sample user authentication (in a real app, use a proper authentication system)
def authenticate(username, password):
    return username == "user" and password == "password"

# Sample data for user-specific content
user_data = {
    "user": {
        "name": "John Doe",
        "courses": ["Calculus", "Physics", "Computer Science"],
        "bookmarks": ["How to study effectively", "Useful resources for Physics"]
    }
}

# Function to fetch user data
def get_user_data(username):
    return user_data.get(username, {})

def main():
    st.title("University Student Dashboard")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Go to", ("Home", "Clubs Resources", "University Resources", "Chatbot", "Profile"))

    if section == "Home":
        show_homepage()
    elif section == "Clubs Resources":
        show_clubs_resources()
    elif section == "University Resources":
        show_university_resources()
    elif section == "Chatbot":
        show_chatbot()
    elif section == "Profile":
        show_profile()

    st.divider()
    st.caption("Designed & Developed by [Your Name]")
    st.caption("The app is designed using Streamlit")

def show_homepage():
    st.header("Welcome to the University Student Dashboard!")
    st.write("Use the sidebar to navigate to different sections.")

def show_clubs_resources():
    st.header("Clubs Resources")
    st.markdown("---")

    # ... Your club resources content ...

def show_university_resources():
    st.header("University Resources")
    st.markdown("---")

    # ... Your university resources content ...

def show_chatbot():
    st.header("Chatbot - Predicting Questions")
    st.markdown("---")

    user_question = st.text_input("Ask a question:")
    if user_question:
        # Preprocess the user's question
        user_question = preprocess_text(user_question)

        # Calculate cosine similarity between user's question and previous year questions
        user_question_vector = vectorizer.transform([user_question])
        similarities = cosine_similarity(user_question_vector, question_vectors)

        # Find the most similar question from previous year questions
        most_similar_index = similarities.argmax()
        suggested_question = previous_year_questions[most_similar_index]

        st.subheader("Suggested Question for This Year:")
        st.write(suggested_question)

def show_profile():
    st.header("User Profile")
    st.markdown("---")

    st.sidebar.subheader("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            user_info = get_user_data(username)
            st.write(f"Welcome, {user_info.get('name', 'User')}!")
            st.write(f"Enrolled Courses: {', '.join(user_info.get('courses', []))}")
            st.write(f"Bookmarks: {', '.join(user_info.get('bookmarks', []))}")
        else:
            st.warning("Invalid username or password.")

if __name__ == '__main__':
    main()
