import math
import pygame
from sys import exit

from const import *
from config import Config

from objects.player import Player
from objects.cursor import Cursor
from objects.bullet import Bullet


class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Game, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        pygame.init()

        self.config = Config()
        self.config.load_config_from_json()

        self.window = pygame.display.set_mode(self.config["window_size"])
        self.screen = pygame.Surface(SCREEN_SIZE)
        self.window_proportion = (
            self.config["window_size"][0] / SCREEN_SIZE[0],
            self.config["window_size"][1] / SCREEN_SIZE[1],
        )

        self.clock = pygame.Clock()

        self.object_group = pygame.sprite.Group()

    def event_handle(self, event_list: list[pygame.Event]):
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def game_loop(self):
        game_player = Player((16, 16), (0, 0))
        cursor = Cursor((8, 8), (0, 0))

        game_player.add(self.object_group)
        cursor.add(self.object_group)

        # for i in range(0, 360, 5):
        #     rad = math.radians(i)
        #     velocity = (math.cos(rad), math.sin(rad))
        #     bullet = Bullet(
        #         (2, 2), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2),
        #         velocity, 2
        #     )
        #     bullet.add(object_group)

        while 1:
            self.event_handle(pygame.event.get())

            self.object_group.update()

            self.screen.fill("gray")
            self.object_group.draw(self.screen)

            self.window.blit(
                pygame.transform.scale(
                    self.screen, self.config["window_size"]
                ), (0, 0)
            )

            pygame.display.update()

            self.clock.tick(self.config["fps"])
