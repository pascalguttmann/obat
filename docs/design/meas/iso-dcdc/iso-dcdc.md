# Isolated DC/DC

## Interface & Requirements

1. Input
    - $5V$ 200mA (not isolated)
2. Output
    - $5V$ 100mA (isolated)

## Circuit Selection and Design

### Circuit

To deliver an isolated 5V voltage an isolated regulated 5V to 5V DCDC-converter
is used.

The components are decoupled by capacitors as described in the datasheets.

#### Protection Circuit

The isolated 5V voltage at the output of the DCDC-converter is protected from
exceeding the specifications of the digital isolator by usage of a zener diode
to limit the voltage and if necessary provide a small load current to reduce
the output voltage of the DCDC-converter.
To lower switching noise from the DCDC-converter the output of the converter is
loaded with a resistive load of $R=330 \Omega$, which will load the output with
approximately $15mA$.

The isolated ground is connected via a $1 M \Omega$ resistor to the ground of
the rest of the pcb to avoid electrostatic charge to built up on the isolated
net. This will cause a small current flow in case the voltage at the isolated
ground is not equal to the ground voltage.

### Component Selection

#### DCDC-converter

Search on Mouser for: [R05C05TE05S](https://mou.sr/4eUT3cS)

- DCDC-converter
- isolated
- regulated output
- $5V$ input, $5V$ output
- output power $P \in [100mW, 1W]
- SMD mounting, (hand solderable friendly)
- Sort by Price

#### Zener Diode

Search on Mouser for: [PDZ5.6B,115](https://mou.sr/3B8nGxS)

- Zener Diode
- Zener voltage $5.6V \pm 2 \%$
- SMD mounting, (hand solderable friendly)
- Sort by Price

## Simulation

Not available.

## Hardware tests in Laboratory

## Layout and Assembly Considerations

### PCB Layout

- Pull up/down for inputs, when stage is isolated, to run other tests.

### Assembly

## Commissioning and Testing

### Isolation

Test ID: `v1.0.0/meas/iso-dcdc/isolation/<suffix>`

Available suffix: `GND`, `+5V`

1. Measure Resistance
    - $R_{iso}$ from `<suffix>` to `<suffix>I`
2. Test passed if
    - $R_{iso} > 100 k\Omega$

### Output

Test ID: `v1.0.0/meas/iso-dcdc/output`

1. Connections
    - Input $5V$
2. Measure output voltage $U_{out}$
3. Test passed if $U_{out} \in 5V \pm 100mV$
