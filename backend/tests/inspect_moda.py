import json
from pathlib import Path


dataset_path = (
    Path(__file__)
    .resolve()
    .parent.parent
    / "data"
    / "raw"
    / "comercios"
    / "moda-complementos.json"
)

with open(
    dataset_path,
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)


print(data[0])