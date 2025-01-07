import streamlit as st 
from streamlit_lottie import st_lottie
import json

def app():
    
    st.markdown("""
        <h1 style='text-align: center; color: white;'>COMPUTER VISION APP</h1>
        """, unsafe_allow_html=True)  
    
    st.write("\n")
    st.write("\n")

    with open("cv_animation.json") as source:
            animation = json.load(source)

    st_lottie(animation, width = 800)

    st.write("Computer vision plays an important role in technical as well as non-technical fields")
    st.write("It is used to extract useful insights from a given image or video.\nIn this case we have to analyze the quality of given images and videos of yellow split peas.")
    st.write("\n")
    

