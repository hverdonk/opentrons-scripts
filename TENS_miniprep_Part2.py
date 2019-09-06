from opentrons import labware, instruments, modules, robot

# metadata
metadata = {
    'protocolName': 'TENS Plasmid Purification - Part 1',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automated plasmid purification using the TENS method "
                   "(https://openwetware.org/wiki/Miniprep/TENS_miniprep)",
}

# Define sample labware
old_samples = labware.load("corning_96_wellplate_360ul_flat", 6)
samples = labware.load("corning_96_wellplate_360ul_flat", 5)
trash = labware.load('axygen_1_reservoir_90ml', 1)

# Define reagents
EtOH_100 = labware.load('usascientific_12_reservoir_22ml', 4, share='true')
EtOH_70 = labware.load('usascientific_12_reservoir_22ml', 9)
# TROUGHS MUST BE CALIBRATED BEFORE USE

# Define tip racks
tiprack_1 = labware.load('opentrons-tiprack-300ul', 7)
tiprack_2 = labware.load('opentrons-tiprack-300ul', 8)
tiprack_3 = labware.load('opentrons-tiprack-300ul', 10)
tiprack_4 = labware.load('opentrons-tiprack-300ul', 11)

# Define module
tempdeck = modules.load('tempdeck', 4)


# pipette
p300 = instruments.P300_Multi(
    mount='right',
    tip_racks=[tiprack_1, tiprack_2, tiprack_3, tiprack_4])


# Protocol:

# Transfer supernatant to a new plate. Tip remains 2 mm from the bottom of the well
# to avoid disturbing the pellet
p300.transfer(
    450,
    old_samples,
    samples,
    new_tip='always'
).bottom(2)

# Add 1 mL 100% ice cold EtOH
p300.distribute(
    1000,
    EtOH_100,
    samples,
    pipette_after=(10, 300),
    new_tip='always'
)

# Spin down plate, then return to robot
robot.pause()
