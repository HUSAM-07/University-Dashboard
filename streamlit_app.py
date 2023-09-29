import streamlit as st

def main():
    st.set_page_config(layout="centered",page_title="unidash")
    st.title("University Clubs Dashboard")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Go to", ("Home", "Clubs Resources", "University Resources"))

    if section == "Home":
        show_homepage()
    elif section == "Clubs Resources":
        show_clubs_resources()
    elif section == "University Resources":
        show_university_resources()

    st.divider()
    st.caption("Designed & Developed by HUSAM")
    st.caption("The app is designed using Streamlit")

def show_homepage():
    st.header("Welcome to the University Clubs Dashboard!")
    st.write("Use the sidebar to navigate to different sections.")

def show_clubs_resources():
    st.header("Clubs Resources")
    st.markdown("---")

    st.subheader("GDSC Resources")
    st.components.v1.html(
        f'<iframe src="https://gdscbpdc.github.io/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=True,
    )

    st.markdown("---")
    st.subheader("ACM Resources")
    st.components.v1.html(
        f'<iframe src="https://openlib-cs.acmbpdc.org/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=True,
    )

    st.markdown("---")
    st.subheader("Ahmed Thahir's Notes")
    st.components.v1.html(
        f'<iframe src="https://uni-notes.netlify.app/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=True,
    )

def show_university_resources():
    st.header("University Resources")
    st.markdown("---")

    st.subheader("Library Resources")
    st.components.v1.html(
        f'<iframe src="http://webopac.bits-dubai.ac.ae/AutoLib/index.jsp" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=True,
    )

    st.markdown("---")
    st.subheader("Courses & LMS")
    st.components.v1.html(
        f'<iframe src="https://lms.bitspilanidubai.ae/login/index.php" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=True,
    )

    st.markdown("---")
    st.subheader("BITS ERP")
    st.components.v1.html(
        f'<iframe src="https://erp.bits-pilani.ac.in/" width="100%" height="400" style="border: none;"></iframe>',
        width=800,
        height=400,
        scrolling=True,
    )

if __name__ == '__main__':
    main()
