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

            # Wait for a key event (1 ms)
            key = cv.waitKey(1)

            # Check if the window is still open
            if cv.getWindowProperty('zoomed', cv.WND_PROP_VISIBLE) < 1:
                print("Window closed")
                break

            # Check if the 'esc' key was pressed (27 is the ASCII value for 'esc')
            if key == 27:
                print("ESC key pressed")
                break
    except Exception:
        print("The image content is not the same as expected")
    return None


if __name__ == "__main__":
    zoom("animal.jpeg")
