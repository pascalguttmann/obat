# Enclosure

| Front | Back |
| ------------- | -------------- |
| ![img](./instance_1_enclosure_front.jpg)  | ![img](./instance_1_enclosure_back.jpg) |

Uses schematic version 1.1.2 and board layout version 1.0.0 (git tag sch-1.1.2_brd-1.0.0)

## Heating and Cooling

The maximum heating and cooling capabilities are measured by heating and
cooling with maximal power for $t \approx 15 min$ with closed lid. The
temperature is measured using an infrared thermometer at the interior aluminium
surface of the mechanical enclosure.

For cooling with the peltier element with 144W and full fan speed, the
temperature is measured as follows:
$$ \vartheta_{inside} = 23 °C \quad \land \quad \vartheta_{outside} = 60 °C $$

For heating with the heater (50W), the peltier element (144W) and full fan speed, the
temperature is measured as follows:
$$ \vartheta_{inside} = 72 °C \quad \land \quad \vartheta_{outside} = 32 °C $$

## Assembly Checklist

- [x] Test: `power`
- [x] Test: `digital-interface`
- [x] Test: `dac`
- [x] Test: `pwm`
- [x] Test: `full-bridge`

## Tests

### Fan

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/enclosure/fan` | pass | $I_{fan,100} = 178 mA$, $I_{fan,25} = 17 mA$|

### Peltier

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/enclosure/peltier` | pass | $I_{peltier,100} = 4.506 A$, $I_{peltier,25} = 1.609 A$|

### Heater

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/enclosure/heater` | pass | $I_{heater,100} = 1.75 A$, $I_{heater,25} = 612 mA$|
