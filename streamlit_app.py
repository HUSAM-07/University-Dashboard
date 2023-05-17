import streamlit as st
st.set_page_config(layout="wide")

def main():
    st.title("University Clubs Dashboard")
    st.markdown("---")

    st.header("Clubs Resources")
    st.markdown("---")

    st.subheader("GDSC Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://gdscbpdc.github.io/" width="1200" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("ACM Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://openlib-cs.acmbpdc.org/" width="1200" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Ahmed Thahir's Notes")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://uni-notes.netlify.app/" width="800" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.header("University Resources")
    st.markdown("---")

    st.subheader("Library Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="http://webopac.bits-dubai.ac.ae/AutoLib/index.jsp" width="1200" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Courses & LMS")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://lms.bitspilanidubai.ae/login/index.php" width="1200" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("BITS ERP")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://erp.bits-pilani.ac.in/" width="1200" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
st.divider()
st.caption("Designed & Developed by HUSAM")

