import pygame
from abc import abstractmethod


class GameSprites(pygame.sprite.Sprite):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def update(self):
        pass