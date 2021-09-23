import numpy as np
from common import j, f


def solve(X0, teta, max_iter, tolm):
    X0 = np.array(X0)
    B0 = j(X0)

    for _ in range(max_iter):
        J = B0
        dX = -1 * np.linalg.inv(J) @ f(X0, teta)

        X = X0 + dX
        Y = f(X, teta) - f(X0, teta)

        tolk = np.linalg.norm(dX)/np.linalg.norm(X)
        if tolk <= tolm:
            return X0
        else:
            B0 = B0 + (Y - B0 @ dX) @ dX.T / (dX.T @ dX)

        X0 = X

    raise Exception('Conversion wasn`t reached')
