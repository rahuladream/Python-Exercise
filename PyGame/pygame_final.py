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

# Initialize the game
pygame.init()

# Define the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

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

	# FIll the screen with color
	screen.fill((255,255,255))

	# Create surface and pass the tuple containing it's length and width
	surf = pygame.Surface((50, 50))

	# GIve the surface a color to seprate it from background
	surf.fill((0,0,0))
	rect = surf.get_rect()

	# Draw surf onto the screen at the center
	screen.blit(surf, (SCREEN_WIDTH/2 , SCREEN_HEIGHT/2))
	pygame.display.flip()

	# Put the center of surf at the center of the display
	surf_center = (
		(SCREEN_WIDTH - surf.get_width()) / 2,
		(SCREEN_HEIGHT - surf.get_height()) / 2
	)

	# Draw surf at the new coordinates
	screen.blit(surf, surf_center)
	pygame.display.flip()