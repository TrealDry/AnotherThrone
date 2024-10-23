import pygame
from sys import exit

from const import *
from config import Config

from objects.player import Player
from objects.cursor import Cursor
from objects.entity import Entity

from objects.hud.hp_bar import HPBar

from engine.group_manager import GroupManager


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

        self.group_mng = GroupManager()

    def event_handle(self, event_list: list[pygame.Event]):
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def game_loop(self):
        game_player = Player((16, 16), (0, 0))
        entity = Entity((16, 16), (100, 100), 10, 10)
        hp_bar = HPBar(entity)
        cursor = Cursor((8, 8), (0, 0))

        game_player.add(self.group_mng["player"])
        entity.add(self.group_mng["entity"])
        hp_bar.add(self.group_mng["hud"])
        cursor.add(self.group_mng["hud"])

        while 1:
            self.event_handle(pygame.event.get())

            self.group_mng.update()

            self.screen.fill("gray")
            self.group_mng.draw(self.screen)

            self.window.blit(
                pygame.transform.scale(
                    self.screen, self.config["window_size"]
                ), (0, 0)
            )

            pygame.display.update()

            self.clock.tick(self.config["fps"])
