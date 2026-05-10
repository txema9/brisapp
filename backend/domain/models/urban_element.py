from dataclasses import dataclass


@dataclass
class UrbanElement:

    id: str

    name: str

    element_type: str

    latitude: float
    longitude: float

    source_dataset: str