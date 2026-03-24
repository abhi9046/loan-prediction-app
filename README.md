# 💰 Loan Approval Prediction System

A Machine Learning web application that predicts whether a loan application will be **Approved or Rejected** based on applicant details.

---

## 🚀 Project Overview

This project uses a **Random Forest Classifier** to predict loan approval status.  
The model is trained on financial and personal attributes such as income, loan amount, CIBIL score, assets, and employment status.

The application is deployed using **Streamlit**, allowing users to input data and get real-time predictions.

---

## 🧠 Features

- ✅ Real-time loan approval prediction
- 📊 Probability score for approval
- 🎯 Clean and interactive UI using Streamlit
- ⚙️ End-to-end ML pipeline (data → model → deployment)
- 💾 Model saved using Pickle for fast loading

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn (Random Forest)**
- **Streamlit**
- **Pickle**

---

## 📂 Project Structure
roject Structure


ML project/
│
├── app.py # Streamlit web app
├── train_model.py # Model training script
├── model.pkl # Trained model
├── columns.pkl # Feature columns
├── loan_approval_dataset.csv
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/loan-prediction-app.git
cd loan-prediction-app
2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
