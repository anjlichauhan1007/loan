from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('customer_model')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/content')
def content():
    return render_template('content.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    customer_type = int(request.form['customer_type'])
    satisfaction = int(request.form['satisfaction'])
    age = int(request.form['age'])
    inflight_wifi = int(request.form['inflight_wifi'])
    dep_arr_time = int(request.form['dep_arr_time'])
    ease_online_booking = int(request.form['ease_online_booking'])
    gate_location = int(request.form['gate_location'])
    dep_delay = float(request.form['dep_delay'])

    # Create input array
    features = np.array([[customer_type, satisfaction, age, inflight_wifi, dep_arr_time, ease_online_booking,
                          gate_location, dep_delay]])

    # Predict
    prediction = model.predict(features)[0]

    return render_template('index.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)