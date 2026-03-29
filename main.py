
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorized = pickle.load(f)

# Load model
with open("model (1).pkl", "rb") as g:
    model = pickle.load(g)

# Input schema
class TextInput(BaseModel):
    text: str

@app.post("/predict")
def prediction(data: TextInput):
    vec = vectorized.transform([data.text])
    pred = model.predict(vec)
    return {
    "prediction": "spam" if pred[0] == 1 else "ham"
}