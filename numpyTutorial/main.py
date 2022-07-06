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
    print("Max", table.max())
    print("Max axis 0", table.max(axis=0))
    print("Max axis 1", table.max(axis=1))
    # So, axis 0 is like Y and axis 1 is like X in a 2d coordinate system


# Broadcasting
def broadcasting():
    print("Broadcasting".center(30, "="))
    A = np.arange(32).reshape(4, 1, 8)
    print("A", A)

    B = np.arange(48).reshape(1, 6, 8)
    print("B", B)

    print("A+B", A + B)


# Indexing
def indexing():
    print("Indexing".center(30, "="))
    square = np.array([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]])

    for i in range(4):
        print(square[:, i], "\n")
        assert square[:, i].sum() == 34
        print(square[i, :], "\n\n")
        assert square[i, :].sum() == 34
    # [axis 0, ..., axis n]


# Masking and Filtering
def masking_and_filtering():
    print("Masking and Filtering".center(30, "="))
    numbers = np.linspace(start=1, stop=50, num=24, dtype=int).reshape(4, -1)
    print(numbers)
    mask = numbers % 4 == 0
    print(mask)
    print(numbers[mask])
    print(numbers[numbers % 4 == 0])
    # Can use binary [ &, | ] operators with masks


if __name__ == "__main__":
    mastering_shape()
    understanding_axes()
    broadcasting()
    indexing()
    masking_and_filtering()
