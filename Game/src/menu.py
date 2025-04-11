import pygame
from src.setting import *
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.play_button = pygame.Rect(Screen_Width/3, Screen_Height/3, 200, 50)
        self.benchmark_button = pygame.Rect(Screen_Width/3, Screen_Height/3 + 70, 200, 50)
        
    def render(self):
        from src.setup import blocky_font
        # Fill the screen with white
        self.screen.fill(DarkGrey)

        # Draw the title
        title_text = blocky_font.render("Rush Hour", True, White) 
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 50))
        self.screen.blit(title_text, title_rect)

        # Draw the play button
        pygame.draw.rect(self.screen, Silver, self.play_button)  
        play_text = blocky_font.render("Play", True, Black)
        play_text_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_text_rect)
        
        # Benchmark
        pygame.draw.rect(self.screen, Silver, self.benchmark_button)
        benchmark_text = blocky_font.render("Benchmark", True, Black)
        benchmark_rect = benchmark_text.get_rect(center=self.benchmark_button.center)
        self.screen.blit(benchmark_text, benchmark_rect)
        

        

    def render_level_selection(self, levels):
        from src.setup import blocky_font
        # Fill the screen for level selection
        self.screen.fill(DarkGrey)  

        # Draw title for level selection
        title_text = blocky_font.render("Select Level", True, White)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 50))
        self.screen.blit(title_text, title_rect)

        for index, _ in enumerate(levels): 
            level_rect = pygame.Rect(Screen_Width // 2 - 100, Screen_Height // 4 + index * 50 - 20, 200, 40)
            pygame.draw.rect(self.screen, Silver, level_rect) 
            level_text = blocky_font.render(f"Level {index + 1}", True, Black)
            level_text_rect = level_text.get_rect(center=level_rect.center)
            self.screen.blit(level_text, level_text_rect)
