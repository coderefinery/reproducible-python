import math


def surface_area(radius: float) -> float:
    return 4.0 * math.pi * radius**2


europa = {"name": "Europa", "radius": 1560.8, "contains_water": True}


print(europa)
print(f"Surface area (km^2) of {europa['name']}: {surface_area(europa['radius'])}")
