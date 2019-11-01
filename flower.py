import pygame
from pygame.sprite import Sprite


class Flower(Sprite):
    def __init__(self, x, y, screen, boundries, mario):
        super(Flower, self).__init__()
        self.mario = mario

        self.screen_rect = screen.get_rect()
        self.bd = boundries
        self.screen = screen
        self.type = type

        self.image = pygame.image.load('resources/graphics/flower/flower1.png')
        self.frames = [
            pygame.image.load('resources/graphics/flower/flower1.png'),
            pygame.image.load('resources/graphics/flower/flower2.png'),
            pygame.image.load('resources/graphics/flower/flower3.png')
        ]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)
        self.count = 0

    def update(self):


        if self.count == 10:
            self.image = self.frames[0]

        if self.count == 20:
            self.image = self.frames[1  ]

        if self.count == 30:
            self.image = self.frames[2]
            self.count = 0

        self.count += 1

    def mario_collision(self):
        col = pygame.sprite.collide_rect(self, self.mario)

        if col:
            self.mario.make_big()
            self.mario.make_lit()
            self.kill()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
