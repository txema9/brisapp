from dataclasses import dataclass, field

from domain.models.zone_metrics import ZoneMetrics


@dataclass
class Zone:

    id: int

    name: str

    latitude: float
    longitude: float

    radius: int

    marker: str


    # CAPAS BRISA

    zone_type: str = ""

    leisure_mood: str = ""

    traffic_mood: str = ""


    urban_elements: list = field(
        default_factory=list
    )

    metrics: ZoneMetrics = field(
        default_factory=ZoneMetrics
    )