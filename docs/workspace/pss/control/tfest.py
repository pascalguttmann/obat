import control as ct
from scipy.optimize import least_squares

def tfest(order, frd, num0=None, den0=None, orderNum=None):
    """Estimates a complex valued transfer function of order 'order' for frequency
    response data 'frd' via least squares

    Arguments:
        - order : The order of the system to estimate
        - frd   : Dict of frequency response data in the form
                  {"omega": [...], "H": [...]}

    Returns:
        - num   : A list representing a polynomial of degree 'order', which zeros
                  are the zeros of the estimated system.
        - den   : A list representing a polynomial of degree 'order', which zeros
                  are the poles of the estimated system.
    """

    def packArg(num, den):
        return list(num) + list(den)

    def unpackArg(p):
        halfIndex = len(p)//2
        return p[:orderNum+1], p[orderNum+1:]

    def residuals(p, frd, order):
        """Wrapper function to adhere to function definition of
        scipy.optimize.least_squares function definition

        Computes the residuals
        """
        num, den = unpackArg(p)
        sys = ct.tf(num, den)
        mag, phase, omega = ct.frequency_response(sys, frd["omega"])
        H_calc = mag * e**(1j * phase)
        residuals = [abs(a - b) for a, b in zip(H_calc, frd["H"])]
        return residuals

    if orderNum is None:
        orderNum = order

    if num0 is None:
        num0 = [0.0] * (orderNum + 1)
        num0[-1] = 1.0

    if den0 is None:
        den0 = [0.0] * (order + 1)
        den0[-1] = 1.0


    p0 = packArg(num0, den0)

    p = least_squares(residuals, p0, method='trf', loss='soft_l1', max_nfev=1e4,
                      xtol=1e-15, ftol=1e-15,
                      verbose=2, args=(frd, order))

    num, den = unpackArg(p["x"])

    return num, den

if __name__=="__main__":
    import control as ct
    import matplotlib.pyplot as plt
    import numpy as np
    from math import e

    omega = np.logspace(-1, 1, num=50)
    print(omega)
    sys = ct.tf([0, 0, 1], [1, 0, 1.01])
    mag, phase, omega = ct.frequency_response(sys, omega)

    H = mag * e**(1j * phase)
    frd = {"omega": list(omega), "H": list(H)}

    num, den = tfest(2, frd, orderNum=1)
    sys_model = ct.tf(num, den)

    print(f"{num=} {den=}")

    ct.pzmap([sys, sys_model], plot=True)
    plt.show()

    ct.bode_plot([sys, sys_model], plot=True)
    plt.show()

