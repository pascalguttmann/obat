# Multiplexer

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 3mA$
        - `conf_vref`, signal of configured reference voltage
        - `conf_iref`, signal of configured reference current
        - `conf_lcl`, signal of configured lower current limit
        - `conf_ucl`, signal of configured upper current limit
        - `conf_lvl`, signal of configured lower voltage limit
        - `conf_uvl`, signal of configured upper voltage limit
        - `meas_out_v`, signal of measured output voltage
        - `meas_out_i`, signal of measured output current
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
        - `mode_vc`, voltage control
        - `mode_lclc`, lower current limit control
        - `mode_uclc`, upper current limit control
        - `mode_cc`, current control
        - `mode_lvlc`, lower voltage level control
        - `mode_uvlc`, upper voltage level control
2. Voltage output
    - analog with $U \in [0V, 5V]$ with $R < 350 \Omega \forall I < 3mA$
        - `mux_ref`, multiplexer reference output
        - `mux_meas`, multiplexer measurement output
3. Supply Voltages
    - $+10V$ @ $500 \mu W$ ($50 \mu A$)
    - $-5V$ @ $250 \mu W$ ($50 \mu A$)

## Circuit Selection and Design

The multiplexer is used to connect one of the given reference signals to the
reference output and one of the measured signals to the measurement output. The
selection of the required connections is performed by the digital `mode_*`
signals. Because multiple modes use the same measured signal an OR-Gate is used
to connect the measured signal for each of the modes in question.

### Circuit

The switching is performed using a analog bidirectional switch, because the
switching time is fast an reasonable low on resistance can be achieved.
Additionally the switching does not reduce the lifetime of the device as it
would be the case for a mechanical switch like a relay.
Because multiple switches could be closed at the same instance of time, if a
gapping switching behavior is desired, the selection of the modes should also
be implemented in a gapping manner. This can be used to avoid connecting
multiple low resistance sources at the multiplexers input.

### Component Selection

#### Analog Bidirectional Switch

[CD4066BM96] Selection (sort by Price): 4x SPST, SMD, 15V VCC,
$R_{on} <= 250 \Omega$

[CD4066BM96]: https://mou.sr/3MQOnJI

#### OR-Gate

Reuse of already implemented three input or gate from `mode-transition`

## Simulation

TODO: link to simulation files

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Test pins for
    - each individual mode
    - each input and output

### Assembly

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
