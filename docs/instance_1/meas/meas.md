# U / I / T Measurement

| Front | Back |
| ------------- | -------------- |
| ![img](./instance_1_meas_front.jpg)  | ![img](./instance_1_meas_back.jpg) |

Uses schematic version 1.0.0 and board layout version 1.0.0 (git tag sch-1.0.0_brd-1.0.0)

## Assembly Checklist

- [ ] Test: `power`
- [ ] Test: `digital-interface`, `digital-interface1`, `digital-interface2`, `digital-interface3`
- [ ] Test: `iso-dcdc`,`iso-dcdc1`,`iso-dcdc2`,`iso-dcdc3`
- [ ] Test: `adc0`, `adc1`, `adc2`
- [ ] Test: `i-transduce`

## Tests

### Voltage Measurement

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/meas/voltage`| pass | $U_{in} = 0.002 V$, $U_{spi} = 0.00000 V$ |

### Temperature Measurement

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/meas/temperature`| pass | $U_{in} = 0.002 V$, $U_{spi} = 0.00000 V$ |

### Current Measurement

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/meas/current`| pass | $I_{in} = 0.002 A$, $I_{spi} = 0.00000 A$ |
