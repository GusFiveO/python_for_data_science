


def all_thing_is_obj(obj: any):
	object_type = type(obj)
	if isinstance(obj, list) == True:
		print(f"List : {object_type}")
	elif isinstance(obj, tuple) == True:
		print(f"Tuple : {object_type}")
	elif isinstance(obj, set) == True:
		print(f"Set : {object_type}")
	elif isinstance(obj, dict) == True:
		print(f"Dict : {object_type}")
	elif isinstance(obj, str) == True:
		print(f"Brian is in the kitchen : {object_type}")
	else:
		print("Type not found")
	return 42

