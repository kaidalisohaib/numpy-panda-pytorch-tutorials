from decimal import getcontext
from math import e, factorial

import numpy as np

fac = np.vectorize(factorial)


def e_x(x, terms=10):
    """Approximates e^x using a given number of terms of the Maclaurin series"""

    n = np.arange(terms)
    return np.sum((x**n) / fac(n))


if __name__ == "__main__":
    getcontext().prec = 15
    num = 3
    iterations = 13
    actualMaclaurin = e**num
    print("Actual:", actualMaclaurin)
    print("N (terms)".ljust(10), "Maclaurin".rjust(10), "Error".rjust(10), sep="│")
    for n in range(iterations):
        calculatedMaclaurin = e_x(num, terms=n + 1)
        print(
            f"{n+1}".ljust(10),
            f"{calculatedMaclaurin:.3f}".rjust(10),
            f"{actualMaclaurin - calculatedMaclaurin:.3f}".rjust(10),
            sep="│",
        )
