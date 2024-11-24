# FitPulse App

FitPulse App is a mobile application designed to predict **Body Fat Percentage** based on user-provided inputs (weight, height, BMI, gender and age). It integrates a **FastAPI backend** for predictions and provides a clean, user-friendly interface.

## Features

- **Personalized Body Fat Prediction**: Predicts body fat percentage using a trained machine learning model.
- **Clean UI**: Intuitive interface for entering user data.
- **FastAPI Integration**: Communicates with a FastAPI backend for real-time predictions.
- **Flutter Framework**: Built using Flutter.

## Tech Stack

- **Frontend**: Flutter (Dart)
- **Backend**: FastAPI (Python)
- **Machine Learning**: Trained Linear Regression Model
- **Deployment**: Render for backend hosting


## Installation

### Prerequisites
- **Flutter SDK** (version 3.5.2 or higher)
- **Android Studio** or **VS Code** with Flutter setup
- A compatible emulator or physical device

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/fitpulse_app.git
   cd fitpulse_app
   flutter pub get
   flutter run ```

# Usage

1. Launch the app on your device.
2. Use the **"Get Started"** button to navigate to the input screen.
3. Fill in the required fields:
    - Weight (kg)
    - Height (m)
    - BMI
    - Gender (Male/Female)
    - Age (years)
4. Tap **"PREDICT"** to view the predicted body fat percentage.


## API Endpoints

The app communicates with a backend hosted at:  
**Base URL**: `https://fitpulse-app.onrender.com`


## Contact

**Author**: Geofrey Tumwesigye  
**Email**: g.tumwesigy@alustudent.com  




