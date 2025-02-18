# Digital Interface

## Instance specific

!!! info "DC/DC converter minimal load"
    To avoid ringing of DC/DC converter *input* a $330 \Omega$ resistor is  placed
    between the isolated output voltage to draw approximately $15mA$ of current.

## Tests

### Isolation

Test ID: `v1.0.0/pss/digital-interface/isolation/<suffix>`

Available suffix: `GND`, `+5V`

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/digital-interface/isolation/GND` | pass | $R_{iso} \geq 1M \Omega$ |
| `v1.0.0/pss/digital-interface/isolation/+5V` | pass | $R_{iso} \geq 1M \Omega$ |

### Low State

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/digital-interface/low/!CS` | pass | $U_{out} = 0V$ |
| `v1.0.0/pss/digital-interface/low/SCKL` | pass | $U_{out} = 0V$ |
| `v1.0.0/pss/digital-interface/low/SDI` | pass | $U_{out} = 0V$ |
| `v1.0.0/pss/digital-interface/low/SDO` | pass | $U_{out} = 0V$ |

### High State

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/digital-interface/high/!CS` | pass | $U_{out} = 5V$ |
| `v1.0.0/pss/digital-interface/high/SCKL` | pass | $U_{out} = 5V$ |
| `v1.0.0/pss/digital-interface/high/SDI` | pass | $U_{out} = 5V$ |
| `v1.0.0/pss/digital-interface/high/SDO` | pass | $U_{out} = 5V$ |
