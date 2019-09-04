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
reagents = labware.load('opentrons-tuberack-2ml-eppendorf', 4)
'''Let Solution I be in A1, Solution II be in B1, N3 buffer in C1, 
'''

# Define tip racks
tiprack_1 = labware.load('opentrons-tiprack-300ul', 10)
tiprack_2 = labware.load('opentrons-tiprack-300ul', 11)

# Define Modules
magdeck = modules.load('magdeck', 7)

# pipettes
p50 = instruments.P50_Single(
    mount='left',
    tip_racks=[tiprack_1])

p300 = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack_2])

# pipette = instruments.P300_Multi(mount='right', tip_racks=[tiprack])  just in case


# commands

# add Solution I/RNase A to each well & resuspend cells
p300.distribute(
    250,
    reagents.wells('A1'),
    samples,
    mix_after=(3, 50),
    new_tip='always'
)

# add Solution II to each well
p300.distribute(
    250,
    reagents.wells('B1'),
    samples
)
