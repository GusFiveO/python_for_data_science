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
		print('=' * round(i / length * term_width - 15), end="\r")
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
