# Workspace Site

Intended for use as:

  - Shared workspace size to collaborate for system integration
  - documentation for inter-team agreements

## Agreements / Decisions

### ECAD

As the used ECAD Tooling the following options are investigated and KiCAD 8 is
decided to be used as the ECAD tool for obat. Mainly because it is more suitable
for the future as it is a thriving open source project and not discontinued as
EAGLE. Also by its FOSS nature and the ecosystem "data ownership" is placed at
obat project and not a third party company.
With EAGLE being discontinued officially by 7th of June 2026 it is not seen as a
future safe option for a new project.

- AUTODESK Eagle
    - Disadvantages:
        - discontinued (announced by Autodesk to be discontinued by 7th June 2026)
        - little to no updates
        - Not free, license required (educational license available)
        - proprietary software (Autodesk might enforce online storage)
        - licensing might change at any time
        - footprints and symbols are "linked" atomically in library (depending
            on opinion this can be good)
    - Advantages:
        - used at by others at HFU
        - good library support
        - nice part search bulk editing for big projects
- KiCAD 8
    - Disadvantes:
        - Currently not used by many other at HFU
    - Advantages:
        - Free (no license) and free as in freedom
        - Open Source
        - Active Project, Regular Updates and new versions
        - good library support
        - Footprint and Schematic symbols separated in libraries
        - EAGLE project importer
        - (softpoint) handy tools and calculators, it just works

## Meeting Agreements

### 18. Apr 2024

- PC / Controller
    - separation of realtime / non-realtime code into distinct packages, which
        have a defined interface. This separation shall allow a change of the
        realtime code for harder realtime constraints. (Port of language, port
        to other hardware).
- PowerSupplySink
    - PI(D) controller for constant current or other controller type is suited
        better?
- Enclosure
    - Temperature control loop should be managed in the PC / Controller
    - Interface definition of actuators and sensors is required to be shared /
        agreed
    - Power for temperature control can be sourced from 24V power source by
        using isolation DC/DC amplifiers for other voltages.
    - safety disconnect can be achieved by using a control signal (Steuersignal)
        to switch a relay.

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

