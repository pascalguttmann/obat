# Measurement

## Instance specific

!!! info "Opamp type U1501"
    Opamp U1501 is used to add offset compensation to the current measurement. Using
    the faster OPA2810 instead of the TLV9352 for increased phase margin while
    in current control modes. The additional phase margin gives enhanced stability.
    For details why increased stability is needed see `control`, which
    describes the effect of hysteresis in the `bias` stage on the controller.

!!! info "Offset adjustment"
    In order to adjust the current offset for the hall sensor to measure zero
    when, no current is flowing the voltage divider with R1502 can be used. The
    coil of the relay generates a stray magnetic field, influencing the measurement
    of the hall based current sensor. To adjust for that influence, the value of
    R1502 is changed to $R= 8.2 k \Omega$.

## Tests

### Current Sensor

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/meas/current-sensor/-3A` | pass | $U_{meas,out} = 2.228 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/-1A` | pass | $U_{meas,out} = 2.425 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/0A` | pass | $U_{meas,out} = 2.527 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/1A` | pass | $U_{meas,out} = 2.617 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/3A` | pass | $U_{meas,out} = 2.825 V$, $U_{vzcr} = 2.498 V$ |
