from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

# ==========================
# LOAD TRAINED MODEL
# ==========================
model = joblib.load('loan_aprovel_model')

app = Flask(__name__)

# ==========================
# ENCODING DICTIONARIES
# ==========================
loan_intent_dct = {
    'PERSONAL': 1, 'EDUCATION': 2, 'MEDICAL': 3,
    'VENTURE': 4, 'HOMEIMPROVEMENT': 5, 'DEBTCONSOLIDATION': 6
}

person_gender_dict = {'female': 1, 'male': 0}

person_edu = {
    'Master': 1, 'High School': 2, 'Bachelor': 3,
    'Associate': 4, 'Doctorate': 5
}

person_home_ownership_dict = {
    'RENT': 1, 'OWN': 2, 'MORTGAGE': 3, 'OTHER': 4
}

previous_loan_defaults_on_file_dct = {'No': 1, 'Yes': 2}

# ==========================
# ROUTES
# ==========================
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        person_age = float(request.form.get('person_age', 0))
        person_gender = request.form.get('person_gender', '')
        person_education = request.form.get('person_education', '')
        person_income = float(request.form.get('person_income', 0))
        person_emp_exp = int(request.form.get('person_emp_exp', 0))
        person_home_ownership = request.form.get('person_home_ownership', '')
        loan_amount = float(request.form.get('loan_amount', 0))
        loan_intent = request.form.get('loan_intent', '')
        loan_interest_rate = float(request.form.get('loan_interest_rate', 0))
        loan_percent_income = float(request.form.get('loan_percent_income', 0))
        cb_person_cred_hist_length = float(request.form.get('cb_person_cred_hist_length', 0))
        credit_score = int(request.form.get('credit_score', 0))
        previous_loan_defaults_on_file = request.form.get('previous_loan_defaults_on_file', '')
        
        # Encode categorical variables
        try:
            person_gender_encoded = person_gender_dict[person_gender]
            person_education_encoded = person_edu[person_education]
            person_home_ownership_encoded = person_home_ownership_dict[person_home_ownership]
            loan_intent_encoded = loan_intent_dct[loan_intent]
            previous_loan_defaults_encoded = previous_loan_defaults_on_file_dct[previous_loan_defaults_on_file]
        except KeyError as e:
            return jsonify({'error': f'Invalid value: {str(e)}', 'success': False})

        # Create feature array - all 13 features
        features = np.array([[
            person_age,
            person_gender_encoded,
            person_education_encoded,
            person_income,
            person_emp_exp,
            person_home_ownership_encoded,
            loan_amount,
            loan_intent_encoded,
            loan_interest_rate,
            loan_percent_income,
            cb_person_cred_hist_length,
            credit_score,
            previous_loan_defaults_encoded
        ]])

        # Make prediction
        prediction = model.predict(features)[0]
        
        try:
            probability = model.predict_proba(features)[0]
            confidence = float(max(probability) * 100)
        except:
            confidence = 0.0

        result = {
            'prediction': int(prediction),
            'status': 'Loan Approved ✓' if prediction == 1 else 'Loan Denied ✗',
            'confidence': confidence,
            'success': True
        }

        return jsonify(result)

    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}', 'success': False})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)