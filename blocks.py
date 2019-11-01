import pygame
from pygame.sprite import Sprite

class Blocks(Sprite):
    def __init__(self, screen, x, y, box_width, box_height, q_block, mario):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.mario = mario
        self.q_block = q_block
        self.image = pygame.Surface([box_width, box_height])
        self.hit = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.scroll_val = 0

        if q_block:
            self.image = pygame.image.load("resources/graphics/blocks/q_block_sprite.png")
        else:
            self.image = pygame.image.load("resources/graphics/blocks/block1.png")

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x = self.x

    def get_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def mario_collision(self):

        print("block y: " + str(self.y))
        print("mario y: " + str(self.mario.rect.y))
        if self.rect.y + 32 == self.mario.rect.y + 4 and self.mario.rect.x in range(self.rect.x, self.rect.x + 33):
            if self.q_block:
                self.mario.rect.y = self.rect.y
                self.mario.jumpcount = 0
                self.mario.injump = False
                self.image = pygame.image.load("resources/graphics/blocks/block1_hit.png")
                print("hit")
            else:
                self.kill()
                print("boom")

        # for posx in range(self.rect.x, self.rect.x + 32):
        #     for m_posx in range(self.mario.rect.x, self.mario.rect.x + 32):
        #         if self.rect.y + 32 == self.mario.rect.y:
        #             print("hello")
        #             self.mario.rect.y = self.rect.y + 33
        #             if self.q_block:
        #                 self.image = pygame.image.load("resources/graphics/blocks/block1_hit.png")
        #                 print("hit")
        #             else:
        #                 self.kill()
        #                 print("boom")


        # if self.mario.rect.y == (self.rect.y + 32) and self.mario.rect.x == (self.rect.x + 32):
        #     self.mario.rect.y = self.y + 32
        #     if self.q_block:
        #         self.image = pygame.image.load("resources/graphics/blocks/block1_hit.png")
        #         print("hit")
        #     else:
        #         self.kill()
        #         print("boom")

        # collision = pygame.sprite.collide_rect(self, self.mario)
        #
        # if collision:
        #     if self.q_block:
        #         self.image = pygame.image.load("resources/graphics/blocks/block1_hit.png")
        #         print("hit")
        #     else:
        #         self.kill()
        #         print("boom")

