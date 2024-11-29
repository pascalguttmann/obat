# Channel Map

This channel map gives information, which channel of during the configuration
is setting which feature of the `pss`.

The instructions and specification of the SPI interface and general usage
information of the DAC is given in the [DAC datasheet], which should be used in
conjunction with this page.

[DAC datasheet]: https://www.analog.com/media/en/technical-documentation/data-sheets/ad5672r_5676r.pdf

!!! note "Reset State"
    After power up or after reset, the default value for all channels is `0x000`.

!!! note "Current Setting Range"
    The current reference and current limits shall only be set in the range
    $I \in [-20A, +20A]$. The device will not be damaged if other values are
    set, but specification may not be met.

!!! note "Upper and Lower Limit"
    The upper limit shall be configured to be greater than the lower limit. If
    the condition is not met, the output will not be connected, regardless of
    configuration `conf_output`.

!!! note "Digital Channels"
    The Channels with configuration type _Digital_ must only be configured with
    the explicitly specified values. Failing to configure one of the specified
    values will not damage the device, but the configuration is undefined and
    may be either of the given values.

| Channel Number | Configuration Type | Mnemonic | Description |
| -------------- | ------------------ | -------- | ----------- |
| 0 | Digital | conf_output | `0x000` = output high Z, `0xFFF` = output defined by settings in channel 1 to 7 |
| 1 | Digital | conf_refselect | `0x000` = voltage (follow conf_vref, limited by conf_lcl and conf_ucl), `0xFFF` = current (follow conf_iref, limited by conf_lvl and conf_uvl) |
| 2 | Analog | conf_vref | Set voltage reference to $U = \frac{n}{2^{12}} \cdot 5V$ |
| 3 | Analog | conf_iref | Set current reference to $I = \frac{n}{2^{12}} \cdot 50A - 25 A$ |
| 4 | Analog | conf_lvl | Set lower voltage limit to $U = \frac{n}{2^{12}} \cdot 5V$ |
| 5 | Analog | conf_uvl | Set upper voltage limit to $U = \frac{n}{2^{12}} \cdot 5V$ |
| 6 | Analog | conf_lcl | Set lower current limit to $I = \frac{n}{2^{12}} \cdot 50A - 25 A$ |
| 7 | Analog | conf_ucl | Set upper current limit to $I = \frac{n}{2^{12}} \cdot 50A - 25 A$ |

!!! info
    $$ n \in [0, 2^{12} - 1] \quad | \quad n \in \mathbb{N}_0 $$
