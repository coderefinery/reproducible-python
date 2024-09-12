import math
from collections import namedtuple


def surface_area(radius: float) -> float:
    return 4.0 * math.pi * radius**2


Moon = namedtuple("Moon", ["name", "radius", "contains_water"])


europa = Moon(name="Europa", radius=1560.8, contains_water=True)

print(europa)
print(f"Surface area (km^2) of {europa.name}: {surface_area(europa.radius)}")
