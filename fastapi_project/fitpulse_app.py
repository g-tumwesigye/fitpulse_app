from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import joblib
import pandas as pd

# Initialize FastAPI application
app = FastAPI(title="Fitpulse Body Fat Prediction API", version="1.0.0")

# Load the trained model and scaler from disk
model = joblib.load("best_model.pkl")  # Ensure the model file is correct
scaler = joblib.load("scaler.pkl")    # Ensure the scaler used for training is also loaded

# List of feature names expected by the model
FEATURE_ORDER = ["Weight", "Height", "BMI", "Gender", "Age"]
# Mapping for gender as the model was trained with numeric encoding
GENDER_MAPPING = {"Male": 1, "Female": 0}

# Define the structure of the input data using Pydantic
class InputData(BaseModel):
    Weight: float  # User's weight (kg)
    Height: float  # User's height (cm)
    BMI: float     # User's BMI (calculated from weight and height)
    Gender: str    # User's gender ('Male' or 'Female')
    Age: int       # User's age in years

    # Validator to ensure the values for the fields are positive
    @field_validator("Weight", "Height", "BMI", "Age")
    def validate_positive(cls, value):
        if value <= 0:
            raise ValueError("All values must be greater than zero.")  # Ensure all inputs are positive
        return value

    # Validator for gender to ensure it matches the expected values
    @field_validator("Gender")
    def validate_gender(cls, value):
        if value not in GENDER_MAPPING:
            raise ValueError("Gender must be either 'Male' or 'Female'.")  # Validate gender input
        return value

# Root endpoint to test if the API is running
@app.get("/")
def home():
    return {"message": "Welcome to the Fitpulse Body Fat Prediction API!"}

# Endpoint to handle prediction requests
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert the input data to a pandas DataFrame for processing
        input_df = pd.DataFrame([{
            "Weight": data.Weight,
            "Height": data.Height,
            "BMI": data.BMI,
            "Gender": GENDER_MAPPING[data.Gender],
            "Age": data.Age,
        }])

        # Scale the input data using the same scaler used during training
        scaled_input = scaler.transform(input_df)

        # Predict Body Fat Percentage using the trained model
        prediction = model.predict(scaled_input)

        # Return the prediction result as a JSON response
        return {"Body Fat Percentage": float(prediction[0])}

    except Exception as e:
        # Handle any errors during prediction and return a 500 error
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Ensure the app runs on all interfaces for access from other devices
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

