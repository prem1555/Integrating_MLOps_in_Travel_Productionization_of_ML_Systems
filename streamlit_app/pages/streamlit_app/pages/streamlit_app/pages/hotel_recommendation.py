import streamlit as st
import requests
import pandas as pd


st.title('Hotel Recommendation System')


hotel_name = st.text_input(
    'Enter Hotel Name'
)


if st.button('Recommend Hotels'):

    data = {

        'hotel_name': hotel_name

    }

    response = requests.post(

        'http://127.0.0.1:5000/recommend-hotels',

        json=data

    )

    recommendations = response.json()

    st.write(

        pd.DataFrame(

            recommendations['Recommendations']

        )

    )
