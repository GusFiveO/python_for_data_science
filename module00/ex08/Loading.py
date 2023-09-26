from time import sleep
from tqdm import tqdm
import sys
import os

def ft_tqdm(lst):
    total = len(lst)
    term_size = os.get_terminal_size()
    bar_length = term_size.columns - 8
    for i, item in enumerate(lst):
        yield item
        progress = (i + 1) / total
        filled_length = int(bar_length * progress)
        bar = '=' * filled_length + '>' + '-' * (bar_length - filled_length)
        percentage = f'{int(progress * 100):3}%'
        sys.stdout.write(f'\r{percentage} [{bar}]')
        sys.stdout.flush()
    
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
	"""main"""
	for i in ft_tqdm(range(133)):
		sleep(0.01)

if __name__ == "__main__":
	main()
