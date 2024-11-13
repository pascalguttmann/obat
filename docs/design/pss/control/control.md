Control
=======

Interface & Requirements
------------------------

- Voltage Input `ref` & `meas`
    - Voltage Input Swing $V_{in} \in [0V, +5V]$
    - Input Current $| \pm I_{in} | \leq 2.3mA$
- Voltage output `out`
    - In phase with $V_{ref}$
    - $V_{out} \in [-5V, 10V]$
    - Output current $I_{out \pm} \geq \pm 800 mA$
- Supply Voltages
    - $+10V$ @ $1W$ ($100mA$)
    - $-5V$ @ $0.5W$ ($50mA$)

Circuit Selection and Design
----------------------------

### Circuit

As the circuit a classical control loop is selected with a reference that should
be tracked by minimizing the error.
The PID controller is implemented using the depicted circuit:
![PID Controller Circuit](./pid_circuit.png)

The difference junction is implemented using a standard subtraction circuit
from literature [^TB]: ![Subtraction Circuit](./subtraction_circuit.png)

[^TB]: Europa-Lehrmittel, Tabellenbuch Elektrotechnik, 2018

#### PID Controller

##### Circuit Derivation

Considering an ideal operational amplifier in inverting configuration connected
with two impedances. The positive input terminal of the opamp connected to a
shared reference voltage (ground).

1. $Z_1$ from input voltage $U_e$ to the negative input terminal of the opamp
2. $Z_2$ feedback from the output to the negative input terminal of the opamp

the transfer function is then

$$ G = - \frac{Z_2}{Z_1} $$

When the circuit desired should be constructed from RC components only to form
the impedances $Z$ for cost reasons, the following two fundamental networks can
be combined. Considering the electrical network at the negative input of the
opamp, while neglecting the current flow into the opamp input the current flow
$I_{Z_1} = I_{Z_2}$. Assuming stability of the circuit the voltage at the
negative input terminal will be $V_{-} = V_{+} = 0V$. Therefore the impedance
$Z_1 = \frac{1}{Y_1}$ can be viewed as a linear system which takes as an input
a voltage and transforms it into a current. The impedance $Z_2$ can be viewed
as a linear system, which transforms this current in a voltage, which will be
present at the output. The transfer function can therefore be thought of as

$$ G = - Z_2 Y_1 $$

For each of the two fundamental networks two transformations can be associated.
Those transformations can be combined to select the desired network at the
desired position to obtain a desired transfer function.

- RC - Series network  
    - $Z_{series} = \frac{U}{I} = R + \frac{1}{sC} = \frac{1+sRC}{sC}$  
      Pole at origin, zero at $-RC$
    - $Y_{series} = \frac{I}{U} = \frac{sC}{1+sRC}$  
      Zero at origin, pole at $-RC$
- RC - Parallel network  
    - $Z_{parallel}=\frac{U}{I} = \frac{1}{\frac{1}{R}+sC} = \frac{R}{1+sRC}$  
      Pole at $-RC$
    - $Y_{parallel}=\frac{I}{U} = \frac{1}{R} + sC = \frac{1+sRC}{R}$  
      Zero at $-RC$

The inverting opamp configuration allows to combine the transfer functions of
one admittance and one impedance. A PID controller has a single pole at the
origin and two zeros in the left open plane. Therefore we can select

$$ Z_{series} = Z_2 \quad \land \quad Y_{parallel} = \frac{1}{Z_1} $$

The transfer function of the pid controller circuit is therefore:

$$ G
  = - \frac{Z_2}{Z_1}
  = - \left( R_2 + \frac{1}{sC_2} \right) \left( \frac{1}{R_1} + sC_1 \right)
  = - \frac{R_2}{R_1} - \frac{C_1}{C_2} - s R_2 C_1 - \frac{1}{sR_1C_2}
$$

Substituting $K_P = \frac{R_2}{R_1} + \frac{C_1}{C_2}$ the standard form of a
pid controller can be deduced:

$$ G
  = - K_P \left\{ \frac{1}{s R_1 C_2 K_P} + 1 + s \frac{R_2 C_1}{K_P} \right\}
$$

By comparing the factors it can be seen that:

$$ K_P = \frac{R_2}{R_1} + \frac{C_1}{C_2} \quad \land \quad
  T_I = K_P \cdot R_1 C_2 \quad \land \quad
  T_D = \frac{R_2 C_1}{K_P}
$$

##### Component Values

The parasitic capacitance together with the resistance of $R_{2}$ acts
as a low pass filter, which adds a pole to closed loop system. In order to
neglect the influence of the pole it's frequency should be higher than the
operating frequency. For the [OPA2810IDR] the parasitic capacitance
$C_{parasitic} \approx C_{in} + C_{diff} = 3 pF$. For a operating frequency $f
= 10 MHz$ a higher frequency of $f' = 2 \cdot f = 20 MHz$ is chosen and the
feddback resistance is limited by:
$$ R_{2} < \frac{1}{2 \pi f' C_{parasitic}} = 2.65 k \Omega $$

A lower limit of the feedback resistance is imposed by the maximum output
current of the [OPA2810IDR]. The maximum continous output current is $40mA$,
but to limit the thermal stress
of the device the output current is desired to not exceed $30mA$. The current
available for the feedback path is the remaining current, which is not used for
the following bias stage.
$$ R_{2} > \frac{U_{signal,max}}{I_{out,max} - I_{bias}} \approx
\frac{10V}{30mA - 20mA} = 1k \Omega $$

The values of $K_P$, $T_I$ and $T_D$ are given from the [controller design]. By
selecting a value for $R_2$ the value of

$$ C_1 = \frac{T_D K_P}{R_2} $$

is implicitly also selected. Equivalently $R_1$ and $C_2$ are connected by
$T_I$ and $K_P$:

$$ R_1 = \frac{T_I}{K_P C_2} $$

with the knowledge that $T_I$ is defined as

$$ T_I = K_P R_1 C_2 = R_1 C_1 + R_2 C_2 $$

one can derive the quadratic formula for the two solutions that can be used to
select $C_2$, by substituting $R_1 = \frac{T_I}{K_P C_2}$.

$$ R_2 K_P C_2^2 - K_P T_I C_2 + C_1 T_I = 0 $$

$$ C_2 = T_I \left( \frac{1 \pm \sqrt{1-4\frac{T_D}{T_I}}}{2R_2} \right) $$

For the given values of the controller the two solutions for $C_2$ are
approximately equal and they are inside the tolerance of capacitances.

When choosing $R_2 = 2.2 k \Omega$ we can find the component values:

$$
  R_1 = 240 \Omega \land
  R_2 = 1.2 k \Omega \land
  C_1 = 470pF \land
  C_2 = 100pF
$$

[controller design]: ./controller-design/controller-design.md

#### Difference Junction

To minimize the number of different components at unity gain for each channel
of the subtraction circuit we choose R_{e1} = R_{e2} = R_K = R_Q$.
The same restrictions apply for the feedback resistance as in the PID
controller, because the input resistance of the PID with
$$ R_{in,PID} \approx R_1 = 240 \Omega \implies I_{in,PID,max} \approx
\frac{u_{e,max}}{R_{in,PID}} = 20 mA $$.

Therefore we can select
$$ R_{e1} = R_{e2} = R_K = R_Q = 2.2 k \Omega $$

#### High Impedance Input Drive

To drive the inputs in a defined state when no preceding stage is connected
either during testing or when the `limit-logic` is performing a mode transition
and the multiplexer is switching in a gapping manner high impedance input drive
is used. The high impedance makes it possible to override the signal by a low
impedance source from the multiplexer. The reference `ref` of the controller is
connected to some voltage which it should follow, and the measurement `meas` of
the controller is connected to the output of the controller. The feedback path
from the controller output to the `meas` input can be neglected during the
normal operation of the controller, because the voltage on both terminals of
the resistor is driven by low impedance sources. Similarly, the voltage high
impedance voltage source driving the reference `ref` can be neglected during
normal operation, because the reference voltage will be driven by a low
impedance voltage source, which delivers the required current to force the
voltage across resistance of the high impedance voltage source.This assumes the
current through the resistance is small enough to be driven by both sources.

The high impedance of the input drive is connected in series to the resistors
$R_{e1}$ and $R_{e2}$ during gapping operation. Therefore the gain of the
difference junction is reduced. To obtain equal reduction of gain the impedance
of the feedback resistance should be equal to that of the voltage source
connected to the reference.

A value of $$ R = 1 M \Omega $$ can be chosen for the feedback resistor and the
impedance of the voltage source, which is able to

- neglect the currents required to drive the normal voltages during normal
operation
- neglect the input currents required by the operational amplifier during
gapping operation
- enable reuse of existing pull up/down resistors and increase the quantity of
a single component value

To choose an appropriate "default" voltage for the controller reference during
gapping a constant voltage can be used. This will yield easy implementation,
but introduces unnecessary voltage swing of the controller, when the default
voltage is not inside of the interval defined by the voltage before and after
the switching. To reduce the amount of unnecessary voltage swing a RC-lowpass
filter is used to obtain the reference voltage during normal operation and keep
it almost constant during the gapping switching. This requires that the
switching time is much smaller than the time constant of the filter, which is
in turn smaller than the time spent in normal operation.
$$ t_{transition} \approx 330ns << \tau_{RC} << t_{normal} \gtrapprox 1s $$

!!! note "Normal Operation Time"
    The time used for $t_{normal}$ is based on the expected behavior of
    connected loads to the powersupplysink. It is therefore tied to the
    expectations an user might have on the device (requirements) and not based
    on simulation or of physical meaning.

The time constant be chosen to be approximately $10ms$ which allows to reuse
the $10nF$ capacitances of the controller with _C0G_ dielectric.
$$ \tau_{RC} \approx 10ms \implies C = 10nF $$

Because the RC-lowpass is connected and discharged to ground via $R_{e2}$ and
$R_Q$ of the difference junction after $t \rightarrow \infty$ the reference
voltage will reach $0V$.

#### Anti Integral Windup

To avoid the integration to high limits during non-linear operation, when e.g.
the output voltage can not rise to the required level to reduce the controller
error to zero, diodes are connected antiparallel to the capacitance of the
integrator.
A voltage equal to the required offset introduced by the "rubber diode" of the
`bias` stage in the _powerelectronics_ is expected to be present across the
integration capacitance. Therefore multiple diodes can be connected in series
to allow the desired integration voltage.
$$ n_{diodes} = \left\lceil \frac{max(U_{offset})}{U_f(I_f)} \right\rceil $$
For $max(U_{offset}) \approx 2V \land U_f(I_f \approx 4mA) \approx 600mV
\implies n_{diodes} = 4$.
When the offset is adjusted to a lower value sparse diodes may be bridged by a
solder bridge. In the reverse direction a single diode is sufficient, because
no windup is expected due to the bias offset.

### Component Selection

#### Operational Amplifier

[OPA2810IDR] Selection (sort by Price): $n_{Ch} >= 2$, $GBWP
\approx 100 MHz$, 15V VCC, $SR \approx 150 V / \mu s$

!!! note "GBWP & SR"
    The GBWP is approximated by using the approximate oparating frequency $f$ of
    the closed loop control loop and the desired gain $K_P$.
    $$ GBWP \approx f \cdot K_P = 10 MHz \cdot 10 $$
    The slew rate is approximated by taking the maximum slope of a sine wave at
    maximum amplitude at the approximated operating frequency. $$ SR \approx 2.5V
    \cdot 10 MHz \cdot 2 \pi $$

[OPA2810IDR]: https://mou.sr/3X9Oofi

#### Anti Windup Diode

[1N4148W-7-F] Selection (sort by Price) from search on Mouser

- Small Signal Switching Diode
- in Stock
- SMD/SMT
- Forward Current $I_f > 10mA$
- Recovery Time $\leq 5ns$

[1N4148W-7-F]: https://mou.sr/3Lhk651

Simulation
----------

TODO: link to simulation files

Hardware tests in Laboratory
----------------------------

Layout and Assembly Considerations
----------------------------------

### PCB Layout

- Consider [OPA2810 Datasheet] Section _11 Layout_
- Low impedance decoupling of opamp
- Low impedance feedback of opamp (avoid parasitic capacitance)
- (Dis-) connector between _controller_ and _powerelectronics_, (solderbridge /
  jumper) Label with testname hint
- Add optional connectors from `out` to `meas` for unity plant test.
- Pull up/down for inputs, when stage is isolated, to run other tests.
- Add test pins for: `out`, `ref`, `meas`, `error`

[OPA2810 Datasheet]: <../../../datasheet/opa2810.pdf>

### Assembly

Commissioning and Testing
-------------------------

1. Pass all tests for `control`.
2. If all tests for _powerelectronics_ are passed connect _control_ and
   _powerelectronics_.

### Sign Propagation

Test ID: `v1.0.0/pss/control/sign-propagation/<suffix>`

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

### Closed Loop Stability for Unity Plant

Test ID: `v1.0.0/pss/control/stability-unity-plant/<suffix>`

1. Connections
    - Output `out` disconnected from following stage
    - Input `meas` connected to output `out` of PID controller
    - Input `ref` connected to $U_{ref} = 2.5V$
2. Power on supply voltage
3. Wait for steady state $t_{wait} \gtrapprox 1ms$
4. Measure Voltages
      - Voltage series $u_{out}(t) at PID controller output with oscilloscope
      for $t = 1s$
5. Power off supply voltage
6. Disconnect input `meas` from output `out` of PID controller
7. Test passed if
    1. Mean Value (test id suffix: `mean`)
        - $\overline{u_{out}(t)} \in 2.5V (1 \pm 1\%)$
    2. Output Signal Boundedness (test id suffix: `bounds`)
        - $\forall t u_{out}(t) \in 2.5V (1 \pm 1\%)$

!!! note
    Passing test `bounds` implies, that test `mean` is passed. Separation of
    test is conducted to make information of instability visible in test report,
    even when the mean is accurately tracked.
