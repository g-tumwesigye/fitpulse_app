# FitPulse App

FitPulse App predicts Body Fat Percentage using a trained Linear regression model. This App helps users track their fitness levels by providing predictions based on their personal details such as weight, height, age, BMI, and gender. The application is built using Flutter for the frontend and FastAPI for the backend, integrating machine learning for the prediction.

## Table of Contents
1. [Introduction](#1-introduction)
2. [Features](#2-features)
3. [Tech Stack](#3-tech-stack)
4. [Installation](#4-installation)
5. [Model Training](#5-model-training)
6. [API (FastAPI)](#6-api-fastapi)
7. [Usage](#7-usage)
8. [Conclusion](#8-conclusion)

## 1. Introduction

The **FitPulse App** is a mobile application designed to predict Body Fat Percentage (BFP) based on various factors like weight, height, BMI, age, and gender. The model is trained using a dataset and implemented through machine learning techniques using  linear regression). The app interacts with an API built using FastAPI, which serves the trained model for prediction requests.

### Problem Statement:
Track and predict the body fat percentage for individuals based on their personal information. This can help users better understand their health and make informed decisions on how to improve.

---

## 2. Features

- **Linear Regression Model**: Predicts Body Fat Percentage based on user input.
- **Flutter Mobile App**: User-friendly app to input data and receive predictions.
- **FastAPI Backend**: Provides a robust and fast API for making predictions.
- **Real-Time Predictions**: Predict body fat percentage instantly using the trained model.

---

## 3. Tech Stack

- **Machine Learning**: Python, Scikit-Learn
- **Backend**: FastAPI, Uvicorn
- **Frontend**: Flutter
- **Database**: None (Data handled via API)
- **Model Deployment**: The model is deployed via FastAPI backend, which communicates with the Flutter app.
- **Version Control**: Git, GitHub

---

## 4. Installation

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

```markdown
Model Training
The model is trained on the dataset from Kaggle (https://www.kaggle.com/datasets/mustafa20635/fitness-exercises-using-bfp-and-bmi) using Linear Regression to predict Body Fat Percentage based on the user's weight, height, BMI, Gender, and age.

Usage
Input data (weight, height, BMI, age, gender) in the Flutter app.
Get the predicted Body Fat Percentage from the FastAPI backend.

