# Pulse Width Modulator

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
      - $U_{mod}$ voltage used to modulate the PWM output
2. Voltage output
    - digital positive logic with $U \in [0V, 5V]$, driving up to $I = 20 mA$
    load with duty cycle controlled by $U_{mod}$ with $f_{pwm} = 7812.5 Hz$
3. Supply Voltages
    - $5V$ @ $100mW$ ($20mA$)

## Circuit Selection and Design

### Circuit

The LTC6992-1 is used to generate a modulated PWM signal. The duty cycle is
controlled by the input voltage $U_{mod}$, which is divided by a factor of $5$
by a voltage divider to achieve the input range of $0V .. 1V$ required by the
LTC6992-1.

The LTC6992-1 clock speed and divisor are set according to the datasheet to a
frequency of $f_{pwm} = 7812.5 Hz$.

The transfer function for the duty cycle $D$ is:

$$ D = \frac{\frac{1}{5} U_{mod} - 100mV}{800mV} \forall U_{mod} \in [500mV, 4.5V] $$

For voltages $U_{mod} < 500mV \implies D = 0$, i.e. the output is permanently low.
For voltages $U_{mod} > 4.5V \implies D = 1$, i.e. the output is permanently high.

### Component Selection

The selection of the LTC6992-1 is chosen, because it allows for low development
effort and easy implementation of a pwm modulator.
Other approaches would be the usages of a triangle oscillator and a comparator
to obtain a similar outcome.

## Simulation

Not available.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.

### Assembly

## Commissioning and Testing

### Frequency

Test ID: `v1.0.0/enclosure/pwm`

1. Connections
    - $U_{mod} = 2.5V$
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ with oscilloscope
4. Calculate frequency of oscillation of $f_{u,out}$
5. Power off supply voltage
6. Test passed if
    - $f_{u,out} \in 7812.5 Hz (1 \pm 5\%)$

### Duty cycle

Test ID: `v1.0.0/enclosure/duty-cycle/<suffix>`

Available suffix: `0V`, `2V`, `5V`

1. Connections
    - $U_{mod} = <suffix>$
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ with oscilloscope
4. Calculate duty cycle of oscillation of $D_{u,out}$
5. Power off supply voltage
6. Test passed if
    - $D_{u,out} = 0$ for `0V`
    - $D_{u,out} \in 0.375 (1 \pm 5\%)$ for `2V`
    - $D_{u,out} = 1 (1 \pm 5\%)$ for `5V`
