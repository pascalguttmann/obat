# PowerSupplySink

Uses schematic version 1.0.0 and board layout version 1.0.0 (git tag sch-1.0.0_brd-1.0.0)

## Assembly Checklist

- [x] Test: `power`
- [x] Test: `conf`
- [x] Test: `adc0`, `adc1`
- [x] Test: `relay`
- [x] Test: `measurement`
- [x] Test: `limit-logic`
- [x] Test: `mux`
- [x] Test: `control-var`
- [x] Test: `power-electronics`

## Tests

### Open Circuit

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/open-circuit/voltage-control0`| pass | $U_{out,multi} = 0.002 V$, $U_{out,spi} = 0.00000 V$ |
| `v1.0.0/pss/open-circuit/voltage-control3`| pass | $U_{out,multi} = 2.996 V$, $U_{out,spi} = 2.99750 V$ |
| `v1.0.0/pss/open-circuit/voltage-control5`| pass | $U_{out,multi} = 4.995 V$, $U_{out,spi} = 4.99625 V$ |
| `v1.0.0/pss/open-circuit/upper-voltage-limit-control` | pass | $U_{out,multi} = 3.996 V$, $U_{out,spi} = 3.99750 V$ |
| `v1.0.0/pss/open-circuit/lower-voltage-limit-control` | pass | $U_{out,multi} = 1.000 V$, $U_{out,spi} = 0.99875 V$ |

### Short Circuit

!!! info "High current measurement"
    To conduct the test `v1.0.0/pss/short-circuit/current-control+20` a shunt
    resistance of $R=170 m \Omega$ is used to measure the current indirectly by a
    voltage measurement instead of directly with a multimeter.

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/short-circuit/current-control0`| pass | $I_{out,multi} = 0.031 A$, $I_{out,spi} = 0.05000 A$ |
| `v1.0.0/pss/short-circuit/current-control-20`| skip (no 20A source for testing) | |
| `v1.0.0/pss/short-circuit/current-control+20`| pass | $I_{out,multi} = 19.65 A$, $I_{out,spi} = 19.96 A$ |
| `v1.0.0/pss/short-circuit/lower-current-limit-control` | pass | $I_{out,multi} = 0.970 A$, $I_{out,spi} = 0.962500 A$ |
| `v1.0.0/pss/short-circuit/upper-current-limit-control` | pass | $I_{out,multi} = 10.145 A$, $I_{out,spi} = 9.950000 A$ |
