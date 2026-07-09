import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data():

    users = pd.read_csv('data/raw/users.csv')

    return users


def preprocess_data():

    users = load_data()

    # Remove duplicates
    users.drop_duplicates(inplace=True)

    # Handle missing values
    users.fillna(method='ffill', inplace=True)

    # Create Label Encoders
    company_encoder = LabelEncoder()
    name_encoder = LabelEncoder()
    gender_encoder = LabelEncoder()

    # Encode categorical columns
    users['company'] = company_encoder.fit_transform(
        users['company']
    )

    users['name'] = name_encoder.fit_transform(
        users['name']
    )

    users['gender'] = gender_encoder.fit_transform(
        users['gender']
    )

    # Features
    X = users[
        [
            'company',
            'age',
            'name'
        ]
    ]

    # Target
    y = users['gender']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test