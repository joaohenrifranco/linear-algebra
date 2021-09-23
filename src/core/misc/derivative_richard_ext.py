import derivative


def solve(dX1, dX2, c):
    d1 = derivative(1, dX1, c, 'forward')
    d2 = derivative(1, dX2, c, 'forward')
    q = dX1/dX2

    return d1 + (d1 - d2) / (q**-1 - 1)
