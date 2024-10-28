# Limit Logic

TODO: Add visual State indication?

## Interface & Requirements

TODO: Add Input specs
TODO: Add Output specs
TODO: Add Power Consumption

1. Voltage Input `ref` & `meas`
    - Voltage Input Swing $V_{in} \in [0V, +5V]$
    - Input Current $| \pm I_{in} | \leq 2.3mA$
2. Voltage output `out`
    - In phase with $V_{ref}$
    - $V_{out} \in [-5V, 10V]$
    - Output current $I_{out \pm} \geq \pm 800 mA$
3. Supply Voltages
    - $+10V$ @ $1W$ ($100mA$)
    - $-5V$ @ $0.5W$ ($50mA$)

## Circuit Selection and Design

The limit logic implements the limit behavior of the powersupplysink. When the
regulated desired target measure is

- voltage, an upper and lower current limit are enforced by the limit logic.
- current, an upper and lower voltage limit are enforced by the limit logic.

The limit logic achieves this by observing the configured limits and references
together with the current measured output quantity and selecting one of six
states:

- `VC` voltage control
- `CC` current control
- `LVLC` lower voltage limit control
- `UVLC` upper voltage limit control
- `LCLC` lower current limit control
- `UCLC` upper current limit control

The states of the limit logic are used to connect the corresponding reference
of the configuration and the corresponding measured output quantity from the
power electronics to the controller.

A transition between states is initiated, when the sub circuit `mode-transition`
detects an event, that is specified to change the mode. An event could be for
example, that the output current exceeds the configured upper current limit and
thus a transition from `VC` voltage control to `UCLC` upper current limit
control is initiated. By design only a maximum of one state can be active at
the same time. The transitions of states can be observed in the
[statemachine](./mode-transition/statemachine.md), which is implemented by the
limit-logic. The transition between states is implemented in a _gapping_
manner, thus for a short duration during the transition none of the states is
active. As `mode-transition` implements an activation of exactly one state for
each possible event this duration during the transition is unstable and not
considered as a separate state.

!!! info "Gapping Mode Transition"
    The _gapping_ mode transition is the opposite of _bridging_ mode transition.
    Gapping mode transition allows to use multiple _SPST_ single pole single
    throw switches to implement a multiplexer for connection of configuration
    and measurement signals to the controller without connecting actively driven
    outputs of the multiplexed sources.
    On the other hand during the gapping period the inputs of the controller sub
    circuit are not connected and left floating, if no default input is provided
    by for example pull up/down resistors.

Events are combinations of _digital_ signals indicating when limits are
exceeded and the relation of the measured output quantity to the configured
reference quantity. To obtain those _digital_ signals from the _analog_
configuration voltages and the measured output quantities the `compare logic`
is used.

### Circuit

The states are represented and stored by using R/S Latches. The state is
considered active, when the output `Q` of the RS-Latch is at high voltage
level. Using an OR gate an active state is detected and used to block other
states from being activated due to the logic of the `mode-transition`.
When an event requires a state transition the `mode-transition` circuit

1. First, resets the active state
2. Second, when no active state is detected the next state is activated by
   setting it.

In case of power/start up or an malformed configuration all the states are
reset and the RS-Latches are disabled (Tri-State).
Thus for all sub circuits the default values set by pull ups/downs takes effect
until start up is completed and the configuration setting is not malformed.

### Component Selection

#### R/S Latches

[CD4043BDR] Quad R/S Latch from 4000 series. Search on Mouser, sort by price.

[CD4043BDR]: https://mou.sr/40mZDFB

#### Or Gate

[CD4078BM96] 8-Input CMOS or Gate from 4000 series. Search on Mouser, sort by
price.

[CD4078BM96]: https://www.ti.com/lit/ds/symlink/cd4078b.pdf

#### Decoupling Capacitor

Reuse of already implemented ceramic X7R 100nF cap.

## Simulation

TODO: link to simulation files

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
TODO: Add test pins
TODO: Add (dic-)connector note, with testcase required for connecting

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
