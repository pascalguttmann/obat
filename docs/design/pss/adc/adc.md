# Analog Digital Converter

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 50 \Omega \forall I < 5 \mu A$
        - `AIN_P`, analog input
2. SPI Output Interface
    - digital with $U \in [0V, 5V]$
        - `!CS`, input, chip select, low active
        - `SCLK`, input, serial clock CPHA=0, CPOL=0=`SCKL`
        - `SDI`, input, serial data in
        - `SDO`, output, serial data out
3. Supply Voltages
    - $+5V$ @ $50mW$ ($10mA$)

## Circuit Selection and Design

The analog-digital-converter (ADC) is used to convert an analog signal in the
range of $U_{in} \in [0V, 5V]$ in a digital signal by quantization in amplitude
and discretization in time.

The ADC features a digital SPI interface to be read by the `pc`.

### Circuit

The adc is connected with decoupling capacitors at its power supplies and
reference pins as described in the datasheet.

Additionally, the reset pin $\overline{RST}$ is tied high either by

- a RC lowpass filter ($\tau = 1ms$) to allow for delay startup, when the
  device powers up or
- a direct connection to allow for instanteneous startup.

A low power led is used at the general purpose output for debugging purposes. A
current of $I_f \approx 500 \mu A$ is set by the series resistance in order to
not exceed the pins output current specification.
While the LED might be less bright it should still be visible in ambient indoor
lighting conditions. The use of a current amplifying transistor is avoided in
order to reduce the amount of components used.

The analog input of the adc is filtered with a firsto order RC low pass filter
to avoid aliasing. (Additionally, to the second order low pass filter $f_{-3dB,
internal} \approx 15kHz$ included in the adc.) The cutoff frequency of the low
pass filter is selected at $f_{-3dB} \approx f_{-3dB, internal}$. The cutoff
frequency establishes a connection between the selected total series resistance
and the capacitance:
$$ C = \frac{1}{2\pi f_{-3dB} R} $$

The total series resitance is limited by the acceptable error introduced by the
voltage divider formed by the intrinsic, parasitic resistance of the adc analog
input and the external series resistance. To keep the error in the range of one
LSB at full scale, the total series resistance should not exceed:
$$ R \lessapprox \frac{R_{in}}{n_{resolution}} = \frac{1M\Omega}{2^{12}}
\approx 250 \Omega $$

Therefore the values for $R$ and $C$ can be selected as:
$$ R = 200 \Omega \quad \land \quad C = 47nF $$

### Component Selection

#### ADC

Search on mouser for: [ADS8665](https://mou.sr/4eQgioK)

- ADC
- Resolution >= 12-bit
- sampling rate >= 500kHz
- SPI interface with daisychain option
- single ended input $0V$ to $5V$
- internal voltage reference
- package: smd handsolderable
- family: prefer adc with pin compatible "upgrades" (higher resolution and
sampling rate)
- Sort by price

## Simulation

For the adc sub circuit no simulation is conducted, as the SPI interface is not
subject to simulation, which focuses on the analog circuit.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
- Add test pins for:
    - analog input and analog measurement ground.
    - Refio
    - GPO

### Assembly

## Commissioning and Testing

### Conversion

Test ID: `v1.0.0/pss/adc/conversion/<suffix>`

Available suffix: `0V`, `3V`, `5V`

1. Power on supply voltage
2. Connections
    - Input `AIN_P` connected to $U_{in} = <suffix>$
3. Measure Voltages with ADC via SPI interface
    - $n_{U_{in}}$
4. Power off supply voltage
5. Test passed if
    - $n_{U_{in}} \in \frac{<suffix>}{5V} 2^{12} \cdot \pm 41$
