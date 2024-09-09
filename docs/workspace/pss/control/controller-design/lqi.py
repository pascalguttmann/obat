import control as ct
import numpy as np
from numpy.typing import NDArray


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

    Computes the optimal linear state feedback controller `K`, that minimizes
    the quadratic cost `J` for the continous linear time invariant system `sys`
    with respect to the cost weight matrices `Q`, `R` and the cost cross weight
    matrix `N`.
    System `sys` is given in statespace representation `A`, `B`, `C` and `D`.

    $$ J = \int_0^\infty (x' Q x + u' R u + 2 x' N u) dt $$

    The optimization problem is solved by solving the `lqr` problem for the
    augmented system. (Integrating performance output `x_i`)

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

    AAugment = np.block(
        [
            [A, 0.0],
            [-C, 0.0],
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
