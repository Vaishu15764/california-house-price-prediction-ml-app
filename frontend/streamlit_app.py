import streamlit as st
import requests

from components.sidebar import load_history
from components.form_inputs import user_form
from components.chatbot import speak

API_URL = "http://127.0.0.1:8000"

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page Title
st.title("✨ California House Price Prediction (AI + Voice)")

# Sidebar history
load_history(API_URL)

# Input form
inputs = user_form()

# Prediction button
predict_btn = st.button("🔮 Predict Price")

# Clear Prediction Button
clear_prediction_btn = st.button("❌ Clear Prediction")

if clear_prediction_btn:
    st.session_state.latest_prediction = None
    st.session_state.latest_inputs = None
    st.session_state.text_input = ""  # clear question input
    st.rerun()  # refresh the UI


# Session state
if "latest_prediction" not in st.session_state:
    st.session_state.latest_prediction = None

if "latest_inputs" not in st.session_state:
    st.session_state.latest_inputs = None

# ---------------------------
#       PREDICT PRICE
# ---------------------------
if predict_btn:
    response = requests.post(f"{API_URL}/predict", json=inputs).json()
    st.session_state.latest_prediction = response["prediction"]
    st.session_state.latest_inputs = inputs

# Show prediction card ONLY
if st.session_state.latest_prediction is not None:
    st.markdown(
        f"""
        <div class="card" style="max-width: 500px; margin: auto;">
            <h3>🏠 Predicted Price: {st.session_state.latest_prediction}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
#          CHAT AREA
# ---------------------------
st.markdown("### 💬 Ask AI anything about this prediction")

user_msg = st.text_input("Type your question:")

chat_btn = st.button("📩 Ask AI")

if chat_btn:
    if st.session_state.latest_prediction is None:
        st.warning("Please make a prediction first.")
    elif not user_msg.strip():
        st.warning("Please enter a question.")
    else:

        # Ask backend WITH question
        chat_response = requests.post(
            f"{API_URL}/explain",
            json={
                "prediction": st.session_state.latest_prediction,
                "inputs": st.session_state.latest_inputs,
                "question": user_msg
            }
        ).json()

        ai_reply = chat_response["explanation"]

        # Chat bubble display
        st.markdown(
            f"""
            <div class="chatbox">
                <b>You:</b> {user_msg}<br><br>
                <b>AI:</b> {ai_reply}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Voice output
        speak(ai_reply)
