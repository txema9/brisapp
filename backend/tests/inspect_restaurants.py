from services.loaders.restaurant_loader import load_restaurants


restaurants = load_restaurants()

print(restaurants[0])