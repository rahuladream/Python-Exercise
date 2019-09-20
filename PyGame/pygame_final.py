import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
	K_q
	)


# Define the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

	# Define a player object by extending pygame.sprite.Sprite
	# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.Surface((75, 75))
		self.surf.fill((255,255,255))
		self.rect = self.surf.get_rect()

# Initialize the pygame
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Inititate player
player = Player()

# Variable a keep the main loop running
running = True

# Main loop
while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		# Did the user click the window close button, if so stop
		elif event.type == QUIT:
			running = False

	# GIve the surface a color to seprate it from background
	screen.fill((0,0,0))

	# Draw surf onto the screen at the center
	screen.blit(player.surf, (SCREEN_WIDTH/2 , SCREEN_HEIGHT/2))
	pygame.display.flip()

