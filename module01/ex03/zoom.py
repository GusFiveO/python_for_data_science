from load_image import ft_load
import numpy as np
import cv2 as cv


def zoom(path: str):
	img = ft_load(path)
	print(img)
	zoomed_img = img[100:500, 450:850, :1]
	print(zoomed_img.shape)
	print(zoomed_img.shape)
	cv.imshow("zoomed", zoomed_img)
	cv.imshow("original", img)
	cv.waitKey(0)
	return None

if __name__ == "__main__":
	zoom("animal.jpeg")
