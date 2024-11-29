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

Test ID: `v1.0.0/pss/digital-interface/isolation/<suffix>`

Available suffix: `GND`, `+5V`

1. Measure Resistance
    - $R_{iso}$ from `<suffix>` to `<suffix>I`
2. Test passed if
    - $R_{iso} > 1 M\Omega$

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
