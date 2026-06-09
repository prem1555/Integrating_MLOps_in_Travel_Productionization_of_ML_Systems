import joblib
import pandas as pd

from recommendation_model.recommendation_engine import (
    recommend_hotels
)


# Load models
flight_model = joblib.load(
    'models/flight_price_model.pkl'
)

gender_model = joblib.load(
    'models/gender_model.pkl'
)


# Flight price prediction
def predict_flight_price(data):

    input_data = pd.DataFrame([data])

    prediction = flight_model.predict(input_data)

    return float(prediction[0])


# Gender prediction
def predict_gender(data):

    input_data = pd.DataFrame([data])

    prediction = gender_model.predict(input_data)

    if prediction[0] == 1:

        return 'Male'

    else:

        return 'Female'


# Hotel recommendation
def hotel_recommendation(hotel_name):

    recommendations = recommend_hotels(hotel_name)

    return recommendations.to_dict(
        orient='records'
    )
