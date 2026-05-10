from backend.services.geo.zone_service import get_zones


zones = get_zones()

print(type(zones))

print(len(zones))

print()

print(zones[0])

print()

print(zones[-1])