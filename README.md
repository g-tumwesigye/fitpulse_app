# FitPulse App


## Table of Contents
1. [Introduction](#introduction)  
2. [Problem Statement](#problem-statement)
3. [Features](#features)   
4. [Tech Stack](#tech-stack)
5. [Model Development](#model-development)  
6. [API Details](#api-details)  
7. [Flutter App](#flutter-app)  
8. [Video Demo](#video-demo)  
9. [Setup Instructions](#setup-instructions)  
10. [Acknowledgements](#acknowledgements)


---

## Introduction  
The **FitPulse App** is a predictive mobile application that predicts **Body Fat Percentage (BFP)** using user-provided inputs of **Weight, Height, BMI, Gender and Age**. The application was built using Flutter for the frontend (a user-friendly mobile application) and FastAPI for the backend. The prediction model was built using the **Random Forest Model** trained using dataset from Kaggle (https://www.kaggle.com/datasets/mustafa20635/fitness-exercises-using-bfp-and-bmi) and implemented through machine learning techniques. The app interacts with an API built using FastAPI which serves the trained model for prediction requests.


### Problem Statement:
Track and predict the body fat percentage of individuals based on their personal information (Weight, Height, BMI, Age & Gender). This can help users better understand their health and make informed decisions on how to improve.

---

## Features  
- **Machine Learning**: A Random Forest model for predicting Body Fat Percentage based on usr in put.
- **API**: FastAPI for the backend with public access via Render.  
- **Flutter Mobile App**:  User-friendly app to input data and receive predictions. 
- **Real-Time Predictions**: Predict body fat percentage instantly using the trained model. 

---


## Tech Stack

- **Machine Learning**: Python, Scikit-Learn
- **Backend**: FastAPI, Uvicorn
- **Frontend**: Flutter
- **Model Deployment**: The model is deployed via FastAPI backend, which communicates with the Flutter app.
- **Version Control**: Git, GitHub

---

## Model Development  
The project compared three machine learning models:  
1. **Linear Regression**  
2. **Decision Trees**  
3. **Random Forest**  

**Final Model**:  
- The **Random Forest model** was selected for deployment due to its superior performance.  
- Model artifacts:  
  - `best_model.pkl`: The trained model.  
  - `scaler.pkl`: StandardScaler used to normalize inputs.  

---

## API Details  
The FastAPI application allows for seamless predictions.  

### **Public Endpoint**:  
- URL: [https://fitpulse-app.onrender.com/]  

**POST Endpoint**:  
   - **Path**: `https://fitpulse-app.onrender.com/docs#/default/api_predict_predict_post`  
   - **Inputs**:  
     - `weight` 
     - `height`  
     - `bmi` 
     - `gender`  
     - `age`   
   - **Output**: Predicted Body Fat Percentage or an error message if input constraints are violated.  
**CORS Middleware**: Enables cross-origin requests.  
**Swagger UI**: API documentation available at `https://fitpulse-app.onrender.com/docs`.  

---

## Flutter App  
The Flutter mobile app interacts with the FastAPI endpoint to make predictions.  

### **Key Features**:  
- Input fields for **Weight, Height, BMI, Gender and Age**.  
- A "Predict" button for triggering predictions.  
- Display area for showing prediction results or error messages.  

### **UI Layout**:  
- Text fields are aligned cleanly for easy data input.  
- Results are prominently displayed in the app interface.  

---


## Figma Design  
The design for the FitPulse App's user interface was created in Figma. 

[Figma Design for FitPulse App](https://www.figma.com/design/b6unAKFAvl92AXWiwlsZBB/FITPULSE_APP?node-id=0-1&node-type=canvas&t=lQLLBIpmwXGiCiF9-0)

---

## Video Demo  
- [YouTube Video Demo](#)  
  - The video demonstrates:  
    1. **Swagger UI**: Testing API predictions.  
    2. **Flutter App**: Feeding inputs, predicting Body Fat Percentage and displaying results.  

---

## Setup Instructions

Follow the instructions below to set up the **FitPulse App** locally.

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/g-tumwesigye/fitpulse_app.git


Backend Setup

1. Create a virtual environment:
python -m venv venv

2. Activate the virtual environment:

Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run FastAPI server:
uvicorn main:app --reload

Frontend Set Up (Flutter App)
1. Install Flutter SDK

2. Run the Flutter app:
flutter run
```


### Acknowledgements
Dataset: The dataset used to train the model was sourced from Kaggle (https://www.kaggle.com/datasets/mustafa20635/fitness-exercises-using-bfp-and-bmi).


