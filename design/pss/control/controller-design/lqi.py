import control as ct
import numpy as np
from numpy.typing import NDArray


def ss2ABCD(sys: ct.StateSpace):
    A: NDArray[np.number] = np.array(sys.A)
    B: NDArray[np.number] = np.array(sys.B)
    C: NDArray[np.number] = np.array(sys.C)
    D: NDArray[np.number] = np.array(sys.D)
    return A, B, C, D


def lqi(
    A: NDArray[np.number],
    B: NDArray[np.number],
    C: NDArray[np.number],
    D: NDArray[np.number],
    Q: NDArray[np.number],
    R: NDArray[np.number],
    N: NDArray[np.number] | None = None,
):
    r"""
    Linear Quadratic Integral Compensator

    Computes the optimal linear state feedback controller `u = -Kx`, that
    minimizes the quadratic cost `J` for the continous linear time invariant
    system `sys` with respect to the cost weight matrices `Q`, `R` and the cost
    cross weight matrix `N`. System `sys` is given in statespace representation
    `A`, `B`, `C` and `D`.

    $$ J = \int_0^\infty (x' Q x + u' R u + 2 x' N u) dt $$

    The optimization problem is solved by solving the `lqr` problem for the
    augmented system. The augmented system adds a performance output for each
    output of the system by integrating the inverse of of the output.
    Negation of output signal is applied before the integrator, such that a
    non-inverted reference signal can be superimposed to realize tracking
    control.

    $$ A^* =\begin{bmatrix}
            A & 0 \\
            -C & 0
        \end{bmatrix}

        B^* =\begin{bmatrix}
            B \\
            -D
        \end{bmatrix}
    $$
    """

    noStates: int = A.shape[0]
    noOutputs: int = C.shape[0]

    AAugment = np.block(
        [
            [A, np.zeros((noStates, noOutputs))],
            [-C, np.zeros((noOutputs, noOutputs))],
        ]
    )
    BAugment = np.block(
        [
            [B],
            [-D],
        ]
    )

    if N:
        K, S, E = ct.lqr(AAugment, BAugment, Q, R, N)
    else:
        K, S, E = ct.lqr(AAugment, BAugment, Q, R)

    return K, S, E


if __name__ == "__main__":
    A = np.array(
        [
            [1],
        ]
    )
    B = np.array(
        [
            [1],
        ]
    )
    C = np.array([[1]])
    D = np.array([[0]])

    Q = np.eye(A.shape[0] + 1)
    R = np.eye(B.shape[1])

    K, S, E = lqi(A, B, C, D, Q, R)

    print(f"{K=}\n{S=}\n{E=}\n")
