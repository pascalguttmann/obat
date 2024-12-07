# Layout

!!! info "mil"
    One `mil` is a thousands of an inch.
    $$ 1 \text{mil} = 25.4 \mu m $$

## Clearance Distance

IPC2221 suggests a minimal spacing of $\approx 4 \text{mil}$ for external
uncoated conductors from sea level to 3050m altitude for voltages up to 30V.
For internal conductors the clearance distance is lower ($\approx 2
\text{mil}).

Therefore a spacing of $8 \text{mil}$ can be selected for all conductors to
ease the production and lower cost.

## Track Width

For increased currents the required track width to avoid excessive heating of
the track is increased. IPC2221 gives an approximation formula, which relates
the track width $w$, the temperature rise above ambient $\Delta T$, the track
thickness $h$ and the current trough the track. The approximation should be
used up to approximately $I<35A \land \Delta T < 100K \land w < 400 \text{mil}$
for approximating *outer* layer tracks:

$$ I = 0.048 \cdot K \cdot \Delta T^{0.44} \cdot (w \cdot h)^{0.725} $$

Calculations are for $\Delta T = 10K$, $h = 35 \mu m \widehat{=} 1
\frac{\text{oz}_{cu}}{\text{ft}^2}$ unless otherwise noted.

To ease manufacturing and lower costs the minimal track width is selected to
equal $8 \text{mil}$. A maximal current is therefore obtained:
$$ I_{8mil} \approx 750mil $$

A class of tracks carrying up to $I = 3A$ is desired and the minimal track
width is approximately:
$$ w_{3A} \approx 50mil \implies I_{50mil} \approx 3A $$

For currents up to $I = 12.5A$ the calculated track width is equal to:
$$ w_{12.5A} \approx 400mil \implies I_{400mil} \approx 12.5A $$
The track can also be split up on the top and bottom layer for THT mounted
connectors to allow for connection at terminal blocks with a pitch of $5.08 mm
= 200mil$. A copper pour is preferred for the tracks of this class.

For currents up to $I = 25A$ the calculated track width is equal to:
$$ w_{25A} \approx 800mil \implies I_{800mil} \approx 25A $$
The track can also be split up on the top and bottom layer for THT mounted
connectors to allow for connection at terminal blocks with a pitch of $5.08 mm
= 200mil$. A copper pour is preferred for the tracks of this class.
A track width of $200mil$ on top and bottom layer will give an approximate
temperature rise of $30 K$ and is acceptable for connection to terminal blocks,
but copper pours should be preferred when possible.

### Terminal Block Connection

A copper fill under terminal blocks may reduce the track width from $200mil$ to
$192mil$ to allow for adequate clearance spacing to adjacent tracks.

## Vias

Keeping PCB manufacturing costs low can be achieved by using standard sized
vias as per manufacturer requirement.
A standard size acceptable for most manufacturers "simple"/"economical" pcb
quotes is:
$$ d_{via,drill} = 0.3mm \land d_{via,copper} = 0.5mm $$
Micro-Vias should be avoided to keep manufacturing costs low.

Using KiCads Via Calculator the via with $d_{via,drill} = 0.3mm$,
$d_{via,copper} = 0.5mm$, plating thickness $T = 18 \mu m$ and via length $h =
1.6mm$ has the following properties:
$$ C_{via} \approx 0.4 pF$$
$$ L_{via} \approx 1.3 nH$$
$$ R_{via} \approx 1.5 m \Omega$$
$$ R_{th,via} \approx 220 \frac{K}{W} $$
$$ I_{via} \approx 1.5A \bigg|_{\Delta T = 10K} $$

## Plated Through Hole (PTH)

PTH should be in the range of $0.5mm < d_{pth,drill} < 5.6mm$. The annular
copper ring should be a minimum of $\Delta d_{pth,copper} = 0.6mm$ larger than
$d_{pth,drill}$ to avoid increased cost for precision manufacturing.

## Board Outline

To allow for mounting and handling of the pcb a distance of $2.5mm$ should be
kept free of copper and parts measured from the board outline.

## PCB Dimensions

PCB dimensions should be a height of $h = 100mm$ for mounting in 3U sub-rack
and a maximal length of $l_{max} = 220mm$ for mounting in the sub-rack. Shorter
pcbs are possible to mount and preferably comply to the [standard eurocard
sizes](https://en.wikipedia.org/wiki/Eurocard_(printed_circuit_board)#Dimensions).
