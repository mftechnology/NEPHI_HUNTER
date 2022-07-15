import pyray
from constants import *
from nephi_hunter.game.casting.actor import Actor


class Arrow(Actor):
	"""
	class Arrow(pygame.sprite.Sprite):
		def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(ARROW_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

		def update(self):
		self.rect.y -= 5
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, animal_group, True):
			self.kill()
			animal_sound.play()
	"""
	def __init__(self):
		super().__init__()

		self.image = pyray.image.load(ARROW_IMAGE)


	
	