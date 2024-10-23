from objects.object import Object


class Entity(Object):
    def __init__(
        self, image_size: tuple[int, int], position: tuple[int, int],
        hp_max: int, hp_value: int
    ):
        super().__init__(image_size, position)

        self.hp_max = hp_max
        self.hp_value = hp_value

    def take_damage(self, damage: int):
        self.hp_value -= abs(damage)

        if self.hp_value <= 0:
            self.kill()
