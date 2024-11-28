# Configuration

## Interface & Requirements

1. SPI Input Interface
    - digital with $U \in [0V, 5V]$
        - `!CS`, input, chip select, low active
        - `!SCLK`, input, serial clock CPHA=0, CPOL=1=`!SCLK`, (CPOL=0=`SCKL`)
        - `SDI`, input, serial data in
        - `SDO`, output, serial data out
2. Voltage output
    - analog with $U \in [0V, 5V]$ with $R < 100 \Omega \forall I < 1mA$
    - analog with $U \in [0V, 5V]$ with $R < 200m \Omega \forall I < 20mA$
        - `conf_vref`, signal of configured reference voltage
        - `conf_iref`, signal of configured reference current
        - `conf_lcl`, signal of configured lower current limit
        - `conf_ucl`, signal of configured upper current limit
        - `conf_lvl`, signal of configured lower voltage limit
        - `conf_uvl`, signal of configured upper voltage limit
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
        - `conf_refselect_v`, signal that the desired reference is voltage
        - `conf_refselect_i`, signal that the desired reference is current
        - `conf_ok`, signal that the configured signals are consistent
    - digital negative logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
        - `!relay_connect`, connect relay output
3. Supply Voltages
    - $+10V$ @ $100mW$ ($10mA$)
    - $-5V$ @ $50mW$ ($10mA$)
    - $+5VA$ @ $250mW$ ($50mA$)

## Circuit Selection and Design

The `conf` sub circuit is used to convert digital serial commands from the `pc`
to analog or digital signals, which are all present in parallel so they can be
accessed by the circuits of the `pss`.

### Circuit

The `conf` sub circuit utilizes a 12-bit digital to analog converter with 8
channels and SPI interface to produce the desired analog signals. The digital
signals are obtained by limiting the allowable configuration range of the
corersponding channels to the maximum and minimum value of the analog
conversion range. Those signals have a range of $U \in [0V, 5V]$ at the DAC
output, but shall be converted to $U \in [-5V, 10V]$ for compatibility with
other sub circuits. The conversion is performed by applying level shifting with
two transistors as amplifiers in emitter configuration.

#### Level Shifter

The emitter configurations of the level shifter each perform a level shift of
one of two voltage levels. The first stage shifts from $U_0 \in [0V, 5V]$ to
$U_1 \in [0V, 10V]$ and the second stage shifts from $U_1$ to $U_2 \in [-5V,
10V]$.

The collector resistances are calculated to allow an appoximate quiescant
currentflow of $I_q \approx 1mA$ during maximal voltage swing $U_{max}$.
$$ R_C = \frac{U_{max}}{I_q} $$

The base resistance is calculated with a large signal current gain of $\beta
\approx 100$, which already includes overdriving of the transistor into
saturation. The voltage is given by the preceeding stage $U_{on}$.
$$ R_B = \frac{U_{on} \beta}{I_q} $$

A pull down resistance of $R = 1 M \Omega$ is added at the input of the first
stage to define the output voltage, in case the DAC output is in tri-state.

#### Config Checker

The programmed configuration is checked for its correctness by the `conf` sub
circuit. A correct configuration is indicated by the `conf_ok` signal. The
correctness of the configuration is determined by:

- If the selected reference is voltage `conf_refselect_v`
    - The upper current limit `ucl` must be greater than the lower current
    limit `lcl`
- If the selected reference is current `conf_refselect_i`
    - The upper voltage limit `uvl` must be greater than the lower voltage
    limit `lvl`

The analog comparison is perfomed by an operational amplifier, which is used as
a comparator. No hysteresis is used, but footprints are provided to place
resistances for a additional hysteresis if required later on.

#### Relay Connect Masking

If the programmed configuration is evaluated as correct and therefore `conf_ok`
is set, the configured state of the output relay `conf_output` is forwarded to
the `relay` sub circuit. If the configuration is not correct, the `relay` sub
circuit is signaled to disconnect. The logic is implemented using a NAND gate.
$$ \text{!relay_connect} = \overline{\text{conf_ok} \land \text{conf_output}} $$

### Component Selection

TODO: Add component selection

## Simulation

TODO: link to simulation files

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.
TODO: Add test pins
TODO: Add (dic-)connector note, with testcase required for connecting

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
