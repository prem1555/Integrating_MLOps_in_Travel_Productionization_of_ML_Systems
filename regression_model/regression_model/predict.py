import joblib
import pandas as pd

# Load model
model = joblib.load(
    '../models/flight_price_model.pkl'
)

# Example input
sample = pd.DataFrame({

    'from': [1],
    'to': [2],
    'distance': [1200],
    'time': [3],
    'agency': [1],
    'flightType': [0],
    'year': [2025],
    'month': [5],
    'day': [10]

})

# Prediction
prediction = model.predict(sample)

print('Predicted Flight Price:', prediction[0])
