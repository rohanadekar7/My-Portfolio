import streamlit as st
from PIL import Image

def app():
    st.title("Skills")

    skills = [
        {"name": "Python", "logo": "images/python.jpeg"},
        {"name": "C", "logo": "images/c.jpeg"},
        {"name": "C++", "logo": "images/cpp.jpeg"},
        {"name": "Java", "logo": "images/java.jpeg"},
        {"name": "SQL", "logo": "images/mysql.jpeg"},
        {"name": "GitHub", "logo": "images/github.jpeg"},
        {"name": "Jupyter", "logo": "images/jupyter.jpeg"},
        {"name": "Machine Learning", "logo": "images/ml.jpeg"},
        {"name": "Data Science", "logo": "images/ds.jpeg"},
        {"name": "Data Structures and Algorithms", "logo": "images/dsa.jpeg"},
    ]

    num_columns = 3
    columns = st.columns(num_columns)
    for i, skill in enumerate(skills):
        with columns[i % num_columns]:
            img = Image.open(skill["logo"]).convert("RGBA")
            img = img.resize((120, 120))
            st.image(img, width=200)
            st.write(f"**{skill['name']}**")

if __name__ == "__main__":
    app()