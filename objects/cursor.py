import pygame

from tools.win_proportion import set_window_proportion

from objects.object import Object


class Cursor(Object):
    def __init__(self, image_size: tuple[int, int], position: tuple[int, int]):
        super().__init__(image_size, position)

        self.image.fill("black")

        from game import Game
        self.game = Game()

    def update(self, *args, **kwargs):
        self.pos.xy = set_window_proportion(pygame.mouse.get_pos())

        self.centering_position()
        self.update_position()
