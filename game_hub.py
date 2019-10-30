import pygame
from mario import Mario

class GameHub:
    def __init__(self, screen, mario):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.Font('resources/font/Fixedsys500c.ttf', 16)
        self.text = 'SCORE COINS WORLD TIME LIVES'
        self.text_color = (255, 255, 255)
        self.mario = mario

    def show_ui(self, mario):
        x = 10
        for word in self.text.split(' '):
            rect = self.font.render(word, False, self.text_color)
            self.screen.blit(rect, (x, 0))
            x += 110

        """Code for values. We pass in the functions that will get the player's scores, number of
        coins they have acquired, the world number, the time, and number of lives"""

        text = self.font.render(str(mario.score), False, self.text_color)
        rect = text.get_rect(center=(30, 35))
        self.screen.blit(text, rect)

        text = self.font.render(str(mario.coin_count), False, self.text_color)
        rect = text.get_rect(center=(150, 35))
        self.screen.blit(text, rect)

        text = self.font.render(str("1 - 1"), False, self.text_color)
        rect = text.get_rect(center=(250, 35))
        self.screen.blit(text, rect)

        # text = self.font.render(str("get the time"), False, self.text_color)
        # rect = text.get_rect(center=(557, 35))
        # self.screen.blit(text, rect)

        text = self.font.render(str(mario.lives), False, self.text_color)
        rect = text.get_rect(center=(470, 35))
        self.screen.blit(text, rect)
