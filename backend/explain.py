import os
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_NAME)

def explain_prediction(price, features, question):
    """
    AI should answer EXACTLY what user asked while still using prediction context.
    """

    prompt = f"""
You are an AI real estate assistant.

House Price: {price}
House Features: {features}

User's Question: {question}

📝 Your task:
- ANSWER ONLY the user’s question.
- DO NOT repeat full price explanation unless the question asks for it.
- If the question is unrelated (example: "what is longitude"), answer normally.

Give a clear, short, helpful response.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"(Gemini Error: {e})"
