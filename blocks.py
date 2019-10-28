import pygame
from pygame.sprite import Sprite

class Blocks(Sprite):
    def __init__(self, screen, x, y, box_width, box_height, q_block):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.Surface([box_width, box_height])
        self.hit = False
       # pygame.draw.rect(self.image, [0, 0, box_width, box_height])
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
        if self.hit:
            self.kill()
