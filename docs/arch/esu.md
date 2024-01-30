# Emergency Stop Unit (ESU)

The Emergency Stop Unit (ESU) is responsible to disconnect the battery from the
power supply unit in the case that specified operating conditions are violated.
The ESU should not rely in software to disconnect the battery from the power
supply. Analog circuitry for example with a logic family like `78xx` or others
is possible.
It uses 0V to 5V inputs from the measurement transducer to evaluate when to
disconnect the battery.

## Requirements and Interface to other Components

### Interfaces

- [ ] The ESU shall have the following connection:
    - [ ] OUT+
    - [ ] OUT-
    - [ ] IN+
    - [ ] IN-
    - [ ] V_MEAS
    - [ ] V_REF
    - [ ] I_MEAS
    - [ ] I_REF
    - [ ] T_MEAS
    - [ ] T_REF
    - [ ] X_MEAS
    - [ ] X_REF
- [ ] Additionally, the ESU might have a power connection.
- [ ] The ESU shall have the following user interfaces:
    - [ ] Button `connect`
    - [ ] Button `disconnect`
    - [ ] Limit set `V_LOW`
    - [ ] Limit set `V_HIGH`
    - [ ] Limit set `I_LOW`
    - [ ] Limit set `I_HIGH`
    - [ ] Limit set `T_LOW`
    - [ ] Limit set `T_HIGH`
    - [ ] Limit set `X_LOW`
    - [ ] Limit set `X_HIGH`

!!! info
    The `X` connection is at the moment unused, but is included for the ability
    to extend the ESU unit in the future. Is must fulfill the same
    specifications as the `V`, `I` and `T` measurements.
    A possible use case is the initialization to perform a disconnect by
    software from the main PC in obat.

### States

- [ ] The state of the ESU is `connected` if `IN+` is galvanic connected
    to `OUT+` and `IN-` is galvanic connected to `OUT-`.
- [ ] The state of the ESU is `disconnected`if `IN+` is galvanic
    disconnected from `OUT+` and `IN-` is galvanic disconnected from `OUT-`.
- [ ] It must be ensured by hardware (e.g. a relay with multiple contacts),
    that the ESU is always either in `connected` or `disconnected` state.
- [ ] The connections `OUT+`, `OUT-`, `IN+` and `IN-` must be isolated from all
    other terminals and electronics in ESU.
- [ ] The state after power on must be `disconnected`.

### State Transitions

- [ ] The ESU shall transition from `disconnected` to `connected` state if and
    only if the physical button `connect` is pressed and the ESU is able to
    transition back to the `disconnected` state at any time after the
    `connected` state is entered.  (E.g. The energy storage to switch of is
    charged.)

    !!! note
        Because the transition to the `disconnected` state has the highest
        precedence, a transition to `connected` state can only occur, if all
        `input voltages` of the measured quantities (voltage, current,
        temperature) are in the `operation interval`.

- [ ] The ESU shall transition from `connected` to `disconnected` state if the
    physical button `disconnect`is pressed.
- [ ] If a power fail occurs the ESU must switch to the `disconnected` state.
    (Therefore the ESU must store enough energy to transition to the
    `disconnected` state, when the main power is not available.)
- [ ] The buttons `connect` and `disconnect` must be momentary and return by
    itself to the original position if not pressed.  [ ] The ESU must transition
- from `connected` to `unconnected` state if one or
    more of the following criteria are met:
    - [ ] The measured voltage is not in the `operation interval`.
    - [ ] The measured current is not in the `operation interval`.
    - [ ] The measured temperature is not in the `operation interval`.
    - [ ] The measured X voltage is not in the `operation interval`.

- [ ] The connections `*_MEAS` and `*_REF` shall form pairs, in which the
    `*_REF` connection acts as the reference for the electric potential, and
    `*_MEAS` is a voltage in the interval  [`*_MEAS`, `*_MEAS`+5V].

    !!! note
        The voltage from `*_MEAS` to `*_REF` is the `input voltage` for the given measured quantity (voltage, current, temperature, X at battery).

    - [ ] The pairs must be galvanic isolated from all other connections of the
        ESU. (E.g. by using an optocoupler).
- [ ] The ESU shall have for each measurement input pair internally the `limits`
    -  `*_LOW`
    -  `*_HIGH`
    - [ ] The interval [`*_LOW`, `*_HIGH`] is the `operating
        interval` for the corresponding measured quantity (voltage, current,
        temperature, X).
    - [ ] The `limits` must be constant during operation.
    - [ ] The `limits` shall be physically adjustable independent of each other.
        (E.g with a potentiometer).
- [ ] The transition to the `disconnect` state must be of higher precedence than the
    transition to the `connected` state. If criteria for both transitions are
    met, the transition to the `disconnected` state must be performed.
- [ ] A connection disruption must **not** trigger a transition to the `connected`
    state.
- [ ] A connection disruption must trigger a transition to the `disconnected`
    state if the connection disruption inhibits the defined transitions to the
    `disconnected` state.

### Other

- [ ] The operation of the ESU must not depend software execution.
    - [ ] Software must not be able to influence the internal `limits` or
        perform a transition to the `connected` state.

## Internals

- TTL or CMOS logic ?
- Bi- or Monostable relay?
- Setting process? Process to set the desired internal limits.
