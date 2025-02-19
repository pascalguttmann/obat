# Enclosure

The enclosure is the physical container in which the device under test will be
placed. It shall be portable and give space to store the other electronic
devices.

## Requirements and Interface to other Components

### Interfaces

- The enclosure shall have the following connections:
  - [ ] High current connections for `+` terminal of device under test
  - [ ] High current connections for `-` terminal of device under test
  - [ ] Normal current sense connection for `+` terminal of device under test
  - [ ] Normal current sense connection for `-` terminal of device under test
  - [ ] Temperature sensor output positive
  - [ ] Temperature sensor output negative
  - [ ] Control Interface to control heating / cooling: TO BE DEFINED

### Internal

- [ ] The enclosure shall contain the power source required for heating and
    cooling.
- [ ] The enclosure shall disconnect the device under test mechanically when the
    enclosure is opened.

## Components

The mechanical enclosure uses the following electrical components, that shall
be actuated by the enclosure pcb adapter:

- Heating Element, 24V 50W
- Peltier Element, 24V 144W
- Fan, 12V 2.4W
