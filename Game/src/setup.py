import pygame
import copy
from src.board import Board
from src.menu import Menu
from src.function_buttons import MoveCounter, MenuButton
from src.levels import get_levels
from src.setting import *
from src.solver import *

# Set up display
pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption(Title)

# Imported my own icon into the game
program_icon = pygame.image.load('./Assets/photo/icon.png')
pygame.display.set_icon(program_icon)

# Set up the font
blocky_font_path = './Assets/font/PressStart2P.ttf'  
blocky_font_size = 20
blocky_font = pygame.font.Font(blocky_font_path, blocky_font_size)

# Set up for the sound effect
block_move_sound = pygame.mixer.Sound('./Assets/effects/audio/block_move_sound.wav')
button_click_sound = pygame.mixer.Sound('./Assets/effects/audio/button_click_sound.wav')
win_sound = pygame.mixer.Sound('./Assets/effects/audio/win_sound.wav')
window_xp_logon_sound = pygame.mixer.Sound('./Assets/effects/audio/window_xp_logon_sound.wav')
window_xp_logoff_sound = pygame.mixer.Sound('./Assets/effects/audio/window_xp_logoff_sound.wav')

board = Board()
current_level_index = 0
blocks = []
levels = get_levels() 
menu_button = MenuButton(screen)
menu = Menu(screen)
# Main menu
move_counter = MoveCounter()
window_xp_logon_sound.play()