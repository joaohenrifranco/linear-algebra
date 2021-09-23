from common import f, f_derivative


def bissection(a, b, constants, tol):
    while(abs(b-a) > tol):
        x = (a+b) / 2
        if f(x, constants) > 0:
            b = x
        else:
            a = x
    return x


def newton(a, b, constants, tol):
    max_iterations = 1000
    x0 = (a+b) / 2

    for _ in range(max_iterations):
        x = x0 - f(x0, constants) / f_derivative(x0, constants)
        tolk = abs(x - x0)
        if tolk <= tol:
            return x
        x0 = x

    raise Exception('Conversion not reached.')

def solve(a, b, constants, tol, method):
    if method == 'newton':
        return newton(a, b, constants, tol)
    elif method == 'bissection':
        return bissection(a, b, constants, tol)
    else:
        raise Exception('Invalid method name. Choose: bissection or newton.')