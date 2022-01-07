import pygame

# Defining the class who'll handle the animations
class AnimateSprite(pygame.sprite.Sprite):

	# Defining the things to do for create the entity
	def __init__(self, sprite_name):
		super().__init__()
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.current_image = 0 # Start the animation at the image n°1
		self.images = animations.get(sprite_name)
		self.animation = False

	# Defining the method to start the animation
	def start_animation(self):
		self.animation = True

	# Defining a method to animate the sprite
	def animate(self, loop=False):

		# Verify if the animation if active
		if self.animation:

			# Move to the next image
			self.current_image += 1

			# Verify if we have reached the end of the animation
			if self.current_image >= len(self.images):
				# Reset the animation to the start point
				self.current_image = 0

				# Verify if the animation isn't in loop mode
				if loop is False:
					# Desactivate the animation
					self.animation = False

			# Modify the previous image by the next image
			self.image = self.images[self.current_image]

# Defining a function to charge the sprite's images
def load_animation_images(sprite_name):
	# Charging the 24 images of this sprite in the specified folder
	images = []
	# Collecting the folder route for this sprite
	path = f"assets/{sprite_name}/{sprite_name}"

	# Loop for every image in this folder
	for num in range(1, 24):
		image_path = path + str(num) + '.png'
		images.append(pygame.image.load(image_path))

	# Resend the content of the list of images
	return images


# Defining a dictionnary who'll host the images
# mummy -> [...mummy1.png, ...mummy2.png, ...]
# player -> [...player1.png, ...player2.png, ...]
animations = {
	'mummy': load_animation_images('mummy'),
	'player': load_animation_images('player')
}