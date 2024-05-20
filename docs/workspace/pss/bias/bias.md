Bias Stage
==========

Bias and driver stage for the class AB output stage of the powersupplysink.

Interface & Requirements
------------------------

- Voltage Input
    - Voltage Input Swing $V_{in} \in [-2V, +6V] \subset [-3V, +8V]$
    - Input Current $| \pm I_{in} | \leq 20mA$
- Double voltage out with offset voltage
    - In phase with $V_{in}$
    - $V_{out-} \approx V_{in} - 0.6V + 1V = V_{in} + 0.4V$
    - $V_{out+} \approx V_{in} + 0.6V - 1V + V_{offset} = V_{in} + V_{offset} - 0.4V$
    - $V_{offset} \in [+0.73V, +1.8V]$
- $V_{offset}$ adjustable via trimmer
- Supply Voltages
    - $+10V$ @ $?W$
    - $-5V$ @ $?W$

Circuit Selection and Design
----------------------------

Simulation
----------

Hardware tests in Laboratory
----------------------------

Layout and Assembly Considerations
----------------------------------

Commissioning and Testing
-------------------------

