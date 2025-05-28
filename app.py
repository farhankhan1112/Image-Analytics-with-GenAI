import streamlit as st
import google.generativeai as genai
from PIL import Image

############ API Key #############
api_key=(" Enter your API key")
genai.configure(api_key=api_key)

############## choose Heading ###############3
st.header("Image analytics")

################## upload file ( image ) ##############
uploaded_file= st.file_uploader("upload an image ", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

################## What you want to search from Image ###############
prompt=st.text_input("Enter the text")

############# use GenAi skill ################
if st.button("Get RESPONSE"):
    image= Image.open(uploaded_file)
    # Initialize the GenerativeModel with the correct model name
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    response= model.generate_content([prompt,image])

    st.markdown(response.text)
