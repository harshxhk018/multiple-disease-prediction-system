import streamlit as st
import joblib
import numpy as np

# =========================
# Load Models
# =========================

heart_model = joblib.load("heart_model.pkl")
diabetes_model = joblib.load("diabetes_model.pkl")
breast_model = joblib.load("breast_cancer_model.pkl")

diabetes_scaler = joblib.load("diabetes_scaler.pkl")
breast_scaler = joblib.load("breast_cancer_scaler.pkl")

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Multiple Disease Prediction System")
st.write("Select a disease from the sidebar and enter patient information.")

# =========================
# Sidebar
# =========================

disease = st.sidebar.selectbox(
    "Choose Disease",
    (
        "Heart Disease",
        "Diabetes",
        "Breast Cancer"
    )
)

# ==================================================
# HEART DISEASE
# ==================================================

if disease == "Heart Disease":

    st.header("❤️ Heart Disease Prediction")

    age = st.number_input("Age", 0, 120, 45)
    sex = st.number_input("Sex (0=Female,1=Male)", 0, 1, 1)
    restbp = st.number_input("RestBP", 50, 250, 120)
    chol = st.number_input("Cholesterol", 50, 600, 200)
    fbs = st.number_input("FBS", 0, 1, 0)
    restecg = st.number_input("RestECG", 0, 2, 0)
    maxhr = st.number_input("MaxHR", 50, 250, 150)
    exang = st.number_input("ExAng", 0, 1, 0)
    oldpeak = st.number_input("OldPeak", 0.0, 10.0, 1.0)
    slope = st.number_input("Slope", 0, 2, 1)
    ca = st.number_input("CA", 0, 4, 0)

    chest_nonanginal = st.number_input("ChestPain_nonanginal", 0, 1, 0)
    chest_nontypical = st.number_input("ChestPain_nontypical", 0, 1, 0)
    chest_typical = st.number_input("ChestPain_typical", 0, 1, 0)

    thal_normal = st.number_input("Thal_normal", 0, 1, 1)
    thal_reversible = st.number_input("Thal_reversable", 0, 1, 0)

    if st.button("Predict Heart Disease"):

        features = np.array([[

            age,
            sex,
            restbp,
            chol,
            fbs,
            restecg,
            maxhr,
            exang,
            oldpeak,
            slope,
            ca,
            chest_nonanginal,
            chest_nontypical,
            chest_typical,
            thal_normal,
            thal_reversible

        ]])

        prediction = heart_model.predict(features)

        if prediction[0] == 1:
            st.error("Heart Disease Detected")
        else:
            st.success("No Heart Disease Detected")

# ==================================================
# DIABETES
# ==================================================

elif disease == "Diabetes":

    st.header("🩸 Diabetes Prediction")

    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose", 0, 300, 100)
    bloodpressure = st.number_input("Blood Pressure", 0, 200, 70)
    skinthickness = st.number_input("Skin Thickness", 0, 100, 20)
    insulin = st.number_input("Insulin", 0, 1000, 80)
    bmi = st.number_input("BMI", 0.0, 80.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 5.0, 0.5)
    age = st.number_input("Age", 1, 120, 30)

    if st.button("Predict Diabetes"):

        features = np.array([[

            pregnancies,
            glucose,
            bloodpressure,
            skinthickness,
            insulin,
            bmi,
            dpf,
            age

        ]])

        features = diabetes_scaler.transform(features)

        prediction = diabetes_model.predict(features)

        if prediction[0] == 1:
            st.error("Diabetes Detected")
        else:
            st.success("No Diabetes Detected")

# ==================================================
# BREAST CANCER
# ==================================================

elif disease == "Breast Cancer":

    st.header("🎗️ Breast Cancer Prediction")

    age = st.number_input("Age Category", 0, 5, 2)
    menopause = st.number_input("Menopause Category", 0, 2, 1)
    tumor_size = st.number_input("Tumor Size Category", 0, 10, 2)
    inv_nodes = st.number_input("Inv Nodes", 0, 5, 0)

    node_caps = st.number_input("Node Caps", 0, 1, 0)

    deg_malig = st.number_input("Deg Malig", 1, 3, 2)

    breast = st.number_input("Breast", 0, 1, 1)

    breast_quad = st.number_input("Breast Quad", 0, 4, 2)

    irradiat = st.number_input("Irradiat", 0, 1, 0)

    if st.button("Predict Breast Cancer"):

        features = np.array([[

            age,
            menopause,
            tumor_size,
            inv_nodes,
            node_caps,
            deg_malig,
            breast,
            breast_quad,
            irradiat

        ]])

        features = breast_scaler.transform(features)

        prediction = breast_model.predict(features)

        if prediction[0] == 1:
            st.error("Cancer Recurrence Detected")
        else:
            st.success("No Cancer Recurrence Detected")