import numpy as np
import cv2 as cv


def ft_load(path: str) -> np.array:
    """load an image, print its format and it pixels content in RGB format"""
    try:
        img = cv.imread(path)
        if img is None:
            print("Filepath gived as parameter is not valid")
            return None
        print(f"The shape of this image is: {img.shape}")
        return img
    except Exception:
        print("The image path must be valid")
