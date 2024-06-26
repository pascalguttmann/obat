import control as ct
from scipy.optimize import least_squares

def tfest(order, frd):
    """Estimates a complex valued transfer function of order 'order' for frequency
    response data 'frd' via least squares

    Arguments:
        - order : The order of the system to estimate
        - frd   : Tuple of frequency ressponse data in the form
                  (omega, complex)

    Returns:
        - num   : A list representing a polynomial of degree 'order', which zeros
                  are the zeros of the estimated system.
        - den   : A list representing a polynomial of degree 'order', which zeros
                  are the poles of the estimated system.
    """

    def tf(order, num, den, omega):
        s = [complex(0, w) for w in omega]

        def evalPoly(coef, x):
            return sum((x**power) * factor
                       for power, factor
                       in enumerate(reversed(coef)))

        return [evalPoly(num, sx) / evalPoly(den, sx) for sx in s]

    def packArg(num, den):
        return list(num) + list(den)

    def unpackArg(p):
        halfIndex = len(p)//2
        return p[:halfIndex], p[halfIndex:]

    def tfWrap(p, omega, H, order):
        """Wrapper function to adhere to function definition of
        scipy.optimize.least_squares function definition

        Computes the residuals
        """
        num, den = unpackArg(p)
        sys = ct.tf(num, den)
        mag, phase, omega = ct.frequency_response(sys)
        H_calc = mag * e**(1j * phase)

        residuals = [abs(H_calc - H) for H_calc, H in zip(H_calc, H)]

        return residuals

    num = [0.0] * order
    num[-1] = 1.0
    den = [0.0] * order
    den[-1] = 1.0


    p0 = packArg(num, den)
    print(f"{num=} {den=} {p0=}")

    p = least_squares(tfWrap, p0, method='trf', ftol=None,
                      args=(frd[0], frd[1], order))
    print(f"{p=}")

    return (p)

print("running")

if __name__=="__main__":
    import control as ct
    from math import e

    sys = ct.tf([0, 0, 1], [1, 0, 1])
    mag, phase, omega = ct.frequency_response(sys)

    H = mag * e**(1j * phase)
    frd = (list(omega), list(H))

    tfest(3, frd)

