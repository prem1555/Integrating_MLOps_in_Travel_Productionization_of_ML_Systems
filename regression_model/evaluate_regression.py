import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from preprocess import preprocess_data


# Load processed data
X_train, X_test, y_train, y_test = preprocess_data()

# Load model
model = joblib.load(
    '../models/flight_price_model.pkl'
)

# Predictions
predictions = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print('MAE:', mae)
print('MSE:', mse)
print('R2 Score:', r2)

# Visualization
plt.figure(figsize=(8,5))

plt.scatter(y_test, predictions)

plt.xlabel('Actual Prices')

plt.ylabel('Predicted Prices')

plt.title('Actual vs Predicted Flight Prices')

plt.show()
