from S1E9 import Character

class Baratheon(Character):
	"""Baratheon class"""
	
	def __init__(self, first_name: str, is_alive: bool = True):
		"""__init__ method"""
		self.first_name = first_name
		self.is_alive = is_alive
		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "dark"

	def __str__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def die(self):
		"""die method"""
		if self.is_alive:
			self.is_alive = False

class Lannister(Character):
	"""Lannister Class"""

	def __init__(self, first_name: str, is_alive: bool = True):
		"""__init__ method"""
		self.first_name = first_name
		self.is_alive = is_alive
		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"

	def __str__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def create_lannister(first_name: str, is_alive: bool):
		"""create a lannister"""
		return Lannister(first_name, is_alive)

	def die(self):
		"""die method"""
		if self.is_alive:
			self.is_alive = False
