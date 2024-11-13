import control as ct
import matplotlib.pyplot as plt
import numpy as np


def firstOrderLowPass(omega: float) -> ct.StateSpace:
    return ct.StateSpace([-omega], [omega], [1], [0])


def firstOrderHighPass(omega: float) -> ct.StateSpace:
    return ct.StateSpace([-omega], [omega], [-1], [1])


# scale numerical values (pzmap will calculate wrong poles and zeros)
scale = 1e3
plantOmega = 2 * np.pi * 10e6
plantOmegaScaled = plantOmega / scale
plant = firstOrderLowPass(plantOmegaScaled)

zero = [-plantOmegaScaled * 0.9, -plantOmegaScaled * 0.8]
neutralGain = -1 / np.sum(zero)
pid = ct.zpk([zero[0], zero[1]], [0], 10 * neutralGain)

outerCircuitOmega = 0.5 * plantOmegaScaled
rUtoI = ct.ss([], [], [], [1])
lUtoI = firstOrderLowPass(outerCircuitOmega)
cUtoI = firstOrderHighPass(outerCircuitOmega)
admittance = [rUtoI, lUtoI, cUtoI]

openLoop = [ct.series(pid, ct.ss2tf(plant), ct.ss2tf(Y)) for Y in admittance]
sysOpenLoop = [ct.ss(ct.tf2ss(tf)) for tf in openLoop]

fig, axes = plt.subplots(3, 3, sharex="col", sharey="col")
ct.rlocus(sysOpenLoop[0], ax=axes[0][0], grid=False)
axes[0][0].set_title("rlocus for R")
ct.rlocus(sysOpenLoop[1], ax=axes[1][0], grid=False)
axes[1][0].set_title("rlocus for L")
ct.rlocus(sysOpenLoop[2], ax=axes[2][0], grid=False)
axes[2][0].set_title("rlocus for C")


simulationTime = 500e-9
simulationTimeScaled = simulationTime * scale

sysClosedLoop = [ct.feedback(sys) for sys in sysOpenLoop]
ct.step_response(
    sysClosedLoop[0],
    T=simulationTimeScaled,
).plot(
    ax=np.array([[axes[0][1]]]),
    title="",
)
axes[0][1].set_title("step response for R")
axes[0][1].set_xlabel(f"Time [{1/scale}s]")
ct.step_response(
    sysClosedLoop[1],
    T=simulationTimeScaled,
).plot(
    ax=np.array([[axes[1][1]]]),
    title="",
)
axes[1][1].set_title("step response for L")
axes[1][1].set_xlabel(f"Time [{1/scale}s]")
ct.step_response(
    sysClosedLoop[2],
    T=simulationTimeScaled,
).plot(
    ax=np.array([[axes[2][1]]]),
    title="",
)
axes[2][1].set_title("step response for C")
axes[2][1].set_xlabel(f"Time [{1/scale}s]")

ct.pzmap(sysClosedLoop[0], ax=axes[0][2], grid=False)
axes[0][2].set_title("pzmap for R")
ct.pzmap(sysClosedLoop[1], ax=axes[1][2], grid=False)
axes[1][2].set_title("pzmap for L")
ct.pzmap(sysClosedLoop[2], ax=axes[2][2], grid=False)
axes[2][2].set_title("pzmap for C")

pidNum = pid.num[0][0].tolist()
Kd, Kp, Ki = pidNum[0] / scale, pidNum[1], pidNum[2] * scale
Ti = float(Kp) / float(Ki)
Td = float(Kd) / float(Kp)

print(f"pid {pid}")
print(f"{Kp=}")
print(f"{Ti=} {Ki=}")
print(f"{Td=} {Kd=}")

for ax in axes.reshape(-1):
    ax.grid()

plt.get_current_fig_manager().window.state("zoomed")  # pyright: ignore
plt.show()
