# Required imports
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Load the trained Random Forest model and scaler
random_forest = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load the feature names from the training process
X = pd.DataFrame(columns=['Weight', 'Height', 'BMI', 'Gender', 'Age', 'BFPcase', 'BMIcase', 'Exercise Recommendation Plan'])

# Initialize FastAPI app
app = FastAPI(
    title="FitPulse Prediction API",
    description="An API to predict Body Fat Percentage using a trained Random Forest model.",
    version="1.0.0"
)

# Add CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input schema for FastAPI
class PredictionInput(BaseModel):
    weight: float
    height: float
    bmi: float
    gender: str
    age: int

    # Validation logic
    def validate(self):
        if not (2.5 <= self.weight <= 300):
            raise HTTPException(status_code=400, detail="Weight must be between 2.5 and 300 kg.")
        if not (0.5 <= self.height <= 2.5):
            raise HTTPException(status_code=400, detail="Height must be between 0.5 and 2.5 meters.")
        if not (10 <= self.bmi <= 60):
            raise HTTPException(status_code=400, detail="BMI must be between 10 and 60.")
        if self.gender.capitalize() not in ['Male', 'Female']:
            raise HTTPException(status_code=400, detail="Gender must be 'Male' or 'Female'.")
        if not (0 <= self.age <= 120):
            raise HTTPException(status_code=400, detail="Age must be between 0 and 120 years.")

# Function to predict Body Fat Percentage
def predict_body_fat(weight, height, bmi, gender, age):
    # Map gender to numerical values
    gender_map = {'Male': 1, 'Female': 0}
    gender_encoded = gender_map.get(gender.capitalize(), -1)

    if gender_encoded == -1:
        raise ValueError("Invalid gender input. Please enter 'Male' or 'Female'.")

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Weight': [weight],
        'Height': [height],
        'BMI': [bmi],
        'Gender': [gender_encoded],
        'Age': [age],
        'BFPcase': [0],  
        'BMIcase': [0],  
        'Exercise Recommendation Plan': [0]  
    })

    # Align the input data with model features
    input_data = input_data[X.columns]

    # Scale the input data
    input_scaled = scaler.transform(input_data)

    # Predict Body Fat Percentage
    predicted_bfp = random_forest.predict(input_scaled)

    return predicted_bfp[0]

# FastAPI root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FitPulse Prediction API. Use the /predict endpoint to make predictions."}

# FastAPI prediction endpoint
@app.post("/predict")
def api_predict(data: PredictionInput):
    # Validate input data
    data.validate()

    # Make prediction
    predicted_bfp = predict_body_fat(
        weight=data.weight,
        height=data.height,
        bmi=data.bmi,
        gender=data.gender,
        age=data.age
    )

    return {"Predicted Body Fat Percentage": predicted_bfp}

# CLI prediction logic (to remain intact)
if __name__ == "__main__":
    def get_user_input():
        # Prompting the user for inputs 
        weight = float(input("Enter your weight (kg): "))
        if not (2.5 <= weight <= 300):
            raise ValueError("Weight must be between 2.5 and 300 kg.")
        
        height = float(input("Enter your height (m): "))
        if not (0.5 <= height <= 2.5):
            raise ValueError("Height must be between 0.5 and 2.5 meters.")
        
        bmi = float(input("Enter your BMI: "))
        if not (10 <= bmi <= 60):
            raise ValueError("BMI must be between 10 and 60.")
        
        gender = input("Enter your gender (Male/Female): ").capitalize()
        if gender not in ['Male', 'Female']:
            raise ValueError("Please enter a valid gender (Male/Female).")
        
        age = int(input("Enter your age: "))
        if not (0 <= age <= 120):
            raise ValueError("Age must be between 0 and 120 years.")

        return weight, height, bmi, gender, age

    weight, height, bmi, gender, age = get_user_input()
    predicted_bfp = predict_body_fat(weight, height, bmi, gender, age)
    print(f"Predicted Body Fat Percentage: {predicted_bfp}")

