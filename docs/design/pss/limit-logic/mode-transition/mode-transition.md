# Mode Transition

## Interface & Requirements

1. Voltage inputs, digital positive logic with $U \in [-5V, 10V]$, driving up
   to $I = 1 mA$ load
    - `conf_refselect_v`, signal that the desired reference is voltage
    - `conf_refselect_i`, signal that the desired reference is current
    - `power_ok`, signal that the internal power lines of the pss are
    operating
    - `conf_ok`, signal that the configured signals are consistent
    - `!mode`, signal that no mode is active (all RS-Latches are reset)
    - `comp_lcle`, signal that lower current limit exceeded
    - `comp_ucle`, signal that upper current limit exceeded
    - `comp_lvle`, signal that lower voltage limit exceeded
    - `comp_uvle`, signal that upper voltage limit exceeded
    - `comp_mstt`, signal that measured is smaller than target reference
    - `comp_mgtt`, signal that measured is greater than target reference
2. Voltage output, digital positive logic $U \in [-5V, 10V]$ driving up to $I =
   2.5mA$
    - `enable_ok`, signal that RS-Latches can be enabled and actively drive the
    output
    - `s_mode_vc`, signal set mode voltage control
    - `s_mode_lclc`, signal set mode lower current limit control
    - `s_mode_uclc`, signal set mode upper current limit control
    - `s_mode_cc`, signal set mode current control
    - `s_mode_lvlc`, signal set mode lower voltage limit control
    - `s_mode_uvlc`, signal set mode upper voltage limit control
    - `r_mode_vc`, signal reset mode voltage control
    - `r_mode_lclc`, signal reset mode lower current limit control
    - `r_mode_uclc`, signal reset mode upper current limit control
    - `r_mode_cc`, signal reset mode current control
    - `r_mode_lvlc`, signal reset mode lower voltage limit control
    - `r_mode_uvlc`, signal reset mode upper voltage limit control
3. Supply Voltages
    - $+10V$ @ $15mW$ ($1.5mA$)
    - $-5V$ @ $7.5mW$ ($1.5mA$)

!!! info "Power Consumption"
    Power consumption at the supply voltages includes $\approx 1mA$ for the
    internal discrete inverter. A reuse of another integrated inverter from a
    sub circuit could reduce the power consumption.

## Circuit Selection and Design

The mode-transition sub circuit implements a boolean function. Boolean input
arguments are the comparator outputs of the `compare-logic`, which indicate the
events mentioned in `limit-logic`, for which a state transition should be
performed. Additionally, boolean configuration is used as an input to the sub
circuit.
The outputs indicate with a set and reset signal, which states represented by
the RS-Latches should be set and reset.

To ensure that only one of the RS-Latches is active at maximum the gapping
transition is implemented by only allowing to set any state, when the
_transition is ready_, implying that no RS-Latch is active at the moment.
Because every transition has a short duration in which all the RS-Latches are
not set, for every possible event at the inputs exactly one state should be set
to uniquely determine which state should be set during the transition.
Exceptions can be made for events which are excluded by design of the circuit
to optimize the logic circuit for cost efficiency.
Because a transition can only be started with a reset of the currently active
state the transition can also be constrained to only start from certain states,
by only applying a reset to some states for a given event.

!!! info "State Transition Example"
    A transition from state A to B can be performed by

    1. Reset State A
    2. Detect, that all states are inactive
    3. Set State B

    For Robustness State B can be set for multiple possible events, to activate
    the state, when all states are inactive. A transition from starting from a
    state C, from which the transition to A should *not* be started can be
    prohibited, by *not* applying a reset to state C.

During startup or when the configuration is not consistent all states in the
RS-Latches are reset at the same time ensuring a consistent state in the
RS-Latches.

The encoded mode-transitions are documented in
[`./truth-table-mode-set-reset.xlsx`](./truth-table-mode-set-reset.xlsx).

### Circuit

The boolean function can be implemented using a memory IC with parallel
interface. The inputs of the function can address a stored word, which contains
in the bits the states of the outputs. While this approach offers flexibility
and implementation of arbitrary functions it is more costly for the
implementation of the desired transitions, because by applying boolean algebra
the function can also be represented by using a few standard logic gates.
Additionally, the programming step of the memory can be avoided by providing
the logic function through the wiring of the logic gates.

The logic is implemented using `AND`, `OR` and `INVERTER` gates. The cost is
optimized manually by combining multiple input signals with a single gate and
reusing the signal. The combination introduces some events, which for example
set multiple states, which is not desired. Therefore it is ensured by the
circuit design, that those events can never occur:

- `MSTT` and `MGTT` are mutually excluded by the design of the
`window-comparator`.
- `LCLE` and `UCLE`, `LVLE` and `UVLE` are mutually excluded by the
`config-checker`, which checks that the lower limit is always below the upper
limit, if the configuration does not obey this constraints the entire state
machine is reset. The `window-comparator` ensures for correctly configured
limits, that not both are active at the same time.
- `conf_refselect_v` and `conf_refselect_i` are mutually excluded by the check
of the `config-checker`.

TODO: config-checker, implemnt config-checker

### Component Selection

#### Logic Gates

The logic gates are selected from the 4000 series with a search on mouser,
preferred SOIC packaging and sorted by price.

| Gate               | IC      |
| :----------------- | :------ |
| Quad 2-input AND   | CD4081B |
| Triple 3-input AND | CD4073B |
| Triple 3-input OR  | CD4075B |
| Hex inverter       | CD4069B |

#### Decoupling Capacitor

Reuse of already implemented ceramic X7R 100nF cap.

## Simulation

Simulation example can be found in `./sim_mode-transition.asc`.
Hierarchical simulation block is available as `./mode-transition.asc` and
`./mode-transition.asy`.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Test pins for
    - each individual mode set/reset
    - `!mode` signal
    - `enable_ok` signal
    - `!enable_ok` signal
    - `power_ok` signal

## Commissioning and Testing

1. Pass tests for `mode-transition`

### State Reset

Test ID: `v1.0.0/pss/limit-logic/mode-transition/state-reset`

1. Connections
    - `conf_ok` $U = -5V$
    - `power_ok` $U = 10V$
2. Power on supply voltage
3. Measure Voltage
    - $U_{s\_mode\_*}$
    - $U_{r\_mode\_*}$
    - $U_{enable\_ok}$
    - $U_{\overline{enable\_ok}}$
4. Power off supply voltage
5. Test passed if
    - $U_{s\_mode\_*} < -3V$
    - $U_{r\_mode\_*} > 8V$
    - $U_{enable\_ok} < -3V$
    - $U_{\overline{enable\_ok}} > 8V$
