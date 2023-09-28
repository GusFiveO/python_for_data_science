from load_image import ft_load
import numpy as np
import cv2 as cv

def rotate_array(array):
	"""rotate an array"""
	rows, cols = array.shape[:2]
	print(array.shape)

	rotated_array = np.zeros((cols, rows, 1), dtype=np.uint8)
	print(rotated_array)
	print(rotated_array.shape)
	for y in range(rows):
		for x in range(cols):
			#print(rows, cols, rows - x - 1, y, x)
			rotated_array[cols - x - 1, y] = array[y, x]
	return rotated_array


def rotate(path: str):
	"""display rotated image"""
	img = ft_load(path)

	cropped_img = img[100:500, 450:850, 2:]
	rotated_img = rotate_array(cropped_img)

	cv.imshow("zoomed", cropped_img)
	cv.imshow("rotated", rotated_img)
	cv.imshow("original", img)
	cv.waitKey(0)
	return None

if __name__ == "__main__":
	rotate("animal.jpeg")
