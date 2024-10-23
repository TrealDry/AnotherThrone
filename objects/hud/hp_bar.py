import pygame

from objects.object import Object
from objects.entity import Entity


class HPBar(Object):
    def __init__(self, target_entity: Entity):
        self.target_entity = target_entity

        super().__init__((25, 3), (0, 0))

        self.image.fill("green")

        self.target_hp = {
            "max": self.target_entity.hp_max,
            "value": self.target_entity.hp_value
        }

    def follow_target(self):
        self.pos.xy = (
            self.target_entity.rect.centerx, self.target_entity.rect.top - 5
        )
        self.centering_position()
        self.update_position()

    def update_image(self):
        self.image.fill("red")

        hp_indicator = pygame.surface.Surface((
            self.image.size[0] / (self.target_hp["max"] / self.target_hp["value"]),
            self.image.size[1]
        ))
        hp_indicator.fill("green")

        self.image.blit(hp_indicator, (0, 0))

    def update_target_hp(self):
        # TODO вызов функции при помощи сигналов, а не каждый кадр.
        temp_target_hp = {
            "max": self.target_entity.hp_max,
            "value": self.target_entity.hp_value
        }

        # == Смерть вместе с владельцем ==
        if temp_target_hp["value"] <= 0:
            self.kill()
            return
        # == ==

        if self.target_hp["max"] != temp_target_hp["max"] or \
          self.target_hp["value"] != temp_target_hp["value"]:

            self.target_hp = temp_target_hp
            self.update_image()

    def update(self, *args, **kwargs):
        self.follow_target()
        self.update_target_hp()
