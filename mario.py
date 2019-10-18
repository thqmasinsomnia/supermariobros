import pygame
from pygame.sprite import Sprite
vec = pygame.math.Vector2



class Mario(Sprite):
    def __init__(self, x, y, screen, boundries):
        super(Mario, self).__init__()
        self.moving_right = False
        self.bd = boundries
        self.screen = screen
        self.moving_left = False
        self.image = pygame.image.load('resources/graphics/marioimgs/mario.png')
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.center = float(self.rect.centerx)
        self.screen_rect = screen.get_rect()
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.injump = False
        self.jumpcount = 0

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):


        hits = pygame.sprite.spritecollide(self, self.bd, False)

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 4
        if self.moving_left and self.rect.left > 0:
            self.center -= 4
        if not hits:
            self.rect.centery += 4
        self.rect.centerx = self.center

        if self.injump:
            if self.jumpcount < 25:
                self.rect.y -= 10
                self.jumpcount += 1
            if self.jumpcount >= 25 and self.jumpcount < 50:
                self.jumpcount += 1
            if self.jumpcount == 50:
                self.injump = False
                self.jumpcount = 0


    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.bd, False)
        self.rect.x += 1

        if hits:
            print("jump!")
            self.injump = True

