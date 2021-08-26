# P is an 2d array with each element being a point
# Each point is an array with x and y coordinates 
def get_interpolated(P, x0):
    n = P.shape[0]
    y0 = 0.0

    for i in range(n):  
        p = 1
        for j in range(n):
            if i != j:
                p = p * (x0 - P[j,0])/(P[i,0] - P[j,0])
        
        y0 = y0 + p * P[i,1]    

    return y0