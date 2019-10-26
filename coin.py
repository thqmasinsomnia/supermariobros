import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    def __init__(self, x, y, screen, boundries, mario):
        super(Coin, self).__init__()
        self.bd = boundries
        self.mario = mario
        self.image = pygame.image.load('resources/graphics/coin_imgs/coin_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.counter = 0

        self.frames = [
        pygame.image.load('resources/graphics/coin_imgs/coin_1.png'),
        pygame.image.load('resources/graphics/coin_imgs/coin_2.png'),
        pygame.image.load('resources/graphics/coin_imgs/coin_3.png'),
        pygame.image.load('resources/graphics/coin_imgs/coin_4.png')
        ]


    def update(self):

        if self.counter == 10:
            self.image = self.frames[0]
        if self.counter == 20:
            self.image = self.frames[1]
        if self.counter == 30:
            self.image = self.frames[2]
        if self.counter == 40:
            self.image = self.frames[3]
            self.counter = 0
        self.counter += 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def mario_collision(self):
        coin_hit = pygame.sprite.collide_rect(self, self.mario)

        if coin_hit:
            coin_sfx = pygame.mixer.Sound("resources/sounds/coin.ogg")
            pygame.mixer.Sound.play(coin_sfx)
            self.mario.score += 100

            self.kill()