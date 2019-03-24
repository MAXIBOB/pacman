import pygame, sys, random
from pygame.locals import *
pygame.init()

WIDTH = 560
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")

BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

def drawMap():
    
    
    #TOP&BOTTOM
    pygame.draw.rect (screen, BLUE, [0, 0, 560, 10], 0)
    pygame.draw.rect (screen, BLUE, [0, 610, 560, 10], 0)
    
    #RIGHTSIDE
    pygame.draw.rect (screen, BLUE, [0, 0, 10, 200], 0)
    pygame.draw.rect (screen, BLUE, [0, 380, 10, 240], 0)
    pygame.draw.rect (screen, BLUE, [0, 190, 110, 80], 0)
    pygame.draw.rect (screen, BLUE, [0, 310, 110, 80], 0)
    pygame.draw.rect (screen, BLUE, [0, 510, 50, 20], 0)
    
    #LEFTSIDE
    pygame.draw.rect (screen, BLUE, [550, 0, 10, 200], 0)
    pygame.draw.rect (screen, BLUE, [550, 380, 10, 240], 0)
    pygame.draw.rect (screen, BLUE, [450, 190, 110, 80], 0)
    pygame.draw.rect (screen, BLUE, [450, 310, 110, 80], 0)
    pygame.draw.rect (screen, BLUE, [510, 510, 50, 20], 0)
    
    #ROW1
    pygame.draw.rect (screen, BLUE, [50, 50, 60, 40], 0)
    pygame.draw.rect (screen, BLUE, [150, 50, 80, 40], 0)
    pygame.draw.rect (screen, BLUE, [270, 0, 20, 90], 0)
    pygame.draw.rect (screen, BLUE, [330, 50, 80, 40], 0)
    pygame.draw.rect (screen, BLUE, [450, 50, 60, 40], 0)
    
    #ROW2
    pygame.draw.rect (screen, BLUE, [50, 130, 60, 20], 0)
    pygame.draw.rect (screen, BLUE, [150, 130, 20, 140], 0)
    pygame.draw.rect (screen, BLUE, [150, 190, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [210, 130, 140, 20], 0)
    pygame.draw.rect (screen, BLUE, [390, 130, 20, 140], 0)
    pygame.draw.rect (screen, BLUE, [330, 190, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [450, 130, 60, 20], 0)
    
    #ROW3
    pygame.draw.rect (screen, BLUE, [150, 310, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [390, 310, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [210, 370, 140, 20], 0)
    pygame.draw.rect (screen, BLUE, [270, 370, 20, 80], 0)
    
    #ROW4
    pygame.draw.rect (screen, BLUE, [50, 430, 60, 20], 0)
    pygame.draw.rect (screen, BLUE, [90, 430, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [150, 430, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [330, 430, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [450, 430, 60, 20], 0)
    pygame.draw.rect (screen, BLUE, [450, 430, 20, 80], 0)
    
    #ROW5
    pygame.draw.rect (screen, BLUE, [150, 490, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [50, 560, 180, 20], 0)
    pygame.draw.rect (screen, BLUE, [210, 490, 140, 20], 0)
    pygame.draw.rect (screen, BLUE, [270, 490, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [390, 490, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [330, 560, 180, 20], 0)

def drawDots():
    x = 20
    y = 20
    for i in range(0, 40):
        for j in range(0, 40):
            pygame.draw.rect (screen, WHITE, [x+20*i, y+20*j, 5, 5], 0)
    if x == 20 and y == 100:
        pygame.draw.rect (screen, BLACK, [x+20*i, y+20*j, 5, 5], 0)


def main():
    screen.fill (BLACK)
    drawDots()
    drawMap()
    
    
    
inPlay = True
print "Hit ESC to end the program."
while inPlay: #Animation loop
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    main()
    pygame.display.update()

pygame.quit()
