from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import cv2 as cv

array = ft_load("landscape.jpg")
invert = ft_invert(array)
red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
grey = ft_grey(array)
print(ft_invert.__doc__)

cv.imshow("invert", invert)
cv.waitKey(0)
cv.destroyWindow("invert")
cv.imshow("red", red)
cv.waitKey(0)
cv.destroyWindow("red")
cv.imshow("green", green)
cv.waitKey(0)
cv.destroyWindow("green")
cv.imshow("blue", blue)
cv.waitKey(0)
cv.destroyWindow("blue")
cv.imshow("grey", grey)
cv.waitKey(0)
cv.destroyWindow("grey")
cv.imshow("original", array)
cv.waitKey(0)
cv.destroyWindow("original")
