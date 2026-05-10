from backend.services.loaders.bus_timing_loader import (
    load_bus_timings
)

from backend.services.mobility.bus_activity_service import (
    calculate_hourly_activity
)


bus_timings = load_bus_timings()


hourly_activity = (
    calculate_hourly_activity(
        bus_timings
    )
)


for hour, activity in sorted(
    hourly_activity.items()
):

    print()

    print(f"{hour}:00")

    print(
        "Actividad:",
        activity
    )