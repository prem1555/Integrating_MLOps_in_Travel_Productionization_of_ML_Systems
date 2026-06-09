import streamlit as st
import requests


st.title('Flight Price Prediction')


# User Inputs
from_location = st.number_input(
    'From Location',
    min_value=0
)

to_location = st.number_input(
    'To Location',
    min_value=0
)

distance = st.number_input(
    'Distance'
)

time = st.number_input(
    'Flight Time'
)

agency = st.number_input(
    'Agency'
)

flight_type = st.number_input(
    'Flight Type'
)

year = st.number_input(
    'Year',
    value=2025
)

month = st.number_input(
    'Month',
    value=5
)

day = st.number_input(
    'Day',
    value=10
)


# Predict Button
if st.button('Predict Flight Price'):

    data = {

        'from': from_location,
        'to': to_location,
        'distance': distance,
        'time': time,
        'agency': agency,
        'flightType': flight_type,
        'year': year,
        'month': month,
        'day': day

    }

    # API call
    response = requests.post(

        'http://127.0.0.1:5000/predict-flight-price',

        json=data

    )

    prediction = response.json()

    st.success(prediction)
