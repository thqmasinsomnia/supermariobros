import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Pipe(Sprite):
    def __init__(self, type, cent_x, screen, mario):
        super(Pipe, self).__init__()
        self.width = 70
        self.type = type
        self.center = cent_x
        self.mario = mario
        self.screen = screen

        # use blank sprite for pipe sprite
        self.rectangle = pygame.image.load('resources/graphics/nothing.png')
        self.rectangle_rect = self.rectangle.get_rect()

        # if type is short
        if self.type == 'short':
            self.height = 70
        # if type is medium
        elif self.type == 'medium':
            self.height = 105
        # if type is long
        elif self.type == 'long':
            self.height = 140
        else:
            print("Error: type of pipe loaded was not short, medium, or long")
            exit()

        self.image = pygame.Surface((70, self.height)).convert()
        # resize the blank sprite
        self.rectangle = pygame.transform.scale(self.rectangle, (self.width, self.height))

        # Place the rect on the screen
        self.rectangle_rect.midbottom = (cent_x, 445 - (self.height / 2))




    # We can land on the pipe sprite
    # def mario_is_on_top(self, mario):
    #     pass
    # If pipe can be entered
        # If pressed down
            # Enter pipe, change level

    # In the main file, we will create a list of pipes when the game starts
        # We will already know the height and location of each pipe before the game starts
    # In main
        # When we


    # If mario collides with the side of pipe
        # Leave his x where the collision happened instead of changing x as normal when pressing arrow

    def mario_col(self):
        if self.center - 35 < self.mario.rect.x < self.center + 35:
            self.mario.rect.y = 450 - self.height


    def blitme(self):
        self.screen.blit(self.rectangle, self.rectangle_rect)