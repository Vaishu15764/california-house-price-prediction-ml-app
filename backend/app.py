from fastapi import FastAPI
from pydantic import BaseModel
from backend.load_model import load_model
from backend.explain import explain_prediction
import json

app = FastAPI()

# Load model dictionary
d = load_model()
model = d["model"]

HISTORY_FILE = "history.json"

# Input schema
class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float

# Save prediction history
def save_history(data):
    try:
        history = json.load(open(HISTORY_FILE))
    except:
        history = []
    history.append(data)
    json.dump(history, open(HISTORY_FILE, "w"), indent=2)


# -----------------------------
#      PREDICTION ROUTE
# -----------------------------
@app.post("/predict")
def predict(data: InputData):
    input_values = list(data.dict().values())
    predicted_price = model.predict([input_values])[0]

    entry = {
        "inputs": data.dict(),
        "prediction": float(predicted_price)
    }
    save_history(entry)

    return {"prediction": predicted_price}


# -----------------------------
#      AI EXPLANATION ROUTE
# -----------------------------
@app.post("/explain")
def explain(data: dict):
    prediction = data["prediction"]
    inputs = data["inputs"]
    question = data["question"]

    reply = explain_prediction(prediction, inputs, question)
    return {"explanation": reply}


# -----------------------------
#        HISTORY ROUTES
# -----------------------------
@app.get("/history")
def get_history():
    try:
        return json.load(open(HISTORY_FILE))
    except:
        return []


@app.delete("/history")
def clear_history():
    open(HISTORY_FILE, "w").write("[]")
    return {"status": "cleared"}
