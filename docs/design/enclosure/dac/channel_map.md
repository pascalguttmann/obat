# Channel Map

The instructions and specification of the SPI interface and general usage
information of the DAC is given in the [DAC datasheet], which should be used in
conjunction with this page.

[DAC datasheet]: https://www.analog.com/media/en/technical-documentation/data-sheets/ad5672r_5676r.pdf

!!! note "Reset State"
    After power up or after reset, the default value for all channels is `0x000`.

TODO: Define Channel Map for Enclosure

| Channel Number | Configuration Type | Mnemonic | Description |
| -------------- | ------------------ | -------- | ----------- |
| 0 | Digital | | |
| 1 | Digital | | |
| 2 | Analog  | | |
| 3 | Analog  | | |
| 4 | Analog  | | |
| 5 | Analog  | | |
| 6 | Analog  | | |
| 7 | Analog  | | |

!!! info
    $$ n \in [0, 2^{12} - 1] \quad | \quad n \in \mathbb{N}_0 $$
