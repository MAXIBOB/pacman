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

xCoordinates = [40, 67, 99, 131, 162, 190, 227, 259, 275, 305, 335, 365, 395, 425, 455, 485]
yCoordinates = [40, 75, 115, 142, 170, 200, 235, 285, 345, 405, 432, 460, 490, 520, 548]

dotScores = []
for i in range(0, len(xCoordinates)):
    dotScores.append([])
    for j in range(0, len(yCoordinates)):
        dotScores[i].append(True)
            

YELLOW = (255,255,153)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BORDER_COLOR = (0, 128, 248, 255)

image = pygame.image.load("template.png").convert()
image = pygame.transform.scale(image, (560, 620))

def drawMap():
    screen.blit(image, [0,0])
    for i in range(0, len(xCoordinates)):
        for j in range(0, len(yCoordinates)):
            if dotScores[i][j] == True:
                pygame.draw.rect (screen, WHITE, [xCoordinates[i], yCoordinates[j], 5, 5], 0)
            else:
                pygame.draw.rect (screen, BLACK, [xCoordinates[i], yCoordinates[j], 5, 5], 0)
    #print dotScores

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
			
			if detectCollide():
				PACMAN_X += PACMAN_VEL
			time.sleep(0.002)

		if keys[pygame.K_RIGHT]:
			PACMAN_X += PACMAN_VEL
			
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
        print PACMAN_X, PACMAN_Y
        for i in range(0, len(xCoordinates)):
            for j in range(0, len(yCoordinates)):
                if (PACMAN_X == xCoordinates[i] and PACMAN_Y == yCoordinates[j]) or (PACMAN_X+5== xCoordinates[i] and PACMAN_Y == yCoordinates[j]) or (PACMAN_X-5 == xCoordinates[i] and PACMAN_Y == yCoordinates[j]) or (PACMAN_X == xCoordinates[i] and PACMAN_Y+5 == yCoordinates[j]) or (PACMAN_X == xCoordinates[i] and PACMAN_Y-5 == yCoordinates[j]):
                    dotScores[i][j] = False
        drawMap()
        pygame.display.update()
def drawPacman():
    pygame.draw.rect(screen, YELLOW, (PACMAN_X, PACMAN_Y, PACMAN_WIDTH, PACMAN_HEIGHT))

def main():
    drawMap()
    drawPacman()
    #sprite_move()
    

 
inPlay = True
print "Hit ESC to end the program."
while inPlay: #Animation loop
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    
    if keys[pygame.K_LEFT]:
		PACMAN_X -= PACMAN_VEL
		if detectCollide():
			PACMAN_X += PACMAN_VEL
			time.sleep(0.002)

    if keys[pygame.K_RIGHT]:
		PACMAN_X += PACMAN_VEL
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
    drawPacman()
    pygame.display.update()
    print PACMAN_X, PACMAN_Y
    for i in range(0, len(xCoordinates)):
        for j in range(0, len(yCoordinates)):
            if PACMAN_X >= xCoordinates[i]-15 and PACMAN_X <= xCoordinates[i]+15:
                if PACMAN_Y >= yCoordinates[j]-15 and PACMAN_Y <= yCoordinates[j]+15:
                    dotScores[i][j] = False
    
    main()

pygame.quit()