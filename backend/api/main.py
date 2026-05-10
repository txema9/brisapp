from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from backend.services.pipeline.city_pipeline import (
    build_city
)


app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/zones")
def get_zones():

    zones = build_city()

    response = []


    for zone in zones:

        response.append({

            "name": zone.name,

            "latitude": zone.latitude,

            "longitude": zone.longitude,

            "marker": zone.marker,

            "zone_type": zone.zone_type,

            "leisure_mood":
                zone.leisure_mood,

            "traffic_mood":
                zone.traffic_mood
        })


    return response