from . import derivative


def solve(dX1, dX2, c):
    d1 = derivative.solve(1, dX1, c, 'backward')
    d2 = derivative.solve(1, dX2, c, 'backward')
    q = dX1/dX2

    return d1 + (d1 - d2) / (q**-1 - 1)
