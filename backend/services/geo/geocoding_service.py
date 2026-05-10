from geopy.geocoders import Nominatim


geolocator = Nominatim(
    user_agent="brisa"
)


def geocode_address(address):

    queries = [

        f"{address}, Santander, Cantabria, Spain",

        f"{address}, Santander, Spain",

        f"{address}, Cantabria, Spain"
    ]


    for query in queries:

        try:

            location = geolocator.geocode(query)

            if location:

                return (
                    location.latitude,
                    location.longitude
                )

        except Exception:

            pass


    return (
        None,
        None
    )