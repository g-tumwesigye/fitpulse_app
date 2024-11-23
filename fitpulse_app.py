from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib


# Load the trained model and scaler
random_forest = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
except Exception as e:
    print(f"Error loading model or scaler: {e}")

# Initialize FastAPI app
app = FastAPI()

# Define the Pydantic model for input validation
class UserInput(BaseModel):
    weight: float
    height: float
    bmi: float
    gender: str
    age: int

# Function to validate input range
def validate_input(weight, height, bmi, gender, age):
    if not (2.5 <= weight <= 300):
        raise HTTPException(status_code=400, detail="Weight must be between 2.5 and 300 kg.")
    if not (0.5 <= height <= 2.5):
        raise HTTPException(status_code=400, detail="Height must be between 0.5 and 2.5 meters.")
    if not (10 <= bmi <= 60):
        raise HTTPException(status_code=400, detail="BMI must be between 10 and 60.")
    if gender not in ['Male', 'Female']:
        raise HTTPException(status_code=400, detail="Gender must be 'Male' or 'Female'.")
    if not (0 <= age <= 120):
        raise HTTPException(status_code=400, detail="Age must be between 0 and 120 years.")

# Define the prediction function
def predict_body_fat(weight, height, bmi, gender, age):
    # Defining the mappings for Gender
    gender_map = {'Male': 1, 'Female': 0}
    gender_encoded = gender_map.get(gender, -1)
    if gender_encoded == -1:
        raise ValueError("Invalid gender input. Please enter 'Male' or 'Female'.")

    # Create a DataFrame with the same structure as the model training data
    input_data = pd.DataFrame({
        'Weight': [weight],
        'Height': [height],
        'BMI': [bmi],
        'Gender': [gender_encoded],
        'Age': [age],
        'BFPcase': [0],  # Placeholder
        'BMIcase': [0],  # Placeholder
        'Exercise Recommendation Plan': [0]  # Placeholder
    })

    # Ensure the input columns match the model's expected features
    input_data = input_data[['Weight', 'Height', 'BMI', 'Gender', 'Age', 'BFPcase', 'BMIcase', 'Exercise Recommendation Plan']]

    # Standardize the input features
    input_scaled = scaler.transform(input_data)

    # Predict using the Random Forest model
    predicted_bfp = random_forest.predict(input_scaled)

    return predicted_bfp[0]

# Define the POST endpoint to receive user input and make predictions
@app.post("/predict")
def get_prediction(user_input: UserInput):
    # Validate input values
    validate_input(user_input.weight, user_input.height, user_input.bmi, user_input.gender, user_input.age)

    # Make the prediction
    predicted_bfp = predict_body_fat(user_input.weight, user_input.height, user_input.bmi, user_input.gender, user_input.age)

    return {"predicted_bfp": predicted_bfp}


