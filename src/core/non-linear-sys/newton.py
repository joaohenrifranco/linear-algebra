def solve(F, dF, x0, tol, n_iter):
    xn = x0

    for n in range(0, n_iter):
        fxn = F(xn)

        if abs(fxn) < tol:
            return xn

        dfxn = dF(xn)

        if dfxn == 0:
            raise Exception("Derivative is zero")

        xn = xn - fxn/dfxn

    raise Exception("Maximum iterations reached")
