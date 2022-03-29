import pygame
from pygame.locals import *
import pygame_menu

#Initializing 
SCREEN_HEIGHT, SCREEN_WIDTH = 600, 600
MENU_HEIGHT, MENU_WIDTH = 300, 400

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass
  
def main():
  pygame.init()
  FramePerSec = pygame.time.Clock()

  displaysurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("GAME")

  menu = pygame_menu.Menu('Welcome', MENU_WIDTH, MENU_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
  menu.add.text_input('Name : ', default='John Doe')
  menu.add.selector('Difficulty : ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
  menu.add.button('Play', start_the_game)
  menu.add.button('Quit', pygame_menu.events.EXIT)

  menu.mainloop(displaysurface)
  
if __name__ == "__main__":
  main()