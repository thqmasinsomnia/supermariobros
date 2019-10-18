import pygame
from pygame.sprite import Sprite


class Boundry(Sprite):

    def __init__(self, x, y, width, height, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.image.fill([0, 0, 0])
        self.rect.y = y
        self.state = None
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image, self.rect)
