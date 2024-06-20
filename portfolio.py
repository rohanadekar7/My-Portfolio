import streamlit as st
import webbrowser
import skills
import education

name = "Rohan Nadekar"
bio = "I excel in C/C++, Machine Learning, Java, Python,SQL and Data Structures & Algorithms. As a beginner in Jupyter Notebook, Streamlit, and GitHub, I am eager to make tech projects successful. Constantly seeking to upgrade my skills and drive innovation, I am passionate about shaping the future of technology. Beyond my professional interests, I enjoy reading books, watching movies and web series, and playing outdoor games. Inspired by my dear friend Vedant, I am motivated to collaborate and push boundaries, creating remarkable solutions that leave a lasting impact. Let's connect and transform the tech world together!"
email = "rohan.22210182@viit.ac.in"
phone = "+91-8600837496"
linkedin = "http://www.linkedin.com/in/rohanadekar93a712258"
github = "https://github.com/rohanadekar7"
profile_pic = "Lord.jpg"
whatsapp_link = "https://wa.me/8600837496" 

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate_to(page):
    st.session_state.page = page

st.set_page_config(page_title=f"{name} - Portfolio", layout="wide")

with st.sidebar:
    st.title("Navigation")
    if st.button("Home"):
        navigate_to('home')
    if st.button("Skills"):
        navigate_to('skills')
    if st.button("Education"):
        navigate_to('education')

if st.session_state.page == 'home':
    st.title(f"Welcome to My Portfolio Website\n")

    col1, col2 = st.columns([4, 7])  
    with col1:
        st.image(profile_pic, width=300, use_column_width=True, output_format='jpg')
    with col2:
        st.write(f"# {name}")
        st.write(bio)

    # Contact details
    st.subheader("Contact Me")
    st.write(f"📧 [Email](mailto:{email})")
    st.write(f"📞 {phone}")
    st.write(f"🔗 [LinkedIn]({linkedin})")
    st.write(f"💻 [GitHub]({github})")
    if st.button("Contact via WhatsApp", key='whatsapp_home'):
        webbrowser.open(whatsapp_link)
elif st.session_state.page == 'skills':
    skills.app()
elif st.session_state.page == 'education':
    education.app()

st.markdown("""
    <style>
        footer {
            visibility: hidden;
        }
        .footer {
            visibility: visible;
            position: fixed;
            right: 0;
            bottom: 0;
            text-align: right;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        Made by Rohan Nadekar 🫡
    </div>
""", unsafe_allow_html=True)