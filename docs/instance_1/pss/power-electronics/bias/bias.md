# Bias Stage

## Instance specific

!!! info "Increased rubber diode voltage"
    R1903 is changed from $R = 100 \Omega$ to $R = 270 \Omega$ in order to
    achieve higher offset voltages to increase the quiescent current.
    A higher quiescent current reduces the hysteresis by the `outstage`. The hysteresis
    is undesired as it violates the assumption of linearity, which is assumed
    for controller synthesis.

## Tests

# Transfer Characteristic

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/power-electronics/bias/transfer/-2V`| pass | $U_{out-} = -1.95 V$, $U_{out+} = -0.375 V$ |
| `v1.0.0/pss/power-electronics/bias/transfer/+2V`| pass | $U_{out-} = +2.054 V$, $U_{out+} = +3.59 V$ |
| `v1.0.0/pss/power-electronics/bias/transfer/+6V`| pass | $U_{out-} = +5.95 V$, $U_{out+} = +7.49 V$ |

# Offset Adjustment

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.1/pss/power-electronics/bias/offset-adjustment`| pass | $U_{out-,0} = 2.07 V$, $U_{out-,1} = 2.07 V$, $U_{out+,0} = 3.61 V$, $U_{out+,1} = 2.77 V$ |
