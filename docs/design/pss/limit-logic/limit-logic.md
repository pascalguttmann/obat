# Limit Logic

Interface & Requirements
------------------------

TODO: Add Input specs
TODO: Add Output specs
TODO: Add Power Consumption

1. Voltage Input `ref` & `meas`
    - Voltage Input Swing $V_{in} \in [0V, +5V]$
    - Input Current $| \pm I_{in} | \leq 2.3mA$
2. Voltage output `out`
    - In phase with $V_{ref}$
    - $V_{out} \in [-5V, 10V]$
    - Output current $I_{out \pm} \geq \pm 800 mA$
3. Supply Voltages
    - $+10V$ @ $1W$ ($100mA$)
    - $-5V$ @ $0.5W$ ($50mA$)

Circuit Selection and Design
----------------------------

### Circuit

TODO: Add circuit description

### Component Selection

#### R/S Latches

[CD4044BDR] Quad R/S Latch from 4000 series. Search on Mouser, sort by price.

[CD4044BDR]: https://mou.sr/3XPJrtv

#### Analog Bidirectional Switch

[CD4066BM96] Selection (sort by Price): 4x SPST, SMD, 15V VCC,
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

- Pull up/down for inputs, when stage is isolated, to run other tests.
TODO: Add test pins
TODO: Add (dic-)connector note, with testcase required for connecting

### Assembly

Commissioning and Testing
-------------------------

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
