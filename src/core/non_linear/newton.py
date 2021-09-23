import numpy as np
from common import j, f


def solve(X0, theta, max_iter, tol):
    for _ in range(max_iter):
        J = j(X0)
        F = f(X0, theta)
        
        dX = -1 * np.linalg.inv(J) @ F
        X0 = X0 + dX
        
        tolk = np.linalg.norm(dX) / np.linalg.norm(X0)        
        if tolk <= tol:
            return X0
    
    raise Exception('Did not converge')
