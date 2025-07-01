# Model evaluation logic
import pandas as pd
from sklearn.metrics import classification_report
from joblib import load

model = load("models/model.joblib")
data = pd.read_csv("data/processed/iris_processed.csv")

X = data.drop(columns=["target"])
y = data["target"]

preds = model.predict(X)
report = classification_report(y, preds)
print("Evaluation Report:\n", report)