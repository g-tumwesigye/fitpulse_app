from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import joblib
import numpy as np
import pandas as pd

# FastAPI app initialization
app = FastAPI(title="Fitpulse Body Fat Prediction API", version="1.0.0")

# Load pre-trained model and scaler
model = joblib.load("best_model.pkl")  # Ensure this file exists and matches the training model
scaler = joblib.load("scaler.pkl")    # Load the saved StandardScaler used during training

# Feature order and preprocessing
FEATURE_ORDER = ["Weight", "Height", "BMI", "Gender", "Age"]  # Ensure the order matches training
GENDER_MAPPING = {"Male": 1, "Female": 0}  # Matches the encoding used during training


# Request schema
class InputData(BaseModel):
    Weight: float
    Height: float
    BMI: float
    Gender: str
    Age: int

    @field_validator("Weight", "Height", "BMI", "Age")
    def validate_positive(cls, value):
        if value <= 0:
            raise ValueError("All values must be greater than zero.")
        return value

    @field_validator("Gender")
    def validate_gender(cls, value):
        if value not in GENDER_MAPPING:
            raise ValueError("Gender must be either 'Male' or 'Female'.")
        return value


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Fitpulse Body Fat Prediction API!"}


# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([{
            "Weight": data.Weight,
            "Height": data.Height,
            "BMI": data.BMI,
            "Gender": GENDER_MAPPING[data.Gender],
            "Age": data.Age,
        }])

        # Scale input features
        scaled_input = scaler.transform(input_df)

        # Predict Body Fat Percentage
        prediction = model.predict(scaled_input)

        return {"Body Fat Percentage": float(prediction[0])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
