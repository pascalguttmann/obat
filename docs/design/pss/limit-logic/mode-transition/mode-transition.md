# Mode Transition

## Interface & Requirements

1. Voltage inputs
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
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
    subcircuit could reduce the power consumption.

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
