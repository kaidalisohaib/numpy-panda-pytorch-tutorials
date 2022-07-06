import numpy as np


# Mastering Shape
def mastering_shape():
    temperatures = np.array(
        [29.3, 42.1, 18.8, 16.1, 38.0, 12.5, 12.6, 49.9, 38.6, 31.3, 9.2, 22.2]
    ).reshape(2, 2, 3)
    print(temperatures)
    print(temperatures.shape)

    temperatures = temperatures.swapaxes(1, 2)
    print(temperatures)
    print(temperatures.shape)


if __name__ == "__main__":
    mastering_shape()
