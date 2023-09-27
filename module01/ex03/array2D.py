import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	"""slice_me"""
	if not isinstance(family, list):
		print("Parameter must be a list")
		return None
	np_family = np.array(family)
	new_family = np_family[start:end]
	print(f"My shape is : {np_family.shape}")
	print(f"My new shape is : {new_family.shape}")
	return new_family
