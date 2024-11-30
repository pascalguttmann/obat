# Power

## Interface & Requirements

TODO: Add Input specs
TODO: Add Output specs
TODO: Add Power Consumption

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 20mA$
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
2. Voltage output
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 20mA$
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
3. Supply Voltages
    - $+10V$ @ $1W$ ($100mA$)
    - $-5V$ @ $0.5W$ ($50mA$)

## Circuit Selection and Design

A voltage regulator is used to output $U = 5V$ from the input of $U = 10V$. The
regulator used is a non-switching regulator, which exhibits improved ripple
characteristics compared to switching voltage regulators, because the device
operates continuously. The disadvantage of increased power loss, due to low
efficiency is tolerable in this application as the required current is
relatively low $I < 100mA$.

### Circuit

The voltage regulator has an approximate maximal power dissipation of

$ P = \Delta U \cdot I = (10V - 5V) 100mA = 500mW $

The specified maximal junction temperature is $T_{J,max} = 150 °C$. In order to
avoid usage above the specification and to achieve an increase of the
components lifetime the planned maximally reached junction temperature during
the operation is set to be $T_J = 100 °C$. Assuming a maximal ambient
temperature of $T_{amb} = 50°C$ the maximal tolerable thermal resistance
(junction-to-air) $R_{\Theta,JA}$ for a dissipation of $P$ can be calculated.

$$ R_{\Theta,JA} < \frac{T_J - T_{amb}}{P} = \frac{100 °C - 50°C}{500mW} = 100
\frac{K}{W} $$

When modelling the heat transfer of a pcb up to an approximate area of $4.5
\text{in}^2$ the thermal resistance can be modelled using (Source: [TI-Thermal])

- $R_{PCB,2 \text{Oz},1\text{in}^2} \approx 100 \frac{K}{W}$ for a copper
thickness of $2 \frac{\text{Oz}}{\text{in}^2}$ at and area of one square inch
- $R_{PCB,1 \text{Oz},1\text{in}^2} \approx 125 \frac{K}{W}$ for a copper
thickness of $2 \frac{\text{Oz}}{\text{in}^2}$ at and area of one square inch

Therefore an approximate area of
$$ A = \frac{R_{PCB,1 \text{Oz},1\text{in}^2}}{R_{\Theta,JA}} = 1.25
\text{in}^2 \approx 800 mm^2 $$

is needed to provide adequate thermal relief. The area can be split up to the
top and bottom plane, at which it than can be realized as two squares with
side length:

$$ d_\square = \sqrt{\frac{A}{2}} = 20 mm $$

Of course the regulator can also be placed on a much greater ground plane to
achieve the minimum area $A$.

[TI-Thermal]: https://www.ti.com/lit/an/slpa015/slpa015.pdf?ts=1732986483715&ref_url=https%253A%252F%252Fduckduckgo.com%252F

The voltage regulator is decoupled using capacitors as specified in the
datasheet and protected against reverse currents by a diode.

### Component Selection

#### Voltage Regulator

Search on Mouser for: [MC7805BDTG](https://mou.sr/4eRkZ1s)

- Linear Voltage Regulator
- positive Voltage out $+5V$
- output current $I \in [100mA, 1A]$
- single channel
- fixed output type
- Smd mounting (hand solderable)
- sort by price

## Simulation

TODO: link to simulation files

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
TODO: Add test pins
TODO: Add (dic-)connector note, with testcase required for connecting
- Place regulator on $A=800mm^2$ of copper fill for thermal relief
    - e.g. square on top and bottom with $d_\square = 20mm$ stitched by thermal
    vias

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
