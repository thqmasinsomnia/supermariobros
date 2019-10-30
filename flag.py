import pygame
from pygame.sprite import Sprite


class Flag(Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert()
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
        self.change_x = 0
        # self.screen = screen
        self.image = pygame.image.load("resources/graphics/other/flag.png")

        # if invis:
        #     self.image = pygame.image.load("resources/graphics/nothing.png")
        # else:
        #     self.image.fill([0, 0, 0])

    def blitme(self):

        self.screen.blit(self.image, self.rect)