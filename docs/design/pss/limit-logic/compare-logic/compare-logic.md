# Compare Logic

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
2. Voltage output, digital positive logic $U \in [-5V, 10V]$ driving up to $I =
   2.5mA$
    - `comp_mgtt`, measured greater than target
    - `comp_mstt`, measured smaller than target
    - `comp_lvle`, lower voltage level exceeded
    - `comp_uvle`, upper voltage level exceeded
    - `comp_lcle`, lower current level exceeded
    - `comp_ucle`, upper current level exceeded
3. Supply Voltages
    - $+10V$ @ $80mW$ ($8mA$)
    - $-5V$ @ $40mW$ ($8mA$)

## Circuit Selection and Design

The compare-logic is used to compare the measured output voltage and current
with the configured limits and reference to generate digital signals used by
the `mode-transition`. The digital output signals indicate, that a configured
level of voltage or current is exceeded. Additionally the outputs indicate,
whether the measured quantity is greater or smaller than the set target
reference.

In order to compare the measured quantities with the configured limit the
`window-comparator` sub circuit is used for analog comparison. To convert all
signals to positive logic an inverter gate is used for the desired signals.

Depending on the configuration of `conf_refselect_*` the quantity (voltage or
current) used for comparison of the measured  quantity and the set target
reference is different. Both combinations are compared in parallel and the
digital signal is selected depending on the configuration of
`conf_refselect_*`.

### Circuit

The selection of the digital signals used to provide `comp_mgtt` and
`comp_mstt` is performed by utilizing an _and/or select gate_. A inconsistent
configuration of `conf_refselect_*` is not checked in this sub circuit. The
output of `comp_mstt` and `comp_mgtt` will be the logical _OR_ combination of
both selectable comparison results. circuit using the `compare-logic` should
tolerate this behavior, avoid inconsistent configuration and/or perform
additional consistency checks if required.

### Component Selection

#### AND/OR Select Gate

[CD4078BM96] 8-Input CMOS or Gate from 4000 series. Search on Mouser, sort by
price.

[CD4078BM96]: https://www.ti.com/lit/ds/symlink/cd4019b.pdf

#### Inverter

Reuse of already implemented hex inverter from `mode-transition`

## Simulation

TODO: link to simulation files

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Test pins for
    - each individual input
    - each individual output

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
