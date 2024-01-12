from load_image import ft_load
import numpy as np
import cv2 as cv


def rotate_array(array):
    """rotate an array"""
    rows, cols = array.shape[:2]
    print(array.shape)

    twisted_array = np.zeros((rows, cols, 1), dtype=np.uint8)
    for y in range(rows):
        for x in range(cols):
            # rotated_array[rows - x - 1, y] = array[y, x]
            twisted_array[y, cols - x - 1] = array[y, x]
    rotated_array = np.zeros((cols, rows, 1), dtype=np.uint8)
    for y in range(rows):
        for x in range(cols):
            rotated_array[rows - x - 1, y] = twisted_array[y, x]
    return rotated_array


def rotate(path: str):
    """display rotated image"""
    img = ft_load(path)
    if img is None:
        return None
    try:
        cropped_img = img[100:500, 450:850, 2:]
        rotated_img = rotate_array(cropped_img)
        print(f"New shape after Transpose: {rotated_img.shape}")
        print(rotated_img)
        # cv.imshow("zoomed", cropped_img)
        # cv.imshow("original", img)
        cv.imshow("rotated", rotated_img)
        while True:

            key = cv.waitKey(1)

            if cv.getWindowProperty('rotated', cv.WND_PROP_VISIBLE) < 1:
                print("Window closed")
                break

            if key == 27:
                print("ESC key pressed")
                break
    except Exception:
        print("The image content is not the same as expected")
    return None


if __name__ == "__main__":
    rotate("animal.jpeg")
