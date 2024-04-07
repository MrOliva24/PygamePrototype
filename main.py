from bird import Bird
from cloud import Cloud
from factory_sprites import FactorySprites
import pygame
from game import Game
from mountain import Mountain
from umbrella import Umbrella
from screen import Screen



pygame.mixer.init()
pygame.init()

pygame.display.set_mode((Screen.width, Screen.height))

level = str("difficult")

if level == 'easy':
    factory_flying = FactorySprites([Bird()], [300], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud()], [400], pygame.USEREVENT + 10)
elif level == 'difficult':
    factory_flying = FactorySprites([Bird(), Umbrella()], [300, 500],
                                    pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [500, 2000],
                                    pygame.USEREVENT + 10)
else:
    assert False


# start playing
game = Game(factory_flying, factory_landscape)
game.play()

