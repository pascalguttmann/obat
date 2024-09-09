import control as ct
import matplotlib.pyplot as plt
import numpy as np

from lqi import lqi, ss2ABCD

sysOmega = 10e6
sysPowerElectronics: ct.StateSpace = ct.StateSpace(
    ct.ss(
        ct.zpk([], [-sysOmega], sysOmega),
        inputs="u",
        outputs="y",
        name="plant",
    )
)

stateWeight = np.eye(2) * 1
inputWeight = np.eye(1) * 1
crossWeight = None


K, S, E = lqi(
    *ss2ABCD(sysPowerElectronics),
    Q=stateWeight,
    R=inputWeight,
    N=crossWeight,
)

print(K)
print(E)

sysController: ct.StateSpace = ct.StateSpace(
    ct.ss(
        np.zeros((0, 0)),
        np.zeros((0, 2)),
        np.zeros((1, 0)),
        -K,
        inputs=["plantStates", "performanceMeasure"],
        outputs="u",
        name="controller",
    )
)
# print(sysController)

sysIntegrator: ct.StateSpace = ct.StateSpace(
    ct.ss(
        [0],
        [1],
        [1],
        [0],
        inputs="e",
        outputs="performanceMeasure",
        name="integrator",
    )
)
# print(sysIntegrator)

sysSummingJunctionInt: ct.StateSpace = ct.summing_junction(
    inputs=["r", "-y"],
    output="e",
    name="sumJunctionInt",
)
# print(sysSummingJunctionInt)

sysSummingJunctionProportional: ct.StateSpace = ct.summing_junction(
    inputs=["-r", "y"],
    output="e",
    name="sumJunctionProportional",
)
# print(sysSummingJunctionProportional)

sysInputBuffer: ct.StateSpace = ct.StateSpace(
    ct.ss([0], [0], [0], [1], inputs="in", outputs="out", name="inputbuf")
)

sysClosedLoop: ct.StateSpace = ct.interconnect(
    syslist=[
        sysInputBuffer,
        sysSummingJunctionInt,
        sysSummingJunctionProportional,
        sysIntegrator,
        sysController,
        sysPowerElectronics,
    ],
    connections=[
        ["plant.u", "controller.u"],
        ["controller.plantStates", "sumJunctionProportional.e"],
        ["sumJunctionProportional.y", "plant.y"],
        ["sumJunctionProportional.r", "inputbuf.out"],
        ["controller.performanceMeasure", "integrator.performanceMeasure"],
        ["integrator.e", "sumJunctionInt.e"],
        ["sumJunctionInt.y", "plant.y"],
        ["sumJunctionInt.r", "inputbuf.out"],
    ],
    inplist=[["inputbuf.in"]],
    outlist=[["plant.y"], ["controller.u"]],
    inputs=["r"],
    outputs=["y", "u"],
    name="closeLoop",
    check_unused=True,
    warn_duplicate=True,
    debug=False,
)
# print(sysClosedLoop)

ct.step_response(sysClosedLoop).plot(
    overlay_signals=True,
)
plt.gca().grid(True, which="both")
plt.show()
# ct.pzmap(sysClosedLoop, plot=True)
# plt.show()
# ct.nyquist_plot(sysClosedLoop, plot=True)
# plt.show()
# ct.bode_plot(sysClosedLoop, plot=True)
# plt.show()
