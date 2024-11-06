# Window Comparator

## Interface & Requirements

1. Voltage inputs
    - analog with $U \in [0V, 5V]$ with $R < 1 \Omega \forall I < 1mA$
        - `ul` upper limit
        - `ll` lower limit
    - analog with $U \in [0V, 5V]$ with $R < 10 \Omega \forall I < 250\mu A$
        - `meas` measured quantity
2. Voltage output
    - digital positive logic with $U \in [-5V, 10V]$, driving up to $I = 1 mA$
    load
        - `ule` upper limit exceeded
        - `!lle` not lower limit exceeded
3. Supply Voltages
    - $+10V$ @ $20mW$ ($2mA$)
    - $-5V$ @ $10mW$ ($2mA$)

## Circuit Selection and Design

The window-comparator can be used to check, whether a measured signal `meas` is
inside a window defined by a lower limit `ll` and an upper limit `ul`. If the
measured signal is outside of the defined window the corresponding digital
output signals that the window limits are exceeded with the signals `lle`
(lower limit exceeded) and `ule` (upper limit exceeded).

- $\text{meas} > \text{ul} \implies \text{ule}$
- $\text{meas} < \text{ll} \implies \text{lle}$

A small offset is added to the configured limits increasing/decreasing
`ul`/`ll` to allow the use with a single limit for both the upper limit and
lower limit and still generate a well-defined window.
Therefore the window-comparator can be used to check if a two voltages are
approximately equal.

### Circuit

The offset added to the limits should generate a window approximately
$U_{window} \approx 5mV$. To add the offset voltage a voltage divider is
chosen. The usage of the depicted voltage divider will not always assure a
_symmetric_ window around the given limit signal, but will maintain a constant
width of the window. For a high limit signal close to 5V the limit signal will
get closer to the upper bound of the window, but further from the lower bound
of the window, and vice versa. In order to ease computation the calculations
are performed for a centered _symmetric_ window at $U_{ul} = U_{ll} = 2.5V$.
The addition of an offset for a single of the two limits should therefore be
$U_{offset} \approx 2.5mV$. When using the supply voltages at $U_{+} = 10V$ and
$U_{-} = -5V$ a voltage drop of $7.5V$ across the voltage divider is present.
For a quiescent current of $I_q \approx 75 \mu A$ at $7.5V$ across the voltage
divider a total resistance of
$$ R_1 + R_2 = \frac{7.5V}{75 \mu A} \approx 100k \Omega $$
is chosen. For the maximum and minimum value of the limit signal the quiescent
current will therefore be an element of $I_q \in [50 \mu A, 100 \mu A] >
I_{comp,in}$ and considerably larger than the input current of the comparator,
which can therefore be neglected. With a ratio of the resistances defined by
the desired offset the following resistances can be obtained:
$$ \frac{R_1 + R_2}{R_2} = \frac{7.5V}{2.5mV} \implies R_1 \approx 100k \Omega
\land R_2 \approx 33 \Omega $$

The tolerance of the offset addition due to tolerances and the offset voltage
of the comparator should not allow for the window size to shrink below
$U_{window} < 0V$. For a tolerance of $1\%$ of the resistances the tolerance of
the tolerance of the offset voltage can be approximated:
$$ \frac{\Delta U_{offset}}{U_{voltage divider}} \approx \Delta R_1
\frac{d}{dR_1} \frac{R_2}{R_1 + R_2} + \Delta R_2 \frac{d}{dR_2} \frac{R_2}{R_1
+ R_2} $$
Using $\Delta R_i = \pm R_i \cdot 0.01 \land U_{voltage divider} = 7.5V$ the
tolerance of the offset voltage can be estimated to not exceed:
$$ |\Delta U_{offset}| \leq \left|\frac{-2 \cdot 0.01 R_1 R_2}{(R_1 + R_2)^2}
\cdot U_{voltage divider}\right| \approx 50 \mu V $$

Therefore the input offset voltage of the comparator shall not exceed
$U_{off,in} < 2.5mV - 50 \mu V$, but can be chosen smaller to increase the
accuracy of the comparator.

To add a hysteresis of $U_{hist} \big|_{U_{ll} = U_{ul} = 2.5V} \approx 1mV$.
Positive feedback is used to create a Schmitt-trigger. This can be achieved by
selecting $R_5 + R_7 \lessapprox 1M \Omega$ to allow for a large enough
quiescent current to neglect the comparator input current. And selecting a
large $R_5$ to neglect parasitic resistances. With $\frac{R_7}{R_5} =
\frac{7.5V}{1mV}$ the following resistances can be selected:
$$ R_7 = 1M\Omega \land R_5 = 130 \Omega $$

### Component Selection

#### Comparator / Opamp

[TLV9352](https://mou.sr/3BJsKZm)

- 2 or 4 channels
- SMD Mount, SOIC preferred
- rail-to-rail preferred
- $\text{SR} > 5V / \mu s$
- $V_{off} \leq 1mV$
- $I_{bias, in} \leq 1nA$ (To allow neglect of input current for high feedback resistance)
- $I_{out} \geq 20mA$
- Price sort on Mouser

## Simulation

TODO: link to simulation files

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Test pins for `ul`, `ll`, `meas`, `ule`, `lle`

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
