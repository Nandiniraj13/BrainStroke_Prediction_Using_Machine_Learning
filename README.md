# BrainStroke_Prediction_using_Machine_Learning

## Brain Stroke Prediction Web Application

This is a Flask-based web application for predicting the risk of brain stroke using machine learning models. It leverages patient health data such as age, BMI, average glucose level, and other relevant features to estimate the likelihood of a stroke.

## Project Overview

Stroke is a serious medical condition that can cause long-term disability or death. Early prediction of stroke risk is crucial for timely intervention and prevention. This application uses machine learning models (Random Forest, Decision Tree, KNN, and Logistic Regression) to predict the likelihood of a stroke based on the user's health metrics.

## Features

- **Prediction of Stroke Risk**: Users input their personal and health data (age, blood pressure, smoking status, etc.) and the system predicts if they are at risk for a stroke.
- **User-Friendly Interface**: The application has a simple form-based UI for collecting user data and displaying the prediction result.
- **Trained Machine Learning Model**: The prediction is based on a pre-trained RandomForest classifier model that has been optimized for accuracy.

## Project Structure

```bash
.
├── app.py                  # Main Flask application
├── model.pickle            # Pre-trained machine learning model
├── templates/
│   ├── index.html          # Home page template
│   ├── predict.html        # Prediction form template
│   └── result.html         # Result page template
├── static/
│   ├── styles.css          # Custom CSS for styling
│   └── images/             # Image assets
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/brain-stroke-prediction.git
   cd brain-stroke-prediction
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

1. Go to the "Predict" page.
2. Fill in your details such as age, gender, blood pressure, smoking status, etc.
3. Click the "Submit" button to get the prediction result.
4. The result will indicate whether you are at risk for a stroke or not.

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, Bootstrap
- **Machine Learning**: Random Forest Classifier (with comparison to other models like Decision Tree, KNN)
- **Data**: Healthcare Stroke Prediction Dataset from Kaggle

## Dataset

The dataset used for training the machine learning model was sourced from [Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset). It contains patient health records such as age, gender, blood pressure, and more.

## Future Enhancements

- Add real-time data input from health monitoring devices.
- Provide personalized lifestyle recommendations based on stroke risk.
- Explore additional machine learning algorithms for higher accuracy.


