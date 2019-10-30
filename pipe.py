import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

pygame.init()
window = pygame.display.set_mode((100, 100))
class Pipe(Sprite):

    def __init__(self, type, cent_x, screen):
        self.width = 70
        self.type = type
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

        # resize the blank sprite
        self.rectangle = pygame.transform.scale(self.rectangle, (self.width, self.height))
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



    def blitme(self):
        self.screen.blit(self.image, self.rectangle_rect)