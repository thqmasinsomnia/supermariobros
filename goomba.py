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
        self.image = pygame.image.load('resources/graphics/goombaimgs/goomba1.png')
        self.rect = self.image.get_rect()
        self.center = float(self.rect.centerx)
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.moving_left = False
        self.moving_right = True
        self.dead = False
        self.frames = [
            pygame.image.load('resources/graphics/goombaimgs/goomba1.png'),
            pygame.image.load('resources/graphics/goombaimgs/goomba2.png'),
            pygame.image.load('resources/graphics/goombaimgs/goomba3.png'),
        ]
        self.walkcounter = 0;

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

        if self.walkcounter == 20:
            self.image = pygame.image.load('resources/graphics/goombaimgs/goomba2.png')
        elif self.walkcounter == 40:
            self.image = pygame.image.load('resources/graphics/goombaimgs/goomba1.png')
            self.walkcounter = 0

        self.walkcounter += 1

        if self.walkcounter == 120:
            self.kill()

        if self.rect.y > 1000:
            self.kill()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def mario_collision(self):

        col = False
        oof = False

        print(self.rect.y)
        print(self.mario.rect.y)

        print("------------")
        if self.mario.is_big:
            if self.rect.y >= self.mario.rect.y + 64 > self.rect.y - 5 and self.rect.x < self.mario.rect.x < self.rect.x + 32:
                col = True
        elif not self.mario.is_big:
            if self.rect.y >= self.mario.rect.y + 32 > self.rect.y - 5 and self.rect.x < self.mario.rect.x < self.rect.x + 32:
                col = True

        oof = pygame.sprite.collide_rect(self, self.mario)

        if col:
            self.image = pygame.image.load('resources/graphics/goombaimgs/goomba3.png')
            big_sfx = pygame.mixer.Sound("resources/sounds/stomp.ogg")
            pygame.mixer.Sound.play(big_sfx)

            self.walkcounter = 100
            self.moving_left = False
            self.moving_right = False
            self.dead = True

        if not self.dead:
                if oof:
                    big_sfx = pygame.mixer.Sound("resources/sounds/pipe.ogg")
                    pygame.mixer.Sound.play(big_sfx)
