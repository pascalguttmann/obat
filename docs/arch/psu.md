# Power Supply Unit

The Power Supply Unit is controlled from the PC via a programmable bus interface
to set the desired voltage, current or power.

## Block Diagram

```mermaid
---
title: PSU Design
---
flowchart TB
pc[PC]
main[230 V @ 50Hz]
bat[Battery]

subgraph psu[PSU]
    direction TB
    esd_in[ESD Protection]
    subgraph dac[DAC]
        dac-u[DAC U]
        dac-i[DAC I]
        dac-p[DAC P]
        dac-m[Mode Selector?]
    end
    limiter[Limiting Logic]
    amp[Linear non-switchting amplifier]
    relay[Emergency Stop Unit]
    esd_out[ESD Protection]

    esd_main[ESD Protection Main]
    emc_main[EMC Filter Main]
    rect[Transformer and Rectifier]
end

main --> esd_main --> emc_main --> rect --> amp & dac & limiter
pc --> esd_in --> dac --> limiter
limiter --> amp <--> relay <--> esd_out <--> bat
```

## Design Choices Reasoning

### Linear Amplifier

The considered benefits of using a linear amplifier over using a switching
amplifier are:

Advantages:

- easy to control electronically
- fast response time
- stable very low ripple output
- no switched elements with high EMR

Disadvantages:

- low efficiency for large voltage drops and large currents
- requires cooling
