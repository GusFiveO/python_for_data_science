from abc import ABC, abstractmethod

class Character(ABC):
	"""Class Character"""
	def __init__(self, first_name: str, is_alive: bool = True):
		"""Constructor"""
		self.first_name = first_name
		self.is_alive = is_alive
	
	@abstractmethod
	def die(self):
		pass
		"""make the character die"""
		if self.is_alive:
			self.is_alive = False

class Stark(Character):
	"""Stark Class"""
	def __init(self):
		self
	def die(self):
		pass
		"""make Stark die"""
		if self.is_alive:
			self.is_alive = False

