import pygame, sys, os
from pygame.locals import * #load constants

red = [255, 0, 0] # It can be a list too

# Intializing the py game
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))

#setup Window
#window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Slither.eat - The Snake Game')

# Set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.flip()

#count = 0

while True:
    #main Game Loop
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
