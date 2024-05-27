import streamlit as st
import pandas as pd
import calendar

# Define a sample timetable for illustration purposes
sample_timetable = {
    'Course': ['CS F211', 'CS F212', 'CS F241', 'CS F211', 'ME F211'],
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Start Time': ['10:00', '09:00', '10:00', '11:00', '09:00'],
    'End Time': ['11:00', '10:00', '11:00', '12:00', '10:00'],
    'Location': ['6102', '6102', '1024', '6102', '1024'],
    'Type': ['Lecture', 'Quiz', 'Lecture', 'Lecture', 'Lecture']
}

def main():
    st.title("University Dashboard")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Go to", ("Home", "Calendar", "Timetable Creator", "University Resources", "Clubs Resources"))

    if section == "Home":
        show_homepage()
    elif section == "Calendar":
        show_calendar()
    elif section == "Timetable Creator":
        show_timetable_creator()
    elif section == "University Resources":
        show_university_resources()
    elif section == "Clubs Resources":
        show_clubs_resources()

    st.divider()
    st.caption("Designed & Developed by HUSAM")
    st.write("This Web App Is Made to Help You Access All The Important BITS Pilani, Dubai Admin & Academic Websites at a Single Website")
    st.caption("The app is designed using Streamlit")

def show_homepage():
    st.header("Welcome to the University Dashboard!")
    st.write("Use the sidebar to navigate to different sections.")

def show_calendar():
    st.header("Calendar")
    st.markdown("---")
    st.subheader("September 2023")

    # Display a sample calendar
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Week View**")
        calendar_data = pd.DataFrame(sample_timetable)
        st.table(calendar_data)

    with col2:
        st.write("**Month View**")
        st.markdown('<iframe src="https://calendar.google.com/calendar/embed?src=example%40gmail.com&ctz=America%2FNew_York" style="border: 0" width="400" height="300" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)

def show_timetable_creator():
    st.header("Timetable Creator")
    st.markdown("---")
    
    # Sample timetable form
    with st.form("timetable_form"):
        course = st.selectbox("Course", ['CS F211', 'CS F212', 'CS F241', 'ME F211'])
        day = st.selectbox("Day", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        start_time = st.time_input("Start Time")
        end_time = st.time_input("End Time")
        location = st.text_input("Location")
        class_type = st.selectbox("Type", ['Lecture', 'Quiz', 'Lab'])
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.write(f"Course: {course}, Day: {day}, Start Time: {start_time}, End Time: {end_time}, Location: {location}, Type: {class_type}")

    st.write("Your Timetable")
    timetable_data = pd.DataFrame(sample_timetable)
    st.table(timetable_data)

def show_university_resources():
    st.header("University Resources")
    st.markdown("---")

    st.subheader("Library Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="http://webopac.bits-dubai.ac.ae/AutoLib/index.jsp" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Courses & LMS")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://lms.bitspilanidubai.ae/login/index.php" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("BITS ERP")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://erp.bits-pilani.ac.in/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

def show_clubs_resources():
    st.header("Clubs Resources")
    st.markdown("---")
    st.markdown("Feel free to contribute")

    st.subheader("GDSC Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://gdscbpdc.github.io/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("ACM Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://openlib-cs.acmbpdc.org/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Ahmed Thahir's Notes")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://uni-notes.netlify.app/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
