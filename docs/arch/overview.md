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
    - Include in U/I Measurement?
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
flowchart TD
    pc[PC]

    pss-internal[2 Quadrant Power supplysink]

    subgraph sub-esu [ESU Integration]
        stop-button[Stop Button]
        esu[Emergency Stop Unit]
        measurement2[secondary U/I Measurement]
    end

    subgraph sub-meas [Measurement Electronics]
        measurement[U/I Measurement]
        meas[U/I/T digitalization]
    end

    subgraph sub-enclosure [Enclosure]
        measurement_T[T Measurement]
        control_T[T Control]
        subgraph sub-dut [Device Under Test]
            bat[Battery]
        end
    end

    subgraph sub-supply [Power Source]
        ac-outlet[AC Outlet]
        acdc-conv[AC/DC Converter]
    end

    pc --> pss-internal
    pss-internal --> stop-button
    stop-button --> esu
    esu --> bat
    bat --> measurement
    bat --> measurement2
    bat --> measurement_T
    measurement2 -. optional redundancy check .-> pc
    meas --> pc
    pc -. optional disconnect by software .-> esu
    pc --> control_T

    measurement -- 0..5V interface --> meas
    measurement_T -- 0..5V interface --> meas
    measurement_T -- 0..5V interface --> esu
    measurement2 -- 0..5V interface --> esu

    ac-outlet ==> pc & acdc-conv
    acdc-conv ==> pss-internal
    acdc-conv ==> esu
    acdc-conv ==> measurement
    acdc-conv ==> measurement2
    acdc-conv ==> control_T
    acdc-conv -. optional power delivery .-> measurement_T
```

## Safety Relevance Table

| Component            | Safety Relevant | Description                                      |
|:---------------------|:----------------|:-------------------------------------------------|
| PC                   | No              | Raspberry Pi                                     |
| Power Supply Sink    | No              | 2 Quadrant Bus Programmable                      |
| Emergency Stop Unit  | Yes             | Relay with Voltage and Temperature Control       |
| T Measurement        | Yes             | Transduces Temperature to voltage signal         |
| U/I Measurement      | No              | Transduces U/I to voltage signal                 |
| sec. U/I Measurement | Yes             | Transduce U/I to voltage signal for ESU (robust) |
| U/I/T measurement    | No              | Measurement of voltage signals                   |
