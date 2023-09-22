from time import sleep
from tqdm import tqdm
import os

def ft_tqdm(lst: range) -> None:
	"""loading"""
	length = len(lst)
	term_width = os.get_terminal_size().columns
	for i in lst:
		if i == 0:
			progress = 0
		else:
			progress =  round(i / length * 100) + 1
		# 6 + len(range) * 2
		print(f"{progress:3}%|", end="")
		# progress_equal = '=' * round(i / length * term_width - 15)
		# progress_space = ' ' * (term_width -11 - round(i / length * term_width - 15))
		# print(progress_equal, progress_space, end="\r")
		# progress_space too long so retour a la ligne
		print(progress_equal, end="\r")
		yield i
	print()

def main():
	"""main"""
	for i in ft_tqdm(range(133)):
		sleep(0.05)

if __name__ == "__main__":
	main()
	# for i in tqdm(range(100)):
	# 	sleep(0.005)
	# for i in tqdm(range(333)):
	# 	sleep(0.005)
