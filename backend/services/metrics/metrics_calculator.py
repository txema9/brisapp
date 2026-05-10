def calculate_zone_metrics(zone):

    for element in zone.urban_elements:

        if element.element_type == "food":
            zone.metrics.food_count += 1

        elif element.element_type == "transport":
            zone.metrics.transport_count += 1

        elif element.element_type == "culture":
            zone.metrics.culture_count += 1

        elif element.element_type == "nightlife":
            zone.metrics.nightlife_count += 1

        elif element.element_type == "commerce":
            zone.metrics.commerce_count += 1

        elif element.element_type == "health":
            zone.metrics.health_count += 1