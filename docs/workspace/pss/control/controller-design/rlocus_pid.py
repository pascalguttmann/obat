import control as ct
import matplotlib.pyplot as plt
import numpy as np

plantOmega = 10e6
plant = ct.zpk([], [-plantOmega], plantOmega)

zero = [-plantOmega * 0.9, -plantOmega * 0.8]
neutralGain = -1 / np.sum(zero)
pid = ct.zpk([zero[0], zero[1]], [0], 10 * neutralGain)

outerCircuitOmega = 0.5 * plantOmega
rUtoI = ct.zpk([], [], 1)
lUtoI = ct.zpk([], [-outerCircuitOmega], [outerCircuitOmega])
cUtoI = ct.zpk([0], [-outerCircuitOmega], 1)
admittance = [rUtoI, lUtoI, cUtoI]

openLoop = [pid * plant * Y for Y in admittance]
sysOpenLoop = [ct.ss(tf) for tf in openLoop]

fig, axes = plt.subplots(3, 2)
ct.rlocus(sysOpenLoop[0], ax=axes[0][0], grid=False)
axes[0][0].set_title("rlocus for R")
ct.rlocus(sysOpenLoop[1], ax=axes[1][0], grid=False)
axes[1][0].set_title("rlocus for L")
ct.rlocus(sysOpenLoop[2], ax=axes[2][0], grid=False)
axes[2][0].set_title("rlocus for C")

sysClosedLoop = [ct.feedback(sys) for sys in sysOpenLoop]
ct.step_response(sysClosedLoop[0]).plot(
    ax=np.array([[axes[0][1]]]),
    title="",
)
axes[0][1].set_title("step response for R")
ct.step_response(sysClosedLoop[1]).plot(
    ax=np.array([[axes[1][1]]]),
    title="",
)
axes[1][1].set_title("step response for L")
ct.step_response(sysClosedLoop[2]).plot(
    ax=np.array([[axes[2][1]]]),
    title="",
)
axes[2][1].set_title("step response for C")


plt.get_current_fig_manager().window.state("zoomed")  # pyright: ignore
plt.show()
