# 🩺 Health Risk Predictor

A cutting-edge, clinical AI diagnostic web application that utilizes **Machine Learning** to perform multi-disease risk assessments based on patient biometrics and vital statistics.

![UI Preview](https://img.shields.io/badge/UI-Clinical_Glassmorphism-06B6D4?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Flask-0B1121?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Vercel Ready](https://img.shields.io/badge/Vercel-Deployed-black?style=for-the-badge&logo=vercel&logoColor=white)

---

## ✨ Features

- **Multi-Disease Prediction:** Simultaneously evaluates the risk of **Heart Disease**, **Stroke**, and **Diabetes** using Scikit-Learn predictive models.
- **Biometric Vitals Processing:** Analyzes complex health indicators including Systolic/Diastolic Blood Pressure, Fasting Glucose, Cholesterol, BMI, and Lifestyle factors (Smoking status).
- **Automated BP Categorization:** Instantly categorizes Blood Pressure (e.g., Normal, Elevated, Stage 1 Hypertension) according to clinical guidelines.
- **Premium Clinical UI:** Features an immersive, dark-mode medical dashboard with glassmorphism, glowing custom sliders, and smooth CSS animations (scanning radar effects).
- **Vercel Serverless Ready:** Optimized Python 3.12 dependencies and routing via `vercel.json` to deploy flawlessly on Vercel's serverless functions.

---

## 🛠️ Technology Stack

* **Backend Framework:** Flask (Python 3.12)
* **Machine Learning:** Scikit-Learn (Predictive models & StandardScaler), Pandas, Numpy
* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
* **Deployment:** Vercel (Serverless Functions)

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/healthriskpredictor-main.git
cd healthriskpredictor-main
```

### 2. Create a Virtual Environment (Optional but recommended)
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Flask Server
```bash
python app.py
```

### 5. View Dashboard
Open your browser and navigate to: [http://localhost:5000](http://localhost:5000)

---

## ☁️ How to Deploy on Vercel

This application is fully optimized for Vercel deployment and has been patched for Python 3.12 dependency compatibility.

1. Push your code to a GitHub repository.
2. Go to your [Vercel Dashboard](https://vercel.com/dashboard) and click **Add New > Project**.
3. Import your repository.
4. Click **Deploy**. Vercel will use the provided `vercel.json` and `requirements.txt` to instantly build and deploy your Flask app.

---

## ⚠️ Medical Disclaimer
**This application is an AI predictive model built for educational and software demonstration purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment.**
