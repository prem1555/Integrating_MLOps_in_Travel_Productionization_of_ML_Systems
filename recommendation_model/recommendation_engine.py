import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from recommendation_model.preprocess import preprocess_data


def build_similarity():

    # Load data
    data = preprocess_data()

    # Vectorization
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(
        data['features']
    )

    # Similarity matrix
    similarity = cosine_similarity(
        count_matrix
    )

    return data, similarity


def recommend_hotels(hotel_name):

    # Build similarity
    data, similarity = build_similarity()

    hotel_name = hotel_name.lower()

    # Lowercase hotel names
    data['hotel_name_lower'] = (
        data['name_x'].str.lower()
    )

    # Hotel exists check
    if hotel_name not in data[
        'hotel_name_lower'
    ].values:

        return pd.DataFrame({

            'Message': ['Hotel Not Found']

        })

    # Get index
    index = data[
        data['hotel_name_lower']
        == hotel_name
    ].index[0]

    # Similarity scores
    scores = list(
        enumerate(similarity[index])
    )

    # Sort
    sorted_scores = sorted(

        scores,

        key=lambda x: x[1],

        reverse=True

    )

    recommendations = []

    seen = set()

    for item in sorted_scores[1:20]:

        hotel_index = item[0]

        hotel = data.iloc[
            hotel_index
        ]['name_x']

        place = data.iloc[
            hotel_index
        ]['place']

        if hotel not in seen:

            recommendations.append({

                'Hotel': hotel,

                'Place': place

            })

            seen.add(hotel)

        if len(recommendations) == 5:
            break

    return pd.DataFrame(recommendations)