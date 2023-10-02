from load_image import ft_load
import numpy as np
import cv2 as cv

def ft_invert(arr):
	"""invert color of an image"""
	return 255 - arr

def ft_red(arr):
	"""only keep red pixels of an image"""
	red_arr = arr.copy()
	red_arr[:, :, 0] = 0
	red_arr[:, :, 1] = 0
	return red_arr

def ft_green(arr):
	"""only keep green pixels of an image"""
	green_arr = arr.copy()
	green_arr[:, :, 0] = 0
	green_arr[:, :, 2] = 0
	return green_arr

def ft_blue(arr):
	"""only keep blue pixels of an image"""
	blue_arr = arr.copy()
	blue_arr[:, :, 1] = 0
	blue_arr[:, :, 2] = 0
	return blue_arr

def ft_grey(arr):
	"""make an image become balck and white"""
	r_coeff = 0.2989
	g_coeff = 0.5870
	b_coeff = 0.1140
	array_copy = np.zeros_like(arr)
	for i in range(array_copy.shape[0]):
		for j in range(array_copy.shape[1]):
			pixel = arr[i, j]
			value = pixel[0] * r_coeff + pixel[1] * g_coeff + pixel[2] * b_coeff
			array_copy[i, j] = np.repeat(value, 3)
	return array_copy

