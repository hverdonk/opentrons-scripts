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

# Experiment parameters
# input volume (in uL) in each well of deepwell plate
well_volume = 1200


# Protocol:

# Remove & discard supernatant after centrifuging

# Dispense slowly to avoid splashes & contamination
p300.set_flow_rate(dispense=100)  # in uL/s

# Find number of transfers per well
full_transfers = well_volume // 300
remainder = (well_volume/300) - full_transfers
partial_transfer_volume = round(300*remainder)

# Discard full supernatant volume in 300 uL increments
for c in range(len(samples.columns())):
    p300.pick_up_tip(tiprack_1.columns(c))
    n = full_transfers
    while n > 0:
        p300.aspirate(300, samples.columns(c))
        p300.dispense(300, trash).top()
        n -= 1
    if partial_transfer_volume > 0:
        p300.aspirate(partial_transfer_volume, samples.columns(c))
        p300.dispense(partial_transfer_volume, trash).top()
    p300.drop_tip()

# Set dispense rate back to the default
p300.set_flow_rate(dispense=300)


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
