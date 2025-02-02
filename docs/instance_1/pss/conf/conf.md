# Configuration

## Tests

### Level Shifter Low

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/conf/level-shifter/low/output` | pass | $U_{shift} =  -5.02V$ |
| `v1.0.0/pss/conf/level-shifter/low/refselect` | pass | $U_{shift} =  -5.02V$ |

### Level Shifter High

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/conf/level-shifter/high/output` | pass | $U_{shift} =  11.98V$ |
| `v1.0.0/pss/conf/level-shifter/high/refselect` | pass | $U_{shift} =  11.98V$ |

### DAC - Conf Ok

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/conf/dac/conf-ok` | pass | $U_{conf_ok} = 11.79V$, $U_{!relay_connect} = -4.89 V$ |

### DAC - Conf Not Ok

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/conf/dac/conf-not-ok` | pass | $U_{conf_ok} = -5.02$, $U_{!relay_connect} = 12.03V$ |
