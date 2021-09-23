import math


def f(x, constants):
    c1, c2, c3, c4 = constants

    return c1 * math.e**(c2 * x) + c3 * x**c4


def f_derivative(x, constants):
    c1, c2, c3, c4 = constants

    return c1 * c2 * math.e**(c2 * x) + c3 * c4 * x**(c4 - 1)
