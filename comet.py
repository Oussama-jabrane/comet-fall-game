import pygame
import random

# Create the class to handle this comet
class Comet(pygame.sprite.Sprite):

	def __init__(self, comet_event):
		super().__init__()
		# define the image associated with this comet
		self.image = pygame.image.load('assets/comet.png')
		self.rect = self.image.get_rect()
		self.velocity = random.randint(1, 3)
		self.rect.x = random.randint(20, 800)
		self.comet_event = comet_event

	def remove(self):
		self.comet_event.all_comets.remove(self)

		# Verify if the number of comets is 0
		if len(self.comet_event.all_comets) == 0:
			print("The event is done")
			# Reset the bar at 0
			self.comet_event.reset_percent()
			# Showing the 2 first monsters
			self.comet_event.game.spawn_monster()

	def fall(self):
		self.rect.y += self.velocity

		# Doesn't fall on ground
		if self.rect.y >= 500:
			print('Ground')
			# Delete the Comet
			self.remove()

		# Verify if the comet touches the player
		if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
			print("Player Touched!!!")
			# Delete the comet
			self.remove()
			# Damage the player and lose 20 points
			self.comet_event.game.player.damage(20)