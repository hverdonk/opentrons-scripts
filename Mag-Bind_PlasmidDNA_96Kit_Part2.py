from opentrons import labware, instruments, modules

# metadata
metadata = {
    'protocolName': 'Plasmid Mag-Bind Purification Part 2',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automates Omega Bio-Tek's Mag-Bind plasmid purification kit",
}

# Define sample labware
samples = labware.load("corning_96_wellplate_360ul_flat", 8)
mag_plate = labware.load('usascientific_96_wellplate_2.4ml_deep', 7, share=True)

# Define reagents
reagents = labware.load('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 4)
'''
Let ETR binding buffer be in B3 and the magbeads be in A2
'''

# Define tip racks
tiprack_1 = labware.load('opentrons-tiprack-300ul', 10)
tiprack_2 = labware.load('opentrons-tiprack-300ul', 11)

# Define Modules
magdeck = modules.load('magdeck', 7)

# pipettes
p300 = instruments.P300_Single(
    mount='right',
    tip_racks=[tiprack_1, tiprack_2])


# Protocol:

# Transfer cleared cell lysate into deepwell plate. First plate of tips is now gone
p300.transfer(
    500,
    samples,
    mag_plate,
    new_tip='always'
)

# Add 500 μL ETR Binding Buffer (48mL total) and 20 μL (about 2mL) Mag-Bind® Particles RQ.
# Mix thoroughly by pipetting up and down 10 times.
p300.distribute(
    500,
    reagents.wells('B3'),
    mag_plate
)

p300.distribute(
    20,
    reagents.wells('A2'),
    mag_plate,
    mix_after=(10, 300)
)

# Let sit for 5 minutes at room temperature.
p300.delay(minutes=5)

# Engage magdeck and wait 5 mins until beads are completely cleared from solution
magdeck.engage(offset=-4)  # offset in mm down from default position
p300.delay(minutes=5)
