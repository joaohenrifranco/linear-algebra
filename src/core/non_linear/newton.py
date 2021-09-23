import numpy as np
from .common import j, f


def solve(X0, teta, max_iter, tolm):
    for _ in range(max_iter):
        J = j(X0)
        F = f(X0, teta)
        
        dX = -1 * np.linalg.inv(J) @ F
        X0 = X0 + dX
        
        tolk = np.linalg.norm(dX) / np.linalg.norm(X0)        
        if tolk <= tolm:
            return X0
    
    raise Exception('Conversion wasn`t reached')
