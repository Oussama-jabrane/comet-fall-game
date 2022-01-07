import pygame
import random
import animation


# Create a class who'll manage the monster in our game
class Monster(animation.AnimateSprite):

	def __init__(self, game, name):
		super().__init__(name)
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 0.1
		self.rect = self.image.get_rect()
		self.rect.x = 1000 + random.randint(0, 300)
		self.rect.y = 530
		self.velocity = random.randint(1, 2)
		self.start_animation()

	def damage(self, amount):
		# Damaging the monster
		self.health -= amount

		# Verify if the new number of health points is greater than 0
		if self.health <= 0:
			# Appear as a new monster
			self.rect.x = 1000 + random.randint(0, 400)
			self.velocity = random.randint(1, 2)
			self.health = self.max_health

			# If the event bar is maximumly charged
			if self.game.comet_event.is_full_loaded():
				# Remove from game
				self.game.all_monsters.remove(self)

				# Calling the method to try to launch the comettes rain
				self.game.comet_event.attempt_fall()

	def update_animation(self):
		self.animate(loop=True)

	def update_health_bar(self, surface):
		# Drawing the health bar
		pygame.draw.rect(surface, (120,120,120), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
		pygame.draw.rect(surface, (52, 227, 34), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

	def forward(self):
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity

	# If the monster is in collision with the player
		else:
			# Damaging the player
			self.game.player.damage(self.attack)

# Defining a class for the mummy
class Mummy(Monster):

	def __init__(self, game):
		super().__init__(game, 'mummy')
		