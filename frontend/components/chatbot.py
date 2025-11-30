import streamlit as st
from gtts import gTTS
import base64

def speak(text):
    tts = gTTS(text)
    tts.save("voice.mp3")
    audio_file = open("voice.mp3", "rb").read()
    st.audio(audio_file, format="audio/mp3")

def show_explanation(text):
    st.markdown(
        f"""
        <div style="
            background:#1e1e1e;
            padding:20px;
            border-radius:10px;
            font-size:16px;
            color:white;
            max-width: 600px;
            line-height: 1.5;
            word-wrap: break-word;
            white-space: normal;
            margin-bottom: 20px;
        ">
            <b>AI Explanation:</b><br><br>{text}
        </div>
        """,
        unsafe_allow_html=True,
    )
