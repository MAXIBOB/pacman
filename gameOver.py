import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2
pygame.init()

WIDTH = 560
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")
BLACK = (0, 0, 0)
ghostP = Vector2(20,20)
ghostV = Vector2(8,0)
ghostTwoP = Vector2(450,20)
ghostTwoV = Vector2(8,0)

def ghostOne():
    ghost1 = pygame.image.load("/Users/teresalin/Desktop/ghost1.png")
    screen.blit(ghost1, (ghostP.x, ghostP.y+50))
    if ghostP.x > screen.get_width()-130 or ghostP.x < 10:
        ghostV.x *= -1
def ghostTwo():
    ghost2 = pygame.image.load("/Users/teresalin/Desktop/ghost2.png")
    screen.blit(ghost2, (ghostTwoP.x, ghostTwoP.y+430))
    if ghostTwoP.x > screen.get_width()-105 or ghostTwoP.x < 0:
        ghostTwoV.x *= -1


def drawScreen():

    screen.fill (BLACK)
    gameover2 = pygame.image.load("/Users/teresalin/Desktop/gameover2.jpg")
    screen.blit(gameover2, (50, 165))

inPlay = True
print "Hit ESC to end the program."
while inPlay:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    drawScreen()
    ghostOne()
    ghostTwo()
    ghostP += ghostV
    ghostTwoP += ghostTwoV
    pygame.display.update()

pygame.quit()
