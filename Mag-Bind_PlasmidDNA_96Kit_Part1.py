# Written by Hannah Verdonk
# 4 Sept 2019
from opentrons import labware, instruments, robot, modules

# TODO: remember to split this into multiple scripts, based on when you run out of tips & need to replace them

# metadata
metadata = {
    'protocolName': 'Plasmid Mag-Bind Purification',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automates Omega Bio-Tek's Mag-Bind plasmid purification kit",
}

# Define sample labware
samples = labware.load("corning_96_wellplate_360ul_flat", 8)
mag_plate = labware.load('usascientific_96_wellplate_2.4ml_deep', 7, share=True)

# Define reagents
# TODO: a tuberack won't hold enough volume. change this to some kind of trough
reagents = labware.load('opentrons-tuberack-2ml-eppendorf', 4)
'''6 columns A-F, 4 rows (I think)
Let Solution I be in A1, Solution II be in B1, N3 buffer in C1, 
'''

# Define tip racks
tiprack_1 = labware.load('opentrons-tiprack-300ul', 10)
tiprack_2 = labware.load('opentrons-tiprack-300ul', 11)

# Define Modules
magdeck = modules.load('magdeck', 7)

# pipettes
p300 = instruments.P300_Multi(
    mount='right',
    tip_racks=[tiprack_1, tiprack_2])


# Protocol:

# add Solution I/RNase A to each well & resuspend cells (24 mL total)
p300.distribute(
    250,
    reagents.wells('A1'),
    samples,
    mix_after=(3, 50),
    new_tip='always'
)

# add Solution II to each well (24 mL total)
p300.distribute(
    250,
    reagents.wells('B1'),
    samples
)

# 5 min incubation at room temperature
p300.delay(minutes=5)

# add N3 buffer to each well
p300.distribute(
    125,
    reagents.wells('C1'),
    samples
)

# End part 1. The user should centrifuge the cells 10 mins, then proceed to step 2
