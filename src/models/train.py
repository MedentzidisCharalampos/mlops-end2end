# Model training logic
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
import mlflow
import os

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("IrisClassifier")

data = pd.read_csv("data/processed/iris_processed.csv")
X = data.drop(columns=["target"])
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run():
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    acc = clf.score(X_test, y_test)
    mlflow.log_metric("accuracy", acc)

    os.makedirs("models", exist_ok=True)
    dump(clf, "models/model.joblib")
    mlflow.sklearn.log_model(clf, "model")