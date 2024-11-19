# Relay

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 1 \Omega \forall |I| < 20A$
        - `in`, current input
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 2 mA$
    load
        - `relay_connect`, connect relay output
2. Voltage output
    - analog with $U \in [0V, 5V]$ with $R < 1 \Omega \forall |I| < 20A$
        - `out`, current output
3. Supply Voltages
    - $+10V$ @ $1.2W$ ($120mA$)
    - $-5V$ @ $0.6W$ ($120mA$)

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

A simulation with a model of the relay coil is given in `./relay.asc`.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Add test pins for: `relay_connect`, `in`, `out`

## Commissioning and Testing

### Switch On

Test ID: `v1.0.0/pss/relay/switch/on`

1. Connections
    - Input `relay_connect` connected to $U = 10V$
2. Power on supply voltage
3. Measure resistance
    - $R$ from `in` to `out`
4. Power off supply voltage
5. Test passed if
    - $R < 100 m \Omega$

### Switch Off

Test ID: `v1.0.0/pss/relay/switch/off`

1. Connections
    - Input `relay_connect` connected to $U = -5V$
2. Power on supply voltage
3. Measure resistance
    - $R$ from `in` to `out`
4. Power off supply voltage
5. Test passed if
    - $R > 1 M \Omega$
