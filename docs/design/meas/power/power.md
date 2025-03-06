# Power

TODO: Adapt $R_{1001} \approx 2.3 \Omega$ for enhanced current sharing

## Interface & Requirements

1. Voltage inputs
    - 24V Power Supply
2. Voltage output
    - 5V Power Supply (150mA)
3. Supply Voltages
    - 24V (150mA)

## Circuit Selection and Design

Linear regulators are used to create the voltage level of 5V.

### Circuit

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
- Working voltage $U = 24V$
- Diode Capacitance $C \leq 1pF$
- SMD mounting (hand solderable)
- sort by price

## Simulation

Not available.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
- Add test pins for: `5V`
- Place regulator on $A=800mm^2$ of copper fill for thermal relief
    - e.g. square on top and bottom with $d_\square = 20mm$ stitched by thermal
    vias
- TSV diodes shall be placed close (at best without vias) at the ESD source for
more specific hints see
[TI-ESD-Layout](https://www.ti.com/lit/an/slva680a/slva680a.pdf?ts=1732384419368)

### Assembly

## Commissioning and Testing

### Output Voltage 5V

Test ID: `v1.0.0/meas/power/output-voltage/5V`

1. Connections
    - $U_{in} = 24V$
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ Output voltage of regulator
4. Power off supply voltage
5. Test passed if
    - $U_{out} \in 5V \cdot (1 \pm 10\%)$

### Output Voltage Ripple 5V

Test ID: `v1.0.0/meas/power/output-voltage-ripple/5V`

1. Connections
    - $U_{in} = 24V$
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ Output voltage of regulator with oscilloscope for 500ms
4. Power off supply voltage
5. Test passed if
    - $\Delta U_{out} = max(U_{out}) - min(U_{out}) \leq 100mV$
