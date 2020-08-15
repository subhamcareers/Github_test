import pygame, sys
from pygame.locals import *

catx = 10
caty = 10
screen = 0

def myquit():
    #Quit Function
    pygame.quit()
    sys.exit(0)
def check_inputs(events):
    global catx,caty,screen
    #Fucntion to handle the events occured
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
                elif event.key == K_LEFT:
                    catx-=5
                    print("Move Rect Left")
                elif event.key == K_RIGHT:
                    catx+=5
                    print("Move Rect Right")
                else:
                    print(event.key)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255, 255, 255),(catx,50, 50, 10))
    pygame.display.update()

def main():
    global screen
    #initialize game
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("SNAKE GAME BY SUBHAM")
    screen = pygame.display.get_surface()

    pygame.display.update()

    while True:
        check_inputs(pygame.event.get())

main()
