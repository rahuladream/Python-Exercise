"""
We are learning today
1. Draw items on your screen
2. Play sound effects and music
3. Handle user input
4. Implenent event loops
5. Programming from standard procedural python programming
"""

# Initialize pygame library
import pygame
import keyboard
pygame.init()

# setup screen drawing window
screen = pygame.display.set_mode([500, 500])

# Breaking point game
running = True
while running:
	# Didthe user click the window close button?
	for event in pygame.event.get():
		if keyboard.is_pressed('q'):
			running = False
		elif event.type == pygame.QUIT:
			running = False


	# Fill the background
	screen.fill((255, 255, 255))

	# Draw solid blue screen
	pygame.draw.circle(screen, (0,0,255), (250, 250), 75)

	# Fill the display
	pygame.display.flip()

pygame.quit()