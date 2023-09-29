import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="unidash", layout="centered")
    st.title("University Student Dashboard")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Go to", ("Home", "Clubs Resources", "University Resources", "Profile"))

    if section == "Home":
        show_homepage()
    elif section == "Clubs Resources":
        show_clubs_resources()
    elif section == "University Resources":
        show_university_resources()
    elif section == "Profile":
        show_profile()

    st.divider()
    st.caption("Designed & Developed by Mohammed Husamuddin")
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
