import pygame
from pygame.sprite import Sprite


#    pygame.image.load('resources/graphics/goombaimgs/green_koopa_shell.png'),
class Star(Sprite):
    def __init__(self, x, y, screen, boundries, mario):
        super(Star, self).__init__()
        self.bd = boundries
        self.mario = mario
        self.image = pygame.image.load('resources/graphics/star/star1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.moving_left = True
        self.moving_right = False
        self.injump = False
        self.jumpcount = 0
        self.frame = [
            pygame.image.load('resources/graphics/star/star1.png'),
            pygame.image.load('resources/graphics/star/star2.png'),
            pygame.image.load('resources/graphics/star/star3.png'),
            pygame.image.load('resources/graphics/star/star4.png')
        ]

        self.walkcounter = 0

    def update(self):

        self.jump()
        self.jumpdate()

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
        if self.rect.right > 7000:
            self.moving_left = True
            self.moving_right = False
        self.rect.centerx = self.center

        if self.walkcounter == 20:
            self.image = self.frame[0]
        elif self.walkcounter == 40:
            self.image = self.frame[1]
        elif self.walkcounter == 60:
            self.image = self.frame[2]
        elif self.walkcounter == 80:
            self.image = self.frame[3]
            self.walkcounter = 0

        self.walkcounter += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def mario_collision(self):

        oof = pygame.sprite.collide_rect(self, self.mario)

        if oof:
            self.mario.make_big()
            self.mario.make_star()
            self.kill()

    def jump(self):
        self.rect.x += 1
        on_plat = pygame.sprite.spritecollide(self, self.bd, False)
        self.rect.x += 1

        if not self.injump:
            if on_plat:
                self.injump = True

    def jumpdate(self):
        if self.injump:
            if self.jumpcount < 30:
                self.rect.y -= 7
                self.jumpcount += 1
            if 25 <= self.jumpcount < 60:
                self.jumpcount += 1
            if self.jumpcount == 60:
                self.injump = False
                self.jumpcount = 0
