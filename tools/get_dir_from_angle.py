import math
from pygame.math import Vector2


def get_dir_from_angle(angle_degrees: float) -> Vector2:
    angle_radians = math.radians(angle_degrees)
    return Vector2(math.cos(angle_radians), math.sin(angle_radians))
