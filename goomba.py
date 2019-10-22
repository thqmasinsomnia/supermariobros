import pygame
from pygame.sprite import Sprite
from mario import Mario
from pygame.sprite import Group
from boundry import Boundry

vec = pygame.math.Vector2

class Goomba(Sprite):
    def __init__(self, x, y, screen, boundries, mario):
        super(Goomba, self).__init__()
        self.bd = boundries
        self.mario = mario
        self.image = pygame.image.load('resources/graphics/goomba.png')
        self.rect = self.image.get_rect()
        self.center = float(self.rect.centerx)
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.moving_left = False
        self.moving_right = True


    def update(self):

        hits = pygame.sprite.spritecollide(self, self.bd, False)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= 1
        if not hits:
            self.rect.centery += 4
        if self.rect.left == 0:
            self.moving_left = False
            self.moving_right = True
        if self.rect.right == self.screen_rect.right:
            self.moving_left = True
            self.moving_right = False
        self.rect.centerx = self.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def mario_collision(self):

        col = False

        print(self.rect.y)
        print(self.mario.rect.y)
        print("------------")
        if self.mario.is_big:
            if self.mario.rect.y + 38 >= self.rect.y and self.mario.rect.x == self.rect.x:
                col = True
        else:
            col = pygame.sprite.collide_rect(self, self.mario)

        if col:
            self.kill()


