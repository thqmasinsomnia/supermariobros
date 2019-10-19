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
        self.pos = vec(x, y)
        self.center = float(self.rect.centerx)
        self.screen_rect = screen.get_rect()
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.injump = False
        self.jumpcount = 0
        self.is_big = False

        """Mario animation sprite lists for L and R"""
        self.change_x = 0;
        self.walking_frames_r = [
            # small stance
            pygame.image.load('resources/graphics/marioimgs/mario.png'),
            # small move right 1
            pygame.image.load('resources/graphics/marioimgs/mario_move0.png'),
            # small move right 2
            pygame.image.load('resources/graphics/marioimgs/mario_move1.png'),
            # small move right 3
            pygame.image.load('resources/graphics/marioimgs/mario_move2.png'),
        ]
        self.walking_frames_l = [
            # small stance
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario.png'), True, False),
            # small move right 1
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario_move0.png'), True, False),
            # small move right 2
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario_move1.png'), True, False),
            # small move right 3
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario_move2.png'), True, False),
        ]
        self.big_walking_frames_r = [
            # big stance
            pygame.image.load('resources/graphics/marioimgs/mario1.png'),
            # big move right 1
            pygame.image.load('resources/graphics/marioimgs/mario1_move0.png'),
            # big move right 2
            pygame.image.load('resources/graphics/marioimgs/mario1_move1.png'),
            # bbig move right 3
            pygame.image.load('resources/graphics/marioimgs/mario1_move2.png'),
        ]
        self.big_walking_frames_l = [

            # big stance
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario1.png'), True, False),
            # big move left 1
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario1_move0.png'), True, False),
            # big move left 2
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario1_move1.png'), True, False),
            # big move left 3
            pygame.transform.flip(pygame.image.load('resources/graphics/marioimgs/mario1_move2.png'), True, False),

        ]

        # set initial walking/stance frame
        self.image = self.walking_frames_r[0]

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def make_big(self):

        self.is_big = True
        self.image = pygame.image.load('resources/graphics/marioimgs/mario1.png')
        big_sfx = pygame.mixer.Sound("resources/audio/upgrade.ogg")
        pygame.mixer.Sound.play(big_sfx)

    def update(self):

        if not self.is_big:
            hits = pygame.sprite.spritecollide(self, self.bd, False)
            self.rect.x += self.change_x
            pos = self.rect.x

            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += 4
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            if self.moving_left and self.rect.left > 0:
                self.center -= 4
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
            if not hits:
                self.rect.centery += 4
            self.rect.centerx = self.center

            if self.injump:
                print(self.jumpcount)
                if self.jumpcount > 2:
                    if hits:
                        self.rect.centery += 20
                        self.injump = False
                        self.jumpcount = 0

                if self.jumpcount < 25:
                    self.rect.y -= 10
                    self.jumpcount += 1
                if 25 <= self.jumpcount < 50:
                    self.jumpcount += 1
                if self.jumpcount == 50:
                    self.injump = False
                    self.jumpcount = 0

            if not self.injump:
                for bnd in self.bd:
                    col = pygame.sprite.collide_rect(self, bnd)
                    if col:
                        self.rect.y = bnd.rect.y - 30

        if self.is_big:
            hits = pygame.sprite.spritecollide(self, self.bd, False)
            self.rect.x += self.change_x
            pos = self.rect.x

            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += 4
                frame = (pos // 30) % len(self.big_walking_frames_r)
                self.image = self.big_walking_frames_r[frame]
            if self.moving_left and self.rect.left > 0:
                self.center -= 4
                frame = (pos // 30) % len(self.big_walking_frames_l)
                self.image = self.big_walking_frames_l[frame]
            if not hits:
                print("ass")
                self.rect.centery += 4
            self.rect.centerx = self.center

            if self.injump:
                print(self.jumpcount)
                if self.jumpcount > 2:
                    if hits:
                        self.rect.centery += 20
                        self.injump = False
                        self.jumpcount = 0

                if self.jumpcount < 25:
                    self.rect.y -= 11
                    self.jumpcount += 1
                if 25 <= self.jumpcount < 50:
                    self.jumpcount += 1
                if self.jumpcount == 50:
                    self.injump = False
                    self.jumpcount = 0

            if not self.injump:
                for bnd in self.bd:
                    col = pygame.sprite.collide_rect(self, bnd)
                    if col:
                        self.rect.y = bnd.rect.y - 30
        print(self.rect.y)

    def jump(self):
        self.rect.x += 1
        on_plat = pygame.sprite.spritecollide(self, self.bd, False)
        self.rect.x += 1

        if not self.is_big:
            if on_plat:
                print("jump!")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                self.image = pygame.image.load('resources/graphics/marioimgs/mario_jump.png')
        else:
            if on_plat:
                print("big jump!")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                self.image = pygame.image.load('resources/graphics/marioimgs/mario1_jump.png')

    def stop_left(self):
        # Called when the user lets off the keyboard and sets sprite to stance
        self.change_x = 0
        if not self.is_big:
            self.image = self.walking_frames_l[0]
        else:
            self.image = self.big_walking_frames_l[0]

    def stop_right(self):
        # Called when the user lets off the keyboard and sets sprite to stance
        self.change_x = 0

        if not self.is_big:
            self.image = self.walking_frames_r[0]
        else:
            self.image = self.big_walking_frames_r[0]
