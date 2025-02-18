# Control

## Instance specific

!!! info "Derivative Term unused"
    To avoid instability of closed loop system with outstage, when quiescent current is
    low the derivative term is deactivated.
    To low quiescent current introduces non-linear behavior by introducing hysteresis,
    which yields oscillation for activated derivative term.

!!! info "Opamp type U502"
    The U502 is used for derivative and integral term of the pid controller. As
    the derivative term is deactivated and the integral term only requires low
    bandwidth the opamp *can* be changed to TLV9352.
    The TLV9352 is used here to free the OPA2810 for use in the measurement electronics.
    (No spare OPA2810 in inventory).

## Tests

### Sign propagation

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.1/pss/control/sign-propagation` | pass | $U_{e} = -500 mV$, $U_{out} = 11.964 V$ |

### Closed Loop Stability for Unity Plant

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/control/stability-unity-plant` | pass | $u_{out}(t) \approx 2.5V + 20 mV \cdot sin(t \frac{2 \pi}{15 \mu s})$ |
