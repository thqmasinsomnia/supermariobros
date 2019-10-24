import pygame

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)


class Levels:
    def __init__(self, player):
        # Lists of sprites used in all levels
        self.platform_list = None
        self.enemy_list = None
        # self.img = pygame.image.load("resources/graphics/level_1.png").convert()
        # self.background = pygame.transform.scale(self.img, (3392, 500))
        self.background = pygame.image.load("resources/graphics/level_one.png").convert()

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -3300
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        # Update everything
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(BLUE)
        screen.blit(self.background, (self.world_shift, 0))


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift = shift_x
        print(self.world_shift)

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x