from game_sprites import GameSprites
import pygame
from pygame.locals import RLEACCEL


class Mountain(GameSprites):
    def __init__(self):
        super(Mountain, self).__init__()
        self.surf = pygame.image.load("icons/mountain.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is in the right-bottom corner
        self.rect = self.surf.get_rect(
            center=(
                800, 600
            )
        )

    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Mountain()
