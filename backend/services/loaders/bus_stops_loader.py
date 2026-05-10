import json
from pathlib import Path


def load_bus_stops():

    dataset_path = (
        Path(__file__)
        .resolve()
        .parent.parent.parent
        / "data"
        / "raw"
        / "movilidad"
        / "paradas_bus.json"
    )

    with open(
        dataset_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    return data["resources"]