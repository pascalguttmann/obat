# Measurement

## Interface & Requirements

TODO: Add Input specs
TODO: Add Output specs
TODO: Add Power Consumption

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 20mA$
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
2. Voltage output
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 20mA$
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
3. Supply Voltages
    - $+10V$ @ $1W$ ($100mA$)
    - $-5V$ @ $0.5W$ ($50mA$)

## Circuit Selection and Design

The `measurement` sub circuit measures the output voltage and output current of
the powersupplysink and outputs an analog voltage signal from $0V$ to $5V$ for
the measured quantities.
The output voltage is scaled and the output current is transduced to a voltage.

### Circuit

#### Output Voltage Measurement

The output voltage is designed to be in the interval $[0V, 5V]$, therefore the
output voltage can be directly used by a galvanic connection, as a scaling
factor of $k = 1$ is required.

#### Output Current measurement

The output current is measured by using a magnetic current sensor in an
integrated circuit. A shunt resistor can in theory also be used, but poses a
higher resistance in the path of flow of the current. Therefore to reduce the
power dissipation in the measurement sub circuit a magnetic current sensor is
preferred.

### Component Selection

#### Current Sensor

Current Sensors from _Allegro MicroSystems_ and _Texas Instruments_ are
considered, because of high market share and therefore projected long-term
availability of the component or successor components.

- Current Measurement Range: $I = \pm 20A \lor \pm 25A$
- Bandwidth $f_{BW} \geq 1 MHz$
- Supply Voltage $V \geq 5V$
- Preferred IC Package: SOIC
- For Allegro MicroSystems: Feature: _Zero Current Reference Voltage Output_

For Allegro MicroSystems_: [ACS730] Isolated Currrent Sensor can be used.

Alternatively in SOICW-16 package `CT430` and `CT432` may be used.
Texas Instruments offers only `TMCS1133A4A-Q1` with a $1MHz$ bandwidth, but the
sensor is not available at Mouser (15. Nov. 2024).

[ACS730]: https://mou.sr/3YOkQ98

#### Operational Amplifier

The opamp of the window comparator is reused to lower the amount of different
components in the design. It features a gain bandwidth product of $3.5MHz$,
which is enough for the signal with $1MHz$ bandwidth.
The slew rate is higher, than the slew rate of the current sensor.

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
