import pygame
from projectile import Projectile
import random
import animation


# Creating the first class for the player
class Player(animation.AnimateSprite):

	def __init__(self, game):
		super().__init__("player")
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = random.randint(10, 30)
		self.velocity = 3
		self.all_projectiles = pygame.sprite.Group()
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 490

	def damage(self, amount):
		if self.health - amount > amount:
			self.health -= amount
		else:
			# Checking if the player doesn't have points anymore
			self.game.game_over()

	def update_animation(self):
		self.animate()

	def update_health_bar(self, surface):
		# Drawing the health bar
		pygame.draw.rect(surface, (120,120,120), [self.rect.x + 50, self.rect.y, self.max_health, 7])
		pygame.draw.rect(surface, (52, 227, 34), [self.rect.x + 50, self.rect.y, self.health, 7])

	def launch_projectile(self):
		# Create a new instance for the Projectile class
		self.all_projectiles.add(Projectile(self))
		# Start the animation
		self.start_animation()


	def move_right(self):
		# If the player is not colliding with a monster
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity