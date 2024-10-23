import math
import pygame

from objects.object import Object
from objects.bullet import Bullet

from tools.win_proportion import set_window_proportion
from tools.get_dir_from_angle import get_dir_from_angle


class Player(Object):
    def __init__(self, image_size: tuple[int, int], position: tuple[int, int]):
        super().__init__(image_size, position)

        self.speed = 3
        self.angle = 0  # градусы
        self.velocity = pygame.math.Vector2((0, 0))

        from game import Game
        self.game = Game()

    def update(self, *args, **kwargs):
        # == Куда смотрит игрок ==
        mouse_pos = set_window_proportion(pygame.mouse.get_pos())

        self.angle = math.degrees(math.atan2(
            mouse_pos[1] - self.rect.centery,
            mouse_pos[0] - self.rect.centerx
        ))

        # == ==

        # == Стрельба ==
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            bullet = Bullet(
                (3, 3), self.rect.center, get_dir_from_angle(self.angle),15
            )
            bullet.add(self.game.object_group)
        # == ==

        # == Движение ==
        pressed_keys = pygame.key.get_pressed()

        self.velocity.xy = (0, 0)

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            self.velocity.y = -1
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.velocity.x = -1
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            self.velocity.y = 1
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.velocity.x = 1

        if self.velocity.xy != (0, 0):
            self.velocity.normalize_ip()
            self.pos += self.velocity * self.speed

            self.update_position()
        # == ==
