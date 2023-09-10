import sys
import string as str

def print_lower_case_count(string: str):
	"""print lower case count in a string"""
	lower_case_count = sum(1 for c in string if c.islower())
	print(f"{lower_case_count} lower letters")

def print_upper_case_count(string: str):
	"""print upper case count in a string"""
	upper_case_count = sum(1 for c in string if c.isupper())
	print(f"{upper_case_count} upper letters")

def print_punctuation_count(string: str):
	"""print punctuation count in a string"""
	ponctuation_count = sum(1 for c in string if c in str.punctuation)
	print(f"{ponctuation_count} punctuation marks")

def print_space_count(string: str):
	"""print space count in a string"""
	space_count = sum(1 for c in string if c.isspace() or c == '\n')
	print(f"{space_count} spaces")

def print_digit_count(string: str):
	"""print digit count in a string"""
	digit_count = sum(1 for c in string if c.isdigit())
	print(f"{digit_count} digits")

def main(args : str):
	"""main function"""
	arg = ""
	if (len(args) == 1):
		arg = input("What is the text to count?\n")
	else:
		arg = args[1]

	print(f"The text contain {len(arg)} characters:")

	print_upper_case_count(arg)
	print_lower_case_count(arg)
	print_punctuation_count(arg)
	print_space_count(arg)
	print_digit_count(arg)
	

if __name__ == "__main__":
	main(sys.argv)
