# Power

TODO: Increase output capacitor for enhanced transient response

## Interface & Requirements

1. Voltage inputs
    - 10V Power Supply
    - -5V Power Supply
2. Voltage output
    - 5V Power Supply
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
        - `power_ok`, signal that power rails are ok
3. Supply Voltages
    - $+10V$ @ $1W$ ($100mA$)
    - $+5V$ @ $500mW$ ($100mA$)

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

#### Power Checker

A checker, whether the power rails are present is implemented by a RC low pass
filter with $\tau = 1ms$. This allows for a short delay, when the power is
switched on.

#### Protection Circuit

For protection from electrostatic discharge (ESD) at the connectors transient
voltage suppressor diodes are used to limit the voltage in case of an ESD
event.

Fuses are used to limit the maximum current and break the circuit in case of
prolonged over current faults.

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

#### Fuse (and Socket)

Search on Mouser for: [0287030.PXCN](https://mou.sr/4g1gvqn) and
[178.6165.0002](https://mou.sr/41i6eSk)

- Thermal Fuse / Fuse Socket
- Automotive ATO Fuse (for easy replacement option)
- Nominal Current 30 A
- Sort by Price

#### TSV Diode

Search on Mouser for: [UDD32C15L01](https://mou.sr/49jd2AR)

- ESD Protection Diode / TVS Diode
- Bidirectional Polarity
- Working voltage $U = 15V$
- Diode Capacitance $C \leq 1pF$
- SMD mounting (hand solderable)
- sort by price

## Simulation

Not available.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
- Add test pins for: `10V`, `5V`
- Place regulator on $A=800mm^2$ of copper fill for thermal relief
    - e.g. square on top and bottom with $d_\square = 20mm$ stitched by thermal
    vias
- TSV diodes shall be placed close (at best without vias) at the ESD source for
more specific hints see
[TI-ESD-Layout](https://www.ti.com/lit/an/slva680a/slva680a.pdf?ts=1732384419368)

### Assembly

## Commissioning and Testing

### Output Voltage

Test ID: `v1.0.0/pss/power/output-voltage`

1. Connections
    - $U_{in} = 10V$ Input connected to 10V
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ Output voltage of regulator
4. Power off supply voltage
5. Test passed if
    - $U_{out} \in 5V \cdot (1 \pm 10\%)$

### Output Voltage Ripple

Test ID: `v1.0.0/pss/power/output-voltage-ripple`

1. Connections
    - $U_{in} = 10V$ Input connected to 10V
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ Output voltage of regulator with oscilloscope for 500ms
4. Power off supply voltage
5. Test passed if
    - $\Delta U_{out} = max(U_{out}) - min(U_{out}) \leq 100mV$
