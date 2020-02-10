# Written by Hannah Verdonk
# 4 Sept 2019
from opentrons import labware, instruments, modules, robot

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
reagents = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 4)
'''
Let Solution I be in A 50ML falcon tube in A3, Solution II be in A4, N3 buffer in A1
'''

# Define tip racks
tiprack_1 = labware.load('opentrons-tiprack-300ul', 10)
tiprack_2 = labware.load('opentrons-tiprack-300ul', 11)

# Define Modules
magdeck = modules.load('magdeck', 7)

# pipette
p300 = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack_1, tiprack_2])


# Protocol:

# add Solution I/RNase A to each well & resuspend cells (24 mL total) (one tip box)
p300.distribute(
    250,
    reagents.wells('A3'),
    samples,
    mix_after=(10, 50),
    new_tip='always'
)

# add Solution II to each well (24 mL total)
p300.distribute(
    250,
    reagents.wells('A4'),
    samples
)

# 5 min incubation at room temperature
p300.delay(minutes=5)

# add N3 buffer to each well (12 mL total)
p300.distribute(
    125,
    reagents.wells('A1'),
    samples
)

# two tips from 2nd tip box

# Pause for centrifugation step. 10 mins, room temp, 2,000-3,000 x g


