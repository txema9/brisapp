import json
from pathlib import Path


def load_geocoded_restaurants():

    dataset_path = (
        Path(__file__)
        .resolve()
        .parent.parent.parent
        / "data"
        / "processed"
        / "restaurants_geocoded.json"
    )

    with open(
        dataset_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data