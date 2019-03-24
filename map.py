import pygame, sys, random
from pygame.locals import *
pygame.init()

WIDTH = 560
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")

PACMAN_X = 50
PACMAN_Y = 50
PACMAN_WIDTH = 40
PACMAN_HEIGHT = 60
PACMAN_VEL = 1

YELLOW = (255,255,153)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
def drawMap():
    screen.fill (BLACK)
    #TOP
    pygame.draw.rect (screen, BLUE, [0, 0, 560, 10], 0)
    #RIGHT
    pygame.draw.rect (screen, BLUE, [0, 0, 10, 200], 0)
    
    pygame.draw.rect (screen, BLUE, [0, 380, 10, 240], 0)
    #LEFT
    pygame.draw.rect (screen, BLUE, [550, 0, 10, 200], 0)
    pygame.draw.rect (screen, BLUE, [550, 260, 10, 10], 0)
    pygame.draw.rect (screen, BLUE, [550, 300, 10, 10], 0)
    pygame.draw.rect (screen, BLUE, [550, 380, 10, 240], 0)
    
    pygame.draw.rect (screen, BLUE, [450, 190, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [450, 260, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [450, 190, 10, 80], 0)
    pygame.draw.rect (screen, BLUE, [450, 300, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [450, 380, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [450, 300, 10, 80], 0)
    
    #ROW1
    pygame.draw.rect (screen, BLUE, [50, 50, 60, 40], 0)
    pygame.draw.rect (screen, BLUE, [140, 50, 80, 40], 0)
    pygame.draw.rect (screen, BLUE, [270, 0, 20, 90], 0)
    pygame.draw.rect (screen, BLUE, [330, 50, 80, 40], 0)
    pygame.draw.rect (screen, BLUE, [450, 50, 60, 40], 0)
    #ROW2
    pygame.draw.rect (screen, BLUE, [50, 130, 60, 20], 0)
    pygame.draw.rect (screen, BLUE, [140, 130, 20, 140], 0)
    pygame.draw.rect (screen, BLUE, [140, 190, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [210, 130, 140, 20], 0)
    pygame.draw.rect (screen, BLUE, [390, 130, 20, 140], 0)
    pygame.draw.rect (screen, BLUE, [330, 190, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [450, 130, 60, 20], 0)
    #ROW3
    pygame.draw.rect (screen, BLUE, [0, 190, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [0, 260, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [100, 190, 10, 80], 0)
    pygame.draw.rect (screen, BLUE, [0, 300, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [0, 380, 110, 10], 0)
    pygame.draw.rect (screen, BLUE, [100, 300, 10, 80], 0)
    
    pygame.draw.rect (screen, BLUE, [390, 130, 20, 140], 0)
    pygame.draw.rect (screen, BLUE, [390, 130, 20, 140], 0)
    
    #ROW4
    pygame.draw.rect (screen, BLUE, [150, 305, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [390, 305, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [210, 370, 140, 20], 0)
    pygame.draw.rect (screen, BLUE, [270, 370, 20, 80], 0)
    #row5
    pygame.draw.rect (screen, BLUE, [50, 430, 60, 20], 0)
    pygame.draw.rect (screen, BLUE, [90, 430, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [150, 430, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [330, 430, 80, 20], 0)
    pygame.draw.rect (screen, BLUE, [450, 430, 60, 20], 0)
    pygame.draw.rect (screen, BLUE, [450, 430, 20, 80], 0)
    #row6
    pygame.draw.rect (screen, BLUE, [150, 490, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [50, 570, 180, 20], 0)
    pygame.draw.rect (screen, BLUE, [210, 490, 140, 20], 0)
    pygame.draw.rect (screen, BLUE, [270, 490, 20, 80], 0)
    
    pygame.draw.rect (screen, BLUE, [390, 490, 20, 80], 0)
    pygame.draw.rect (screen, BLUE, [330, 570, 180, 20], 0)
    
    pygame.draw.rect (screen, BLUE, [0, 510, 50, 20], 0)
    pygame.draw.rect (screen, BLUE, [510, 510, 50, 20], 0)
    pygame.draw.rect (screen, BLUE, [0, 610, 560, 10], 0)

    x = 25
    y = 25
    for i in range (0, 12):
        pygame.draw.rect (screen, WHITE, [x, y, 5, 5], 0)
        x = x + 20
    

def sprite_move():
	run = True
	while run:
		

	        for event in pygame.event.get():
        	        if event.type == pygame.QUIT:
        	                run = False
		
		keys = pygame.key.get_pressed()
		global PACMAN_X
		global PACMAN_Y

		if keys[pygame.K_LEFT]:
			PACMAN_X -= PACMAN_VEL
			if PACMAN_X<0:
				PACMAN_X = WIDTH-PACMAN_WIDTH

		if keys[pygame.K_RIGHT]:
			PACMAN_X += PACMAN_VEL
			if PACMAN_X > WIDTH-PACMAN_WIDTH:
				PACMAN_X = 0

		if keys[pygame.K_UP] and PACMAN_Y>0:
			PACMAN_Y -= PACMAN_VEL

		if keys[pygame.K_DOWN] and PACMAN_Y<HEIGHT-60:
			PACMAN_Y += PACMAN_VEL

		drawMap()
		pygame.draw.rect(screen, YELLOW, (PACMAN_X, PACMAN_Y, PACMAN_WIDTH, PACMAN_HEIGHT))
		pygame.display.update()
def main():
    drawMap()
    sprite_move()
    
    
inPlay = True
print "Hit ESC to end the program."
while inPlay: #Animation loop
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    main()

pygame.quit()
