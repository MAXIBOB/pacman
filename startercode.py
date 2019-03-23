import pygame, sys, random
from pygame.locals import *
pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")

BLACK = (0, 0, 0)
def drawScreen():
    screen.fill (BLACK)
    pygame.display.update()
    
inPlay = True
print "Hit ESC to end the program."
while inPlay: #Animation loop
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    drawScreen()

pygame.quit()
