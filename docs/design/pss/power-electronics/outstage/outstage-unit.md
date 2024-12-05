# Outstage Unit

The `outstage` sub circuit is split into two separate units called
`outstage-unit`, in order to allow for a hierarchical pcb design. With standard
sized eurocard of size 100mm x 220mm each `outstage-unit` provides board space
for a single heatsink with fan and six copies of the emitter amplifier.

The two `outstage-unit` sub circuits share the specification with the
`outstage` sub circuit, except that input and output currents are divided by a
factor of two. The specification is not copied here, because the hierarchical
sub circuit is introduced for the layout and shall not introduce a new logical
component.

[Link to `outstage` documentation](./outstage.md)
