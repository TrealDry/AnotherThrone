import pygame

from objects.object import Object


class Bullet(Object):
    def __init__(
        self, image_size: tuple[int, int], position: tuple[int, int],
        direction: tuple[float, float], speed: float
    ):
        super().__init__(image_size, position)

        self.direction = pygame.math.Vector2(direction)
        self.speed = speed

    def update(self, *args, **kwargs):
        self.pos += self.direction * self.speed
        self.update_position()
