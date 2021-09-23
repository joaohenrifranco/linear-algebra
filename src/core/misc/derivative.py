from .common import f


def solve(a, dX, c, method='forward'):
    if method == 'forward':
        return (f(a + dX, c) - f(a, c))/dX

    elif method == 'backward':
        return (f(a, c) - f(a - dX, c))/dX

    elif method == 'central':
        return (f(a + dX, c) - f(a - dX, c)) / (2 * dX)

    else:
        raise Exception(
            "Invalid method name. Choose forward, backward or central.")
