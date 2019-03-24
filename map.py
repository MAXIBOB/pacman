import pygame, sys, random, time
from pygame.locals import *
pygame.init()

WIDTH = 560
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")


PACMAN_X = 25
PACMAN_Y = 25
PACMAN_WIDTH = 20
PACMAN_HEIGHT = 20
PACMAN_VEL = 1

YELLOW = (255,255,153)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BORDER_COLOR = (0, 128, 248, 255)

image = pygame.image.load('template.png').convert()
image = pygame.transform.scale(image, (560, 620))

def drawMap():
    screen.blit(image, [0,0])
    

    x = 35
    y = 35
    for i in range (0, 12):
        pygame.draw.rect (screen, WHITE, [x, y, 5, 5], 0)
        x = x + 20
def detectCollide():
	if tuple(screen.get_at((PACMAN_X, PACMAN_Y))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH, PACMAN_Y+PACMAN_HEIGHT))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH, PACMAN_Y))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X, PACMAN_Y+PACMAN_HEIGHT))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH/2, PACMAN_Y))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X, PACMAN_Y+PACMAN_HEIGHT/2))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X + PACMAN_WIDTH, PACMAN_Y+PACMAN_HEIGHT/2))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH/2, PACMAN_Y+PACMAN_HEIGHT))) == BORDER_COLOR: 
		return True
	else:
		return False


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
			if detectCollide():
				PACMAN_X += PACMAN_VEL
			time.sleep(0.002)

		if keys[pygame.K_RIGHT]:
			PACMAN_X += PACMAN_VEL
			if PACMAN_X > WIDTH-PACMAN_WIDTH:
				PACMAN_X = 0
			if detectCollide():
				PACMAN_X -= PACMAN_VEL
			time.sleep(0.002)

		if keys[pygame.K_UP] and PACMAN_Y>0:
			PACMAN_Y -= PACMAN_VEL
			if detectCollide():
				PACMAN_Y += PACMAN_VEL
			time.sleep(0.002)

		if keys[pygame.K_DOWN] and PACMAN_Y<HEIGHT:
			PACMAN_Y += PACMAN_VEL
			if detectCollide():
				PACMAN_Y -= PACMAN_VEL
			time.sleep(0.002)

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
