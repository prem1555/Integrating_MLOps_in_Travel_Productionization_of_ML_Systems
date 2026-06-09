import pandas as pd


def load_data():

    hotels = pd.read_csv('data/raw/hotels.csv')

    users = pd.read_csv('data/raw/users.csv')

    return hotels, users


def preprocess_data():

    hotels, users = load_data()

    # Remove duplicates
    hotels.drop_duplicates(inplace=True)

    # Handle missing values
    hotels.fillna(method='ffill', inplace=True)

    # Merge datasets
    merged = hotels.merge(
        users,
        left_on='userCode',
        right_on='code',
        how='left'
    )

    # IMPORTANT:
    # name_x = hotel name
    # name_y = user name

    # Create combined features
    merged['features'] = (

        merged['name_x'].astype(str)

        + ' '

        + merged['place'].astype(str)

        + ' '

        + merged['days'].astype(str)

        + ' '

        + merged['price'].astype(str)

    )

    return merged
