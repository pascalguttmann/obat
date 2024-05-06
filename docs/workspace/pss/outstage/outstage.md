Output Stage
============

Output stage class AB for driving the load of the powersupplysink.

Requirements
------------

- [ ] $U_{out} \in [0V, +5V]$
- [ ] $I_{out} \in [-20A, +20A]$
- [ ] Short circuit I limit $I_{max} = [1.25 min(I_{out}), 1.25 max(I_{out})]$
- [ ] $I_{in} < 200mA \quad \forall \quad U_{out} \times I_{out}$

Interface
---------

- Voltage controlled input
- Voltage controlled output
- Supply Voltages
    - $+10V$
    - $-5V$

Circuit Selection and Design
----------------------------

### Transistor Technology Selection

To realize the power amplification complementary bjt transistors are chosen,
because

- their collector current can be controlled by the base current
- driving circuitry for FETs, IGBTs is more complex
- complementary parts are available to construct complementary emitter follower
    (push pull output stage)

### Transistor Type

With the specs it is possible to find parts like `MJ11032` and `MJ11033` as

- complementary
- darlington
- high current
- high power dissipation package TO−204 (TO−3)

transistors, that could maybe be used with high efforts for cooling. Still the
issue of scalability beyond 20A is not solved. In order to ease the requirements
on the thermal management multiple BJTs are connected in parallel to share the
load.

### Load Balancing & Short Circuit Protection

To achieve a balanced load distribution and avoid thermal runaway due to changes
of $V_{BE}$ emitter resistors are used for compensation. The voltage drop at the
emitter resistor can additionally be utilized to deploy short circuit protection
by current limiting. The current limit can be enforced by lowering the bias
currents when the voltage drop across the emitter resistors is exceeding a
predefined threshold.

#### Emitter (Ballast) Resistor

Considering a single npn transistor of the multiple paralleled transistors as
system $S$ the thermal evolution of the system can be approximated by:
$$ \frac{dQ}{dt} = P_{el} - P_{th} $$
The thermal power dissipation $P_{th}$ can be approximated from the stored
thermal energy $Q$ as follows:
$$ P_{th} \approx \frac{C_{th} Q}{R_{th}} = \frac{T}{R_{th}}  $$
Where $C_{th}$ is the thermal mass of the system $S$, $R_{th}$ is the thermal
resistance in $[\frac{K}{W}]$ and $T$ is the absolute temperature.
The delivered electrical power converted to thermal power in $S$ is described
by:
$$ P_{el} = U_{CE} I_{C} + U_{BE} I_{B} $$

The temperature coefficient $\gamma \quad [\frac{mV}{K}]$ of a given npn
transistor describes the change of $U_{BE}$ at a certain operating point for a
given temperature change, for constant $I_C$. [It is mainly derived from the
temperature dependence of the _reverse bias current_
$I_S$.](https://web.mit.edu/klund/www/Dphysics.pdf)
The electrical power can therefore be described depending on the temperature by:
$$
    I_B =
    \underbrace{
    \left[ I_S \exp \left( \frac{U_{BE} - \gamma \Delta T}{U_T} \right) \right]
    }_{I_B}
$$

$$
    P_{el} = I_B \left\{
    \underbrace{
        U_{BE} - \gamma \Delta T
    }_{U_{BE}} +
    \underbrace{
        \beta_0
    }_{I_{C}}
    \underbrace{
        \left( U_C - R_E (\beta_0 + 1) I_S \exp \left( \frac{U_{BE} - \gamma \Delta T}{U_T} \right) \right)
    }_{U_{CE}}
    \right\}
$$

Thermal runaway of the transistor is can be avoided by $\frac{dQ}{dt} < P_{el} -
P_{th}$ and therefore:
$$
    R_E > \frac{1}{I_B} \left(
        U_C + \frac{U_{BE} - \gamma \Delta T}{\beta_0}
        - \frac{T}{R_{th}} \frac{1}{\beta_0 I_B} \right)
$$

For the worst case of $R_{th} \to \infty$ and with $U_C >> \frac{U_BE - \gamma
\Delta T}{\beta_0}$ and $(\beta_0 + 1) \approx \beta_0$ the expression can be simplified to:
$$
    R_E \gtrapprox \frac{U_C}{\beta_0^2 I_B} =
    \frac{U_C}{\beta_0^2 I_S \exp \left( \frac{U_{BE} - \gamma \Delta T}{U_T} \right)}
$$

For $U_C = 15V$, $\beta_0 = 25$, $I_S = 10^{-15} A$, $U_{BE} = 700 mV$, $U_T =
26mV$, $\Delta T = 100K$ and $\gamma = -2 \frac{mV}{K}$ the constrained for the
ballast resistor is
$$ R_E \gtrapprox 22 m \Omega $$

#### Short Circuit Protection

To limit the current in case of a short circuit a current limiting transistor
can be connected from the base of each power transistor over the ballast
resistor. When the voltage across the ballast resistor $U_{RE}$ rises to
$U_{BE}$ of the limiting transistor the base current of the power transistor
will be limited. The current limiting is applied separately for each power
transistor.

### Thermal Resistance Consideration

The current and thermal load distribution are the factors significantly
influencing the multiplicity of paralleled transistors. As it is expected that
thermal load will be more restrictive than current load, the multiplicity is
derived using the thermal characteristics. From the multiplicity a requirement
for component selection regarding the maximum current capability is established.
From that a complementary bjt pair is selected to fulfill the requirements.

The biggest thermal active power is achieved at highest voltage drop and highest
current through the device $P = U I$. The maximum voltage drop and current of
the transistors is achieved with a short circuit of the output.

- Short circuit to $0V$: maximum power dissipation in npn transistors for power
    delivery (operational in first quadrant, supply of electrical power)
- Short circuit to $5V$: maximum power dissipation in pnp transistors for power
    consumption (operational in second quadrant, sink of electrical power)

Because the supply voltages are respectively $5V$ higher or lower than the
limits and the sourced and sunk currents are symmetrical both power dissipation
cases can be treated equal. The following calculations are conducted for the npn
transistors with a short circuit to $0V$. The maximum voltages are limited by
the available voltage of the power supply rails. The following ESD and
protection circuitry also guarantees, that a short circuit will not be able to
imprint voltages outside of the operational interval of $[0V, 5V]$ to the
output.
Similarly the maximum current is enforced by the short circuit protection of
this output stage. The current limit of this output stage is determining the
maximum current, even in case of failure of preceding circuitry.

The maximum thermal power dissipation due to output current is approximated by:
$$ P_{th,max} = U I = (U_{supply} - U_{sc}) I_{max}\
= (10V - 0V) 1.25 \cdot 20A = 250W $$

This approximation is an upper bound for the power dissipation including

- the thermal dissipation by the control voltage and current at the base, in
    case the base current is also limited by the current limiting circuitry.
    That is the case for the short circuit protection utilizing the voltage drop
    across the emitter resistors, because $I_E = I_C + I_B$ holds.  If a
    limiting transistor is used to bypass excess base current this limiting
    transistor must rendered inoperable before the thermal dissipation of the
    output stage transistors is exceeded. It is assumed that the preceding stage
    does not deliver enough power to thermally destroy the current limiting
    transistors, while completely delivering additionally the entire short
    circuit current $I_{max}$. Destruction of the preceding stage is likely
    before the thermal power dissipation limit for the output stage transistors
    is exceeded.
- the quiescent current. The quiescent current is also contributing to the
    limited current $I_{max}$, as it flows from the collector to the emitter.

#### Combination of Heatsinks

Because the worst case conditions for the npn and pnp transistors can only occur
exclusively the transistors can share one combined heatsink with unchanged
thermal requirements.
This requires the assumption, that the preceding stage does not allow excess
quiescent current to flow.

#### Package Selection

To reduce the number of devices needed the thermal resistance should be low.
Therefore only selected well established packages are compared.
The values for thermal resistance are retrieved from _ROHM Co., Ltd_ [^1] unless
noted otherwise.

| Package            | Technology | $R_{th,JA} [K/W]$ | $R_{th,JC} [K/W]$ |
|:-------------------|:-----------|:------------------|:------------------|
| TO-220AB           | THT        | 80                | 0.8               |
| TO-247             | THT        | 30                | 0.6               |
| TO-204 (TO-3) [^2] | THT        | 30                | 0.8               |
| TO-252 (DPAK)      | SMD        | 147               | 4.9               |
| TO-263 (D2PAK)     | SMD        | 80                | 4.2               |
| HSOP8              | SMD        | 41.7              | 5.6               |

!!! info
    Expected thermal resistance for case to heatsink with thermal grease and
    electrical isolation $R_{th,CH} \approx 1 K/W$.
    Heatsinks in extruded profile shape (ger. Strangkühlkörper) can provide
    approximately $R_{th,HA} \approx 1K/W ... 3K/W$ for our use case. [^3]

[^1]: [2023, ROHM Co., Ltd.,
    "List of Transistor Package Thermal Resistance",
    accessed at 06.04.2024][thermal-res]

[^2]: [2021, Hunter, G.,
    "TO-3 Component Package",
    accessed at 07.04.2024][thermal-res-to3]

[^3]: <https://www.fischerelektronik.de/service/kataloge-up-to-date/>

[thermal-res]: https://rohmfs-rohm-com-cn.oss-cn-shanghai.aliyuncs.com/en/products/databook/applinote/common/list_of_transistor_package_thermal_resistance_an-e.pdf
[thermal-res-to3]: https://blog.mbedded.ninja/pcb-design/component-packages/to-3-component-package/

If at an ambient temperature of $40°C$ the maximum desired junction temperature
is considered to be $100°C$ (lifespan), a maximum temperature difference of
$T_{diff} = T_{j,max} - T_{a,max} = 100°C - 40°C = 60K$ is estimated.
For cooling without a heatsink this would imply a lower bound of the
multiplicity of paralleled transistors of:
$$ n_{th,JA} \ge \frac{P_{th,max} R_{th,JA}}{T_{diff}} $$

With $min(R_{th,JA}) = 30 K/W$ in the case of `TO-247` packages this yields an
uneconomical high number of required components:
$$ n_{th,JA} \ge \frac{250W \cdot 30K/W}{60K} = 125 $$

To reduce the number of required components a heatsink will be employed. For the
most conductive SMD package `TO-263 (D2PAK)` even with an ideal heatsink
$R_{th,CA} = 0 K/W$ to the PCB the number of required packages is:
$$ n_{th,TO-263} \ge \frac{P_{th,max} (R_{th,JC} + R_{th,CA})}{T_{diff}}\
= \frac{250W \cdot (4.2K/W + 0K/W)}{60K} = 17.5 $$
For the real application dissipating 250W into the PCB will yield high thermal
stress and require a significant area on the PCB. Therefore one of the THT
mounted packages is preferred. With an ideal heatsink the number of components
is:
$$ n_{th,TO220AB} \ge \frac{250W \cdot (0.8K/W + 0K/W)}{60K} \approx 3.3 $$
$$ n_{th,TO247} \ge \frac{250W \cdot (0.6K/W + 0K/W)}{60K} = 2.5 $$
$$ n_{th,TO204} \ge \frac{250W \cdot (0.8K/W + 0K/W)}{60K} \approx 3.3 $$

Simulation
----------

Hardware tests in Laboratory
----------------------------

Layout and Assembly Considerations
----------------------------------

### PCB Layout

- Add testpins for ballast resistor voltage measurement (measurement)
- Add testpins for input voltages (measurement, test source)
- Add testpin for output (measurement, load) [^4]

[^4]: Screw terminal can be used for up to $|I| = 20 A$

### Assembly

- The power transistors should be mounted thermally coupled on the same heatsink
    to reduce thermal drift of individual transistors.
- Additionally one heatsink can be shared by the npn and pnp power transistor,
    because they are not subject to simultaneous heating.
- Apply thermal grease and electrical insulation from transistors to heatsink.

Commissioning and Testing
-------------------------

### Load Distribution

Test ID: `pss/outstage/load-distribution/<suffix>`

1. Connect
    1. Positive Rail (test id suffix: `positive`)
        - Output with $R = 100 m \Omega$ to _GND_ ($P = 10W$)
        - positive Input $U_{IN+} = 2V$
        - negative Input $U_{IN-} = 0V$
    2. Negative Rail (test id suffix: `negative`)
        - Output with $R = 100 m \Omega$ to _GND_ ($P = 10W$)
        - positive Input $U_{IN+} = 0V$
        - negative Input $U_{IN-} = -2V$
2. Power on supply voltage
3. Measure Voltages
    1. Positive Rail
        - Voltage across positive ballast resistors $U_{RE+}$
    2. Negative Rail
        - Voltage across negative ballast resistors $U_{RE-}$
4. Power off supply voltage
5. Test passed if
    - $U_{RE} \neq 0V \quad \wedge \quad U_{RE} \in \overline{U_{RE}} ( 1 \pm 10 \%) \quad \forall \quad U_{RE}$

### Short Circuit Test

Test ID: `pss/outstage/short-circuit/<suffix>`

1. Connect
    1. Positive Rail (test id suffix: `positive`)
        - Output with $R \to 0 \Omega$ to _GND_ ($I = 20A$)
        - positive Input $U_{IN+} = 2V$
        - negative Input $U_{IN-} = 0V$
    2. Negative Rail (test id suffix: `negative`)
        - Output with $R \to 0 \Omega$ to _5V_ ($I = 20A$)
        - positive Input $U_{IN+} = 0V$
        - negative Input $U_{IN-} = -2V$
2. Power on supply voltage
3. Measure
    1. Positive Rail
        - Voltage across positive ballast resistors $U_{RE+}$
        - Output current $I_{Output}$
    2. Negative Rail
        - Voltage across negative ballast resistors $U_{RE-}$
        - Output current $I_{Output}$
4. Power off supply voltage
    - $U_{RE} \neq 0V \quad \wedge \quad U_{RE} \in \overline{U_{RE}} ( 1 \pm 10 \%) \quad \forall \quad U_{RE}$
    - $20A \leq |I_{Output}| \leq 25 A$

