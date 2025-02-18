# U / I / T Measurement

TODO: Change R1502 to $R = 8.2 k \Omega$ to allow for wider compensation range. (To compensate magnetic field of relay)

The U / I / T measurement is used to measure the voltage and current at the battery
terminals. The measured voltage and current at the battery terminal shall be
converted to a digital signal, which can be read by the PC.
The required accuracy shall be in accordance to achieve the desired measurement
accuracy given in the [overview][obat-overview].

[obat-overview]: ./overview.md

## Requirements and Interface to other Components

### Interfaces

- [ ] The measurement electronics shall have the following connections:
    - [ ] `V_MEAS+`
    - [ ] `V_MEAS-`
    - [ ] `I_MEAS+`
    - [ ] `I_MEAS-`
    - [ ] `T_MEAS+`
    - [ ] `T_MEAS-`
    - [ ] `GLOBAL_REF`
    - [ ] Connections for the digital interface
- [ ] Additionally the measurement electronics might have a power connection.
- [ ] The measurement electronics shall have the following user interfaces:
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
            connection of the measurement electronics with a direct path for the current to
            flow.

    - [ ] Connection `GLOBAL_REF` shall be galvanic decoupled from all other
        connections with $Z > 1M \Omega$, except for the power connector.

## Internals

- Hall sensor based I/V transduction? e.g. product form [ACS Hall Transducer Family][ACS712]
- Trimming adjustment of output with potentiometer to compensate offsets?
- use same voltage level as other components

[ACS712]: https://www.allegromicro.com/en/Products/Sense/Current-Sensor-ICs/Zero-To-Fifty-Amp-Integrated-Conductor-Sensor-ICs/ACS712
