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

## Open Points

- Which component should measure ambient temperature?
    - Include in U/I Transducer?
    - Include in T measurement of Battery?
    - Create new component?
- PC software supervision?
    - e.g. WDOG functionality?
    - Which component should be supervising?
    - PC is not safety relevant at the moment. (Note from PaGu point of view: It
      is not planned to be safety relevant in the future. Is it worth adding the
      feature? Team discussion + decision is desired.)
- How much redundancy is required for safety relevant parts?
    - Redundant battery temperature measurement?
- CMOS or TTL logic level?
    - choose logic [family][7400-families] used for all components
    - Note from PaGu: choose CMOS logic (supply voltage not limited to 5V)? E.g.
        HC or HCT series.
- Limiting Logic of PSS, "soft" vs "hard" limiting? (Note from PaGu: Consult Mr.
    Rumschinski for opinion, see paper notes from PaGu -> Team decision desired)
    - "soft" limit: change reference value (ger.: Führungsgröße) to limited
        value, if limit is reached. Control circuit experiences jump in
        reference value and controls output accordingly.
    - "hard" limit: reference value of controller is unchanged if limit is
        reached. Output of control circuit is overridden if limit is reached.

[7400-families]: https://en.wikipedia.org/wiki/7400-series_integrated_circuits#Families

## System Design

```mermaid
---
title: System Architecture Overview
---
flowchart LR

subgraph sub-dut [Device Under Test]
    bat[Battery]
end

subgraph sub-obat [OBAT]
    direction LR
    pc[PC]

    subgraph sub-power [Power Electronics]
        pss-internal[2 Quadrant Power supplysink]

        subgraph sub-esu [ESU Integration]
            esu[Emergency Stop Unit]
            transducer2[secondary U/I Transducer]
        end

    end

    subgraph sub-meas [Measurement Electronics]
        direction RL
        transducer[U/I Transducer]
        meas[U/I/T measurement]
    end

    subgraph sub-extT [Temperature Measurement]
        transducer_T[T Transducer]
    end

    pc --> pss-internal
    pss-internal --> esu
    esu --> bat
    bat --> transducer
    bat --> transducer2
    bat --> transducer_T
    transducer2 -. optional redundancy check .-> pc
    meas --> pc
    pc -. optional disconnect by software .-> esu

    transducer -- 0..5V interface --> meas
    transducer_T -- 0..5V interface --> meas
    transducer_T -- 0..5V interface --> esu
    transducer2 -- 0..5V interface --> esu
end
```

## Safety Relevance Table

| Component           | Safety Relevant | Description                                      |
|:--------------------|:----------------|:-------------------------------------------------|
| PC                  | No              | Raspberry Pi                                     |
| Power Supply Sink   | No              | 2 Quadrant Bus Programmable                      |
| Emergency Stop Unit | Yes             | Relay with Voltage and Temperature Control       |
| T Transducer        | Yes             | Transduces Temperature to voltage signal         |
| U/I Transducer      | No              | Transduces U/I to voltage signal                 |
| sec. U/I Transducer | Yes             | Transduce U/I to voltage signal for ESU (robust) |
| U/I/T measurement   | No              | Measurement of voltage signals                   |
