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
    - $+5V$ ($10mA$) for the master / controller side of the digital-interface
    - $+5V$ ($10mA$) for the slave / peripheral side of the digital-interface

The master and slave side power supply are isolated in the digital-interface
and can therefore be supplied by a isolated dc/dc converter to achieve
bidirectional isolated communication.

## Circuit Selection and Design

The digital-interface sub circuit is used to isolate the external SPI bus from
the internal SPI bus to achieve isolated operation of the power supply sink.

### Circuit

A quad channel digital isolator is used to isolate the SPI signals. The
isolator has the four inputs distributed 3 to 1, so that

- `!CS`, `SCKL` and `SDI` are transferred from the external SPI bus to the
internal SPI bus
- `SDO` is transferred from the internal SPI bus to the external SPI bus

The components are decoupled by capacitors as described in the datasheets.

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

Test ID: `v1.0.0/meas/digital-interface/isolation/<suffix>`

Available suffix: `GND`, `+5V`

1. Measure Resistance
    - $R_{iso}$ from `<suffix>` to `<suffix>I`
2. Test passed if
    - $R_{iso} > 100 k\Omega$

### Low State

Test ID: `v1.0.0/meas/digital-interface/low/<suffix>`

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

Test ID: `v1.0.0/meas/digital-interface/high/<suffix>`

Available suffix: `!CS`, `SCKL`, `SDI`, `SDO`

1. Connections
    - Input `<suffix>` connected to $U_{in} = 5V$ (with respect to local ground)
2. Power on supply voltage
3. Measure Voltages
    - $U_{out}$ at output of `<suffix>` (with respect to local ground of output)
4. Power off supply voltage
5. Test passed if
    - $U_{out} > 4V$
