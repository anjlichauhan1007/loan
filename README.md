# 🏠 Boston House Price Predictor

A beautiful, interactive web application for predicting Boston house prices using Machine Learning. Built with Flask backend and a modern, responsive frontend.

## 🎨 Features

- **Beautiful UI**: Modern, responsive design with gradient backgrounds and smooth animations
- **Interactive Sliders**: Easy-to-use range sliders for all input parameters
- **Real-time Predictions**: Get instant price predictions with animated results
- **13 Features**: Comprehensive property analysis including:
  - Crime Rate (CRIM)
  - Zoning Information (ZN)
  - Industrial Percentage (INDUS)
  - Charles River Proximity (CHAS)
  - Nitric Oxide Levels (NOX)
  - Average Rooms (RM)
  - House Age (AGE)
  - Distance to Job Centers (DIS)
  - Highway Accessibility (RAD)
  - Property Tax Rate (TAX)
  - Pupil-Teacher Ratio (PTRATIO)
  - Lower Status Population (LSTAT)

- **Machine Learning Model**: Decision Tree Regressor trained on Boston Housing Dataset
- **Error Handling**: Comprehensive error messages and input validation
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## 📋 Project Structure

```
house-price-predictor/
├── app.py                          # Flask backend application
├── requirements.txt                # Python dependencies
├── boston_house_prices_dataset.csv # Training dataset
├── house_price_predict            # Trained ML model (joblib)
├── house_price.ipynb              # Jupyter notebook with model development
├── templates/
│   └── index.html                 # Beautiful HTML frontend
└── static/
    ├── style.css                  # Modern CSS styling
    └── script.js                  # Interactive JavaScript
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone/Navigate to the project directory**
   ```bash
   cd d:\Data science\Flask\house-price-predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in your browser**
   - Navigate to `http://localhost:5000`
   - Use the interactive form to predict house prices!

## 📊 How It Works

### Backend (Flask)
- **app.py**: Main Flask application with two key endpoints:
  - `GET /`: Serves the main HTML page
  - `POST /api/predict`: Receives property data and returns predicted price
  
### Frontend
- **Responsive Design**: Beautiful gradient backgrounds and smooth animations
- **Interactive Sliders**: Dual input (text + slider) for intuitive parameter adjustment
- **Real-time Feedback**: Instant visual feedback with loading states and error handling
- **Results Display**: Animated price display with additional property insights

### Machine Learning Model
- **Algorithm**: Decision Tree Regressor
- **Dataset**: Boston Housing Dataset (506 samples)
- **Features**: 12 input features
- **Target**: Median home value (MEDV) in $1000s

## 🎮 Usage

1. **Fill in Property Details**
   - Use text inputs or sliders to enter property characteristics
   - Real-time validation ensures inputs stay within valid ranges

2. **Click "Predict Price"**
   - The model analyzes your inputs instantly
   - Results display with an animated price value

3. **View Results**
   - Estimated market value in USD
   - Price range estimation
   - Confidence indicator

## 🛠️ API Endpoints

### GET `/`
Returns the main HTML page

### POST `/api/predict`
**Request Body:**
```json
{
  "CRIM": 5,
  "ZN": 25,
  "INDUS": 10,
  "CHAS": 0,
  "NOX": 0.5,
  "RM": 6,
  "AGE": 50,
  "DIS": 5,
  "RAD": 10,
  "TAX": 400,
  "PTRATIO": 15,
  "LSTAT": 10
}
```

**Response:**
```json
{
  "success": true,
  "prediction": 24.5,
  "price": "$24,500.00",
  "price_raw": 24500
}
```

## 🎨 Customization

### Change Color Scheme
Edit the CSS variables in `static/style.css`:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --success-color: #27ae60;
}
```

### Modify Model
To use a different ML model:
1. Update the model training in `house_price.ipynb`
2. Re-run the notebook to generate a new `house_price_predict` file
3. No changes needed to the Flask backend!

## 📈 Performance Metrics

- **Model Type**: Decision Tree Regressor
- **Training Set Size**: 405 samples (80%)
- **Test Set Size**: 101 samples (20%)
- **Features**: 12 numeric input features
- **Response Time**: < 100ms per prediction

## 🌟 Features Highlights

✨ **Modern UI/UX**
- Gradient backgrounds
- Smooth animations
- Responsive layout
- Intuitive controls

⚡ **High Performance**
- Fast predictions
- Optimized frontend
- Efficient backend

🔒 **Input Validation**
- Range checking
- Error messages
- User-friendly feedback

📱 **Mobile Friendly**
- Responsive design
- Touch-friendly sliders
- Adaptive layouts

## 🐛 Troubleshooting

### "Model not found" Error
```bash
# Make sure the house_price_predict file exists in the project root
# Re-run the Jupyter notebook to regenerate it
```

### Port 5000 Already in Use
```bash
# Use a different port:
# Modify app.py and change: app.run(debug=True, port=5001)
```

### Dependencies Issues
```bash
# Update pip and reinstall
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 📝 Project Notes

- The model was trained using scikit-learn's Decision Tree Regressor
- Dataset: Boston Housing Dataset (classic ML benchmark)
- All predictions are estimates and should not be used for actual real estate valuations
- The MEDV values in the dataset are in $1000s units

## 🔄 Model Retraining

To retrain the model with new data:

1. Update `boston_house_prices_dataset.csv` with new data
2. Run all cells in `house_price.ipynb`
3. The model will be automatically saved as `house_price_predict`
4. Restart the Flask application to use the new model

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Technical Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **ML**: scikit-learn
- **Data Processing**: pandas, numpy
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome 6

## 🎓 Learning Resources

This project demonstrates:
- Machine Learning model deployment
- Flask web application development
- Frontend-backend communication via REST API
- Responsive web design
- User input validation

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure the model file exists
4. Check browser console for JavaScript errors

---

**Created with ❤️ for Data Science & Web Development**

Enjoy predicting house prices! 🏡💰
