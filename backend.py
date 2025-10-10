import os
import sys
0
try:
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.metrics import accuracy_score
except Exception as e:
    print("Missing dependency or import error:", e)
    print("Please install required packages, for example: pip install -r requirements.txt")
    raise


def encode_categoricals(df):
    encoders = {}
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
    return df, encoders


def bp_category(s, d):
    if s < 120 and d < 80:
        return "Normal"
    elif 120 <= s <= 129 and d < 80:
        return "Elevated"
    elif 130 <= s <= 139 or 80 <= d <= 89:
        return "Hypertension Stage 1"
    elif 140 <= s <= 180 or 90 <= d <= 120:
        return "Hypertension Stage 2"
    else:
        return "Hypertensive Crisis"


def diabetes_level(g):
    if g < 140:
        return "Controlled"
    elif 140 <= g <= 199:
        return "Prediabetic"
    else:
        return "Uncontrolled"


def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Please enter a value between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_float_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Please enter a value between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_choice_input(prompt, choices, shortcuts=None):
    choices_lower = [c.lower() for c in choices]
    shortcuts = {k.lower(): v.lower() for k, v in (shortcuts or {}).items()}
    while True:
        value = input(prompt).strip().lower()
        if value in shortcuts:
            value = shortcuts[value]
        if value in choices_lower:
            return value
        else:
            print(f"Invalid choice. Please enter one of: {', '.join(choices)}")


def prepare_models(data_dir=None):
    base = data_dir or os.path.dirname(__file__)
    heart_path = os.path.join(base, 'heart.csv')
    stroke_path = os.path.join(base, 'stroke.csv')
    diabetes_path = os.path.join(base, 'diabetes.csv')

    heart_df = pd.read_csv(heart_path)
    stroke_df = pd.read_csv(stroke_path)
    diabetes_df = pd.read_csv(diabetes_path)

    heart_df, _ = encode_categoricals(heart_df)
    stroke_df, _ = encode_categoricals(stroke_df)
    diabetes_df, _ = encode_categoricals(diabetes_df)

    X_heart, y_heart = heart_df.drop('target', axis=1), heart_df['target']
    X_stroke, y_stroke = stroke_df.drop('stroke', axis=1), stroke_df['stroke']
    X_diabetes, y_diabetes = diabetes_df.drop('Outcome', axis=1), diabetes_df['Outcome']

    scaler_heart = StandardScaler().fit(X_heart)
    scaler_stroke = StandardScaler().fit(X_stroke)
    scaler_diabetes = StandardScaler().fit(X_diabetes)

    Xh_train, Xh_test, yh_train, yh_test = train_test_split(scaler_heart.transform(X_heart), y_heart, test_size=0.2, random_state=42)
    Xs_train, Xs_test, ys_train, ys_test = train_test_split(scaler_stroke.transform(X_stroke), y_stroke, test_size=0.2, random_state=42)
    Xd_train, Xd_test, yd_train, yd_test = train_test_split(scaler_diabetes.transform(X_diabetes), y_diabetes, test_size=0.2, random_state=42)

    model_heart = RandomForestClassifier(random_state=42).fit(Xh_train, yh_train)
    model_stroke = RandomForestClassifier(random_state=42).fit(Xs_train, ys_train)
    model_diabetes = RandomForestClassifier(random_state=42).fit(Xd_train, yd_train)

    print("\n--- Model Evaluation ---")
    print("Heart Model Accuracy:", accuracy_score(yh_test, model_heart.predict(Xh_test)))
    print("Stroke Model Accuracy:", accuracy_score(ys_test, model_stroke.predict(Xs_test)))
    print("Diabetes Model Accuracy:", accuracy_score(yd_test, model_diabetes.predict(Xd_test)))

    return {
        'model_heart': model_heart,
        'model_stroke': model_stroke,
        'model_diabetes': model_diabetes,
        'scaler_heart': scaler_heart,
        'scaler_stroke': scaler_stroke,
        'scaler_diabetes': scaler_diabetes,
        'X_heart_cols': X_heart.columns.tolist(),
        'X_stroke_cols': X_stroke.columns.tolist(),
        'X_diabetes_cols': X_diabetes.columns.tolist(),
    }


def interactive_loop(ctx):
    model_heart = ctx['model_heart']
    model_stroke = ctx['model_stroke']
    model_diabetes = ctx['model_diabetes']
    scaler_heart = ctx['scaler_heart']
    scaler_stroke = ctx['scaler_stroke']
    scaler_diabetes = ctx['scaler_diabetes']
    X_heart_cols = ctx['X_heart_cols']
    X_stroke_cols = ctx['X_stroke_cols']
    X_diabetes_cols = ctx['X_diabetes_cols']

    while True:
        print("\n--- Enter Your Health Details ---")
        age = get_int_input("Age: ", 0, 100)
        gender = get_choice_input("Gender (Male/Female): ", ["male", "female"], shortcuts={"m": "male", "f": "female"})
        systolic = get_int_input("Systolic BP: ", 50, 250)
        diastolic = get_int_input("Diastolic BP: ", 30, 200)
        cholesterol = get_float_input("Cholesterol: ", 50, 500)
        glucose = get_float_input("Glucose: ", 50, 500)
        bmi = get_float_input("BMI: ", 10, 60)
        smoking = get_choice_input("Smoking (Yes/No): ", ["yes", "no"], shortcuts={"y": "yes", "n": "no"})
        gender_enc = 1 if gender == "male" else 0
        smoking_enc = 1 if smoking == "yes" else 0
        hypertension = 1 if systolic >= 140 or diastolic >= 90 else 0

        heart_input = pd.DataFrame([[age, gender_enc, cholesterol, systolic, diastolic, bmi, smoking_enc] + [0]*(len(X_heart_cols)-7)], columns=X_heart_cols)
        stroke_input = pd.DataFrame([[gender_enc, age, hypertension, 0, glucose, smoking_enc, bmi, 0, 0] + [0]*(len(X_stroke_cols)-9)], columns=X_stroke_cols)
        diabetes_input = pd.DataFrame([[0, glucose, 0, 0, 0, bmi, 0, age] + [0]*(len(X_diabetes_cols)-8)], columns=X_diabetes_cols)

        heart_pred = model_heart.predict(scaler_heart.transform(heart_input))[0]
        stroke_pred = model_stroke.predict(scaler_stroke.transform(stroke_input))[0]
        diabetes_pred = model_diabetes.predict(scaler_diabetes.transform(diabetes_input))[0]

        print("\n--- Health Risk Report ---")
        print(f"Heart Disease Risk: {'⚠ At Risk' if heart_pred == 1 else '✅ Low Risk'}")
        print(f"Diabetes: {'⚠ At Risk (' + diabetes_level(glucose) + ')' if diabetes_pred == 1 else '✅ Low Risk'}")
        print(f"Stroke Risk: {'⚠ At Risk' if stroke_pred == 1 else '✅ Low Risk'}")
        print(f"Blood Pressure: {bp_category(systolic, diastolic)}")
        again = get_choice_input("\nCheck another person? (Yes/No): ", ["yes", "no"], shortcuts={"y": "yes", "n": "no"})
        if again == "no":
            break


if __name__ == '__main__':
    ctx = prepare_models()
    interactive_loop(ctx)
