# Channel Map

The instructions and specification of the SPI interface and general usage
information of the DAC is given in the [DAC datasheet], which should be used in
conjunction with this page.

[DAC datasheet]: https://www.analog.com/media/en/technical-documentation/data-sheets/ad5672r_5676r.pdf

!!! note "Reset State"
    After power up or after reset, the default value for all channels is `0x000`.

| Channel Number | Configuration Type | Mnemonic | Description |
| -------------- | ------------------ | -------- | ----------- |
| 0 | Analog | d_heater | Set the PWM duty cycle for the heater|
| 1 | Analog | d_peltier | Set the PWM duty cycle for the peltier element |
| 2 | Analog | d_fan | Set the PWM duty cycle for the fan |
| 3 | -  | | |
| 4 | Digital  | p_heater | Set the polarity of the output for the heater, (by default disabled by hardware) |
| 5 | Digital  | p_peltier | Set the polarity of the output for the peltier element |
| 6 | Digital  | p_fan | Set the polarity of the output for the fan, (by default disabled by hardware) |
| 7 | -| | |

## Duty Cycle Setting

To obtain the transfer function from dac counts "n" to duty cycle "d" for each
channel consult the documentation pages for [`./dac`](./dac.md) and
[`../pwm/pwm.md`](../pwm/pwm.md).

## Polarity Setting

Setting a value of `0x000` at the digital channels sets the polarity to
positive. I.e. current flows from positive output to negative output. Setting a
value of `0xFFF` at the digital channels sets the polarity to negative. I.e.
current flows from positive output to negative output.

Defaults to `0x000` on power up.
