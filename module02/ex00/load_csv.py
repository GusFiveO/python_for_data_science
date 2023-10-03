import polars

def load(path: str):
	"""load a csv file"""
	csv = {}
	try:
		csv = polars.read_csv(path)
		print(type(csv))
	except FileNotFoundError as error:
		print(error)
		return None
	return csv
