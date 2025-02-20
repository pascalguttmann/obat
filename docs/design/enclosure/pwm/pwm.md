# Pulse Width Modulator

## Interface & Requirements

TODO: Add Input specs
TODO: Add Output specs
TODO: Add Power Consumption

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
      - $U_{mod}$ voltage used to modulate the PWM output
2. Voltage output
    - digital positive logic with $U \in [0V, 5V]$, driving up to $I = 20 mA$ load
3. Supply Voltages
    - $5V$ @ $100mW$ ($20mA$)

## Circuit Selection and Design

### Circuit

TODO: Add circuit description

### Component Selection

TODO: Add component selection

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
