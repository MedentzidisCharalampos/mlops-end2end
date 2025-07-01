# End-to-End MLOps Pipeline
# End-to-End MLOps Pipeline

## 🧠 Overview
This project demonstrates a complete MLOps pipeline including:
- Data ingestion and preprocessing
- Model training, evaluation, and tracking with MLflow
- Model deployment via FastAPI REST API
- Dataset and model versioning using DVC
- Workflow orchestration using Prefect or Airflow
- CI/CD using GitHub Actions or GitLab CI
- Dockerized infrastructure for reproducibility

## 🗂️ Project Structure
```
mlops_pipeline_project/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── src/
│   ├── api/
│   │   └── main.py
│   ├── data/
│   │   └── preprocess.py
│   ├── models/
│   │   ├── train.py
│   │   └── evaluate.py
│   └── utils/
│       └── helpers.py
├── dvc.yaml
├── Dockerfile
├── .github/workflows/ci.yml
├── .gitlab-ci.yml
├── params.yaml
├── requirements.txt
└── README.md
```

## 🏁 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Initialize DVC and run pipeline
```bash
dvc init
dvc repro
```

### 3. Train model manually (optional)
```bash
python src/models/train.py
```

### 4. Launch FastAPI server
```bash
uvicorn src.api.main:app --reload
```

### 5. Launch MLflow UI
```bash
mlflow ui
```
Visit: http://127.0.0.1:5000

### 6. Orchestrate pipeline (choose one)
```bash
# Prefect
prefect deployment build src/data/preprocess.py:preprocess -n local
prefect agent start

# Airflow
airflow standalone
```

## 📦 API Endpoint
**POST /predict**
```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```
**Response:**
```json
{
  "prediction": 0
}
```

## 🐳 Docker
Build and run:
```bash
docker build -t mlops-pipeline .
docker run -p 8000:8000 mlops-pipeline
```

## ✅ CI/CD
- `.github/workflows/ci.yml` — GitHub Actions
- `.gitlab-ci.yml` — GitLab CI/CD

## 📂 Versioning
- Use `dvc push` to upload models/data to remote
- Use `dvc pull` to retrieve data/models


