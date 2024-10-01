# Power Electronics

## Interface & Requirements

See input interface of [bias](./bias/bias.md) and output interface of
[outstage](./outstage/outstage.md).

## Circuit Selection and Design

![image](./power_electronics.png)

## Simulation

See `./sim_bias+outstage.asc` for simulation.

## Hardware Tests in Laboratory

## Layout and Assembly Considerations

- (Dis-) connector between _bias_ and _outstage_, (solderbridge / jumper)
    Label with testname hint

## Commissioning and Testing

1. Pass all tests for _bias_
2. Pass all tests for _outstage_
3. Connect _bias_ and _outstage_
4. Set Offset adjustment trimmer of _bias_ to $R = 0 \Omega$, verify by
   measurement
5. Connect _bias_ input to $U_{in} = 2V$
6. Power on supply voltage
7. Measure $U_{out}$ of _outstage_ and adjust $U_{in}$ until $U_{out} \approx
   2.5V$
8. Adjust offset adjusment trimmer of _bias_ until ballast resistor current of
   _outstage_ is $\approx 20mA$.
   Therefore measure voltage across a single ballast resistor and calculate $I =
   U/R$
9. Power off supply voltage
