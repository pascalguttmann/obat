# Power Supply Sink

The Power Supply Sink is controlled from the PC via a programmable bus interface
to set the desired voltage, current or power.

## Block Diagram

```mermaid
---
title: PSS Design
---
flowchart TB
pc[PC]
24V_power[24 V DC]
bat[Battery]

subgraph pss[PSS]
    direction TB

    power[10V, 5V, -5V]
    conf[Configuration]
    checker[Conf Checker and Power On Reset]
    direction LR
    mux_ref[Multiplexer Reference]
    control[PID-Controller]
    subgraph pe[Power Electronic]
        bias[Bias Stage]
        outstage[Linear Power Amplifier]
    end
    meas[Output Measurement]
    mux_meas[Multiplexer Measurement]
    relay[Relay]

    subgraph limit[Limit-Logic]
        comp[Compare-Logic]
        mode-tran[Mode Transition]
    end
end

24V_power --> power
pc --> conf --> checker
conf --> mux_ref --> control --> bias --> outstage --> meas --> relay --> bat
meas --> mux_meas --> control
conf --> comp --> mode-tran
limit --> mux_meas
limit --> mux_ref

```
