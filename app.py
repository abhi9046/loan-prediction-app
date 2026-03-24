import streamlit as st
import pickle
import numpy as np

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.set_page_config(page_title="Loan Prediction", layout="centered")

st.title("💰 Loan Approval Prediction System")
st.subheader("Enter Applicant Details")

# -------- INPUT FIELDS --------
income = st.number_input("Income (Annual)", min_value=0, value=50000)
loan_amount = st.number_input("Loan Amount", min_value=0, value=800)

education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

# Optional advanced inputs (better prediction)
cibil = st.slider("CIBIL Score", 300, 900, 650)
loan_term = st.number_input("Loan Term (months)", value=12)

# -------- ENCODING --------
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

# -------- PREPARE INPUT --------
input_data = [0] * len(columns)

for i, col in enumerate(columns):
    col = col.strip()
    
    if col == "income_annum":
        input_data[i] = income
    elif col == "loan_amount":
        input_data[i] = loan_amount
    elif col == "education":
        input_data[i] = education
    elif col == "self_employed":
        input_data[i] = self_employed
    elif col == "cibil_score":
        input_data[i] = cibil
    elif col == "loan_term":
        input_data[i] = loan_term

# -------- PREDICTION --------
if st.button("Predict"):
    prediction = model.predict([input_data])[0]
    prob = model.predict_proba([input_data])[0][1]

    st.write(f"### Approval Probability: {prob:.2f}")

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")