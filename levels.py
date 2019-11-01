import pygame

from coin import Coin
from flag import Flag
from pipe import Pipe

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)


class Levels:

    def __init__(self, goombas, koops, plats, blocks, player):
        # Lists of sprites used in all levels
        self.platform_list = None
        self.enemy_list = None
        # Lists of sprites used in all levels
        self.platform_list = None
        self.enemy_list = None
        self.block_list = None
        self.blocks = blocks
        self.pipe_list = None
        # self.img = pygame.image.load("resources/graphics/level_1.png").convert()
        # self.background = pygame.transform.scale(self.img, (3392, 500))
        self.background = pygame.image.load("resources/graphics/level_one.png").convert()


        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -3300
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

        #self.mario = mario
        self.enemy_list.add(goombas)
        self.enemy_list.add(koops)
        self.platform_list.add(plats)
        self.block_list = pygame.sprite.Group()
        self.pipe_list = pygame.sprite.Group()

        self.player = player

    # Update everything on this level
    def update(self):
        # Update everything

        self.platform_list.update()
        self.enemy_list.update()

        self.block_list.update()

    def draw(self, screen, blocks):
        self.pipe_list()

    def draw(self, screen, pipe):

        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(BLUE)
        screen.blit(self.background, (self.world_shift, 0))


#        self.block_list = blocks

        # pipe1 = Pipe('short', 1035, screen)
        # pipe2 = Pipe('medium', 1393, screen)
        # pipe3 = Pipe('long', 1678, screen)
        # pipe4 = Pipe('long', 2071, screen)
        # pipe5 = Pipe('short', 5857, screen)
        # pipe6 = Pipe('short', 6427, screen)



        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

        self.block_list.draw(screen)

        self.pipe_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift = shift_x
        print("world shift: ", self.world_shift)


        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x = shift_x

        for enemy in self.enemy_list:

            enemy.rect.x = shift_x

        for block in self.block_list:
            block.rect.x = shift_x
