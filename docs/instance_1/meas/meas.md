# U / I / T Measurement

| Front | Back |
| ------------- | -------------- |
| ![img](./instance_1_meas_front.jpg)  | ![img](./instance_1_meas_back.jpg) |

Uses schematic version 1.0.0 and board layout version 1.0.0 (git tag sch-1.0.0_brd-1.0.0)

## Assembly Checklist

- [x] Test: `power`
- [x] Test: `digital-interface`, `digital-interface1`, `digital-interface2`, `digital-interface3`
- [x] Test: `iso-dcdc`,`iso-dcdc1`,`iso-dcdc2`,`iso-dcdc3`
- [x] Test: `adc0`, `adc1`, `adc2`
- [x] Test: `i-transduce`

## Tests

### Voltage Measurement

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/meas/voltage`| pass | $U_{in} = 3.001 V$, $U_{spi} = 3.00000 V$ |

### Temperature Measurement

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/meas/temperature`| pass | $U_{in} = 0.409 V \equiv 24.54 °C, $U_{spi} = 0.40875 V \equiv 24.525 °C$ |

### Current Measurement

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/meas/current`| pass | $I_{in} = 2.999 A$, $I_{spi} = 2.96000 A$ |
