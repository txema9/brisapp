from datetime import datetime

from backend.services.loaders.generic_processed_loader import (
    load_processed_dataset
)

from backend.services.loaders.bus_stops_loader import (
    load_bus_stops
)

from backend.services.normalizers.bus_stop_normalizer import (
    normalize_bus_stops
)

from backend.services.normalizers.restaurant_normalizer import (
    normalize_restaurants
)

from backend.services.normalizers.generic_commerce_normalizer import (
    normalize_commerce_dataset
)

from backend.services.geo.zone_service import (
    get_zones
)

from backend.services.geo.zone_assigner import (
    assign_elements_to_zones
)

from backend.services.metrics.metrics_calculator import (
    calculate_zone_metrics
)

from backend.services.moods.mood_engine import (
    generate_zone_moods
)


def build_city():

    current_hour = datetime.now().hour


    # =========================
    # LOAD DATASETS
    # =========================

    restaurants = load_processed_dataset(
        "restaurants_geocoded.json"
    )

    ocio = load_processed_dataset(
        "ocio_geocoded.json"
    )

    cultura = load_processed_dataset(
        "cultura_geocoded.json"
    )

    moda = load_processed_dataset(
        "moda_geocoded.json"
    )

    salud = load_processed_dataset(
        "salud_geocoded.json"
    )

    bus_stops = load_bus_stops()


    # =========================
    # NORMALIZE
    # =========================

    normalized_restaurants = (
        normalize_restaurants(
            restaurants
        )
    )

    normalized_ocio = (
        normalize_commerce_dataset(
            ocio,
            "nightlife",
            "ocio_geocoded.json"
        )
    )

    normalized_cultura = (
        normalize_commerce_dataset(
            cultura,
            "culture",
            "cultura_geocoded.json"
        )
    )

    normalized_moda = (
        normalize_commerce_dataset(
            moda,
            "commerce",
            "moda_geocoded.json"
        )
    )

    normalized_salud = (
        normalize_commerce_dataset(
            salud,
            "health",
            "salud_geocoded.json"
        )
    )

    normalized_bus_stops = (
        normalize_bus_stops(
            bus_stops
        )
    )


    # =========================
    # MERGE ALL ELEMENTS
    # =========================

    all_elements = (

        normalized_restaurants

        + normalized_ocio

        + normalized_cultura

        + normalized_moda

        + normalized_salud

        + normalized_bus_stops
    )


    # =========================
    # LOAD ZONES
    # =========================

    zones = get_zones()


    # =========================
    # ASSIGN ELEMENTS
    # =========================

    assign_elements_to_zones(
        zones,
        all_elements
    )


    # =========================
    # METRICS + MOODS
    # =========================

    for zone in zones:

        calculate_zone_metrics(zone)

        generate_zone_moods(
            zone,
            current_hour=current_hour
        )


    return zones