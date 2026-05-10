import json
import time
from pathlib import Path

from backend.services.loaders.restaurant_loader import (
    load_restaurants
)

from backend.services.geo.geocoding_service import (
    geocode_address
)


def enrich_restaurants():

    restaurants = load_restaurants()

    enriched_restaurants = []


    for restaurant in restaurants:

        address = restaurant["direccion"]

        latitude, longitude = geocode_address(
            address
        )

        restaurant["latitude"] = latitude
        restaurant["longitude"] = longitude

        enriched_restaurants.append(
            restaurant
        )

        print(
            restaurant["nombre_del_restaurante"],
            latitude,
            longitude
        )

        time.sleep(1)


    output_path = (
        Path(__file__)
        .resolve()
        .parent.parent.parent
        / "data"
        / "processed"
        / "restaurants_geocoded.json"
    )


    output_path.parent.mkdir(
        exist_ok=True
    )


    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            enriched_restaurants,
            file,
            ensure_ascii=False,
            indent=4
        )