Control
=======

Interface & Requirements
------------------------

TODO: Add Requirements and Interface

Circuit Selection and Design
----------------------------

### Circuit

TODO: Add feed forward, offset

As the circuit a classical control loop is selected with a reference that should
be tracked by minimizing the error.
The PID controller is implemented using a standard circuit from literature[^TB]:
![PID Controller Circuit](./pid_circuit.png)

[^TB]: Europa-Lehrmittel, Tabellenbuch Elektrotechnik, 2018

### Component Selection

#### Operational Amplifier

[OPA2810IDR][OPA2810IDR] Selection (sort by Price): $n_{Ch} >= 2$, $GBWP
\approx 100 MHz$, 15V VCC, $SR \approx 150 V / \mu s$

[OPA2810IDR]: https://mou.sr/3X9Oofi

#### Analog Bidirectional Switch

[CD4066BM96][CD4066BM96] Selection (sort by Price): 4x SPST, SMD, 15V VCC,
$R_{on} <= 250 \Omega$

[CD4066BM96]: https://mou.sr/3MQOnJI

Simulation
----------

TODO: link to simulation files

Hardware tests in Laboratory
----------------------------

Layout and Assembly Considerations
----------------------------------

### PCB Layout

- Low impedance decoupling of opamp
- Low impedance feedback of opamp (avoid parasitic capacitance)

### Assembly

Commissioning and Testing
-------------------------

TODO: Add tests
