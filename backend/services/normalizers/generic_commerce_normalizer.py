from backend.domain.models.urban_element import UrbanElement


def normalize_commerce_dataset(
    raw_elements,
    element_type,
    source_dataset
):

    normalized_elements = []


    for index, raw_element in enumerate(
        raw_elements,
        start=1
    ):

        latitude = raw_element.get(
            "latitude"
        )

        longitude = raw_element.get(
            "longitude"
        )


        if latitude is None or longitude is None:

            continue


        normalized_element = UrbanElement(

            id=f"{element_type}_{index}",

            name=raw_element["nombre"],

            element_type=element_type,

            latitude=latitude,
            longitude=longitude,

            source_dataset=source_dataset
        )


        normalized_elements.append(
            normalized_element
        )


    return normalized_elements