import control as ct
import matplotlib.pyplot as plt

sysOmega = 10e6
sysPowerElectronics = ct.zpk([],[-sysOmega], sysOmega)
#print(sysPowerElectronics)

kp = 1
zero = -sysOmega*0.9
ki = -kp*zero
pController = ct.zpk([],[],kp)
iController = ct.zpk([], [0], ki)
controller = ct.parallel(pController, iController)
#print(controller)
#ct.pzmap(controller, plot=True)

sysOpenloop = ct.series(controller, sysPowerElectronics)
#print(sysOpenloop)
#ct.pzmap(sysOpenloop, plot=True)
#ct.root_locus(sysOpenloop, plot=True)
#ct.nyquist_plot(sysOpenloop, plot=True)
#ct.bode_plot(sysOpenloop, plot=True)

sysClosedloop = ct.feedback(sysOpenloop, 1, sign=-1)
print(sysClosedloop)
ct.pzmap(sysClosedloop, plot=True)
#ct.nyquist_plot(sysClosedloop, plot=True)
#T, yout = ct.step_response(sysClosedloop)
#plt.plot(T, yout, label="step response")
s_info = ct.step_info(sysClosedloop)
for i in s_info:
    print(f"{i}: {float(s_info[i]):3.4}")

plt.show()

