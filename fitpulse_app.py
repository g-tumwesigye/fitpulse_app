from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import joblib
import pandas as pd
import logging

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initializing the FastAPI application
app = FastAPI(title="Fitpulse Body Fat Prediction API", version="1.0.0")

# Here I am loading the model and scaler
try:
    model = joblib.load("best_model.pkl")  
    scaler = joblib.load("scaler.pkl")   
    logger.info("Model and scaler loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model or scaler: {e}", exc_info=True)
    raise RuntimeError("Failed to load model or scaler.")

# Feature names & the order
FEATURE_ORDER = ["Weight", "Height", "BMI", "Gender", "Age"]
# Mapping for gender as the model was trained with numeric encoding
GENDER_MAPPING = {"Male": 1, "Female": 0}

# Defining the structure of the input data using Pydantic
class InputData(BaseModel):
    Weight: float  # User's weight (kg)
    Height: float  # User's height (cm)
    BMI: float     # User's BMI 
    Gender: str    # User's gender ('Male' or 'Female')
    Age: int       # User's age in years

    # Validator to ensure the values for the fields are positive
    @field_validator("Weight", "Height", "BMI", "Age")
    def validate_positive(cls, value):
        if value <= 0:
            raise ValueError("All values must be greater than zero.")  
        return value

    # Validator for gender to ensure it matches the expected values
    @field_validator("Gender")
    def validate_gender(cls, value):
        if value not in GENDER_MAPPING:
            raise ValueError("Gender must be either 'Male' or 'Female'.") 
        return value

# Root endpoint to test if the API is running
@app.get("/")
def home():
    logger.info("Home endpoint accessed.")
    return {"message": "Welcome to the Fitpulse Body Fat Prediction API!"}

# Endpoint to handle prediction requests
@app.post("/predict")
def predict(data: InputData):
    try:
        logger.debug(f"Received input data: {data}")
        
        # Converting the input data to a pandas DataFrame for processing
        input_df = pd.DataFrame([{
            "Weight": data.Weight,
            "Height": data.Height,
            "BMI": data.BMI,
            "Gender": GENDER_MAPPING[data.Gender],
            "Age": data.Age,
        }])
        logger.debug(f"Input data as DataFrame: {input_df}")

        # Scaling the input data using the same scaler used during training
        scaled_input = scaler.transform(input_df)
        logger.debug(f"Scaled input data: {scaled_input}")

        # Predict Body Fat Percentage using the trained model
        prediction = model.predict(scaled_input)
        logger.info(f"Prediction result: {prediction[0]}")

        # Return the prediction result as a JSON response
        return {"Body Fat Percentage": float(prediction[0])}

    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        # Handle any errors during prediction and return a 500 error
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# The app runs on all interfaces for access from other devices
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

