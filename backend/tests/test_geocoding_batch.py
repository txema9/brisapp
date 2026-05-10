from backend.services.loaders.restaurant_loader import (
    load_restaurants
)

from backend.services.geo.geocoding_service import (
    geocode_address
)


restaurants = load_restaurants()


for restaurant in restaurants[:10]:

    address = restaurant["direccion"]

    latitude, longitude = geocode_address(
        address
    )

    print()
    print(restaurant["nombre_del_restaurante"])

    print(address)

    print(latitude, longitude)