from load_image import ft_load
import cv2 as cv


def zoom(path: str):
    """Zoom in an image"""
    img = ft_load(path)
    if img is None:
        return None
    print(img)
    try:
        zoomed_img = img[100:500, 450:850, :1]
        print(f"New shape after slicing is: { zoomed_img.shape} or \
               {zoomed_img.shape[:-1]}")
        print(zoomed_img)
        cv.imshow("zoomed", zoomed_img)
        # cv.imshow("original", img)
        while True:

            key = cv.waitKey(1)

            if cv.getWindowProperty('zoomed', cv.WND_PROP_VISIBLE) < 1:
                print("Window closed")
                break

            if key == 27:
                print("ESC key pressed")
                break
    except Exception:
        print("The image content is not the same as expected")
    return None


if __name__ == "__main__":
    zoom("animal.jpeg")
