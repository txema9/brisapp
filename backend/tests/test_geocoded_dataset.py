from backend.services.loaders.geocoded_restaurant_loader import (
    load_geocoded_restaurants
)


restaurants = load_geocoded_restaurants()


print()

print("TOTAL:", len(restaurants))

print()

print(restaurants[0])

print()

valid_coordinates = 0


for restaurant in restaurants:

    latitude = restaurant.get("latitude")
    longitude = restaurant.get("longitude")

    if latitude is not None and longitude is not None:

        valid_coordinates += 1


print("CON COORDENADAS:", valid_coordinates)