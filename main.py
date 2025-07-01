import streamlit as st
from prediction_helper import predict

# Page config
st.set_page_config(page_title="InsureWise", layout="wide")

# 🌈 Custom CSS Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: linear-gradient(-45deg, #1f1c2c, #928DAB, #2c3e50, #3498db);
            background-size: 400% 400%;
            animation: gradientFlow 12s ease infinite;
            color: #ffffff;
        }

        @keyframes gradientFlow {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .main-title {
            font-size: 3.8rem;
            font-weight: 800;
            text-align: center;
            margin-top: 2rem;
            background: -webkit-linear-gradient(45deg, #00e6e6, #33ccff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            text-align: center;
            color: #ffffff;
            font-size: 1.3rem;
            font-weight: 500;
            margin-top: 0.5rem;
        }

        label, .css-1cpxqw2, .css-1l269bu, .css-1q8dd3e {
            color: #ffffff !important;
        }

        .stSlider > div[data-baseweb="slider"] > div {
            background-color: #33ccff !important;
        }

        .stSelectbox, .stNumberInput, .stSlider {
            padding: 10px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            color: white !important;
        }

        .stButton>button {
            background-color: #00e6e6;
            color: #000000;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 0.7rem 2.2rem;
            border-radius: 12px;
            border: none;
            margin-top: 15px;
        }

        .stButton>button:hover {
            background-color: #00cccc;
            transform: scale(1.05);
            transition: 0.3s ease;
        }

        .predict-box {
            background: linear-gradient(to right, #00c9ff, #92fe9d);
            color: #000000;
            padding: 1.5rem;
            font-size: 1.3rem;
            font-weight: bold;
            text-align: center;
            border-radius: 15px;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🎉 InsureWise</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Personalized Health Insurance Cost Estimator</div>', unsafe_allow_html=True)

# Sliders
age = st.slider("🎂 Age", 18, 100, 30)
income_lakhs = st.slider("💰 Income (in Lakhs)", 0, 200, 12)

# Columns for input fields
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("⚧️ Gender", ["Male", "Female"])
    smoking_status = st.selectbox("🚬 Smoking Status", ["No Smoking", "Regular", "Occasional"])
    bmi_category = st.selectbox("⚖️ BMI Category", ["Normal", "Obesity", "Overweight", "Underweight"])
    employment_status = st.selectbox("💼 Employment Status", ["Salaried", "Self-Employed", "Freelancer"])

with col2:
    number_of_dependants = st.number_input("👨‍👩‍👧 Number of Dependants", min_value=0, max_value=20, step=1)
    marital_status = st.selectbox("💍 Marital Status", ["Married", "Unmarried"])
    region = st.selectbox("🌎 Region", ["Northwest", "Southeast", "Northeast", "Southwest"])
    genetical_risk = st.slider("🧬 Genetical Risk (0 to 5)", 0, 5, 2)

with col3:
    insurance_plan = st.selectbox("📜 Insurance Plan", ["Bronze", "Silver", "Gold"])
    medical_history = st.selectbox("🏥 Medical History", [
        'No Disease', 'Diabetes', 'High Blood Pressure', 'Diabetes & High BP',
        'Thyroid', 'Heart Disease', 'BP & Heart Disease', 'Diabetes & Thyroid',
        'Diabetes & Heart Disease'
    ])

# Input dict
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction button
col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    if st.button("🎯 Predict Insurance Cost"):
        prediction = predict(input_dict)
        try:
            formatted_prediction = f"{float(prediction):,.2f} $"
        except:
            formatted_prediction = str(prediction)

        st.markdown(f'<div class="predict-box">💰 Your Estimated Premium: {formatted_prediction}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<footer style="text-align:center; color:#bbb; margin-top: 3rem;">✨ Built with 💜 by the InsureWise Team</footer>', unsafe_allow_html=True)