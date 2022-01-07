import pygame
from player import Player
from comet_event import CometFallEvent
from monster import Mummy
from monster import Monster

# Creating the class for the game
class Game:

	def __init__(self):
		# Checking if our game has been started or not
		self.is_playing = False
		# Generate our player
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		# Generate the event
		self.comet_event = CometFallEvent(self)
		# Monster Group
		self.all_monsters = pygame.sprite.Group()
		self.pressed = {}

	def start(self):
		self.is_playing = True
		# Spawning the monsters
		self.spawn_monster(Mummy)
		self.spawn_monster(Mummy)


	def game_over(self):
		# Restarting the game
		self.all_monsters = pygame.sprite.Group()
		self.comet_event.all_comets = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.reset_percent()
		self.is_playing = False

	def update(self, screen):
		# Showing the player on the screen
		screen.blit(self.player.image, self.player.rect)

		# Refreshing the player's health bar
		self.player.update_health_bar(screen)

		# Refreshing the game event bar
		self.comet_event.update_bar(screen)

		# Refreshing the player's animation
		self.player.update_animation()

		# Collecting the player's projectile
		for projectile in self.player.all_projectiles:
			projectile.move()

		# Collecting the monsters
		for monster in self.all_monsters:
			monster.forward()
			monster.update_health_bar(screen)
			monster.update_animation()

		# Collecting the comets of our game
		for comet in self.comet_event.all_comets:
			comet.fall()

		# Apply the group of images to the projectiles
		self.player.all_projectiles.draw(screen)

		# Apply all images to the Monster Group
		self.all_monsters.draw(screen)

		# Apply all images of the Comet Group
		self.comet_event.all_comets.draw(screen)


		# Checking if the player wants to move right or left
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 920:
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -40:
			self.player.move_left()


	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


	def spawn_monster(self, monster_class_name):
		self.all_monsters.add(monster_class_name.__call__(self))