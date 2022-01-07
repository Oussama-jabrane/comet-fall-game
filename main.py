import pygame
import math
from game import Game
import time

pygame.init()


# Setting up the height and width of the window
HEIGHT = 1080
WIDTH = 680

# Generating the game window
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Importing the game background
background = pygame.image.load('assets/bg.jpg')

# Importing the banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Importing the button to start the game
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.9)


# Charging the game
game = Game()

# The game loop
running = True
while running:

	# Showing the background of our game
	screen.blit(background, (0,-220))

	# Verify if our game has been started or not
	if game.is_playing:
		# Trigger game instructions
		game.update(screen)
	# Verify if our game has not been started
	else:
		# Add welcome page
		screen.blit(play_button, play_button_rect)
		screen.blit(banner, banner_rect)

	# Refreshing the screen
	pygame.display.flip()

	# Checking if the player close the window
	for event in pygame.event.get(): 
		# Checking if the event is closing the window
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		# Detecting if the player release a key
		elif event.type == pygame.KEYDOWN:
			# Checking which key is pressed
			game.pressed[event.key] = True

			# Checking if the key is space to launch the projectile
			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()


		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			# Verify if the user clicks the "Play" button
			if play_button_rect.collidepoint(event.pos):
				# put the game in "launched" mode
				time.sleep(0.1)
				game.is_playing = True
				game.start()