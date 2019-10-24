import pygame
from boundry import Boundry
from mario import Mario
import game_functions
import sys
from pygame.sprite import Group
from goomba import Goomba
from green_koopa import Green_Koopa

clock = pygame.time.Clock()


def run_mario():
    pygame.init()

    gf = game_functions;


    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    screen.fill([0, 255, 0])

    ground = Boundry(0, 400, 1000, 200, screen, False)
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
    green_koopas = Group()
    koop1 = Green_Koopa(200, 300, screen, plats, mario, goombas)

    goombas.add(goomba2)
    green_koopas.add(koop1)

    mario.blitme()


    while True:
        clock.tick(120)
        gf.check_events(mario)
        mario.update()

        for goomba in goombas:
            goomba.update()

        for koopa in green_koopas:
            koopa.update()

        gf.update_screen(screen, plats, mario, goombas, green_koopas)


run_mario()
