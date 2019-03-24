import pygame, sys, random, os
from pygame.locals import *
import PIL

WIDTH = 1200
HEIGHT = 800
#pygME Starts
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")

BLACK = (0, 0, 0)

class Ghosts:
    x = WIDTH/2
    y =  HEIGHT/2
    width = 40
    height = 40
    vel = 0.9

    sprite = pygame.image.load('Pacman.png')
    sprite =  pygame.transform.scale(sprite, (width, height))
    
class Pacman:
    x = WIDTH/2
    y =  HEIGHT/2
    width = 40
    height = 40
    vel = 1.0 

    sprite = pygame.image.load('Pacman.png')
    sprite =  pygame.transform.scale(sprite, (width, height))

    def draw (self):
        screen.blit(self.sprite, (self.x, self.y))
def drawScreen():
    screen.fill (BLACK)
    
inPlay = True
print "Hit ESC to end the program."

player = Pacman()
while inPlay:
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    drawScreen()
    player.draw()
    pygame.display.update()

pygame.quit()
 
