from recommendation_engine import recommend_hotels


# Example hotel name
hotel_name = input('Enter Hotel Name: ')

# Get recommendations
recommendations = recommend_hotels(hotel_name)

print('\\nRecommended Hotels:\\n')

print(recommendations)