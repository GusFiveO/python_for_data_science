import sys
from ft_filter import ft_filter

def check_if_string_long_enough(string, number):
	"""check if a string is long enough"""
	if len(string) < number:
		return False
	return True

if __name__ == "__main__":
	if len(sys.argv) > 3:
		print("AssertionError: the arguments are bad")
	else:
		try:
			word_list = sys.argv[1].split()
			filtered_list = ft_filter(lambda string: len(string) > int(sys.argv[2]), word_list)
			print(filtered_list)
		except:
			print("AssertionError: the arguments are bad")
