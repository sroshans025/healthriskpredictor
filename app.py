from flask import Flask, render_template, request, jsonify
from backend import prepare_models, bp_category, diabetes_level  # Import your existing backend functions
import pandas as pd

app = Flask(__name__)

# Prepare ML models once
ctx = prepare_models()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract values
    age = int(data['age'])
    gender = data['gender'].lower()
    systolic = int(data['systolic'])
    diastolic = int(data['diastolic'])
    cholesterol = float(data['cholesterol'])
    glucose = float(data['glucose'])
    bmi = float(data['bmi'])
    smoking = data['smoking'].lower()

    # Encode
    gender_enc = 1 if gender == "male" else 0
    smoking_enc = 1 if smoking == "yes" else 0
    hypertension = 1 if systolic >= 140 or diastolic >= 90 else 0

    model_heart = ctx['model_heart']
    model_stroke = ctx['model_stroke']
    model_diabetes = ctx['model_diabetes']
    scaler_heart = ctx['scaler_heart']
    scaler_stroke = ctx['scaler_stroke']
    scaler_diabetes = ctx['scaler_diabetes']

    X_heart_cols = ctx['X_heart_cols']
    X_stroke_cols = ctx['X_stroke_cols']
    X_diabetes_cols = ctx['X_diabetes_cols']

    heart_input = pd.DataFrame([[age, gender_enc, cholesterol, systolic, diastolic, bmi, smoking_enc] + [0]*(len(X_heart_cols)-7)], columns=X_heart_cols)
    stroke_input = pd.DataFrame([[gender_enc, age, hypertension, 0, glucose, smoking_enc, bmi, 0, 0] + [0]*(len(X_stroke_cols)-9)], columns=X_stroke_cols)
    diabetes_input = pd.DataFrame([[0, glucose, 0, 0, 0, bmi, 0, age] + [0]*(len(X_diabetes_cols)-8)], columns=X_diabetes_cols)

    heart_pred = model_heart.predict(scaler_heart.transform(heart_input))[0]
    stroke_pred = model_stroke.predict(scaler_stroke.transform(stroke_input))[0]
    diabetes_pred = model_diabetes.predict(scaler_diabetes.transform(diabetes_input))[0]

    result = {
        "heart_risk": "⚠ At Risk" if heart_pred == 1 else "✅ Low Risk",
        "stroke_risk": "⚠ At Risk" if stroke_pred == 1 else "✅ Low Risk",
        "diabetes": f"⚠ At Risk ({diabetes_level(glucose)})" if diabetes_pred == 1 else "✅ Low Risk",
        "bp_category": bp_category(systolic, diastolic)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
