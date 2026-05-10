from backend.domain.models.urban_element import UrbanElement

from backend.services.geo.zone_service import get_zones

from backend.services.geo.zone_assigner import (
    assign_elements_to_zones
)

from backend.services.metrics.metrics_calculator import (
    calculate_zone_metrics
)

from backend.services.moods.mood_engine import (
    generate_zone_moods
)


restaurant = UrbanElement(
    id="restaurant_001",
    name="Restaurante Test",
    element_type="food",
    latitude=43.4725,
    longitude=-3.7827,
    source_dataset="test"
)

bar = UrbanElement(
    id="bar_001",
    name="Bar Test",
    element_type="nightlife",
    latitude=43.4726,
    longitude=-3.7828,
    source_dataset="test"
)

bus_stop = UrbanElement(
    id="bus_001",
    name="Parada Test",
    element_type="transport",
    latitude=43.4724,
    longitude=-3.7829,
    source_dataset="test"
)


urban_elements = [
    restaurant,
    bar,
    bus_stop
]


zones = get_zones()

assign_elements_to_zones(
    zones,
    urban_elements
)


for zone in zones:

    if len(zone.urban_elements) > 0:

        calculate_zone_metrics(zone)

        generate_zone_moods(zone)

        print()
        print(zone.name)

        print(zone.moods)