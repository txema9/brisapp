import json
from pathlib import Path


def load_bus_timings():

    dataset_path = (
        Path(__file__)
        .resolve()
        .parent.parent.parent
        / "data"
        / "raw"
        / "movilidad"
        / "programacionTUS_pasos_parada_10dias.json"
    )

    with open(
        dataset_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    return data["resources"]