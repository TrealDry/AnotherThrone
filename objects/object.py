import pygame


class Object(pygame.sprite.Sprite):
    def __init__(
        self, image_size: tuple[int, int], position: tuple[int, int]
    ):
        super().__init__()

        if image_size is None:
            image_size = (16, 16)

        self.image = pygame.Surface(image_size)
        self.image.fill("green")

        self.rect = self.image.get_rect(
            topleft=position
        )

        self.pos = pygame.math.Vector2(position)

    def centering_position(self):
        self.pos.xy = (
            self.pos.x - self.rect.width / 2,
            self.pos.y - self.rect.height / 2
        )

    def update_position(self):
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
