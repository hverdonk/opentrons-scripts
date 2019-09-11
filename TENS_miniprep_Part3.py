from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'TENS Plasmid Purification - Part 3',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automated plasmid purification using the TENS method "
                   "(https://openwetware.org/wiki/Miniprep/TENS_miniprep)",
}

# Define sample labware
samples = labware.load("corning_96_wellplate_360ul_flat", 5)

# Define reagents
resuspension_buffer = labware.load('usascientific_12_reservoir_22ml', 2)
# TROUGHS MUST BE CALIBRATED BEFORE USE

# Define tip racks
tiprack = labware.load('opentrons-tiprack-300ul', 6)

# pipette
p300 = instruments.P300_Multi(
    mount='right',
    tip_racks=[tiprack]
)


# Protocol:

num_columns = len(samples.columns())

# Resuspend pellet in buffer for long-term use/storage
for c in range(num_columns):
    p300.pick_up_tip(tiprack.columns(c))
    p300.transfer(30, resuspension_buffer, samples, pipette_after=(5, 15))
    p300.drop_tip()

