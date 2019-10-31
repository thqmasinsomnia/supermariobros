import pygame
from pygame.sprite import Sprite


class Mushroom(Sprite):
    def __init__(self, x, y, screen, boundries, type, mario):
        super(Mushroom, self).__init__()
        self.mario = mario

        self.screen_rect = screen.get_rect()
        self.bd = boundries
        self.screen = screen
        self.type = type
        self.moving_right = False
        self.moving_left = True

        if self.type == "one_up":
            self.image = pygame.image.load('resources/graphics/mushrooms/one_up.png')
        elif self.type == "big":
            self.image = pygame.image.load('resources/graphics/mushrooms/big_mushroom.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)

    def update(self):

        hits = pygame.sprite.spritecollide(self, self.bd, False)
        if self.moving_right and self.rect.right < 7000:
            self.center += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= 1
        if not hits:
            self.rect.centery += 4
        if self.rect.left == 0:
            self.moving_left = False
            self.moving_right = True
        if self.rect.right == 7000:
            self.moving_left = True
            self.moving_right = False
        self.rect.centerx = self.center

        if self.rect.y > 1000:
            self.kill()

    def mario_collision(self):
        col = pygame.sprite.collide_rect(self, self.mario)

        if col:
            if self.type == "big":
                self.mario.make_big()
            elif self.type == "one_up":
                one_sfx = pygame.mixer.Sound("resources/sounds/one_up.ogg")
                pygame.mixer.Sound.play(one_sfx)
                self.mario.lives += 1
            self.kill()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
