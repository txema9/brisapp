from services.pipeline.city_pipeline import (
    build_city
)


zones = build_city()


for zone in zones:

    print()

    print(zone.name)

    print(
        "Tipo zona:",
        zone.zone_type
    )

    print(
        "Ocio:",
        zone.leisure_mood
    )

    print(
        "Estado urbano:",
        zone.traffic_mood
    )