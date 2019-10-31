import pygame
from pygame.sprite import Sprite

#    pygame.image.load('resources/graphics/goombaimgs/green_koopa_shell.png'),
class Flying_Koopa(Sprite):
    def __init__(self, x, y, screen, boundries, mario, goombas):
        super(Flying_Koopa, self).__init__()
        self.bd = boundries
        self.goombas = goombas
        self.mario = mario
        self.image = pygame.image.load('resources/graphics/green_koopaimgs/green_koopa_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center = float(self.rect.centerx)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.moving_left = True
        self.moving_right = False
        self.dead = False
        self.grace = 0
        self.isshell = False
        self.movingshell = False
        self.injump = False
        self.jumpcount = 0
        self.frames_l = [
            pygame.image.load('resources/graphics/flying_koopaimgs/fly_koopa_1.png'),
            pygame.image.load('resources/graphics/flying_koopaimgs/fly_koopa_2.png')
        ]
        self.frames_r = [
            pygame.transform.flip(pygame.image.load('resources/graphics/flying_koopaimgs/fly_koopa_2.png'), True,
                                  False),
            pygame.transform.flip(pygame.image.load('resources/graphics/flying_koopaimgs/fly_koopa_2.png'), True,
                                  False)
        ]
        self.walkcounter = 0

    def update(self):

        self.jump()
        self.jumpdate()
        if self.rect.y > 1000:
            self.kill()

        if not self.isshell:
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

            if self.moving_left:
                if self.walkcounter == 20:
                    self.image = self.frames_l[0]
                elif self.walkcounter == 40:
                    self.image = self.frames_l[1]
                    self.walkcounter = 0

            if self.moving_right:
                if self.walkcounter == 20:
                    self.image = self.frames_r[0]
                elif self.walkcounter == 40:
                    self.image = self.frames_r[1]
                    self.walkcounter = 0


            self.walkcounter += 1

        if self.movingshell:
            self.grace += 1

        if self.isshell and self.movingshell:


            hits = pygame.sprite.spritecollide(self, self.bd, False)
            if self.moving_right and self.rect.right < 7000:
                self.center += 4
            if self.moving_left and self.rect.left > 0:
                self.center -= 4
            if not hits:
                self.rect.centery += 4
            if self.rect.left <= 0:
                self.moving_left = False
                self.moving_right = True
            if self.rect.x >= 7000:
                self.moving_left = True
                self.moving_right = False
            self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def mario_collision(self):

        if not self.isshell:
                col = False
                oof = False

                if self.mario.is_big:
                    if self.rect.y >= self.mario.rect.y + 64 > self.rect.y - 5 and self.rect.x < self.mario.rect.x < self.rect.x + 32:
                        col = True
                elif not self.mario.is_big:
                    if self.rect.y >= self.mario.rect.y + 30 > self.rect.y - 10 and self.rect.x - 32 < self.mario.rect.x < self.rect.x + 32:
                        col = True

                oof = pygame.sprite.collide_rect(self, self.mario)

                if col:
                    self.image = pygame.image.load('resources/graphics/green_koopaimgs/green_koopa_shell.png')
                    big_sfx = pygame.mixer.Sound("resources/sounds/stomp.ogg")
                    pygame.mixer.Sound.play(big_sfx)
                    self.mario.score += 100

                    self.walkcounter = 100
                    self.moving_left = False
                    self.moving_right = False
                    self.dead = True
                    self.isshell = True

                if not self.dead:
                    if oof  and self.grace > 30:
                        if not self.mario.is_big:
                            print("FUC")
                            pygame.mixer.music.load('resources/audio/death.wav')
                            pygame.mixer.music.play(1)
                            self.mario.death_animation()
                        elif self.mario.is_big:
                            self.mario.make_small()
                            self.grace = 0
                    else:
                        self.grace += 1

        else:

            oof = pygame.sprite.collide_rect(self, self.mario)


            if oof and self.movingshell == False:
                self.movingshell = True
                self.moving_left = True

            if oof and self.movingshell and self.grace > 20:
                pygame.mixer.music.load('resources/audio/death.wav')
                pygame.mixer.music.play(1)
                self.mario.death_animation()


    def goomba_collisions(self):

        if self.isshell:
            for goomba in self.goombas:
                oof = pygame.sprite.collide_rect(self, goomba)
                if oof:
                    goomba.squish()




    def jump(self):
        self.rect.x += 1
        on_plat = pygame.sprite.spritecollide(self, self.bd, False)
        self.rect.x +=1

        if not self.isshell and not self.injump:
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
