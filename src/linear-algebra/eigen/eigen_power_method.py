import numpy as np

def eigen_power_method(A, rtol):
    n = A.shape[0]
    
    eigenvector = np.ones(n)
    residue = rtol + 1
    prev_eigenvalue = 1
    
    while(rtol < residue):   
        Y = A @ eigenvector
        
        eigenvalue = Y[0]
        eigenvector = Y / eigenvalue
        
        residue = (eigenvalue - prev_eigenvalue) / eigenvalue
        prev_eigenvalue = eigenvalue

    return eigenvector, eigenvalue