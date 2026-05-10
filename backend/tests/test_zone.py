from backend.domain.models.zone import Zone
from backend.domain.models.urban_element import UrbanElement


restaurant = UrbanElement(
    id="restaurant_001",

    name="Restaurante La Bombi",

    element_type="food",

    latitude=43.4630,
    longitude=-3.7900,

    source_dataset="restaurantes.json"
)


bus_stop = UrbanElement(
    id="bus_001",

    name="Parada Ayuntamiento",

    element_type="transport",

    latitude=43.4623,
    longitude=-3.8099,

    source_dataset="paradas_bus.json"
)


el_sardinero = Zone(
    id=1,

    name="El Sardinero",

    latitude=43.47234934934887,
    longitude=-3.7826310695260883,

    radius=350,

    marker="🌊",

    moods=[
        "🚶 Paseo",
        "☕ Tranquilo"
    ]
)


el_sardinero.urban_elements.append(restaurant)
el_sardinero.urban_elements.append(bus_stop)


print(el_sardinero)