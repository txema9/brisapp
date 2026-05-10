from haversine import haversine, Unit


def assign_elements_to_zones(
    zones,
    urban_elements
):

    for element in urban_elements:

        element_coordinates = (
            element.latitude,
            element.longitude
        )

        closest_zone = None

        closest_distance = float("inf")


        for zone in zones:

            zone_coordinates = (
                zone.latitude,
                zone.longitude
            )

            distance = haversine(
                zone_coordinates,
                element_coordinates,
                unit=Unit.METERS
            )


            if (
                distance <= zone.radius
                and distance < closest_distance
            ):

                closest_zone = zone

                closest_distance = distance


        if closest_zone:

            closest_zone.urban_elements.append(
                element
            )