from game_sprites import GameSprites
import random
import pygame
from screen import Screen
from pygame import RLEACCEL

class Umbrella(GameSprites):
    Max_Speed_y = 10
    Min_Speed_y = 5

    def __init__(self):
        super(Umbrella, self).__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, Screen.width),
                0
            )
        )
        self.speed = random.randint(self.Min_Speed_y, self.Max_Speed_y)
        self.time = 0

    # Move the bird based on speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        speed_y = self.speed
        self.rect.move_ip(0, speed_y)
        if self.rect.bottom > Screen.height:
            self.kill()

    def clone(self):
        return Umbrella()