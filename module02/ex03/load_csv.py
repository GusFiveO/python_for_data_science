import pandas

def load(path: str):
	"""load a csv file"""
	csv = {}
	try:
		csv = pandas.read_csv(path)
	except FileNotFoundError as error:
		print(error)
		return None
	return csv
