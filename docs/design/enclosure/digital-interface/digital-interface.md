# Digital Interface

## Interface & Requirements

1. SPI Input Interface
    - digital with $U \in [0V, 5V]$ relative to isolated ground `GNDI`
    isolation voltage max $V_{iso} = 500V$
        - `!CS_ISO`, input, chip select, low active
        - `SCLK_ISO`, input, serial clock CPHA=0, CPOL=0=`SCKL`
        - `SDI_ISO`, input, serial data in
        - `SDO_ISO`, output, serial data out
2. SPI Output Interface
    - digital with $U \in [0V, 5V]$
        - `!CS`, input, chip select, low active
        - `SCLK`, input, serial clock CPHA=0, CPOL=0=`SCKL`
        - `SDI`, input, serial data in
        - `SDO`, output, serial data out
3. Supply Voltages
    - $+5V$ @ $200mW$ ($40mA$)

## Circuit Selection and Design

The digital-interface sub circuit is used to isolate the external SPI bus from
the internal SPI bus to achieve isolated operation of the power supply sink.

### Circuit

A quad channel digital isolator is used to isolate the SPI signals. The
isolator has the four inputs distributed 3 to 1, so that

- `!CS`, `SCKL` and `SDI` are transferred from the external SPI bus to the
internal SPI bus
- `SDO` is transferred from the internal SPI bus to the external SPI bus

To deliver an isolated 5V voltage an isolated regulated 5V to 5V DCDC-converter
is used.

The components are decoupled by capacitors as described in the datasheets.

#### Protection Circuit

For protection from electrostatic discharge (ESD) at the connectors transient
voltage suppressor diodes are used to limit the voltage in case of an ESD
event.

The isolated 5V voltage at the output of the DCDC-converter is protected from
exceeding the specifications of the digital isolator by usage of a zener diode
to limit the voltage and if necessary provide a small load current to reduce
the output voltage of the DCDC-converter.
To lower switching noise from the DCDC-converter the output of the converter is
loaded with a resistive load of $R=330 \Omega$, which will load the output with
approximately $15mA$.

The isolated ground is connected via a $1 M \Omega$ resistor to the ground of
the rest of the pcb to avoid electrostatic charge to built up on the isolated
net. This will cause a small current flow in case the voltage at the isolated
ground is not equal to the ground voltage.

#### Rise Time Limitation

In order to avoid high-frequency signal components, that are present in signals
with short rising time, the outputs of the digital-interface are low pass
filtered by a first order low pass filter. The filter is realized by a RC
network. Which is set to give a rise time of of $T_{rise,10-90} \approx 100ns$,
which results in a required time constant $\tau = \frac{T_{rise,10-90}}{2.2}
\approx 47 ns$. This time constant can be achieved by setting the values:

$$ R = 100 \Omega \quad \land \quad C = 470 pF $$

### Component Selection

#### Digital Isolator

Search on Mouser for: [Si8641BD-B-IS2](https://mou.sr/3VdrQv2)

- Digital Isolator IC
- 4 Channel, (3 in, 1 out)
- propagation delay < 10ns
- SMD mounting, (hand solderable friendly)
- Sort by Price

#### DCDC-converter

Search on Mouser for: [R05C05TE05S](https://mou.sr/4eUT3cS)

- DCDC-converter
- isolated
- regulated output
- $5V$ input, $5V$ output
- output power $P \in [100mW, 1W]
- SMD mounting, (hand solderable friendly)
- Sort by Price

#### Zener Diode

Search on Mouser for: [PDZ5.6B,115](https://mou.sr/3B8nGxS)

- Zener Diode
- Zener voltage $5.6V \pm 2 \%$
- SMD mounting, (hand solderable friendly)
- Sort by Price

#### TSV Diode

Search on Mouser for: [NUP1301,215](https://mou.sr/41gzskh)

- ESD Protection Diode / TVS Diode
- Unidirectional Polarity
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
- Add test pins for:
    - isolated 5V `+5VI`
    - isolated GND `GNDI`
    - SPI ISO signals
    - SPI signals

### Assembly

## Commissioning and Testing

### Isolation

Test ID: `v2.0.0/pss/digital-interface/isolation/<suffix>`

Available suffix: `GND`, `+5V`

1. Measure Resistance
    - $R_{iso}$ from `<suffix>` to `<suffix>I`
2. Test passed if
    - $R_{iso} > 100 k\Omega$

### Low State

Test ID: `v1.0.0/pss/digital-interface/low/<suffix>`

Available suffix: `!CS`, `SCKL`, `SDI`, `SDO`

1. Connections
    - Input `<suffix>` connected to $U_{in} = 0V$ (with respect to local ground)
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ at output of `<suffix>` (with respect to local ground of output)
4. Power off supply voltage
5. Test passed if
    - $U_{out} < 1V$

### High State

Test ID: `v1.0.0/pss/digital-interface/high/<suffix>`

Available suffix: `!CS`, `SCKL`, `SDI`, `SDO`

1. Connections
    - Input `<suffix>` connected to $U_{in} = 5V$ (with respect to local ground)
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ at output of `<suffix>` (with respect to local ground of output)
4. Power off supply voltage
5. Test passed if
    - $U_{out} > 4V$
