from backend.domain.models.urban_element import UrbanElement

from backend.services.geo.zone_service import get_zones

from backend.services.geo.zone_assigner import (
    assign_elements_to_zones
)


restaurant = UrbanElement(
    id="restaurant_001",

    name="Restaurante Test Sardinero",

    element_type="food",

    latitude=43.4725,
    longitude=-3.7827,

    source_dataset="test"
)


museum = UrbanElement(
    id="museum_001",

    name="Centro Botín",

    element_type="culture",

    latitude=43.4620,
    longitude=-3.7985,

    source_dataset="test"
)


urban_elements = [
    restaurant,
    museum
]


zones = get_zones()

assign_elements_to_zones(
    zones,
    urban_elements
)


for zone in zones:

    if len(zone.urban_elements) > 0:

        print()
        print(zone.name)

        for element in zone.urban_elements:

            print("-", element.name)