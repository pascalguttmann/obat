Output Stage
============

Output stage class AB for driving the load of the powersupplysink.

Requirements
------------

- [ ] $U_{out} \in [0V, +5V]$
- [ ] $I_{out} \in [-20A, +20A]$
- [ ] Short circuit protected
- [ ] $I_{in} < 200mA \quad \forall \quad U_{out} \times I_{out}$

Interface
---------

- Voltage controlled input
- Voltage controlled output
- Supply Voltages
    - $+10V$
    - $-5V$

Circuit Selection
-----------------

### Transistor Technology Selection

To realize the power amplification complementary bjt transistors are choosen,
because

- their collector current can be controlled by the base current
- driving circuitry for FETs, IGBTs is more complex
- complementary parts are available to construct complementary emitterfollower
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

Circuit Design
--------------

Simulation
----------

Hardware tests in Laboratory (optional)
---------------------------------------

Layout Considerations
---------------------

Assembly Considerations
-----------------------

Commissioning and Testing
-------------------------

