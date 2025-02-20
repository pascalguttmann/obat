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
