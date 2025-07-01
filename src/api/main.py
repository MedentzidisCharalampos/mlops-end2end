# FastAPI app
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np
import os
from src.utils.db import init_db, log_prediction

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.joblib")

app = FastAPI()

from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)

try:
    model = load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Model not loaded: {e}")

class IrisInput(BaseModel):
    features: list[float]

@app.get("/")
def read_root():
    return {"message": "MLOps pipeline is running."}

@app.post("/predict")
def predict(input: IrisInput):
    if model is None:
        return {"error": "Model not available."}
    data = np.array(input.features).reshape(1, -1)
    pred = model.predict(data)
    return {"prediction": int(pred[0])}

@app.post("/predict")
def predict(input: IrisInput):
    if model is None:
        return {"error": "Model not available."}
    data = np.array(input.features).reshape(1, -1)
    pred = model.predict(data)
    log_prediction(input.features, int(pred[0]))
    return {"prediction": int(pred[0])}

