import pygame, sys, random, time
from pygame.locals import *
pygame.init()

WIDTH = 560
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")


PACMAN_X = WIDTH/2-5
PACMAN_Y = 63
PACMAN_WIDTH = 20
PACMAN_HEIGHT = 20
PACMAN_VEL = 2

GHOST_WIDTH = 20
GHOST_HEIGHT = 20
GHOST1_X = 25
GHOST1_Y = 25
GHOST2_X = 520
GHOST2_Y = 25
GHOST3_X = 520
GHOST3_Y = 580
GHOST4_X = 25
GHOST4_Y = 580
GHOST_VEL = 1
GHOST_UP = True
GHOST_TURN = True
ALIVE = True

YELLOW = (255,255,153)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BORDER_COLOR = (0, 128, 248, 255)
GHOST_COLOR = (42, 191, 242, 255)

image = pygame.image.load('template.png').convert()
image = pygame.transform.scale(image, (560, 620))

class Ghosts(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, vel):
        super(Ghosts, self).__init__()

	self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = vel
        self.image = pygame.image.load('ghost.png').convert_alpha()
        self.image =  pygame.transform.scale(self.image, (self.width, self.height))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def wallStop(self):
	if tuple(screen.get_at((self.x, self.y))) == BORDER_COLOR or tuple(screen.get_at((self.x+self.width, self.y+self.height))) == BORDER_COLOR or tuple(screen.get_at((self.x+self.width, self.y))) == BORDER_COLOR or tuple(screen.get_at((self.x, self.y+self.height))) == BORDER_COLOR or tuple(screen.get_at((self.x+self.width/2, self.y))) == BORDER_COLOR or tuple(screen.get_at((self.x, self.y+self.height/2))) == BORDER_COLOR or tuple(screen.get_at((self.x+self.width/2, self.y+self.height))) == BORDER_COLOR or tuple(screen.get_at((self.x+self.width, self.y+self.height/2))) == BORDER_COLOR:
            return True
        else:
            return False

    def move(self):
	global GHOST_UP
        global GHOST_TURN
	if self.x<PACMAN_X:
            self.x += self.vel
            if self.wallStop():
	        self.x -= self.vel
            time.sleep(0.002)
        else:
	    self.x -= self.vel
            if self.wallStop():
	        self.x += self.vel
	    time.sleep(0.002)
        if self.y<PACMAN_Y:
	    self.y += self.vel
            if self.wallStop():
		self.y -= self.vel
            time.sleep(0.002)
	else:
	    self.y -= self.vel
	    if self.wallStop():
	        self.y += self.vel
	    time.sleep(0.002)

ghost1 = Ghosts(GHOST_WIDTH, GHOST_HEIGHT, GHOST1_X, GHOST1_Y, GHOST_VEL)
ghost2 = Ghosts(GHOST_WIDTH, GHOST_HEIGHT, GHOST2_X, GHOST2_Y, GHOST_VEL)
ghost3 = Ghosts(GHOST_WIDTH, GHOST_HEIGHT, GHOST3_X, GHOST3_Y, GHOST_VEL)
ghost4 = Ghosts(GHOST_WIDTH, GHOST_HEIGHT, GHOST4_X, GHOST4_Y, GHOST_VEL)


def drawMap():
    screen.blit(image, [0,0])
    

    x = 35
    y = 35
    for i in range (0, 12):
        pygame.draw.rect (screen, WHITE, [x, y, 5, 5], 0)
        x = x + 20
    screen.blit (ghost1.image, [ghost1.x, ghost1.y])
    screen.blit (ghost2.image, [ghost2.x, ghost2.y])
    screen.blit (ghost3.image, [ghost3.x, ghost3.y])
    screen.blit (ghost4.image, [ghost4.x, ghost4.y])
def detectCollide():
	if tuple(screen.get_at((PACMAN_X, PACMAN_Y))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH, PACMAN_Y+PACMAN_HEIGHT))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH, PACMAN_Y))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X, PACMAN_Y+PACMAN_HEIGHT))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH/2, PACMAN_Y))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X, PACMAN_Y+PACMAN_HEIGHT/2))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X + PACMAN_WIDTH, PACMAN_Y+PACMAN_HEIGHT/2))) == BORDER_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH/2, PACMAN_Y+PACMAN_HEIGHT))) == BORDER_COLOR: 
		return True
	else:
		return False

def ghostCollide():
	global ALIVE
	if tuple(screen.get_at((PACMAN_X, PACMAN_Y))) == GHOST_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH, PACMAN_Y+PACMAN_HEIGHT))) == GHOST_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH, PACMAN_Y))) == GHOST_COLOR or tuple(screen.get_at((PACMAN_X, PACMAN_Y+PACMAN_HEIGHT))) == GHOST_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH/2, PACMAN_Y))) == GHOST_COLOR or tuple(screen.get_at((PACMAN_X, PACMAN_Y+PACMAN_HEIGHT/2))) == GHOST_COLOR or tuple(screen.get_at((PACMAN_X + PACMAN_WIDTH, PACMAN_Y+PACMAN_HEIGHT/2))) == GHOST_COLOR or tuple(screen.get_at((PACMAN_X+PACMAN_WIDTH/2, PACMAN_Y+PACMAN_HEIGHT))) == GHOST_COLOR: 
		ALIVE = False
		
	else:
		ALIVE = True

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
			time.sleep(0.0006)

		if keys[pygame.K_RIGHT]:
			PACMAN_X += PACMAN_VEL
			
			if detectCollide():
				PACMAN_X -= PACMAN_VEL
			time.sleep(0.0006)

		if keys[pygame.K_UP] and PACMAN_Y>0:
			PACMAN_Y -= PACMAN_VEL
			if detectCollide():
				PACMAN_Y += PACMAN_VEL
			time.sleep(0.0006)

		if keys[pygame.K_DOWN] and PACMAN_Y<HEIGHT:
			PACMAN_Y += PACMAN_VEL
			if detectCollide():
				PACMAN_Y -= PACMAN_VEL
			time.sleep(0.0006)
		if ALIVE:

			ghost4.move()
			ghost3.move()
			ghost2.move()
			ghost1.move()
			ghostCollide()
			drawMap()
			pygame.draw.rect(screen, YELLOW, (PACMAN_X, PACMAN_Y, PACMAN_WIDTH, PACMAN_HEIGHT))
			pygame.display.update()
		else:
			pygame.quit()
		
def main():
    if ALIVE == True:
        drawMap()
        sprite_move()
    else:
	pygame.quit()

print "Hit ESC to end the program."
while ALIVE: #Animation loop
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        ALIVE = False
    main()

pygame.quit()
