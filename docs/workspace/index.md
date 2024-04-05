# Workspace Site

Intended for use as:
  - Shared workspace size to collaborate for system integration
  - documentation for inter-team agreements

## Meeting Agreements

### 27. Mar 2024

- No switch/sensor at mechnical enclosure to check if enclosure is open or
    closed, which has to be read by other components.
    - Safety can be ensured using a concept similar to a "unloosable screw"
        (ger. unverlierbare Schraube)
- Connections from Measurement and PowerSupplySink into enclosure
    - Connected and disconnected mechanically by opening and closing the enclosure
    - Connections for 4 Wire sensing:
      - `+` and `-` connections with high current capability for power delivery
      - `+` and `-` connections in parallel with normal current capability
- Heating and Cooling
    - Power for heating cooling is considered part of the enclosure. Other
        components must only provide "information" for heating and cooling.
- Temperature sensing
    - [0V 5V] interface with linear mapping to temperature interval [T_min T_max]
- Stop Button
    - ESU has `connect` and `disconnect` button for "normal" operation
    - Before ESU is a stop button/lever disconnecting the ESU + DUT
    - Cooling, Heating & Ventilation is not stopped by the stop button
    - Color, size and type of button/lever must be investigated to be in
        accordance with regulations. (CE Examination)

