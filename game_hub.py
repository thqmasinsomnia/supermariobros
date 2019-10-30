import pygame


class GameHub:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.Font('resources/font/Fixedsys500c.ttf', 16)
        self.text = 'SCORE COINS WORLD TIME LIVES'
        self.text_color = (255, 255, 255)

    def show_ui(self):
        x = 10
        for word in self.text.split(' '):
            rect = self.font.render(word, False, self.text_color)
            self.screen.blit(rect, (x, 0))
            x += 110

        """Code for values. We pass in the functions that will get the player's scores, number of
        coins they have acquired, the world number, the time, and number of lives"""

        # text = self.font.render(str("here is where we get the player score"), False, self.text_color)
        # rect = text.get_rect(center=(60, 35))
        # self.screen.blit(text, rect)
        #
        # text = self.font.render(str("number of coins"), False, self.text_color)
        # rect = text.get_rect(center=(230, 35))
        # self.screen.blit(text, rect)
        #
        # text = self.font.render("get world number"), False, self.text_color)
        # rect = text.get_rect(center=(395, 35))
        # self.screen.blit(text, rect)
        #
        # text = self.font.render(str("get the time"), False, self.text_color)
        # rect = text.get_rect(center=(557, 35))
        # self.screen.blit(text, rect)
        #
        # text = self.font.render(str("get number of lives"), False, self.text_color)
        # rect = text.get_rect(center=(730, 35))
        # self.screen.blit(text, rect)