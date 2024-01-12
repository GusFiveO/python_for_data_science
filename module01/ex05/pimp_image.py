import cv2 as cv


def ft_invert(arr):
    """invert color of an image"""
    try:
        return 255 - arr
    except Exception:
        print(Exception)
        return None


def ft_red(arr):
    """only keep red pixels of an image"""
    try:
        red_arr = arr.copy()
        red_arr[:, :, 0] = 0
        red_arr[:, :, 1] = 0
        return red_arr
    except Exception:
        print(Exception)
        return None


def ft_green(arr):
    """only keep green pixels of an image"""
    try:
        green_arr = arr.copy()
        green_arr[:, :, 0] = 0
        green_arr[:, :, 2] = 0
        return green_arr
    except Exception:
        print(Exception)
        return None


def ft_blue(arr):
    """only keep blue pixels of an image"""
    try:
        blue_arr = arr.copy()
        blue_arr[:, :, 1] = 0
        blue_arr[:, :, 2] = 0
        return blue_arr
    except Exception:
        print(Exception)
        return None


def ft_grey(arr):
    """convert an image to grey scale"""
    try:
        blue_channel, green_channel, red_channel = cv.split(arr)

        gray_image = cv.addWeighted(blue_channel, 1/3, green_channel, 1/3, 0)
        gray_image = cv.addWeighted(gray_image, 1, red_channel, 1/3, 0)

        gray_image = gray_image.astype('uint8')

        gray_image = cv.merge([gray_image, gray_image, gray_image])

        return gray_image
    except Exception:
        print(Exception)
        return None
