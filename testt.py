import streamlit as st
import google.generativeai as genai

st.title("Welcome ra boyys")

genai.configure(api_key="AIzaSyCy4ZTxt1DiSBeySNHw-pYJey70Nc_uQ3I")
text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message({"text": text})
    st.write(response.text)

