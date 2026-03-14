import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

def explain_prediction(price, features, question):

    prompt = f"""
You are a helpful real estate AI assistant.

Predicted house price: {price}

House features:
{features}

User question:
{question}

Answer clearly and briefly.
"""

    try:

        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content

    except Exception as e:
        return f"AI Error: {e}"