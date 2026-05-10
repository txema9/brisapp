import json
import time
from pathlib import Path

from services.geo.geocoding_service import (
    geocode_address
)


def enrich_dataset(
    input_filename,
    output_filename
):

    input_path = (
        Path(__file__)
        .resolve()
        .parent.parent.parent
        / "data"
        / "raw"
        / "comercios"
        / input_filename
    )


    with open(
        input_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    enriched_data = []


    for element in data:

        address = element[
            "direccion"
        ][
            "completa"
        ]


        latitude, longitude = (
            geocode_address(address)
        )


        element["latitude"] = latitude
        element["longitude"] = longitude


        enriched_data.append(element)


        print()
        print(element["nombre"])
        print(latitude, longitude)


        time.sleep(1)


    output_path = (
        Path(__file__)
        .resolve()
        .parent.parent.parent
        / "data"
        / "processed"
        / output_filename
    )


    output_path.parent.mkdir(
        exist_ok=True
    )


    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            enriched_data,
            file,
            ensure_ascii=False,
            indent=4
        )