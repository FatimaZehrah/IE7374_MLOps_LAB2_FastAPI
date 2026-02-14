# IE7374_MLOps_LAB2_FastAPI  
## MLOps Lab 2 – FastAPI ML Inference Service

---

## Project Overview

This repository contains **Lab 2** for the course **IE7374: MLOps**.

The objective of this lab is to build a production-style machine learning service using FastAPI, including:

- Model training and serialization
- REST API deployment for inference
- Health monitoring endpoint
- Automated unit testing
- Continuous Integration using GitHub Actions

This project demonstrates core MLOps principles including modular architecture, reproducibility, testing, and CI automation.

---

## Problem Statement

Deploy a machine learning classification model as a web service that:

1. Accepts structured input
2. Returns model predictions
3. Provides confidence scores
4. Includes health monitoring
5. Is automatically validated via CI pipeline

---

## Model Details

- Dataset: Iris Dataset
- Model Type: Scikit-learn Classifier
- Output: Species class prediction (0, 1, 2)
- Confidence: Maximum predicted probability
- Serialization Format: Pickle (`.pkl`)

---

## Project Architecture

# IE7374_MLOps_LAB2_FastAPI  
## MLOps Lab 2 – FastAPI ML Inference Service

---

## Project Overview

This repository contains **Lab 2** for the course **IE7374: MLOps**.

The objective of this lab is to build a production-style machine learning service using FastAPI, including:

- Model training and serialization
- REST API deployment for inference
- Health monitoring endpoint
- Automated unit testing
- Continuous Integration using GitHub Actions

This project demonstrates core MLOps principles including modular architecture, reproducibility, testing, and CI automation.

---

## Problem Statement

Deploy a machine learning classification model as a web service that:

1. Accepts structured input
2. Returns model predictions
3. Provides confidence scores
4. Includes health monitoring
5. Is automatically validated via CI pipeline

---

## Model Details

- Dataset: Iris Dataset
- Model Type: Scikit-learn Classifier
- Output: Species class prediction (0, 1, 2)
- Confidence: Maximum predicted probability
- Serialization Format: Pickle (`.pkl`)

---

## Project Architecture

IE7374_MLOps_LAB2_FastAPI/
│
├── src/
│ ├── train.py # Model training script
│ ├── predict.py # Prediction logic
│ ├── data.py # Pydantic schemas
│ └── main.py # FastAPI application
│
├── model/
│ └── iris_model.pkl # Serialized trained model
│
├── test/
│ └── test_api_logic.py # Unit tests
│
├── .github/
│ └── workflows/
│ └── pytest_action.yml # CI pipeline
│
├── requirements.txt
├── .gitignore
└── README.md

Custom Enhancements Implemented

This lab includes additional improvements beyond the base template:

Confidence score returned with predictions

Dedicated health monitoring endpoint

Clean modular separation (train, predict, API, schema)

Structured project architecture

Automated testing using Pytest

CI validation using GitHub Actions

## How to Run the Project Locally

Follow these steps to run the FastAPI service:

### 1️⃣ Clone the Repository

```bash
git clone <repository_link>
cd IE7374_MLOps_LAB2_FastAPI
python -m venv lab_02_env
lab_02_env\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
http://127.0.0.1:8000/docs
  

