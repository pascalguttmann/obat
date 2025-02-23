# Current Transducer

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 1 \Omega \forall |I| < 20A$
        - `in`, current input
2. Voltage output
    - analog with $U \in [0V, 5V]$ with $R < 1 \Omega \forall |I| < 20A$
        - `out`, current output
    - analog with $U \in [0V, 5V]$ with $R < 10 \Omega \forall I < 20mA$
        - `meas_out_i`, measured output current (flow: `in` $\rightarrow$ `out`)
          sensitivity: $100 \frac{mV}{A}$
3. Supply Voltages
    - $+5V$ @ $300mW$ ($10mA$)

## Circuit Selection and Design

This sub circuit measures the current from `in` to `out` and outputs an analog
voltage signal from $0V$ to $5V$ for the measured current.

### Circuit

#### Output Current Measurement

The output current is measured by using a magnetic current sensor in an
integrated circuit. A shunt resistor can in theory also be used, but poses a
higher resistance in the path of flow of the current. Therefore to reduce the
power dissipation in the measurement sub circuit a magnetic current sensor is
preferred.

In order to get the correct voltage of $2.5V$ at zero current the current
sensor provides a reference voltage output, which is equal to the voltage at
zero current flow.

$$ U_{out} = I \cdot 0.1 \frac{V}{A} +2.5V $$

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

## Simulation

Not available.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Add copper planes for input and output pins of current sensor to lower
thermal resistance.

## Commissioning and Testing

### Current Sensor

Test ID: `v1.0.0/meas/i-transduce/current-sensor/<suffix>`

Available suffix: `-3A`, `0A`, `3A`

1. Connections
    - `in` and `out` connected to external power supply $I_{limit} = suffix$
2. Power on supply voltage
3. Measure Voltages
    - $U_{vzcr}$
    - $U_{meas\_out\_i}$
4. Power off supply voltage
5. Test passed if
    - $U_{vzcr} \in [2.5V \pm 0.1V]$
    - $U_{meas\_out\_i} \in [2.5V + I_{limit} \cdot 100 \frac{mV}{A} \pm 0.1V$
