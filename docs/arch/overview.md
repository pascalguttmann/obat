# Overview

## Requirements

- General
    - [ ] Output Voltage $0V$ to $5V$
    - [ ] Output Current $-20A$ to $+20A$
    - [ ] Voltage Measurement (triggered) (accuracy wish 1mV / 5V)
    - [ ] Current Measurement (triggered) (accuracy wish 1mA / 20A)
    - [ ] Temperature Measurement (triggered)
    - [ ] Voltage Controlled Mode
    - [ ] Current Controlled Mode
    - [ ] Power Controlled Mode
    - [ ] Programmable measurements
    - [ ] Programmable drive cycles
    - [ ] Fast response time to allow programming of wave form
- Safety
    - [ ] Temperature range emergency stop
    - [ ] Voltage range emergency stop
    - [ ] [DGUV 203-049][dguv] test
- Security
    - [ ] ESD Protection

[dguv]: (https://publikationen.dguv.de/widgets/pdf/download/article/829)

## System Design

```mermaid
---
title: System Architecture Overview
---
flowchart LR

subgraph sub-obat [ ]
    direction LR
    pc[PC]

    subgraph sub-power [Power Electronics]
        psu-internal[2 Quadrant Power supplysink]
        esu[Emergency Stop Unit]

        psu-internal --> esu
    end

    subgraph sub-meas [Measurement Electronics]
        direction RL
        transducer[U/I/T Transducer]
        meas[U/I/T measurement]

        transducer --> meas
    end

    subgraph sub-dut [Device Under Test]
        bat[Battery]
    end

    pc --> psu-internal
    esu --> bat
    bat --> transducer
    meas --> pc
    pc -. optional disconnect by software .-> esu

    transducer --> esu
end
```

| Component           | Description                                             |
|:--------------------|:--------------------------------------------------------|
| PC                  | Raspberry Pi                                            |
| Power Supply Unit   | 2 Quadrant Bus Programmable                             |
| Emergency Stop Unit | Relay with Voltage and Temperature Control              |
| U/I/T measurement   | tbd                                                     |
| Transducer          | Transducer of Voltage, Current and Temperature to "TBD" |
