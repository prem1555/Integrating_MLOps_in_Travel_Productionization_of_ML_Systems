import streamlit as st


st.set_page_config(

    page_title='Voyage Analytics',

    layout='wide'

)

st.title('Voyage Analytics Dashboard')

st.markdown('---')

st.header('Project Overview')

st.write(

    '''
    Voyage Analytics is an end-to-end MLOps project
    integrating:

    - Regression Model
    - Classification Model
    - Recommendation System
    - Flask API
    - MLflow
    - Docker
    - Kubernetes
    - Airflow
    - Jenkins
    '''
)

st.markdown('---')

st.header('Features')

st.write(

    '''
    1. Flight Price Prediction
    2. Gender Classification
    3. Hotel Recommendation System
    4. Interactive Data Visualizations
    '''
)
