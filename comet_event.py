import pygame
from comet import Comet

# Create a class to handle this event
class CometFallEvent:
	
	# While loading -> Create a counter
	def __init__(self, game):
		self.percent = 0
		self.percent_speed = 3
		self.game = game
		self.fall_mode = False

		# Define a group of sprites to stock comets
		self.all_comets = pygame.sprite.Group()

	def add_percent(self):
		self.percent += self.percent_speed / 100

	def is_full_loaded(self):
		return self.percent >= 100

	def reset_percent(self):
		self.percent = 0

	def meteor_fall(self):
		# Loop for the numbers between 1 and 10
		for i in range(1, 10):
			# Appear the first ball of fire
			self.all_comets.add(Comet(self))

	def attempt_fall(self):
		# The game gauge is fully charged
		if self.is_full_loaded() and len(self.game.all_monsters) == 0:
			self.meteor_fall()
			self.fall_mode = True # Activate the event


	def update_bar(self, surface):

		# Add pourcentage to the bar
		self.add_percent()

		# Black Bar (In the background)
		pygame.draw.rect(surface, (0, 0, 0), [
			0, # The x-axis
			surface.get_height() - 20, # The y-axis
			surface.get_width(), # The height of the window
			10 # Thickness
		])
		# Red Bar (In the Foreground)
		pygame.draw.rect(surface, (255, 12, 0), [
			0, # The x-axis
			surface.get_height() - 20, # The y-axis
			(surface.get_width() / 100) * self.percent, # The height of the window
			10 # Thickness
		])