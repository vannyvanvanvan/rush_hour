import pygame
from src.setting import *

class MoveCounter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        # add 1 to the initial number
        self.counter += 1

    def reset(self):
        # reset counter
        self.counter = 0

    def get_count(self):
        return self.counter



class MenuButton:
    def __init__(self, screen):
        self.screen = screen
        self.play_button = pygame.Rect(Screen_Width - 130, Screen_Height - 100, 100, 50)


    def render(self):
        from src.setup import blocky_font
        # Fill the screen with white
        self.screen.fill(DarkGrey)
        
        # Draw the menu button
        pygame.draw.rect(self.screen, Silver, self.play_button)  
        menu_text = blocky_font.render("menu", True, Black)
        menu_text_rect = menu_text.get_rect(center=self.play_button.center)
        self.screen.blit(menu_text, menu_text_rect)
        