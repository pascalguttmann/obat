# Compare Logic

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
        - `conf_vref`, signal of configured reference voltage
        - `conf_iref`, signal of configured reference current
        - `conf_lcl`, signal of configured lower current limit
        - `conf_ucl`, signal of configured upper current limit
        - `conf_lvl`, signal of configured lower voltage limit
        - `conf_uvl`, signal of configured upper voltage limit
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 20mA$
        - `meas_out_v`, signal of measured output voltage
        - `meas_out_i`, signal of measured output current
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
        - `conf_refselect_v`, signal that the desired reference is voltage
        - `conf_refselect_i`, signal that the desired reference is current
2. Voltage output, digital positive logic $U \in [-5V, 10V]$ driving up to $I =
   2.5mA$
    - `comp_mgtt`, measured greater than target
    - `comp_mstt`, measured smaller than target
    - `comp_lvle`, lower voltage level exceeded
    - `comp_uvle`, upper voltage level exceeded
    - `comp_lcle`, lower current level exceeded
    - `comp_ucle`, upper current level exceeded
3. Supply Voltages
    - $+10V$ @ $80mW$ ($8mA$)
    - $-5V$ @ $40mW$ ($8mA$)

## Circuit Selection and Design

### Circuit

TODO: Add circuit description

### Component Selection

#### Comparator / Opamp

[TLV9352](https://mou.sr/3BJsKZm)

- 2 or 4 channels
- SMD Mount, SOIC preferred
- rail-to-rail preferred
- $\text{SR} > 5V / \mu s$
- $V_{off} \leq 1mV$
- $I_{bias, in} \leq 1nA$ (To allow neglect of input current for high feedback resistance)
- $I_{out} \geq 20mA$
- Price sort on Mouser

## Simulation

TODO: link to simulation files

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
TODO: Add test pins
TODO: Add (dic-)connector note, with testcase required for connecting

### Assembly

TODO: Add special hints for Assembly or remove

## Commissioning and Testing

TODO: add tests

### Testheading

Test ID: `v1.0.0/pss/control-logic/control/sign-propagation/<suffix>`

1. Connections
    - Output `out` disconnected
    - Input `meas` connected to $U_{meas} = 0V$
    - Input `ref` connected to $U_{ref} = +500mV$
2. Power on supply voltage
3. Wait for steady state $t_{wait} \gtrapprox 1ms$
4. Measure Voltages
    1. Error Signal (test id suffix: `error`)
        - Voltage at subtraction output $U_{e}$
    2. Output Signal (test id suffix: `output`)
        - Voltage at PID controller output $U_{out}$
5. Power off supply voltage
6. Test passed if
    1. Error Signal (test id suffix: `error`)
        - $U_{e} \in 500mV (1 \pm 10\%)$
    2. Output Signal (test id suffix: `output`)
        - $U_{out} \in 10V (1 \pm 10\%)$
