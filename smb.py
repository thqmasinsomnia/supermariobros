import pygame
import sys
from pygame.sprite import Group


def run_mario():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUPER MARIO BRUHS")
    screen.fill([0, 255, 0])

    pygame.display.flip()


while True:


    run_mario()
