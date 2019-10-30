import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from boundry import Boundry
from levels import Levels
from flag import Flag
import sys

vec = pygame.math.Vector2


class Mario(Sprite):
    def __init__(self, x, y, screen, boundries):
        super(Mario, self).__init__()
        self.moving_right = False
        self.score = 0
        self.lives = 3
        self.reset_x = 0
        self.bd = boundries
        # self.flg = flags
        self.screen = screen
        self.moving_left = False
        self.image = pygame.image.load('resources/graphics/marioimgs/mario.png')
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.center = float(self.rect.centerx)
        self.screen_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.injump = False
        self.jumpcount = 0
        self.is_big = False
        self.big_bd = Group()
        # self.flag_group = Group()
        self.lives = 3
        self.deathcount = 0
        self.hit = False
        self.pitdeath = False
        self.crouch = False
        self.is_lit = False
        self.is_star = False
        self.star_counter = 0
        self.facing_right = False
        self.facing_left = False

        for bnd in self.bd:
            x = Boundry(bnd.rect.x, bnd.rect.y - 34, bnd.width, bnd.height, self.screen, True)
            self.big_bd.add(x)

        # for flag in self.flg:
        #     x = Flag(flag.rect.x, flag.rect.y - 34, flag.width, flag.height, self.screen)
        #     self.flag_group.add(x)

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
            pygame.image.load('resources/graphics/marioimgs/marioL.png'),
            # small move left 1
            pygame.image.load('resources/graphics/marioimgs/marioL_move0.png'),
            # small move left 2
            pygame.image.load('resources/graphics/marioimgs/marioL_move1.png'),
            # small move left 3
            pygame.image.load('resources/graphics/marioimgs/marioL_move2.png'),
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

            # big stance left
            pygame.image.load('resources/graphics/marioimgs/mario1L.png'),
            # big move left 1
            pygame.image.load('resources/graphics/marioimgs/mario1L_move0.png'),
            # big move left 2
            pygame.image.load('resources/graphics/marioimgs/mario1L_move1.png'),
            # big move left 3
            pygame.image.load('resources/graphics/marioimgs/mario1L_move2.png'),

        ]
        self.lit_walking_frames_r = [
            # big stance
            pygame.image.load('resources/graphics/marioimgs/mario2.png'),
            # big move right 1
            pygame.image.load('resources/graphics/marioimgs/mario2_move0.png'),
            # big move right 2
            pygame.image.load('resources/graphics/marioimgs/mario2_move1.png'),
            # bbig move right 3
            pygame.image.load('resources/graphics/marioimgs/mario2_move2.png'),
        ]
        self.lit_walking_frames_l = [

            # big stance
            pygame.image.load('resources/graphics/marioimgs/mario2L.png'),
            # big move left 1
            pygame.image.load('resources/graphics/marioimgs/mario2L_move0.png'),
            # big move left 2
            pygame.image.load('resources/graphics/marioimgs/mario2L_move1.png'),
            # big move left 3
            pygame.image.load('resources/graphics/marioimgs/mario2L_move2.png'),

        ]
        self.star_walking_frames_l = [
            pygame.image.load('resources/graphics/marioimgs/mario1L.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2L.png'),
            pygame.image.load('resources/graphics/marioimgs/mario1L_move0.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2L_move0.png'),
            pygame.image.load('resources/graphics/marioimgs/mario1L_move1.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2L_move1.png'),
            pygame.image.load('resources/graphics/marioimgs/mario1L_move2.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2L_move2.png'),
        ]
        self.star_walking_frames_r = [
            pygame.image.load('resources/graphics/marioimgs/mario1.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2.png'),
            pygame.image.load('resources/graphics/marioimgs/mario1_move0.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2_move0.png'),
            pygame.image.load('resources/graphics/marioimgs/mario1_move1.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2_move1.png'),
            pygame.image.load('resources/graphics/marioimgs/mario1_move2.png'),
            pygame.image.load('resources/graphics/marioimgs/mario2_move2.png'),
        ]
        # set initial walking/stance frame
        self.image = self.walking_frames_r[0]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def mario_state(self):
        if self.is_big and not self.is_lit and not self.is_star:
            self.make_lit()
        elif self.is_lit:
            self.make_star()
        elif self.is_star:
            self.make_small()
        else:
            self.make_big()

    def make_big(self):
        self.is_big = True
        self.is_lit = False
        self.image = pygame.image.load('resources/graphics/marioimgs/mario1.png')
        big_sfx = pygame.mixer.Sound("resources/audio/upgrade.ogg")
        pygame.mixer.Sound.play(big_sfx)

    def make_lit(self):
        self.is_lit = True
        self.image = pygame.image.load('resources/graphics/marioimgs/mario2.png')
        big_sfx = pygame.mixer.Sound("resources/audio/upgrade.ogg")
        pygame.mixer.Sound.play(big_sfx)

    def make_star(self):
        self.is_lit = False
        self.is_star = True
        self.image = pygame.image.load('resources/graphics/marioimgs/mario1.png')
        big_sfx = pygame.mixer.Sound("resources/audio/upgrade.ogg")
        pygame.mixer.Sound.play(big_sfx)

    def make_small(self):
        self.is_big = False
        self.is_lit = False
        self.is_star = False
        self.image = pygame.image.load('resources/graphics/marioimgs/mario.png')
        big_sfx = pygame.mixer.Sound("resources/sounds/pipe.ogg")
        pygame.mixer.Sound.play(big_sfx)

    def update(self):
        if self.rect.y > 500 and self.pitdeath == False and self.hit == False:
            self.death_animation()
            self.hit = True
            pygame.mixer.music.load('resources/audio/death.wav')
            pygame.mixer.music.play(1)
            self.pitdeath = True

        if self.hit:
            self.image = pygame.image.load('resources/graphics/marioimgs/mario_death.png')
            if self.deathcount < 50:
                self.rect.y -= 4
                self.deathcount += 1
            elif self.deathcount >= 50:
                self.rect.y += 4
                self.deathcount += 1
            elif self.deathcount == 150:
                self.deathcount = 0
                self.hit = False
                self.pitdeath = False

        if not self.hit:
            # Small Mario
            if not self.is_big and not self.is_lit and not self.is_star:
                self.small_mario()
            # Normal Big Mario
            if self.is_big and not self.is_lit and not self.is_star:
                self.big_mario()
            # Fire Mario
            if self.is_big and self.is_lit and not self.is_star:
               self.fire_mario()
            if self.is_star:
                self.star_mario()
        if self.is_star:
            if self.star_counter == 2000:
                self.star_counter = 0
                self.is_star = False
                self.big_mario()
            self.star_counter += 1

    def jump(self):
        self.rect.x += 1
        on_plat = pygame.sprite.spritecollide(self, self.bd, False)
        on_big_plat = pygame.sprite.spritecollide(self, self.big_bd, False)
        self.rect.x += 1

        if not self.is_big and not self.is_lit and not self.is_star:
            if on_plat:
                print("jump!")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                self.image = pygame.image.load('resources/graphics/marioimgs/mario_jump.png')

        elif self.is_big and not self.is_lit and not self.is_star:
            if on_big_plat:
                print("big jump!")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                self.image = pygame.image.load('resources/graphics/marioimgs/mario1_jump.png')
        elif self.is_lit:
            if on_big_plat:
                print("lit jump")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                self.image = pygame.image.load('resources/graphics/marioimgs/mario2_jump.png')
        elif self.is_star:
            if on_big_plat:
                print("star jump")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                self.image = pygame.image.load('resources/graphics/marioimgs/mario1_jump.png')

    def stop_left(self):
        # Called when the user lets off the keyboard and sets sprite to stance
        self.change_x = 0
        if not self.is_big and not self.is_lit and not self.is_star:
            self.image = self.walking_frames_l[0]
        elif self.is_big and not self.is_lit and not self.is_star:
            self.image = self.big_walking_frames_l[0]
        elif self.is_lit:
            self.image = self.lit_walking_frames_l[0]

    def stop_right(self):
        # Called when the user lets off the keyboard and sets sprite to stance
        self.change_x = 0
        if not self.is_big and not self.is_lit and not self.is_star:
            self.image = self.walking_frames_r[0]
        elif self.is_big and not self.is_lit and not self.is_star:
            self.image = self.big_walking_frames_r[0]
        elif self.is_lit:
            self.image = self.lit_walking_frames_r[0]

    def death_animation(self):
        self.reset_x = self.rect.x
        self.hit = True
        self.image = pygame.image.load('resources/graphics/marioimgs/mario_death.png')
        self.moving_right = False
        self.moving_left = False

    def small_mario(self):
        if not self.is_big and not self.is_lit and not self.is_star:
            hits = pygame.sprite.spritecollide(self, self.bd, False)
            self.rect.x += self.change_x
            pos = self.rect.x

            if self.moving_right and self.rect.right < 7100:
                self.center += 4
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]

                """This part could be used to interact with the flag and make the game end"""
                if self.center == 7068:
                    sys.exit()

            if self.moving_left and self.rect.left > 0:
                self.center -= 4
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
            if not hits:
                self.rect.centery += 4
            self.rect.centerx = self.center
            print("Mario pos:", self.rect.centerx)

            if self.injump:
                if self.jumpcount > 2:
                    if hits:
                        self.rect.centery += 20
                        self.injump = False
                        self.jumpcount = 0
                if self.jumpcount < 40:
                    self.rect.y -= 10
                    self.jumpcount += 1
                if 25 <= self.jumpcount < 80:
                    self.jumpcount += 1
                if self.jumpcount == 80:
                    self.injump = False
                    self.jumpcount = 0
                    if self.facing_left:
                        self.image = pygame.image.load('resources/graphics/marioimgs/marioL.png')
                    else:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario.png')
            if not self.injump:
                for bnd in self.bd:
                    col = pygame.sprite.collide_rect(self, bnd)
                    if col:
                        self.rect.y = bnd.rect.y - 30

    def big_mario(self):
        if self.is_big and not self.is_lit and not self.is_star:
            hits = pygame.sprite.spritecollide(self, self.big_bd, False)
            self.rect.x += self.change_x
            pos = self.rect.x

            if self.moving_right and self.rect.right < 7100:
                self.center += 4
                frame = (pos // 30) % len(self.big_walking_frames_r)
                self.image = self.big_walking_frames_r[frame]
            if self.moving_left and self.rect.left > 0:
                self.center -= 4
                frame = (pos // 30) % len(self.big_walking_frames_l)
                self.image = self.big_walking_frames_l[frame]
            if not hits:
                self.rect.centery += 4
            self.rect.centerx = self.center

            if self.injump:
                if self.jumpcount > 2:
                    if hits:
                        self.rect.centery += 20
                        self.injump = False
                        self.jumpcount = 0
                if self.jumpcount < 40:
                    self.rect.y -= 10
                    self.jumpcount += 1
                if 25 <= self.jumpcount < 80:
                    self.jumpcount += 1
                if self.jumpcount == 80:
                    self.injump = False
                    self.jumpcount = 0
                    if self.facing_left:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario1L.png')
                    else:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario1.png')
            if not self.injump:
                for bnd in self.bd:
                    col = pygame.sprite.collide_rect(self, bnd)
                    if col:
                        self.rect.y = bnd.rect.y - 30
            if self.crouch:
                if self.facing_right:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario1_crouch_r.png')
                elif self.facing_left:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario1_crouch_l.png')

    def fire_mario(self):
        if self.is_lit:
            hits = pygame.sprite.spritecollide(self, self.big_bd, False)
            self.rect.x += self.change_x
            pos = self.rect.x

            if self.moving_right and self.rect.right < 7100:
                self.center += 4
                frame = (pos // 30) % len(self.lit_walking_frames_r)
                self.image = self.lit_walking_frames_r[frame]
            if self.moving_left and self.rect.left > 0:
                self.center -= 4
                frame = (pos // 30) % len(self.lit_walking_frames_l)
                self.image = self.lit_walking_frames_l[frame]
            if not hits:
                self.rect.centery += 4
            self.rect.centerx = self.center

            if self.injump:
                if self.jumpcount > 2:
                    if hits:
                        self.rect.centery += 20
                        self.injump = False
                        self.jumpcount = 0
                if self.jumpcount < 40:
                    self.rect.y -= 10
                    self.jumpcount += 1
                if 25 <= self.jumpcount < 80:
                    self.jumpcount += 1
                if self.jumpcount == 80:
                    self.injump = False
                    self.jumpcount = 0
                    if self.facing_left:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2L.png')
                    else:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2.png')
            if not self.injump:
                for bnd in self.bd:
                    col = pygame.sprite.collide_rect(self, bnd)
                    if col:
                        self.rect.y = bnd.rect.y - 30
                if self.crouch:
                    if self.facing_right:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2_crouch_r.png')
                    elif self.facing_left:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2_crouch_l.png')

    def star_mario(self):
        if self.is_star:
            hits = pygame.sprite.spritecollide(self, self.big_bd, False)
            self.rect.x += self.change_x
            pos = self.rect.x

            if self.star_counter % 6 == 0 and self.star_counter < 500:
                self.image = pygame.image.load('resources/graphics/marioimgs/mario1.png')
            if self.star_counter % 13 == 0 and self.star_counter < 500:
                self.image = pygame.image.load('resources/graphics/marioimgs/mario2.png')
            if self.moving_right and self.rect.right < 7100:
                self.center += 6
                frame = (pos // 30) % len(self.star_walking_frames_r)
                self.image = self.star_walking_frames_r[frame]
            if self.moving_left and self.rect.left > 0:
                self.center -= 6
                frame = (pos // 30) % len(self.star_walking_frames_l)
                self.image = self.star_walking_frames_l[frame]
            if not hits:
                self.rect.centery += 6
            self.rect.centerx = self.center

            if self.injump:
                if self.jumpcount % 6 == 0 and self.jumpcount < 80:
                    if self.facing_right:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario1_jump.png')
                    else:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario1L_jump.png')
                if self.jumpcount % 13 == 0 and self.jumpcount < 80:
                    if self.facing_right:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2_jump.png')
                    else:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2L_jump.png')
                if self.jumpcount > 2:
                    if hits:
                        self.rect.centery += 20
                        self.injump = False
                        self.jumpcount = 0
                if self.jumpcount < 40:
                    self.rect.y -= 10
                    self.jumpcount += 1
                if 25 <= self.jumpcount < 80:
                    self.jumpcount += 1
                if self.jumpcount == 80:
                    self.injump = False
                    self.jumpcount = 0
                    if self.facing_left:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario1L.png')
                    else:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario1.png')
            if not self.injump:
                for bnd in self.bd:
                    col = pygame.sprite.collide_rect(self, bnd)
                    if col:
                        self.rect.y = bnd.rect.y - 30
                if self.crouch:
                    if self.facing_right:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2_crouch_r.png')
                    elif self.facing_left:
                        self.image = pygame.image.load('resources/graphics/marioimgs/mario2_crouch_l.png')

    def jump(self):
        self.rect.x += 1
        on_plat = pygame.sprite.spritecollide(self, self.bd, False)
        on_big_plat = pygame.sprite.spritecollide(self, self.big_bd, False)
        self.rect.x += 1

        if not self.is_big and not self.is_lit and not self.is_star:
            if on_plat:
                print("jump!")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                if self.facing_left:
                    self.image = pygame.image.load('resources/graphics/marioimgs/marioL_jump.png')
                else:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario_jump.png')
        elif self.is_big and not self.is_lit and not self.is_star:
            if on_big_plat:
                print("big jump!")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                if self.facing_left:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario1L_jump.png')
                else:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario1_jump.png')
        elif self.is_lit:
            if on_big_plat:
                print("lit jump")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                if self.facing_left:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario2L_jump.png')
                else:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario2_jump.png')
        elif self.is_star:
            if on_big_plat:
                print("star jump")
                self.injump = True
                jump_sfx = pygame.mixer.Sound("resources/audio/jump.ogg")
                pygame.mixer.Sound.play(jump_sfx)
                if self.facing_left:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario1L_jump.png')
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario2L_jump.png')
                else:
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario1_jump.png')
                    self.image = pygame.image.load('resources/graphics/marioimgs/mario2_jump.png')

    def stop_left(self):
        # Called when the user lets off the keyboard and sets sprite to stance
        self.change_x = 0
        if not self.is_big and not self.is_lit:
            self.image = self.walking_frames_l[0]
        elif self.is_big and not self.is_lit and not self.is_star:
            self.image = self.big_walking_frames_l[0]
        elif self.is_lit:
            self.image = self.lit_walking_frames_l[0]

    def stop_right(self):
        # Called when the user lets off the keyboard and sets sprite to stance
        self.change_x = 0

        if not self.is_big and not self.is_lit:
            self.image = self.walking_frames_r[0]
        elif self.is_big and not self.is_lit and not self.is_star:
            self.image = self.big_walking_frames_r[0]
        elif self.is_lit:
            self.image = self.lit_walking_frames_r[0]


    def wall_col(self):
        for bound in self.bd:
            if self.rect.right == bound.rect.left:
                self.moving_right = False
                if self.rect.y + 30 > bound.rect.y:
                    self.moving_right = False


    def reset(self):
        self.lives -= 1
        self.rect.x = self.reset_x
        self.rect.y = 450
