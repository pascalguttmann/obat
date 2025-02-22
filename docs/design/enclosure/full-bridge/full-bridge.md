# Full Bridge

## Interface & Requirements

1. Voltage inputs
    - digital positive logic with $U \in [0V, 5V]$, driving up to $I = 5 mA$
    load
      - `IN_A`, select `OUT_A` to be of high polarity
      - `IN_B`, select `OUT_B` to be of high polarity
      - `PWM`, enable the output with PWM ($f_{pwm} <= 20 kHz$)
2. Voltage output
    - `OUT_A` & `OUT_B`, digital PWM with duty cycle defined by `PWM` and
    polarity defined by `IN_A` and `IN_B`,
3. Supply Voltages
    - VCC, quiescent current $< 10mA$, output current of `OUT_A` and `OUT_B`

## Circuit Selection and Design

### Circuit

The full bridge driver uses an integrated full bridge to change the polarity of
the outputs `OUT_A` and `OUT_B` and apply a pwm to the output as specified by
the `PWM` input pin, which enables the output.
The boolean logic to determine, when the output connections `OUT_A` and `OUT_B`
are high (VCC) and low are as follows:

$$ \text{OUT_A}_{HIGH} = IN_A $$

$$ \text{OUT_A}_{LOW} = \overline{IN_A} \land \text{PWM} $$

$$ \text{OUT_B}_{HIGH} = IN_B $$

$$ \text{OUT_B}_{LOW} = \overline{IN_B} \land \text{PWM} $$

Otherwise the output connection is in tri-state (Hi-Z).

### Component Selection

A integrated full bridge is selected from ST-Microelectronics, because of the
integrated protection circuits and driver circuitry.

- $I_{out} > 8A$
- $VCC_{max} > 24V$
- Full Bridge
- parallel input interface (IN_A, IN_B and PWM)
- Package easy hand solderable SMT package, without center pads

_VNH7070AS_ is selected. Also offers family parts for other current and voltage
requirements with pin compatible footprint.

## Simulation

Not available.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.

### Assembly

## Commissioning and Testing

### Polarity Positive

Test ID: `v1.0.0/enclosure/full-bridge/polarity/positive`

1. Connections
    - `IN_A` $5V$
    - `IN_B` $0V$
    - `PWM` $5V$
2. Power on supply voltage
3. Measure Voltages
    - `OUT_A` to `OUT_B` $U_{AB}$
4. Power off supply voltage
5. Test passed if
    - $U_{AB} > 0V$

### Polarity Negative

Test ID: `v1.0.0/enclosure/full-bridge/polarity/negative`

1. Connections
    - `IN_A` $0V$
    - `IN_B` $5V$
    - `PWM` $5V$
2. Power on supply voltage
3. Measure Voltages
    - `OUT_A` to `OUT_B` $U_{AB}$
4. Power off supply voltage
5. Test passed if
    - $U_{AB} < 0V$

### PWM Enable

Test ID: `v1.0.0/enclosure/full-bridge/pwm`

1. Connections
    - `IN_A` $0V$
    - `IN_B` $5V$
    - `PWM` $0V$
2. Power on supply voltage
3. Measure Voltages
    - `OUT_A` $U_{A}$
4. Power off supply voltage
5. Test passed if
    - $U_{A} \in U_{VCC} \cdot (1 \pm 5\%)$
