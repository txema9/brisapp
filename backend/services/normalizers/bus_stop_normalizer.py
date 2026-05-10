from domain.models.urban_element import UrbanElement


def normalize_bus_stops(raw_bus_stops):

    normalized_bus_stops = []


    for index, raw_stop in enumerate(
        raw_bus_stops,
        start=1
    ):

        latitude = raw_stop.get(
            "wgs84_pos:lat"
        )

        longitude = raw_stop.get(
            "wgs84_pos:long"
        )


        if latitude is None or longitude is None:

            continue


        normalized_stop = UrbanElement(

            id=f"bus_stop_{index}",

            name=raw_stop[
                "ayto:parada"
            ],

            element_type="transport",

            latitude=float(latitude),

            longitude=float(longitude),

            source_dataset="paradas_bus.json"
        )


        normalized_bus_stops.append(
            normalized_stop
        )


    return normalized_bus_stops