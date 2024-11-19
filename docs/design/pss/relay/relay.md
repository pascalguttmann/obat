# Relay

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

The `relay` sub circuit is used to (dis-)connect the output of the power supply
sink. A electromechanical relay is used to connect the output, because it when
the relay is closed the resistance in the path is small $< 100 m \Omega$.

### Circuit

A non latching (monostable) relay is used in order to avoid inconsistent
states, when the output is configured to be connected or disconnected and the
relay might be in a different (bi-)stable state from other configurations.
The relay is powered by using a NPN transistor to allow the required current
flow through the relay coil.
The relay coil requires approximately $I_{coil} \approx 120mA$ of current,
which will be the collector current of the transistor. With a given current
gain of $\beta > 200$, the minimum required base current is approximately $I_b
\frac{I_{coil}}{\beta} \approx 600 \mu A$. To certainly achieve the desired
current flow, the base current can be further increased to saturate the
transistor. A factor of $n \approx 2$ is selected by experience. The base
resistor voltage drop can be calculated from the maximal input voltage
$U_{relay\_connect} = 10V$ of the digital signal, the minimal input voltage
$U_{min} = -5V$ of the input signal and the base emitter voltage $V_{BE,on}
\approx 1V$ from the transistor datasheet. From the voltage drop the resistance
required to allow a certain base current to flow can easily be deduced by

$$ R_B = \frac{U_{relay\_connect} - V_{BE,on} - U_{min}}{I_b \cdot n} \approx
10k \Omega $$

The collector resistor is used to reduce the voltage drop at the relay coil
from $\approx 15V$ to $\approx 12V$ as required per the datasheet. When
neglecting the collector emitter saturation voltage during the excited state of
the coil a voltage drop of $U_{RC} = 15V - 12V = 3V$ shall be obtained at the
collector current $I_{coil}$. Therefore the resistance can be calculated as
follows

$$ R_C \approx \frac{U_{RC}}{I_{coil}} \approx 22 \Omega $$

A pull down resistor of $R = 1 M \Omega$ is used to keep the transistor in cut
off in case no input signal is connected to the digital input.

A flyback diode is connected antiparallel to the relay coil in order to limit
the voltage induced by the coil, when the transistor is quickly turned off.

### Component Selection

#### Relay

[ALFG2PF12] Electromechanical relay search on Mouser:

- Non-latching, DC coil, normally open SPST
- Current $>25A$
- Coil Voltage $12V$
- Sort by Price

[ALFG2PF12]: https://mou.sr/3UXyMwc

#### Flyback Diode

Reuse of already implemented diode from the `controller` _anti integral windup_
feature.

#### Transistor

Reuse of already implemented smd transistor of the `bias` stage.

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
