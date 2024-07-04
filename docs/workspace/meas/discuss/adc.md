Analog Digital Converter
========================
ADC stands for Analog-to-Digital Converter. It is a system that converts an analog signal, such as a sound picked up by a microphone or light entering a digital camera, into a digital signal.
In more detail, an ADC converts a continuous-time and continuous-amplitude analog signal to a discrete-time and discrete-amplitude digital signal1. This conversion involves quantization of the input, so it necessarily introduces a small amount of quantization error.
The performance of an ADC is primarily characterized by its bandwidth and signal-to-noise ratio (SNR). The bandwidth of an ADC is characterized primarily by its sampling rate.
ADCs are chosen to match the bandwidth and required SNR of the signal to be digitized. If an ADC operates at a sampling rate greater than twice the bandwidth of the signal, then per the Nyquist–Shannon sampling theorem, near-perfect reconstruction is possible.
ADCs are crucial in the modern world as they act as a bridge between the analog world and digital devices. They can be found as individual ADC ICs or embedded into a microcontroller.


Performance Specification
-------------------------
•	Resolution -12/14 bit (or greater)
•	Supply voltage: 5 V
•	Sampling rate: 200 GHz (or greater)
•	Spi interface


Parts Investigated
------------------
- ADS7038: [ADS7038 datasheet]
- MAX1142: [MAX1142 datasheet]
- LTC2308: [LTC2308 datasheet]
- LTC2313-12: [LTC2313-12 datasheet]

ADC configuration audrino code
==============================
#include <SPI.h>
const int CS_PIN = 10;
unsigned char* transfer32(unsigned char* input_data){
  int num = 4;
  static unsigned char output_data[4] = {0};
  for (int i =0; i<num; i++){
    output_data[i] = SPI.transfer(input_data[i]);
    //Serial.print("Sent: ");
    //Serial.print(input_data[i], HEX);
    //Serial.print(", Received: ");
    //Serial.println(output_data[i], HEX);
  }
  return output_data;
}

void setup() {
  Serial.begin(9600);
  pinMode(CS_PIN, OUTPUT);

  // Initialize SPI
  SPI.begin();
 
  // Reset the ADC
  digitalWrite(CS_PIN, LOW);
  delay(10);
  digitalWrite(CS_PIN, HIGH);
  delay(10);

  // Set up the ADC configuration here
  unsigned char config[][4] = {
    {0xD2, 0x00, 0x00, 0x00},
    {0xD4, 0x00, 0x00, 0x00}, //Device ID registration
    {0b11010010, 0b00000100, 0b00000000 ,0b00000000},
    {0xD4, 0x04, 0x69, 0x34}, //Reset
    {0xD2, 0x10, 0x00, 0x00},
    {0xD4, 0x08, 0x00, 0x00}, //SDi reg
    {0xD2, 0x18, 0x00, 0x00},
    {0xD4, 0x18, 0x00, 0x80}, //SD0 reg
    {0xD2, 0x14, 0x00, 0x00},
    {0xD4, 0x14, 0x01, 0x00}, //dataout register
    {0xD2, 0x1C, 0x00, 0x00},
    {0xD4, 0x1C, 0x00, 0x4B}, //range selection
    {0xD2, 0x20, 0x00, 0x00},
    {0xD4, 0x20, 0x00, 0x00}, // alarm flag
    {0xD2, 0x24, 0x00, 0x00},
    {0xD4, 0x28, 0x00, 0x00} //low theshold alarm

  };
 SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
 digitalWrite(CS_PIN, LOW);
 for(int i = 0; i < sizeof(config)/sizeof(config[0]); i++){
    transfer32(config[i]);
  }
 digitalWrite(CS_PIN, HIGH);
 SPI.endTransaction();
}

void loop() {
  digitalWrite(CS_PIN, LOW);

  unsigned char read_cmd[4] = {
    0x48, 0x0A, 0x00, 0x00
  };
  


  //tranfer read cmd
  unsigned char  read1[4] = {0x00};
  
  // read first register
  unsigned char temp_cmd[4] = {0x00, 0x00, 0x00, 0x00};
  unsigned char * temp = transfer32(temp_cmd);

  memcpy(read1, temp, 4);
  digitalWrite(CS_PIN, HIGH);
  SPI.endTransaction();
  unsigned short adc_value = 0;
  adc_value = ((unsigned short)(read1[1]) >> 4); 
  adc_value |= ((unsigned short)(read1[0]) << 4);

  
  for(int i = 0; i < 4; i++) {
    //Serial.print("Byte ");
    //Serial.print(i);
    //Serial.print(": ");
    //Serial.println(read1[i], HEX);
  }
  //Serial.print("ADC Value: ");
  Serial.println(adc_value, DEC);
  delay(100); // Delay between readings
}




[ADS7038 datasheet]: https://www.ti.com/lit/ds/symlink/ads7038.pdf?ts=1713952903321&ref_url=https%253A%252F%252Fwww.google.com%252F
[MAX1142 datasheet]: https://www.analog.com/en/products/max1143.html
[LTC2308 datasheet]: https://www.analog.com/media/en/technical-documentation/data-sheets/2308fc.pdf
[LTC2313-12 datasheet]: https://www.analog.com/en/products/ltc2313-12.html