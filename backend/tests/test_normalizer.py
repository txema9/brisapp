from backend.services.loaders.restaurant_loader import load_restaurants

from backend.services.normalizers.restaurant_normalizer import (
    normalize_restaurants
)


restaurants = load_restaurants()

normalized_restaurants = normalize_restaurants(
    restaurants
)


print(type(normalized_restaurants))

print(len(normalized_restaurants))

print()

print(normalized_restaurants[0])

print()

print(normalized_restaurants[-1])