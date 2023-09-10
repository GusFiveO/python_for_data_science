def NULL_not_found(obj: any) -> int:
	if obj is None:
		print(f"{obj}: <class 'NoneType'>")
	elif isinstance(obj, float) and str(obj) == 'nan':
		print(f"Cheese: {obj} <class 'float'>")
	elif obj == 0:
		print(f"Zero: {obj} <class 'int'>")
	elif obj == '':
		print(f"Empty: <class 'str'>")
	elif isinstance(obj, bool):
		print(f"Fake: {obj} <class 'bool'>")
	else:
		print("Type not Found")
		return 1
	return 0
