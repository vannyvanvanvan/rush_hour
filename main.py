import pygame

from setting import *

pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption(Title)
# pygame.time.Clock()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
            
def run():
    game_running = True
    while game_running:
        events()


if __name__ == "__main__":
    run()