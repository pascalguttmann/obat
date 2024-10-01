# State Machine

A limiting circuit is implemented based on a state machine as shown below. A
priority based approach to switching the limits is not chosen because it would
result in frequent switching between modes at limiting operation.

```mermaid
stateDiagram-v2
  [*] --> CV
  CV --> CC : EvSetCCMode
  CC --> CV : EvSetCVMode

  CV: Constant Voltage
  state CV {
    [*] --> VoltageControl
    VoltageControl --> LowerCurrentLimitControl : EvLowerCurrentLimitExceeded
    VoltageControl --> UpperCurrentLimitControl : EvUpperCurrentLimitExceeded
    LowerCurrentLimitControl --> VoltageControl : EvMeasuredSmallerThanTarget
    UpperCurrentLimitControl --> VoltageControl : EvMeasuredGreaterThanTarget
  }

  CC: Constant Current
  state CC {
    [*] --> CurrentControl
    CurrentControl --> LowerVoltageLimitControl : EvLowerVoltageLimitExceeded
    CurrentControl --> UpperVoltageLimitControl : EvUpperVoltageLimitExceeded
    LowerVoltageLimitControl --> CurrentControl : EvMeasuredSmallerThanTarget
    UpperVoltageLimitControl --> CurrentControl : EvMeasuredGreaterThanTarget
  }
```
