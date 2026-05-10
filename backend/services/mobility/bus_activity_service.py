from collections import defaultdict
from datetime import datetime


def calculate_hourly_activity(
    bus_timings
):

    hourly_activity = defaultdict(int)


    for timing in bus_timings:

        timestamp = timing.get(
            "ayto:instante"
        )


        if not timestamp:

            continue


        try:

            dt = datetime.fromisoformat(
                timestamp.replace("Z", "+00:00")
            )

            hour = dt.hour

            hourly_activity[hour] += 1

        except Exception:

            continue


    return dict(hourly_activity)