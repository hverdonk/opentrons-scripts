# Written by Hannah Verdonk
# 4 Sept 2019
from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'Plasmid Mag-Bind Purification',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automates Omega Bio-Tek's Mag-Bind plasmid purification kit",
}

# labware
tiprack = labware.load('opentrons-tiprack-300ul', '11')
plate = labware.load("usascientific_96_wellplate_2.4ml_deep", '4')
trash = labware.load('trash-box', 'TRASH')

# pipettes
pipette = instruments.P300_Multi(mount='right', tip_racks=[tiprack])  # TODO: change this
# add trash?

# commands

# add Solution I/RNase A to each well & resuspend cells
pipette.distribute(
    250,
    #source well for solution 1,
    plate,
    mix_after=(3, 50),
    new_tip='always'
)
