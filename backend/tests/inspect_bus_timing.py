import json
from pathlib import Path


dataset_path = (
    Path(__file__)
    .resolve()
    .parent.parent
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


resources = data["resources"]

print(type(resources))

print()

print(len(resources))

print()

print(resources[0])