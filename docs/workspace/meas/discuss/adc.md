Analog Digital Converter
========================
ADC stands for Analog-to-Digital Converter. It is a system that converts an analog signal, such as a sound picked up by a microphone or light entering a digital camera, into a digital signal.
In more detail, an ADC converts a continuous-time and continuous-amplitude analog signal to a discrete-time and discrete-amplitude digital signal1. This conversion involves quantization of the input, so it necessarily introduces a small amount of quantization error.
The performance of an ADC is primarily characterized by its bandwidth and signal-to-noise ratio (SNR). The bandwidth of an ADC is characterized primarily by its sampling rate.
ADCs are chosen to match the bandwidth and required SNR of the signal to be digitized. If an ADC operates at a sampling rate greater than twice the bandwidth of the signal, then per the Nyquist–Shannon sampling theorem, near-perfect reconstruction is possible.
ADCs are crucial in the modern world as they act as a bridge between the analog world and digital devices. They can be found as individual ADC ICs or embedded into a microcontroller.

Performance Specification
-------------------------
•	Resolution 12/14 bit (or greater)
•	Supply voltage: 5 V
•	Sampling rate: 200 kHz (or greater)
•	Spi interface

Parts Investigated
------------------
- [ADS7038][ADS7038 datasheet]
- [MAX1142][MAX1142 datasheet]
- [LTC2308][LTC2308 datasheet]
- [LTC2313-12][LTC2313-12 datasheet]

[ADS7038 datasheet]: https://www.ti.com/lit/ds/symlink/ads7038.pdf?ts=1713952903321&ref_url=https%253A%252F%252Fwww.google.com%252F
[MAX1142 datasheet]: https://www.analog.com/en/products/max1143.html
[LTC2308 datasheet]: https://www.analog.com/media/en/technical-documentation/data-sheets/2308fc.pdf
[LTC2313-12 datasheet]: https://www.analog.com/en/products/ltc2313-12.html
