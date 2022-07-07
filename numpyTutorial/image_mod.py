import matplotlib.image as mpimg
import numpy as np

img: np.ndarray = mpimg.imread("kitty.jpg")
print(type(img))
print(img.shape)


def multi_color():
    output: np.ndarray = img.copy()
    # Removing Green and Blue from the first third of the image
    output[:, : int(img.shape[1] / 3), 1:] = 0
    # Removing Red and Blue between the first third and last third of the image
    output[:, int(img.shape[1] / 3) : int(2 * img.shape[1] / 3), ::2] = 0
    # Removing Red and Green from the last third of the image
    output[:, int(2 * img.shape[1] / 3) :, :2] = 0
    mpimg.imsave("multicolor.jpg", output)


def bad_gray_scale():
    average = img.mean(axis=2)
    mpimg.imsave("bad-gray.jpg", average, cmap="gray")


def good_gray_scale():
    weights = np.array([0.3, 0.59, 0.11])
    grayscale = img @ weights
    mpimg.imsave("good-gray.jpg", grayscale, cmap="gray")


if __name__ == "__main__":
    multi_color()
    bad_gray_scale()
    good_gray_scale()
