import joblib
import pandas as pd


# Load model
model = joblib.load(
    '../models/gender_model.pkl'
)

# Example sample input
sample = pd.DataFrame({

    'company': [1],
    'age': [28],
    'name': [15]

})

# Prediction
prediction = model.predict(sample)

# Output
if prediction[0] == 1:
    print('Predicted Gender: Male')

else:
    print('Predicted Gender: Female')