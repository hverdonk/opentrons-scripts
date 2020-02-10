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
final_plate = labware.load("biorad_96_wellplate_200ul_pcr", 3)

# Define reagents
resuspension_buffer = labware.load('agilent_1_reservoir_290ml', 2)

# Define tip racks
tiprack = labware.load('opentrons-tiprack-300ul', 6)

# pipette
p300 = instruments.P300_Multi(
    mount='right',
    tip_racks=[tiprack]
)


# Protocol:

columns = 12

# Resuspend pellet in buffer & transfer to PCR plate
for c in range(columns):
    p300.transfer(30,
                  resuspension_buffer.wells('A1'),
                  samples.columns(c),
                  mix_after=(5, 15),
                  new_tip='never')

    p300.transfer(30,
                  samples.columns(c),
                  final_plate.columns(c),
                  new_tip='always')



