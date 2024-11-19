# State Machine

A limiting circuit is implemented based on a state machine as shown below. A
priority based approach to switching the limits is not chosen because it would
result in frequent switching between modes at limiting operation.

```mermaid
stateDiagram-v2
  [*] --> CV
  CV --> CC : SetCCMode
  CC --> CV : SetCVMode

  CV: Voltage Reference
  state CV {
    [*] --> VoltageControl
    VoltageControl --> LowerCurrentLimitControl : LowerCurrentLimitSubceeded
    UpperCurrentLimitControl --> LowerCurrentLimitControl : LowerCurrentLimitSubceeded
    VoltageControl --> UpperCurrentLimitControl : UpperCurrentLimitExceeded
    LowerCurrentLimitControl --> UpperCurrentLimitControl : UpperCurrentLimitExceeded
    LowerCurrentLimitControl --> VoltageControl : MeasuredSmallerThanTarget
    UpperCurrentLimitControl --> VoltageControl : MeasuredGreaterThanTarget
  }

  CC: Current Reference
  state CC {
    [*] --> CurrentControl
    CurrentControl --> LowerVoltageLimitControl : LowerVoltageLimitSubceeded
    UpperVoltageLimitControl --> LowerVoltageLimitControl : LowerVoltageLimitSubceeded
    CurrentControl --> UpperVoltageLimitControl : UpperVoltageLimitExceeded
    LowerVoltageLimitControl --> UpperVoltageLimitControl : UpperVoltageLimitExceeded
    LowerVoltageLimitControl --> CurrentControl : MeasuredSmallerThanTarget
    UpperVoltageLimitControl --> CurrentControl : MeasuredGreaterThanTarget
  }
```
