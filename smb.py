import pygame
from boundry import Boundry
from mario import Mario
import game_functions
import sys
from pygame.sprite import Group
from goomba import Goomba

clock = pygame.time.Clock()


def run_mario():
    pygame.init()

    gf = game_functions;


    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    screen.fill([0, 255, 0])

    ground = Boundry(0, 400, 500, 500, screen, False)
    plat1 = Boundry(0, 100, 100, 25, screen, False)
    plat2 = Boundry(100, 200, 100, 25, screen, False)
    plat3 = Boundry(200, 300, 100, 25, screen, False)

    ground.blitme()
    plat1.blitme()
    pygame.display.flip()

    plats = Group()

    plats.add(ground)
    plats.add(plat1)
    plats.add(plat2)
    plats.add(plat3)

    mario = Mario(100, 100, screen, plats)

    goomba1 = Goomba(500, 0, screen, plats, mario)
    goomba2 = Goomba(100, 300, screen, plats, mario)

    goombas = Group()


    goombas.add(goomba2)

    mario.blitme()


    while True:
        clock.tick(120)
        gf.check_events(mario)
        mario.update()

        for goomba in goombas:
            goomba.update()

        gf.update_screen(screen, plats, mario, goombas)


run_mario()
