# Measurement Electronics
## Research on components

 **Current Measurement:** A current sense amplifier or a shunt resistor in combination with an ADC can be used for 
 current measurement. The shunt resistor is placed in the path of the current to be measured, and the voltage 
 drop across it (which is proportional to the current) is measured.

**Voltage Measurement:** A high-precision ADC (Analog-to-Digital Converter) can be used for voltage measurement.
 It can convert the analog voltage signal into a digital value for processing. A suitable ADC would be one with 
 a resolution high enough to achieve your desired accuracy of 1mV in a 0-5V range.

 To achieve galvanic isolation an isolation amplifier or linear optocoupler could be used.

### Choice for Current measurement:

 - **Hall Effect Sensors:** These devices measure current and voltage through magnetic fields and provide galvanic 
 isolation. They are suitable for both AC and DC measurements.

**Available option:**


- ACS712-20A/ ACS714-20A:


[ACS712-20A/ ACS714-20A datasheet]

- TMCS1100:


[TMCS1100 datasheet]

The ACS712-20A and the ACS714-20A both serve the same purpose, but the ACS714-20A is better suited for harsher 
environments. Considering the controlled testing environment and cost factors, I recommend opting for the **ACS712-20A** in this case. 

### Choice of FUSE:

- Thermal Fuse or Switch: This is used to protect the circuit from excessive currents. It should be connected between 
I_MEAS+ and I_MEAS- and should be able to disconnect the circuit within a specified time if the current exceeds a certain limit.

**Available option:**

  1.	BOURNS CB72ABB: This is a thermal fuse with a functioning temperature of 72°C and a holding temperature of 40°C.

  2.	BOURNS CB85ABB: This thermal fuse has a functioning temperature of 85°C and a holding temperature of 40°C.

  3.	BOURNS SC82AAA: This thermal fuse has a functioning temperature of 82°C and a holding temperature of 40°C.

  4.	BOURNS CB77ABB: This thermal fuse has a functioning temperature of 77°C and a holding temperature of 40°C.

  5.	BOURNS SC85AAB: This thermal fuse has a functioning temperature of 85°C and a holding temperature of 40°C

  6. Automotive fuses: This fuse is compact, high-quality fuses designed for overcurrent protection in automotive electrical circuits.
      [[Automotive fuses](https://www.littelfuse.com/products/fuses/automotive-passenger-car/blade-fuses.aspx)]


 [Datasheet for fuses]

The below two options are preferable because there is ***no need to replace*** them after each time the fuse goes off,
 unlike thermal fuses or switches.

- **Electronic Fuses (eFuses):** These active devices use a sense resistor and a FET to monitor current flow. When the 
current exceeds a preset value, the control logic turns the FET off, cutting the flow of current.

Electronic fuses are not suitable for the current in use, as they are typically designed for very small currents. 
Therefore, circuit breakers would be a better choice

- **Residual Current Circuit Breakers:** These are resettable switches that open automatically when the current exceeds a certain threshold. 
They can be manual or automatic and are suitable for repeated use.

**Available option:**

F202 25A-30mA/AC:

[F202 25A-30mA/AC datasheet]

**Line safety circuit breaker** 
[Datasheet for Line safety Circuit breaker]

- In the context of measurement electronics, a critical decision has been made to incorporate a thermal fuse into our system. This choice was made after careful consideration of several factors.

Primarily, the cost-effectiveness of the thermal fuse was a significant determinant in this decision. We strive to maintain a balance between affordability and functionality, and the thermal fuse fits this criterion aptly.

Moreover, the specific use and significance of the thermal fuse within the realm of measurement electronics cannot be overstated. Its role in providing preventing potential damage to the system is crucial.

In conclusion, the selection of a thermal fuse for our measurement electronics system is a strategic decision that takes into account the cost implications, the specific use case, and the overall importance of this component in ensuring the safety and efficiency of our system

### Choice for voltage measurement:


[TMCS1100 datasheet]: https://www.ti.com/product/TMCS1100#features
[ACS712-20A/ ACS714-20A datasheet]: https://www.allegromicro.com/en/Products/Sense/Current-Sensor-ICs/Zero-To-Fifty-Amp-Integrated-Conductor-Sensor-ICs/ACS712
[Datasheet for fuses]: https://www.newark.com/c/circuit-protection/fuses-fuse-accessories/fuses/thermal-fuses?fuse-current=25a
[F202 25A-30mA/AC datasheet]: https://new.abb.com/products/1SYF202005R1250/in-f202-25a-30ma-ac
[def]: https://new.abb.com/products/de/2CDS251001R0255/s201-b25
[Datasheet for Line safety Circuit breaker]: ://new.abb.com/products/de/2CDS251001R0255/s201-b25