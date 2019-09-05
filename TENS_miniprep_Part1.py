from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'TENS Plasmid Purification - Part 1',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automated plasmid purification using the TENS method "
                   "(https://openwetware.org/wiki/Miniprep/TENS_miniprep)",
}

# Define sample labware
samples = labware.load("corning_96_wellplate_360ul_flat", 5)
trash = labware.load('axygen_1_reservoir_90ml', 1)

# Define reagents
LB = labware.load('usascientific_12_reservoir_22ml', 9)
TENS = labware.load('usascientific_12_reservoir_22ml', 4)
NaAC = labware.load('usascientific_12_reservoir_22ml', 6)
# TROUGHS MUST BE CALIBRATED BEFORE USE

# Define tip racks
tiprack_1 = labware.load('opentrons-tiprack-300ul', 7)
tiprack_2 = labware.load('opentrons-tiprack-300ul', 8)
tiprack_3 = labware.load('opentrons-tiprack-300ul', 10)
tiprack_4 = labware.load('opentrons-tiprack-300ul', 11)


# pipette
p300 = instruments.P300_Multi(
    mount='right',
    tip_racks=[tiprack_1, tiprack_2, tiprack_3, tiprack_4])


# Protocol:

# Remove & discard supernatant after centrifuging
p300.consolidate(
    1200,
    samples,
    trash,
    new_tip='always'
)

# Resuspend either in 50 μL of LB or P1 buffer or TE/RNAse
p300.distribute(
    50,
    LB,
    samples,
    pipette_after=(10, 300),
    new_tip='always'
)

# Add TENS buffer
p300.distribute(
    300,
    TENS,
    samples,
    pipette_after=(10, 300),
    new_tip='always'
)

# Add NaAC
p300.distribute(
    100,
    NaAC,
    samples,
    pipette_after=(10, 300),
    new_tip='always'
)
