from game_sprites import GameSprites
from pygame.locals import RLEACCEL
import random
from screen import Screen
import pygame


# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(GameSprites):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("icons/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.height + 20, Screen.width + 100),
                random.randint(0, Screen.height),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Cloud()


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
