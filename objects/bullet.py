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
        self.damage = 1

        from game import Game
        self.game = Game()

    def update(self, *args, **kwargs):
        self.pos += self.direction * self.speed
        self.update_position()

        for spr in pygame.sprite.spritecollide(
            self, self.game.group_mng["entity"], False
        ):
            spr.take_damage(self.damage)
            self.kill()
            return
