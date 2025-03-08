# Enclosure

| Front | Back |
| ------------- | -------------- |
| ![img](./instance_1_enclosure_front.jpg)  | ![img](./instance_1_enclosure_back.jpg) |

Uses schematic version 1.1.2 and board layout version 1.0.0 (git tag sch-1.1.2_brd-1.0.0)

## Assembly Checklist

- [x] Test: `power`
- [x] Test: `digital-interface`
- [x] Test: `dac`
- [ ] Test: `pwm`
- [ ] Test: `full-bridge`

## Tests

### Fan

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/enclosure/fan` | pass | $I_{fan,100} =  A$, $I_{fan,25} =  A$|

### Peltier

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/enclosure/peltier` | pass | $I_{peltier,100} =  A$, $I_{peltier,25} =  A$|

### Heater

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/enclosure/heater` | pass | $I_{heater,100} =  A$, $I_{heater,25} =  A$|
