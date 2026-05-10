from backend.domain.models.urban_element import UrbanElement


def normalize_restaurant(raw_restaurant, index):

    latitude = raw_restaurant.get(
        "latitude"
    )

    longitude = raw_restaurant.get(
        "longitude"
    )


    if latitude is None or longitude is None:

        return None


    return UrbanElement(

        id=f"restaurant_{index}",

        name=raw_restaurant[
            "nombre_del_restaurante"
        ],

        element_type="food",

        latitude=latitude,
        longitude=longitude,

        source_dataset="restaurants_geocoded.json"
    )


def normalize_restaurants(restaurants):

    normalized_restaurants = []


    for index, restaurant in enumerate(
        restaurants,
        start=1
    ):

        normalized_restaurant = (
            normalize_restaurant(
                restaurant,
                index
            )
        )


        if normalized_restaurant:

            normalized_restaurants.append(
                normalized_restaurant
            )


    return normalized_restaurants