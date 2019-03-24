import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2
pygame.init()

#CREATING SCREEN
WIDTH = 560
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")

#PACMAN GLOBAL VARIABLES
PACMAN_X = 25
PACMAN_Y = 25
PACMAN_WIDTH = 20
PACMAN_HEIGHT = 20
PACMAN_VEL = 1

#DOTS GLOBAL VARIABLES
xCoordinates = [37, 67, 97, 127, 157, 187, 217, 247, 277, 307, 337, 367, 397, 427, 457, 487, 517]
yCoordinates = [37, 67, 97, 127, 157, 187, 217, 247, 277, 307, 337, 367, 397, 427, 457, 487, 517, 547, 577]
dotScores = []
for i in range(0, len(xCoordinates)):
    dotScores.append([])
    for j in range(0, len(yCoordinates)):
        dotScores[i].append(True)
        
#COLOUR VARIABLES
YELLOW = (255,255,153)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BORDER_COLOR = (0, 128, 248, 255)

#IMAGE VARIABLES
maze = pygame.image.load("template.png").convert()
maze = pygame.transform.scale(maze, (560, 620))
logo = pygame.image.load("logo.png").convert()
logo2 = pygame.image.load("logo2.png").convert()
startButton = pygame.image.load("start.png").convert()
ghost1 = pygame.image.load("ghost1.png").convert()
ghost2 = pygame.image.load("ghost2.png").convert()
gameover2 = pygame.image.load("gameover2.jpg")

#SCREEN VARIABLES
currentScreen = 1

ghostP = Vector2(20,20)
ghostV = Vector2(8,0)
ghostTwoP = Vector2(450,20)
ghostTwoV = Vector2(8,0)



def changeScreen(currentScreen):
    # if currentScreen == 1:
    #     drawScreen1()
    # elif currentScreen == 2:
    #     drawMap()
    # else:
    drawScreen()

def drawScreen1():
    screen.fill (BLACK)
    screen.blit(logo, (0,25))
    screen.blit(logo2, (0,400))
    screen.blit(startButton, (50,200))

def drawMap():
    screen.blit(maze, [0,0])
    for i in range(0, len(xCoordinates)):
        for j in range(0, len(yCoordinates)):
            if dotScores[i][j] == True:
                pygame.draw.rect (screen, WHITE, [xCoordinates[i], yCoordinates[j], 5, 5], 0)
            else:
                pygame.draw.rect (screen, BLACK, [xCoordinates[i], yCoordinates[j], 5, 5], 0)

def ghostOne():
    screen.blit(ghost1, (ghostP.x, ghostP.y+50))
    if ghostP.x > screen.get_width()-130 or ghostP.x < 10:
        ghostV.x *= -1

def ghostTwo():
    screen.blit(ghost2, (ghostTwoP.x, ghostTwoP.y+430))
    if ghostTwoP.x > screen.get_width()-105 or ghostTwoP.x < 0:
        ghostTwoV.x *= -1


def drawScreen():
    screen.fill (BLACK)
    
    screen.blit(gameover2, (50, 165))


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

        for i in range(0, len(xCoordinates)):
            for j in range(0, len(yCoordinates)):
                if (PACMAN_X == xCoordinates[i] and PACMAN_Y == yCoordinates[j]) or (PACMAN_X+5== xCoordinates[i] and PACMAN_Y == yCoordinates[j]) or (PACMAN_X-5 == xCoordinates[i] and PACMAN_Y == yCoordinates[j]) or (PACMAN_X == xCoordinates[i] and PACMAN_Y+5 == yCoordinates[j]) or (PACMAN_X == xCoordinates[i] and PACMAN_Y-5 == yCoordinates[j]):
                    dotScores[i][j] = False
        pygame.display.update()
    
def main():
    drawMap()

inPlay = True
while inPlay:
    pygame.event.get()
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_RETURN]:
        if currentScreen == 1:
            currentScreen = 2
            changeScreen(2)
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

    changeScreen(currentScreen)
    if currentScreen == 2:
        pygame.draw.rect(screen, YELLOW, (PACMAN_X, PACMAN_Y, PACMAN_WIDTH, PACMAN_HEIGHT))
    drawScreen()
    ghostOne()
    ghostTwo()
    ghostP += ghostV
    ghostTwoP += ghostTwoV
    pygame.display.update()
    pygame.display.update()
    print PACMAN_X, PACMAN_Y
    for i in range(0, len(xCoordinates)):
        for j in range(0, len(yCoordinates)):
            if PACMAN_X >= xCoordinates[i]-15 and PACMAN_X <= xCoordinates[i]+15:
                if PACMAN_Y >= yCoordinates[j]-15 and PACMAN_Y <= yCoordinates[j]+15:
                    dotScores[i][j] = False
                    
    
    main()

pygame.quit()
