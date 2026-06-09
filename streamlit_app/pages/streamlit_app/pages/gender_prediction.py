import streamlit as st
import requests


st.title('Gender Prediction')


company = st.number_input(
    'Company',
    min_value=0
)

age = st.number_input(
    'Age',
    min_value=1
)

name = st.number_input(
    'Name',
    min_value=0
)


if st.button('Predict Gender'):

    data = {

        'company': company,
        'age': age,
        'name': name

    }

    response = requests.post(

        'http://127.0.0.1:5000/predict-gender',

        json=data

    )

    prediction = response.json()

    st.success(prediction)
