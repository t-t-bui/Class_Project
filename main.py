import pygame, sys, random
from pygame.locals import *

#Initializing 
pygame.init()

#Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#Other Variables for use in the program
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

#Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill((255,255,255))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.rect = self.image.get.rect()
    self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

  def draw(self, surface):
    surface.blit(self.image, self,rect)
    
def main():
  print("Test")

#Game Look
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  pygame.display.update()
  FramePerSec.tick(FPS)

if __name__ == "__main__":
  main()