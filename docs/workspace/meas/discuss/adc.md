Analog Digital Converter
========================

Performance Specification
-------------------------
- Resolution 12/14 bit (or greater)
- Supply voltage: 5 V
- Sampling rate: 200 kHz (or greater)
- Spi interface

Parts Investigated
------------------

### 4.096V Reference
- [ADS7038][ADS7038 datasheet]
- [MAX1142][MAX1142 datasheet]
- [LTC2308][LTC2308 datasheet]
- [LTC2313-12][LTC2313-12 datasheet]

### 5V Reference Compatible

#### Search

[Mouser ADC Search] with Filters:

- ADC
- Resolution >= 12-bit
- Interface: SPI supported
- Samplingrate >= 200kSps
- Supply Voltage: 5V supported
- Sort by: Price ascending

#### Results

- [ADS7817] Differential Input 2.5V Ref, $U_{in} = 2.5V \pm
    2.5V$, 1 Channel, VSSOP-8
- [ADC121] Single Sided Input, $U_{in} \in [0V, 5V]$, 1
    Channel, SOT-23, Pin-compatible Product Family: 8-bit, 10-bit, 12-bit,
    200kSps, 500kSps, 1MSps
- [ADC122] Single Sided Input, $U_{in} \in [0V, 5V]$, 2
    Channel Multiplex, VSSOP-8, Pin-compatible Product Family: 8-bit, 10-bit, 12-bit,
    200kSps, 500kSps, 1MSps
- [BU79100] Single Sided Input, $U_{in} \in [0V, 5V]$, 1
    Channel, SSOP-6

### SPI Daisychain

To ease the usage at an SPI Interface Daisy Chain capable components will be
preferable. An SPI - Daisy Chain capable ADC is the [ADS8665]. It does not only
feature an ADC but an entire data acquisition system _DAQ_, which has an
internal antialiasing lowpass filter and ADC driver circuit included.

Family Parts

| Part No. | Resolution [bit] | Max. Sample Rate [Msps] |
|----------|------------------|-------------------------|
| ADS8661  | 12               | 1.25                    |
| ADS8665  | 12               | 0.5                     |
| ADS8671  | 14               | 1                       |
| ADS8675  | 14               | 0.5                     |
| ADS8685  | 16               | 0.5                     |
| ADS8681  | 16               | 1                       |
| ADS8695  | 18               | 0.5                     |
| ADS8691  | 18               | 1                       |

#### Recommendation

If further investigation shows, that SPI Daisychain is desired choose an SPI
daisychain capable ADC. Like the [ADS8665], which also provides antialiasing
filters and driver circuitry.

If daisychaining is not required select [ADC121], because it fulfills the known
specification requirements known at this moment in time, is cost efficient.
Single-sided Input. SOT-23 package easier assembly, Pin compatible family.

[ADS7817] Differential Input "more complicated" not pin compatible with
[ADC121]. VSSOP-8 package is ok, but SOT-23 is preferred.

[ADC122] Two channel operation is great, but second channel is multiplexed. If
higher sampling rate is required package price increases. Loosing cost benefit
at cost of flexibility / simplicity.

[BU79100] comparable to [ADC121], but SSOP-6 package

[ADS7038 datasheet]: https://www.ti.com/lit/ds/symlink/ads7038.pdf?ts=1713952903321&ref_url=https%253A%252F%252Fwww.google.com%252F
[MAX1142 datasheet]: https://www.analog.com/en/products/max1143.html
[LTC2308 datasheet]: https://www.analog.com/media/en/technical-documentation/data-sheets/2308fc.pdf
[LTC2313-12 datasheet]: https://www.analog.com/en/products/ltc2313-12.html
[Mouser ADC Search]: https://www.mouser.de/c/semiconductors/data-converter-ics/analog-to-digital-converters-adc/?q=adc&analog%20supply%20voltage=0%20V%20to%205.25%20V%7C~1.8%20V%2C%205%20V%2C%205.4%20V%7C~2.2%20V%20to%205.5%20V%7C~2.25%20V%20to%205%20V%2C%205%20V%7C~2.3%20V%20to%205%20V~~2.3%20V%20to%205.5%20V%7C~2.35%20V%20to%205.25%20V~~2.375%20V%20to%205.25%20V%7C~2.4%20V%20to%205.1%20V%7C~2.5%20V%20to%205%20V%7C~2.5%20V%20to%205.5%20V%7C~2.5%20V%2C%205%20V%7C~2.7%20V%20to%205.25%20V%7C~2.7%20V%20to%205.5%20V%7C~2.85%20V%20to%205.5%20V%7C~3%20V%20to%205.25%20V%7C~3%20V%20to%205.5%20V%7C~3%20V%2C%205%20V%7C~3.13%20V%20to%203.47%20V%2C%204.75%20V%20to%205.25%20V%7C~3.15%20V%20to%205.5%20V%7C~4%20V%20to%205.5%20V%7C~4.5%20V%20to%205.25%20V~~4.5%20V%20to%205.5%20V%7C~4.75%20V%20to%205.25%20V%7C~4.75%20V%20to%205.5%20V%7C~4.95%20V%20to%205.05%20V%7C~5%20V%7C~5%20V%2C%2010%20V&interface%20type=3-Wire%2C%204-Wire%2C%20Microwire%2C%20QSPI%2C%20SPI%7C~3-Wire%2C%20I2C%2C%20SPI~~3-Wire%2C%20Microwire%2C%20SPI%7C~3-Wire%2C%20Parallel%2C%20QSPI%2C%20SPI~~3-Wire%2C%20SPI%7C~I2C%2C%20Parallel%2C%20SPI%7C~JESD204B%2C%20SPI%7C~Microwire%2C%20QSPI%2C%20SPI%7C~Parallel%2C%20SPI%7C~QSPI%2C%20SPI%7C~SPI~~SPI%2C%20USART&resolution=12%20bit~~32%20bit&sampling%20rate=100%20kS%2Fs~~10.4%20GS%2Fs&NewSearch=1&rp=semiconductors%2Fdata-converter-ics%2Fanalog-to-digital-converters-adc%7C~Resolution%7C~Interface%20Type%7C~Sampling%20Rate%7C~Analog%20Supply%20Voltage&sort=pricing&pg=2
[ADS7817]: https://www.ti.com/lit/ds/symlink/ads7817.pdf?ts=1714433703965&ref_url=https%253A%252F%252Fwww.mouser.de%252F
[ADC121]: https://www.ti.com/lit/ds/symlink/adc121s021.pdf?ts=1714380326274&ref_url=https%253A%252F%252Fwww.mouser.fr%252F
[ADC122]: https://www.ti.com/lit/ds/symlink/adc122s021.pdf?ts=1714381766845&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FADC122S021%253Futm_source%253Dgoogle%2526utm_medium%253Dcpc%2526utm_campaign%253Dasc-null-null-GPN_EN-cpc-pf-google-eu%2526utm_content%253DADC122S021%2526ds_k%253DADC122S021%2526DCM%253Dyes%2526gad_source%253D1%2526gclid%253DEAIaIQobChMI_pDF3InnhQMV7D4GAB2oCw5nEAAYASAAEgLjN_D_BwE%2526gclsrc%253Daw.ds
[BU79100]: https://fscdn.rohm.com/en/products/databook/datasheet/ic/data_converter/dac/bu79100g-la-e.pdf
[ADS8665]: https://www.ti.com/lit/ds/symlink/ads8661.pdf?ts=1714606735903&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FADS8661
