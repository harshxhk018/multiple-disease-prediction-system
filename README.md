# 🩺 Multiple Disease Prediction System

A Machine Learning based web application that predicts the likelihood of multiple diseases using trained classification models.

The application provides a simple and user-friendly interface where users can select a disease, enter patient information, and receive real-time predictions.

---

## 🚀 Live Demo

Streamlit App:

[(https://multiple-disease-prediction-system-harsh018nitc.streamlit.app/)](https://multiple-disease-prediction-system-harsh018nitc.streamlit.app/)

---

## 📌 Diseases Supported

### ❤️ Heart Disease Prediction

Predicts the likelihood of heart disease using clinical and cardiovascular parameters.

Features Used:

* Age
* Sex
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Rest ECG
* Maximum Heart Rate
* Exercise Induced Angina
* Old Peak
* Slope
* Number of Major Vessels
* Chest Pain Type
* Thalassemia Information

---

### 🩸 Diabetes Prediction

Predicts diabetes using medical diagnostic measurements.

Features Used:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

### 🎗️ Breast Cancer Prediction

Predicts breast cancer recurrence using clinical parameters.

Features Used:

* Age Category
* Menopause Status
* Tumor Size
* Involved Nodes
* Node Caps
* Degree of Malignancy
* Breast Side
* Breast Quadrant
* Irradiation History

---

## ✨ Features

* Single platform for multiple disease prediction
* Real-time prediction
* User-friendly interface
* Streamlit web application
* Machine Learning based classification models
* Accessible from any device through a browser

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Scikit-Learn
* Joblib

---

## 🤖 Machine Learning Models

| Disease       | Model                    |
| ------------- | ------------------------ |
| Heart Disease | Logistic Regression      |
| Diabetes      | Random Forest Classifier |
| Breast Cancer | Logistic Regression      |

---

## 📂 Project Structure

multiple-disease-prediction-system/

├── app.py

├── requirements.txt

├── README.md

├── heart_model.pkl

├── diabetes_model.pkl

├── diabetes_scaler.pkl

├── breast_cancer_model.pkl

└── breast_cancer_scaler.pkl

---

## ▶️ Run Locally

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py

---

## 🎓 Academic Information

Developed as a Machine Learning project for practical healthcare prediction using classification algorithms.

---

## 👨‍💻 Author

Harsh Kumar

B.Tech Electronics and Communication Engineering (ECE)

National Institute of Technology Calicut (NIT Calicut)
