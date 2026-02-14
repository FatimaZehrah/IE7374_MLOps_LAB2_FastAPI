from fastapi import FastAPI
from src.data import IrisData, IrisResponse
from src.predict import predict_species_with_confidence


app = FastAPI(title="Iris Classifier API")


@app.get("/")
def home():
    return {"message": "FastAPI Iris Classifier is running successfully."}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=IrisResponse)
def predict(data: IrisData):
    prediction, confidence = predict_species_with_confidence(data)
    return {"prediction": prediction, "confidence": confidence}
