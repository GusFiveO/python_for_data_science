import sys

NESTED_MORSE = {
	'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
	}

def main(arg):
	for char in arg:
		if char.upper() not in NESTED_MORSE.keys():
			print(char.upper())
			return print("AssertionError: the arguments are bad")
	print(arg)

	
	

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("AssertionError: the arguments are bad")
	else:
		main(sys.argv[1])
