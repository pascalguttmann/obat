# Outstage

## Tests

!!! info "Test load-distribution resistance deviation"
    Tests `v1.1.0/pss/power-electronics/outstage/load-distribution/*` make use
    of a resistance $R \approx 300 m \Omega$ because $R = 100 m \Omega$ would
    require cutting the available wire, which is not desired.

    The test result is assumed to be of the same significance.

### Outstage Unit \#1.1

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.1.0/pss/power-electronics/outstage/load-distribution/positive`| pass | $U_{RE+,n} = 1.1 V$, $U_{RE-,n} = 0.86 V$ |
| `v1.1.0/pss/power-electronics/outstage/load-distribution/negative`| pass | $U_{RE+,n} = -0.9 V$, $U_{RE-,n} = -1.1 V$ |
| `v1.1.0/pss/power-electronics/outstage/short-circuit/positive` | pass | $U_{RE,n} = 1.04 V$, $I_{Output} = 10.5 A$ |
| `v1.1.0/pss/power-electronics/outstage/short-circuit/negative` | pass | $U_{RE,n} = -1.02 V$, $I_{Output} = -10.4 A$ |

### Outstage Unit \#1.2

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.1.0/pss/power-electronics/outstage/load-distribution/positive`| pass | $U_{RE+,n} = 1.08 V$, $U_{RE-,n} = 0.83 V$ |
| `v1.1.0/pss/power-electronics/outstage/load-distribution/negative`| pass | $U_{RE+,n} = -1.10 V$, $U_{RE-,n} = -0.85 V$ |
| `v1.1.0/pss/power-electronics/outstage/short-circuit/positive` | pass | $U_{RE,n} = 1.2 V$, $I_{Output} = 10.25 A$ |
| `v1.1.0/pss/power-electronics/outstage/short-circuit/negative` | pass | $U_{RE,n} = -0.8 V$, $I_{Output} = -10.18 A$ |
