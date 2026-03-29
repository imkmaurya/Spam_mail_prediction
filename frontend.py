

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 Spam Email Detector")
st.write("Enter an email message to check if it's spam or not.")

# Input box
text = st.text_area("Enter your email text:")

# Button
if st.button("Check Spam"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        try:
            response = requests.post(API_URL, json={"text": text})
            result = response.json()

            prediction = result["prediction"]

            if prediction == 1:
                st.error("🚫 This is SPAM!")
            else:
                st.success("✅ This is NOT spam (Ham)")

        except:
            st.error("⚠️ API not running! Please start FastAPI server.")