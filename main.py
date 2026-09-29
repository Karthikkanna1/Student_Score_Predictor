from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("backend/score_model.pkl")

class StudentData(BaseModel):
    hours_studied: float

@app.post("/predict-score/")
def predict_score(data: StudentData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return {"predicted_score": round(prediction, 2)}