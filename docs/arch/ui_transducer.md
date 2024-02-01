# U / I Transducer

The U / I Transducer is used to transduce the voltage and current at the battery
terminals to a voltages of defined magnitude. The measured voltage and current
at the battery terminal shall be mapped linearly to the corresponding output
voltage. The smallest value shall be mapped to 0V and the biggest value to 5V.
Because the achievable measurement accuracy depends on the transducer. The
transducer shall map the values with an accuracy, so that the [general
measurement accuracy requirements][obat-overview] can be fulfilled.

[obat-overview]: ./overview.md

## Requirements and Interface to other Components

### Interfaces

- [ ] The transducer shall have the following connections:
    - [ ] `V_MEAS+`
    - [ ] `V_MEAS-`
    - [ ] `I_MEAS+`
    - [ ] `I_MEAS-`
    - [ ] `V_OUT_TCV`
    - [ ] `V_OUT_REF`
    - [ ] `I_OUT_TCV`
    - [ ] `I_OUT_REF`
    - [ ] `GLOBAL_REF`
- [ ] Additionally the transducer might have a power connection.
- [ ] The transducer shall have the following user interfaces:
    - [ ] Setting for each output to (dis)connect the output reference
        `*_OUT_REF` from or to `GLOBAL_REF`. (e.g. with a "jumper", solder
        bridge or switch)
- [ ] The connections `V_MEAS+` and `V_MEAS-` shall measure voltages positive
    from `V_MEAS+` to `V_MEAS-` in the range of 0V to 5V.
    - [ ] The connections `V_MEAS+` and `V_MEAS-` shall be galvanic decoupled
        and have an impedance to every other connection $Z > 1M \Omega$. And a
        differential impedance $Z_{diff} > 1M \Omega$.

- [ ] The connections `I_MEAS+` and `I_MEAS-` shall measure voltages positive
    from `I_MEAS+` to `I_MEAS-` in the range of $-20A$ to $+20A$.
    - [ ] The connections `I_MEAS+` and `I_MEAS-` shall be galvanic decoupled
        and have an impedance to every other connection $Z > 1M \Omega$. They
        should be galvanic coupled to each other and have a differential
        impedance $Z_{diff} < 5m \Omega$.
    - [ ] The connection between `I_MEAS+` and `I_MEAS-` shall be able to
        conduct bidirectional current of $I = \pm 20A$ permanently.
    - [ ] The minimum current $I_{min} = -20A$ shall be mapped to a
        voltage of $0V$.
    - [ ] The maximum current $I_{max} = +20A$ shall be mapped to a voltage of
        $5V$.

        !!! info
            Therefore it follows, that if no current is flowing the output
            voltage should be $2.5V$.

    - [ ] The connection between `I_MEAS+` and `I_MEAS-` shall be fused with a
        thermal fuse or a thermal switch for currents exceeding $I_{fuse} =
        25A$, within a time of $t_{fuse} <= 60sec$. (E.g. Car Fuse)

        !!! info
            The connection `I_MEAS+` and `I_MEAS-` is the only galvanic coupled
            connection of the transducer with a direct path for the current to
            flow.

    - [ ] Connection `GLOBAL_REF` shall be galvanic decoupled from all other
        connections with $Z > 1M \Omega$, except for `V_OUT_REF` and `I_OUT_REF`
        if the corresponding switch is set. Then the galvanic connection shall
        have a impedance $Z < 1 \Omega$.

    - [ ] The connections `*_OUT_TCV` and `*_OUT_REF` shall form a differential
        pair to output the transduced voltage.
        - [ ] The differential pair shall be galvanic decoupled from other
            connections with $Z > 1M \Omega$ and have a differential impedance
            $Z_{diff} < 1.25 \Omega$. (Calculated for load of $100 \mu A$ at $5V$
            for maximum voltage drop of $125 \mu V$, to achieve $\frac{1mA}{2
            \cdot 20A}$).
        - [ ] The mapped voltage shall be the output at the connection
            `*_OUT_TCV` with respect to `*_OUT_REF`.

    - [ ] The transducer shall map the values with an accuracy, so that the
        [general measurement accuracy requirements][obat-overview] can be
        fulfilled.

## Internals

- Hall sensor based I/V transduction? e.g. product form [ACS Hall Transducer Family][ACS712]
- Trimming adjustment of output with potentiometer to compensate offsets?
- use same voltage level as other components

[ACS712]: https://www.allegromicro.com/en/Products/Sense/Current-Sensor-ICs/Zero-To-Fifty-Amp-Integrated-Conductor-Sensor-ICs/ACS712
