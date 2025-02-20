# Digital Analog Converter

!!! info "Configuration Options"
    To obtain information, which DAC channels configures which feature please
    see [`./channel_map.md`](./channel_map.md).

!!! warning "AD5672R"
    To daisy chain AD5672R it is necessary to be able to transfer 24-bit data
    into the device with a *single* spi transfer. This is required to enable
    daisychain mode. Before daisychain mode is enabled only the first 24-bit of
    each transfer are used.
    This can be achieved by prepending a 24-bit shift register in front of the
    first AD5672R in the chain of consecutive AD5672R. (Setting data into the
    shift register with longer transfer, followed by a 24-bit transfer).
    For detailed technical background please refer to:
    [`./sw/pc/obat_pc_spi/device_implementation/dac/ad5672/functional_operations.py`](https://github.com/pascalguttmann/obat_pc_spi/blob/main/device_implementation/dac/ad5672/functional_operations.py)

## Interface & Requirements

1. SPI Input Interface
    - digital with $U \in [0V, 5V]$
        - `!CS`, input, chip select, low active
        - `SCLK`, input, serial clock CPHA=0, CPOL=0=`SCKL`
        - `SDI`, input, serial data in
        - `SDO`, output, serial data out
2. Voltage output
    - 8x analog with $U \in [0V, 5V]$ with $R < 200m \Omega \forall I < 20mA$
3. Supply Voltages
    - $+10V$ @ $100mW$ ($10mA$)
    - $-5V$ @ $50mW$ ($10mA$)
    - $+5VA$ @ $250mW$ ($40mA$)

## Circuit Selection and Design

The `dac` sub circuit is used to convert digital serial commands from the `pc`
to analog or digital signals, which are all present in parallel so they can be
accessed by the circuits.

### Circuit

The `dac` sub circuit utilizes a 12-bit digital to analog converter with 8
channels and SPI interface to produce the desired analog signals. The digital
signals are obtained by limiting the allowable configuration range of the
corresponding channels to the maximum and minimum value of the analog
conversion range.

#### Rise Time Limitation

In order to avoid high-frequency signal components, that are present in signals
with short rising time, the outputs of the digital-interface are low pass
filtered by a first order low pass filter. The filter is realized by a RC
network. Which is set to give a rise time of of $T_{rise,10-90} \approx 100ns$,
which results in a required time constant $\tau = \frac{T_{rise,10-90}}{2.2}
\approx 47 ns$. This time constant can be achieved by setting the values:

$$ R = 100 \Omega \quad \land \quad C = 470 pF $$

### Component Selection

#### DAC

Search on Mouser for: [AD5672RBRUZ](https://mou.sr/419AKxw)

- DAC, Voltage Buffered Output
- 8 channels
- Resolution >= 2 bit
- Interface: SPI
- Package: SMD (hand solderable)
- sort by price

## Simulation

Not available.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
- Test pins for
    - all DAC outputs

### Assembly

## Commissioning and Testing

### DAC

Test ID: `v1.0.0/pss/conf/dac/conf-ok`

1. Power on supply voltage
2. Configure DAC with
    - Channel 0: 0xCCC
    - Channel 1: 0xCCC
    - Channel 2: 0xCCC
    - Channel 3: 0xCCC
    - Channel 4: 0xCCC
    - Channel 5: 0xCCC
    - Channel 6: 0xCCC
    - Channel 7: 0xCCC
3. Measure
    - $U_{ch,i}$
4. Power off supply voltage
5. Test passed if
    - $U_{ch,i} \in 4V \pm 10mV \forall i \in [0, 7]$
