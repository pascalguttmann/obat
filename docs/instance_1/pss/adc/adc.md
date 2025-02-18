# Analog Digital Converter

!!! info "Measurement Accuracy"
    The measurements are performed by setting the voltage to within $\pm 1mV$
    of the required voltage according to a non calibrated 4-digit multimeter
    measurement range 20V. That level of accuracy is beyond the specified
    accuracy of $\pm 0.5\% + 2 digits$.  
    However the measurements are reproducible up to $\approx 2 digits = 200 \mu
    V$ and therefore even millivolts are specified.

## Tests Current ADC Index 0

### Conversion

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/adc0/conversion/0V` | pass | $U_{meas} = 0.003V$ |
| `v1.0.0/pss/adc0/conversion/3V` | pass | $U_{meas} = 3.003V$ |
| `v1.0.0/pss/adc0/conversion/5V` | pass | $U_{meas} = 5.003V$ |

## Tests Voltage ADC Index 1

| Test ID | Status | Measured |
| :------ | ------ | :------- |
| `v1.0.0/pss/adc1/conversion/0V` | pass | $U_{meas} = 0.003V$ |
| `v1.0.0/pss/adc1/conversion/3V` | pass | $U_{meas} = 3.003V$ |
| `v1.0.0/pss/adc1/conversion/5V` | pass | $U_{meas} = 5.003V$ |
