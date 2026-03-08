from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# set template directory relative to this file (project5/templates)
template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
app = Flask(__name__, template_folder=template_dir)

# Load the trained model
try:
    model = joblib.load('house_price_predict')
except FileNotFoundError:
    model = None

# Feature information
FEATURES = {
    'CRIM': {'label': 'Crime Rate', 'min': 0, 'max': 100, 'step': 0.01},
    'ZN': {'label': 'Zoning - Residential %', 'min': 0, 'max': 100, 'step': 1},
    'INDUS': {'label': 'Industrial %', 'min': 0, 'max': 30, 'step': 0.1},
    'CHAS': {'label': 'Charles River (1=Yes, 0=No)', 'min': 0, 'max': 1, 'step': 1},
    'NOX': {'label': 'Nitric Oxide Concentration', 'min': 0.3, 'max': 0.9, 'step': 0.01},
    'RM': {'label': 'Avg Rooms per Dwelling', 'min': 3, 'max': 9, 'step': 0.1},
    'AGE': {'label': 'Age of House (%)', 'min': 1, 'max': 150, 'step': 1},
    'DIS': {'label': 'Distance to Job Centers', 'min': 1, 'max': 15, 'step': 0.1},
    'RAD': {'label': 'Accessibility to Highways', 'min': 1, 'max': 24, 'step': 1},
    'TAX': {'label': 'Property Tax Rate', 'min': 100, 'max': 800, 'step': 1},
    'PTRATIO': {'label': 'Pupil-Teacher Ratio', 'min': 10, 'max': 25, 'step': 0.1},
    'LSTAT': {'label': 'Lower Status Population %', 'min': 0, 'max': 40, 'step': 0.1}
}

@app.route('/')
def index():
    return render_template('index.html', features=FEATURES)

@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.json
        
        # Extract features in the correct order
        features_list = []
        for feature_name in FEATURES.keys():
            value = float(data.get(feature_name, 0))
            features_list.append(value)
        
        # Convert to numpy array and reshape
        X = np.array(features_list).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(X)[0]
        
        # Return prediction (multiply by 1000 since MEDV is in $1000s)
        price = round(prediction * 1000, 2)
        
        return jsonify({
            'success': True,
            'prediction': prediction,
            'price': f'${price:,.2f}',
            'price_raw': price
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/features', methods=['GET'])
def get_features():
    return jsonify(FEATURES)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
