import streamlit as st
import pandas as pd

def main():
    st.title("UNI DASH")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Go to", ("Home", "University Resources", "Clubs Resources"))

    if section == "Home":
        show_homepage()
    elif section == "University Resources":
        show_university_resources()
    elif section == "Clubs Resources":
        show_clubs_resources()

    st.divider()
    st.write("This Web App Is Made to Help You Access All The Important BITS Pilani, Dubai Admin & Academic Websites at a Single Place")
    st.markdown("> Designed & Developed by HUSAM")
    st.markdown("""
        ## Contributors

        This project is made possible by the following contributors:

        - **Husam**: Designed and developed the web application.
        - **Riddhi**: Developed the Time Table Generator.
        - **Ahmed Thahir**: For Permitting us to Integrate his Uni-Notes Project.

        Special thanks to my freinds and batchmates at BITS Pilani, Dubai for their support and resources.

        ### Things I am working on:
                - Notes for BioTech and Other Disciplines
        ---
    """)

def show_homepage():
    st.header("Welcome to the University Dashboard!")
    st.write("Use the sidebar to navigate to different sections.")
    

def show_university_resources():
    st.markdown("# University Resources")

    st.markdown(" ### Library Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="http://webopac.bits-dubai.ac.ae/AutoLib/index.jsp" width="100%" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Courses & LMS")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://lms.bitspilanidubai.ae/login/index.php" width="100%" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("BITS ERP")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://erp.bits-pilani.ac.in/" width="100%" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

def show_clubs_resources():
    st.header("Clubs Resources")
    st.markdown("---")
    st.markdown("Feel free to contribute")

    st.subheader("GDSC Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://gdscbpdc.github.io/" width="100%" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("ACM Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://openlib-cs.acmbpdc.org/" width="100%" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Ahmed Thahir's Notes")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://uni-notes.netlify.app/" width="100%" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
