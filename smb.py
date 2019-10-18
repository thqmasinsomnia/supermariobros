import pygame
from boundry import Boundry
from mario import Mario
import game_functions
import sys
from pygame.sprite import Group

clock = pygame.time.Clock()


def run_mario():
    pygame.init()

    gf = game_functions

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    screen.fill([0, 255, 0])


    ground = Boundry(0, 400, 500, 500, screen)
    plat1 = Boundry(0, 100, 100, 25, screen)
    plat2 = Boundry(100, 200, 100, 25, screen)
    plat3 = Boundry(200, 300, 100, 25, screen)


    ground.blitme()
    plat1.blitme()
    pygame.display.flip()

    boundries = Group()

    boundries.add(ground)
    boundries.add(plat1)
    boundries.add(plat2)
    boundries.add(plat3)


    mario = Mario(100, 100, screen, boundries)
    mario.blitme()

    while True:
        clock.tick(120)
        gf.check_events(mario)
        mario.update()
        gf.update_screen(screen, boundries, mario)

run_mario()
