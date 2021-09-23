from os import EX_CANTCREAT
from common import f


def derivative(a, dX, c, method='foward'):
    if method == 'foward':
        return (f(a + dX, c) - f(a, c))/dX
    
    elif method == 'backward':
        return (f(a, c) - f(a - dX, c))/dX
    
    elif method == 'central':
        return (f(a + dX, c) - f(a - dX, c)) / (2 * dX)

    else:
        raise Exception("Invalid method name. Choose foward, backward or central.")