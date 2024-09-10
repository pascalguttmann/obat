import control as ct
import matplotlib.pyplot as plt
import numpy as np

from lqi import lqi, ss2ABCD

plantOmega = 10e6
sysPlant: ct.StateSpace = ct.StateSpace(
    ct.ss(
        ct.zpk([], [-plantOmega], plantOmega),
        inputs="u",
        outputs="y",
        name="plant",
    )
)


# Bandwith limited PID controller
bwOmega = 1e9
proportional = ct.ss([], [], [], [1], inputs="e", outputs="u", name="p")
integral = ct.ss([0], [1], [1], [0], inputs="e", outputs="u", name="i")
derivative = ct.ss(
    [-bwOmega], [1], [-(bwOmega**2)], [bwOmega], inputs="e", outputs="u", name="d"
)

sysInputBuffer: ct.StateSpace = ct.StateSpace(
    ct.ss([], [], [], [1], inputs="r", outputs="r", name="inbuf")
)

sysAugment: ct.StateSpace = ct.interconnect(
    syslist=[sysPlant, proportional, integral, derivative],
    connections=[
        ["p.e", "-plant.y"],
        ["i.e", "-plant.y"],
        ["d.e", "-plant.y"],
        ["plant.u", "p.u", "i.u", "d.u"],
    ],
    inplist=[
        ["plant.u"],
    ],
    outlist=[
        ["plant.y", "p.u", "i.u", "d.u"],
    ],
    inputs=["u"],
    outputs=["y", "p", "i", "d"],
    name="sysAugment",
    check_unused=True,
    warn_duplicate=True,
    debug=False,
)
print(sysAugment)

A, B, _, _ = ss2ABCD(sysAugment)

x_x_weight = 1e0
i_i_weight = 1e0
d_d_weight = 1e0

x_i_weight = 0e0
x_d_weight = 0e0
i_d_weight = 0e0

stateWeight = np.array(
    [
        [x_x_weight, x_i_weight, x_d_weight],
        [x_i_weight, i_i_weight, i_d_weight],
        [x_d_weight, i_d_weight, d_d_weight],
    ]
)
inputWeight = np.eye(1) * 1e-9
crossWeight = None

K, S, E = ct.lqr(A, B, stateWeight, inputWeight)


sysClosedLoop: ct.StateSpace = ct.interconnect(
    syslist=[sysPlant, proportional, integral, derivative, sysInputBuffer],
    connections=[
        ["p.e", "-plant.y", "inbuf.r"],
        ["i.e", "-plant.y", "inbuf.r"],
        ["d.e", "-plant.y", "inbuf.r"],
        ["plant.u", "p.u", "i.u", "d.u"],
    ],
    inplist=[
        ["inbuf.r"],
    ],
    outlist=[
        ["plant.y"],
    ],
    inputs=["r"],
    outputs=["y"],
    name="closedLoop",
    check_unused=True,
    warn_duplicate=True,
    debug=False,
)
# print(sysClosedLoop)
