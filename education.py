import streamlit as st

def app():
    st.title("Education")

    education_details = [
        {
            "name": "B.Tech in Computer Engineering(Pursuing)",
            "institution": "Vishwakarma Institute of Information Technology",
            "year": "Currently in third year",
            "cgpa": "7.1",
            "image": "images/VIIT.jpg",
            "caption": "VIIT"
        },
        {
            "name": "Higher Secondary School Certificate (HSC), 2022",
            "school": "S.S.C.College,Junnar",
            "year": "2022",
            "percentage": "55%(PCMB)",
            "image":"images/SSC.jpg",
            "caption": "S.S.C. College"
        },
        {
            "name": "Secondary School Certificate (SSC), 2020",
            "school": "Shakarrao Butte Patil Vidyalaya, Junnar",
            "year": "2020",
            "percentage": "84.20%",
            "image": "images/sbp.jpeg",
            "caption": "Shakarrao Butte Patil Vidyalaya"
        }
    ]

    for education in education_details:
        st.markdown(f"## {education['name']}")
        col1, col2 = st.columns([1, 3])  

        with col1:
            st.image(education["image"], caption=education["caption"], use_column_width=True)

        with col2:
            st.write(f"- **Institution/School:** {education.get('institution', education.get('school'))}")
            st.write(f"- **CGPA/Percentage:** {education.get('cgpa', education.get('percentage'))}")

if __name__ == '__main__':
    app()