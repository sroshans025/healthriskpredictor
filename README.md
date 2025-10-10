<img width="389" height="877" alt="Screenshot 2025-10-10 211212" src="https://github.com/user-attachments/assets/cd569b8c-bc48-45e7-b2e8-7bc108a833ec" /># Health-Risk-Prediction
A Flask-based web application that predicts health risks such as heart disease, diabetes, and stroke using machine learning models trained with scikit-learn. Includes an elegant, modern front-end with live predictions and interactive UI.
# Health Risk Predictor Web App
A complete **Flask + Machine Learning** web application that predicts risks for **Heart Disease**, **Stroke**, and **Diabetes** based on user health inputs like age, BMI, blood pressure, cholesterol, and glucose levels.
The system includes:
- A **Flask backend** with trained ML models (Random Forest)
- A **modern responsive UI** built with HTML, CSS, and JavaScript
- Real-time health risk prediction with animated feedback
- Modular backend structure for easy extension
---

## Features

✅ Predicts:
- Heart Disease Risk  
- Diabetes Risk (with Glucose Level Categorization)  
- Stroke Risk  
- Blood Pressure Category (Normal, Elevated, Stage 1/2, Crisis)

✅ Tech Stack:
- **Frontend:** HTML, CSS (Glassmorphism UI), JavaScript  
- **Backend:** Flask (Python)  
- **ML Models:** Scikit-learn (RandomForestClassifier)  
- **Data Processing:** Pandas, LabelEncoder, StandardScaler

✅ Modern Interface:
- Gradient background and glass-card style  
- Animated loading and result transitions  
- Color-coded risk cards (safe vs warning)

---

## Folder Structure
health-risk-predictor/
│
├── app.py # Flask web app entry point
├── backend.py # Core ML logic & helper functions
├── templates/
│ └── index.html # Frontend HTML page
├── static/
│ ├── style.css # Modern gradient CSS
│ └── script.js # Fetch + result rendering
├── heart.csv # Dataset for heart model (used in training)
├── stroke.csv # Dataset for stroke model
├── diabetes.csv # Dataset for diabetes model
└── README.md

##Screenshot

<img width="389" height="877" alt="Screenshot 2025-10-10 211212" src="https://github.com/user-attachments/assets/12a3321d-44b2-4bca-ac95-9d1f0cfc6ea2" />


