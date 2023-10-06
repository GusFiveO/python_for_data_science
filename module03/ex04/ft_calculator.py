class calculator:
	"""calculator class"""

	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		"""dotproduct"""
		ret = 0
		for elem1, elem2 in zip(V1, V2):
			ret += elem1 * elem2
		print(f"Dot product is: {ret}")

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		"""add_vec method"""
		ret = []
		for elem1, elem2 in zip(V1, V2):
			ret.append(float(elem1 + elem2))
		print(f"Add vector is: {ret}")

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		"""sous_vec method"""
		ret = []
		for elem1, elem2 in zip(V1, V2):
			ret.append(float(elem1 - elem2))
		print(f"Sous vector is: {ret}")
