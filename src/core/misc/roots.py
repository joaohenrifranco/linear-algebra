from common import f, f_derivative


def bissection(a, b, constants, tolm):
    while(abs(b-a) > tolm):
        x = (a+b) / 2
        if f(x, constants) > 0:
            b = x
        else:
            a = x
    return x


def newton(a, b, constants, tolm):
    max_iterations = 1000
    x0 = (a+b) / 2

    for _ in range(max_iterations):
        x = x0 - f(x0, constants) / f_derivative(x0, constants)
        tolk = abs(x - x0)
        if tolk <= tolm:
            return x
        x0 = x

    raise Exception('Conversion not reached.')

def solve(a, b, constants, tolm, method):
    if method == 'newton':
        return newton(a, b, constants, tolm)
    elif method == 'bissection':
        return bissection(a, b, constants, tolm)
    else:
        raise Exception('Invalid method name. Choose: bissection or newton.')