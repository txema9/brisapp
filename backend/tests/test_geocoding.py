from services.geo.geocoding_service import (
    geocode_address
)


latitude, longitude = geocode_address(
    "Bo Bolado 38, Monte"
)


print()

print(latitude)

print(longitude)