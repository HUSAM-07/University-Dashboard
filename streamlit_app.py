import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(layout="wide",page_title="unidash",page_icon="unidash.png")
    st.title("University Clubs Dashboard")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Go to", ("Home", "Clubs Resources", "University Resources","Tools & Apps"))

    if section == "Home":
        show_homepage()
    elif section == "Clubs Resources":
        show_clubs_resources()
    elif section == "University Resources":
        show_university_resources()
    elif section == "Tools & Apps":
        show_tools_apps()

    st.divider()
    st.caption("Designed & Developed by HUSAM")
    st.caption("The app is designed using Streamlit")

def show_homepage():
    st.header("Welcome to the University Clubs Dashboard!")
    st.write("Explore a world of opportunities and resources available at your fingertips with the University Clubs Dashboard. Whether you're a student looking to engage in exciting club activities or seeking essential university resources, this platform is your gateway to a richer and more fulfilling academic experience.")

    st.write("Navigate through the sidebar to discover the following sections:")

    st.subheader("1. Home")
    st.write("You are currently on the Home page. Use this page as a starting point to access various sections of the dashboard.")

    st.subheader("2. Clubs Resources")
    st.write("Discover a plethora of resources offered by your university clubs. From coding to gaming, explore materials, events, and updates from your favorite clubs, including GDSC and ACM.")

    st.subheader("3. University Resources")
    st.write("Access vital university resources with just a click. Explore the library's vast collection, log in to the Learning Management System (LMS) for your courses, and manage your academic life through BITS ERP.")

    st.write("Get ready to embark on an enriched educational journey. Start exploring now!")

def show_clubs_resources():
    st.header("Clubs Resources")
    st.markdown("---")

    st.subheader("GDSC Resources")
    st.components.v1.html(
        f'<iframe src="https://gdscbpdc.github.io/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=False,
    )

    st.markdown("---")
    st.subheader("ACM Resources")
    st.components.v1.html(
        f'<iframe src="https://openlib-cs.acmbpdc.org/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=False,
    )

    st.markdown("---")
    st.subheader("Ahmed Thahir's Notes")
    st.components.v1.html(
        f'<iframe src="https://uni-notes.netlify.app/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=False,
    )

def show_university_resources():
    st.header("University Resources")
    st.markdown("---")

    st.subheader("Library Resources")
    st.components.v1.html(
        f'<iframe src="http://webopac.bits-dubai.ac.ae/AutoLib/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=False,
    )

    st.markdown("---")
    st.subheader("Courses & LMS")
    st.components.v1.html(
        f'<iframe src="https://lms.bitspilanidubai.ae" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=False,
    )

    st.markdown("---")
    st.subheader("BITS ERP")
    st.components.v1.html(
        f'<iframe src="https://erp.bits-pilani.ac.in/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=False,
    )

def show_tools_apps():
    st.header("Tools & Apps")
    st.write("You can access the following tools and apps to enhance your learning and planning experience for academics.")
    st.toggle("Google Calendar", "Access your academic calendar and plan your schedule.")
    st.toggle("Find the Attendance Tracker Below,Track your attendance and manage your academic progress.")
    st.toggle("Find the GPA Calculator Below,Calculate your GPA and plan your academic goals.")
    st.toggle("Find the Grade Predictor Below, Predict your grades and plan your academic goals.")

def show_footer():
    st.write("Designed & Developed by HUSAM")

if __name__ == '__main__':
    main()
