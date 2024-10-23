import pygame


class GroupManager:
    def __init__(self):
        self.group_dict = {  # TODO сделать парсинг названий групп с файла, чтобы не хардкодить.
            "player": pygame.sprite.GroupSingle(),
            "player_bullet": pygame.sprite.Group(),
            "entity": pygame.sprite.Group(),
            "entity_bullet": pygame.sprite.Group(),
            "hud": pygame.sprite.Group(),
            "wall": pygame.sprite.Group()
        }

    def __getitem__(self, item):
        return self.group_dict[item]

    def update(self, *args, **kwargs):
        for _, group in self.group_dict.items():
            group.update(args, kwargs)

    def draw(self, surface: pygame.Surface):
        for _, group in self.group_dict.items():
            group.draw(surface)
