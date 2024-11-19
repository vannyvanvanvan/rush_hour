import pygame
from setting import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.play_button = pygame.Rect(Screen_Width/3, Screen_Height/3, 200, 50)
        self.button_font = pygame.font.Font(None, 36)

    def render(self):
        # Fill the screen with white
        self.screen.fill(White)

        # Draw the title
        title_text = self.button_font.render("Rush Hour", True, Black) 
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 50))
        self.screen.blit(title_text, title_rect)

        # Draw the play button
        pygame.draw.rect(self.screen, Silver, self.play_button)  
        play_text = self.button_font.render("Play", True, Black)
        play_text_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_text_rect)

        pygame.display.flip() 

    def render_level_selection(self, levels):
        # Fill the screen for level selection
        self.screen.fill(White)  

        # Draw title for level selection
        title_text = self.button_font.render("Select Level", True, Black)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 50))
        self.screen.blit(title_text, title_rect)

        for index, _ in enumerate(levels): 
            level_rect = pygame.Rect(Screen_Width // 2 - 100, Screen_Height // 4 + index * 50 - 20, 200, 40)
            pygame.draw.rect(self.screen, Silver, level_rect) 
            level_text = self.button_font.render(f"Level {index + 1}", True, Black)
            level_text_rect = level_text.get_rect(center=level_rect.center)
            self.screen.blit(level_text, level_text_rect)

        pygame.display.flip()
