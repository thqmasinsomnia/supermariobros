import pygame
import pygame.font


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('resources/font/Fixedsys500c.ttf', 32)
        self.x = 100
        self.y = 350

    def show_menu(self):
        img = pygame.image.load("resources/graphics/mainMenu.png").convert()
        self.screen.blit(img, [0, 0])
        self.screen.blit(self.font.render('PRESS SPACE TO START', True, self.text_color), [self.x - 10, self.y - 50])
