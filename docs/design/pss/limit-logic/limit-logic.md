# Limit Logic

TODO: Add visual State indication?

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
        - `power_ok`, signal that the internal power lines of the pss are
        operating
        - `conf_ok`, signal that the configured signals are consistent
2. Voltage output, digital positive logic $U \in [-5V, 10V]$ driving up to $I =
   2.5mA$
    - `mode_vc`, voltage control
    - `mode_lclc`, lower current limit control
    - `mode_uclc`, upper current limit control
    - `mode_cc`, current control
    - `mode_lvlc`, lower voltage level control
    - `mode_uvlc`, upper voltage level control
3. Supply Voltages
    - $+10V$ @ $250mW$ ($25mA$)
    - $-5V$ @ $125mW$ ($25mA$)

!!! info "Power Consumption"
    Power consumption at the supply voltages includes $\approx 15mA$ for output
    drive, $\approx 8mA$ for `compare-logic`, $\approx 1.5mA$ for
    `mode-transition`

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

- Test pins for
    - each individual mode
    - set and reset signal of mode
    - `!mode` signal
    - enable signal

- Disconnectors for
    - Signals from `compare-logic` to `mode-transition`
    - Signals from `mode-transition` to RS-Latches

### Assembly

## Commissioning and Testing

1. Pass tests for `compare-logic`
2. Pass tests for `mode-transition`
3. Pass tests for `limit-logic` itself
4. Connect `compare-logic` to `mode-transition`
5. Connect `mode-transition` to RS-Latches

### Mode Setting

Test ID: `v1.0.0/pss/limit-logic/mode-setting/<suffix>`

Available suffixes: `vc`, `lclc`, `uclc`, `cc`, `lvlc`, `uvlc`

1. Connections
    - Enable connected to $10V$
    - `r_mode_<suffix>` connected to $-5V$
    - `s_mode_<suffix>` connected to $-5V$
2. Power on supply voltage
3. Connect `r_mode_<suffix>` to $10V$
4. Connect `r_mode_<suffix>` to $-5V$
5. Measure Voltage $U_{reset}$ for `mode_<suffix>`
3. Connect `s_mode_<suffix>` to $10V$
4. Connect `s_mode_<suffix>` to $-5V$
5. Measure Voltage $U_{set}$ for `mode_<suffix>`
6. Power off supply voltage
7. Test passed if
    - $U_{reset} < -3V$
    - $U_{set} > 8V$

### Or Gate

Test ID: `v1.0.0/pss/limit-logic/or-gate`

1. Connections
    - Enable connected to $-5V$
2. Power on supply voltage
3. Measure Voltage $U_{\overline{mode}}$
4. Power off supply voltage
5. Test passed if
    - $U_{\overline{mode}} < -3V$
