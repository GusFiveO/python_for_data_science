def callLimit(limit: int):
	"""call Limit function"""
	count = 0
	def callLimiter(function):
		"""callLimiter function"""
		def limit_function(*args: any, **kwargs: any):
			"""limit function"""
			nonlocal count
			if count != limit:
				count += 1
				return function(*args, **kwargs)
			else:
				print(f"Error: {function} call too many times")
		return limit_function
	return callLimiter

