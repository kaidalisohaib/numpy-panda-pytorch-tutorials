import numpy as np


# Mastering Shape
def mastering_shape():
    print("Mastering Shape".center(30, "="))

    temperatures = np.array(
        [29.3, 42.1, 18.8, 16.1, 38.0, 12.5, 12.6, 49.9, 38.6, 31.3, 9.2, 22.2]
    ).reshape(2, 2, 3)
    print(temperatures)
    print(temperatures.shape)

    temperatures = temperatures.swapaxes(1, 2)
    print(temperatures)
    print(temperatures.shape)


# Understanding Axes
def understanding_axes():
    print("Understanding Axes".center(30, "="))
    table = np.array(
        [
            [5, 3, 7, 1],
            [2, 6, 7, 9],
            [1, 1, 1, 1],
            [4, 3, 2, 0],
        ]
    )
    print(table.max())
    print(table.max(axis=0))
    print(table.max(axis=1))
    # So, axis 0 is like Y and axis 1 is like X in a 2d coordinate system


if __name__ == "__main__":
    mastering_shape()
    understanding_axes()
