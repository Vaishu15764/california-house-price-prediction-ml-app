🌟 California House Price Prediction – AI + Voice Web App

A modern, interactive, fully-powered Machine Learning + FASTAPI + Streamlit application that predicts California house prices using Linear Regression.
Includes a built-in AI Chat Assistant (Gemini API) and Voice Output using gTTS — all wrapped in a beautiful, animated UI.


📌 Features
🔮 1. House Price Prediction

Enter house details such as:

Median Income

House Age

Average Rooms

Average Bedrooms

Population

Average Occupancy

Longitude

Prediction appears instantly with a stylish UI card.

🤖 2. AI Chat Assistant (Gemini API)

Ask questions like:

"Why is the price high?"

"How can I increase the house value?"

"Which features affect price most?"

The AI responds intelligently based on:
✔ Your prediction
✔ Your input features
✔ Your custom question

And includes voice output!

🗣️ 3. Voice Explanation

Every AI response is converted into speech using gTTS.
A modern audio player automatically appears.

📚 4. Prediction History

All predictions are saved in history.json and shown in the sidebar.

Includes:

✔ Clear History button
✔ Clear Prediction button

🎨 5. Modern Glassmorphic UI

Fully customized:

Blur glass cards

Gradient backgrounds

Animated buttons

Custom chat bubble

Styled input fields

Consistent dark mode look

UI powered by custom style.css + Streamlit components.

🧠 ML Model

A Linear Regression model trained on the California Housing Dataset.

Saved as:

backend/model.joblib


Includes both:

Trained model

Column order for prediction consistency

📂 Project Folder Structure
callifornia_house_prediction_project/
│
├── backend/
│   ├── app.py                 # FastAPI backend
│   ├── explain.py             # Gemini AI logic
│   ├── load_model.py          # Loads model.joblib
│   ├── history.json           # Prediction history
│   ├── model.joblib           # Trained ML model
│   └── .env                   # GEMINI_API_KEY
│
├── frontend/
│   ├── streamlit_app.py       # Main Streamlit app
│   ├── style.css              # Full UI styling
│   ├── components/
│   │   ├── sidebar.py
│   │   ├── chatbot.py
│   │   └── form_inputs.py
│   ├── voice.mp3              # AI speech output (auto-generated)
│   └── voice_temp.mp3
│
└── README.md                  # You're here 🙂

🛠️ Tech Stack
🔗 Backend

Python

FASTAPI

Uvicorn

Joblib (ML Model)

Google Gemini API

🖥️ Frontend

Streamlit

Custom HTML/CSS

gTTS (voice)

Requests (API communication)

📈 Machine Learning

Linear Regression (scikit-learn)

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/Vaishu15764/california-house-price-prediction-aichat-voice-webapp
cd your-repo-name

▶️ Backend Setup (FASTAPI)
cd backend
pip install -r requirements.txt

Create .env inside backend/
GEMINI_API_KEY=YOUR_KEY_HERE

Run backend:
uvicorn app:app --reload


Backend will run at:
👉 http://127.0.0.1:8000

💻 Frontend Setup (Streamlit)
cd frontend
pip install -r requirements.txt


Run Streamlit:

streamlit run streamlit_app.py


Frontend will run at:
👉 http://localhost:8501

🔌 API Endpoints
Method	Endpoint	Description
POST	/predict	Predicts house price
POST	/explain	Generates AI explanation
GET	/history	Fetches prediction history
DELETE	/history	Clears prediction history

📸 Screenshots


🏡 Prediction UI
<img width="792" height="697" alt="image" src="https://github.com/user-attachments/assets/fd0a4e4e-6eed-4b9a-a2f6-8421011b414f" />


💬 AI Chat Interface

<img width="763" height="816" alt="image" src="https://github.com/user-attachments/assets/237057e7-692b-432a-8bbe-021df933258d" />


🎧 Voice Output Player

<img width="714" height="365" alt="image" src="https://github.com/user-attachments/assets/ecbc05e6-380c-45ea-9974-8e6fe4c84d75" />


🔮 Future Enhancements

Multi-model comparison (RandomForest, XGBoost, NN)

Add map visualization using Folium

Deploy full system on Render / Railway

User authentication to store personal history

Dark/Light mode toggle

👩‍💻 About the Author

Vaishnavi Sainath Pachange
Passionate about ML, AI, and building interactive real-world applications.

⭐ Support

If you like this project, please ⭐ star the repo!
