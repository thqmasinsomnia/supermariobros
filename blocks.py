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


    def mario_collision(self):
        collision = pygame.sprite.collide_rect(self, self.mario)

        if collision:
            if self.q_block:
                self.image = pygame.image.load("resources/graphics/blocks/block1_hit.png")
            else:
                self.kill()
                print("boom")

