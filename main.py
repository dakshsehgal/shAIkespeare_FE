import streamlit as st
from PIL import Image
from utils.streamlit_utils import *

button_style = """<style>

.stApp {
    background-color: black;
}

.stButton > button {
color: white;

background: black;
border-color: black;
width: 200px;
}

.stButton > button:hover {
color: red;
border-color: black;
}

.stButton > button:focus {
border-color: black;
background: black;

}

.stButton > button:focus:not(:active) {
    background: black;
    border-color: black;
}

</style>

"""

st.markdown(f"<h1 style='text-align: center; color: white; font-family: arial;'>Tech Poets Society</h1>", unsafe_allow_html=True)
st.markdown(button_style, unsafe_allow_html=True)
comedy_of_errors = Image.open('images/comedy.jpg')

st.image(comedy_of_errors)

c1,c2,c3,c4,c5, c6 = st.columns(6)

if c3.button("The Comedy of Errors"):
    nav_page("comedy_of_errors")


image = Image.open('images/father.jpg')
st.image(image)

d1, d2, d3, d4, d5, d6 = st.columns(6)
if d3.button("Father's Day"):
    nav_page("fathers_day")