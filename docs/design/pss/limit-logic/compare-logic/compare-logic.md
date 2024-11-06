# Compare Logic

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 1 \Omega \forall I < 1mA$
        - `conf_vref`, signal of configured reference voltage
        - `conf_iref`, signal of configured reference current
        - `conf_lcl`, signal of configured lower current limit
        - `conf_ucl`, signal of configured upper current limit
        - `conf_lvl`, signal of configured lower voltage limit
        - `conf_uvl`, signal of configured upper voltage limit
    - analog with $U \in [0V, 5V]$ with $R < 10 \Omega \forall I < 1mA$
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

## Commissioning and Testing

1. Pass tests for `compare-logic`
    - This will also test the functionality of the sub circuits
    `window-comparator` to avoid unnecessary usage of connectors.

### Upper Voltage Limit

Test ID: `v1.0.0/pss/limit-logic/compare-logic/upper-voltage-limit/<suffix>`

Available suffixes: `window-comparator0`, `window-comparator1`,
`window-comparator2`, `window-comparator3`

1. Connections
    - Input `meas` of the window-comparator $U=5V$
    - Input `ul` and `ll` of the window-comparator $U=0V$
2. Power on supply voltage
3. Measure Voltages
    - $V_{ule}$ at net `ule` of the window-comparator
    - $V_{!lle}$ at net `!lle` of the window-comparator
4. Power off supply voltage
5. Test passed if
    - $V_{ule} > 8V$ at net `ule` of the window-comparator
    - $V_{!lle} > 8V$ at net `!lle` of the window-comparator

### Lower Voltage Limit

Test ID: `v1.0.0/pss/limit-logic/compare-logic/lower-voltage-limit/<suffix>`

Available suffixes: `window-comparator0`, `window-comparator1`,
`window-comparator2`, `window-comparator3`

1. Connections
    - Input `meas` of the window-comparator $U=0V$
    - Input `ul` and `ll` of the window-comparator $U=5V$
2. Power on supply voltage
3. Measure Voltages
    - $V_{ule}$ at net `ule` of the window-comparator
    - $V_{!lle}$ at net `!lle` of the window-comparator
4. Power off supply voltage
5. Test passed if
    - $V_{ule} < -3V$ at net `ule` of the window-comparator
    - $V_{!lle} < -3V$ at net `!lle` of the window-comparator

### AND OR Select Gate

Test ID: `v1.0.0/pss/limit-logic/compare-logic/and-or-select-gate/<suffix>`

Available suffixes: `conf_refselect_v`, `conf_refselect_i`

1. Connections
    - Input `meas` of the window-comparator0 $U=0V$
    - Input `meas` of the window-comparator1 $U=5V$
    - Input `ul` and `ll` of the window-comparator0 $U=5V$
    - Input `ul` and `ll` of the window-comparator1 $U=0V$
    - `conf_refselect_*` $U=-5V$
2. Power on supply voltage
3. Connect `<suffix>` _conf_refselect_ signal to $U=10V$
4. Measure Voltages
    - $U_{comp_mgtt}$
    - $U_{comp_mstt}$
5. Power off supply voltage
6. Test passed if
    - `<suffix>` is `conf_refselect_v`
        - $U_{comp_mgtt} < -3V$
        - $U_{comp_mstt} > 8V$
    - `<suffix>` is `conf_refselect_i`
        - $U_{comp_mgtt} > 8V$
        - $U_{comp_mstt} < -3V$
