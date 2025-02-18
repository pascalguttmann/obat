# Measurement

## Instance specific

!!! info "Opamp type U1501"
    Opamp U1501 is used to add offset compensation to the current measurement. Using
    the faster OPA2810 instead of the TLV9352 for increased phase margin while
    in current control modes. The additional phase margin gives enhanced stability.
    For details why increased stability is needed see `control`, which
    describes the effect of hysteresis in the `bias` stage on the controller.

## Tests

### Current Sensor

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/meas/current-sensor/-3A` | pass | $U_{meas,out} = 2.228 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/-1A` | pass | $U_{meas,out} = 2.425 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/0A` | pass | $U_{meas,out} = 2.527 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/1A` | pass | $U_{meas,out} = 2.617 V$, $U_{vzcr} = 2.498 V$ |
| `v1.0.0/pss/meas/current-sensor/3A` | pass | $U_{meas,out} = 2.825 V$, $U_{vzcr} = 2.498 V$ |
