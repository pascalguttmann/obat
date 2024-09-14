import control as ct
import matplotlib.pyplot as plt
import numpy as np

plantOmega = 1
plant = ct.zpk([], [-plantOmega], plantOmega)

zero = [-plantOmega * 0.9, -plantOmega * 0.4]
neutralGain = 1 / np.prod(zero)
pid = ct.zpk([zero[0], zero[1]], [0], neutralGain)

rUtoI = ct.zpk([], [], 1)
lUtoI = ct.zpk([], [-0.75 * plantOmega], [0.75 * plantOmega])
cUtoI = ct.zpk([0], [-0.75 * plantOmega], 1)
admittance = [rUtoI, lUtoI, cUtoI]

openLoop = [pid * plant * Y for Y in admittance]
sysOpenLoop = [ct.ss(tf) for tf in openLoop]

print(f"{sysOpenLoop=}\n{type(sysOpenLoop)=}")

fig, axes = plt.subplots(3, 1)
ct.rlocus(sysOpenLoop[0], ax=axes[0], grid=False)
axes[0].set_title("rlocus for R")
ct.rlocus(sysOpenLoop[1], ax=axes[1], grid=False)
axes[1].set_title("rlocus for L")
ct.rlocus(sysOpenLoop[2], ax=axes[2], grid=False)
axes[2].set_title("rlocus for C")

plt.get_current_fig_manager().window.state("zoomed")  # pyright: ignore
plt.show()
