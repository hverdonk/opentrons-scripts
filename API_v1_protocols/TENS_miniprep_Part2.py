from opentrons import labware, instruments, modules, robot

# metadata
metadata = {
    'protocolName': 'TENS Plasmid Purification - Part 2',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automated plasmid purification using the TENS method "
                   "(https://openwetware.org/wiki/Miniprep/TENS_miniprep)",
}

# Define module
tempdeck = modules.load('tempdeck', 4)

# Define sample labware
old_samples = labware.load("corning_96_wellplate_360ul_flat", 3)
samples = labware.load("corning_96_wellplate_360ul_flat", 5)
trash = labware.load('agilent_1_reservoir_290ml', 1)

# Define reagents
EtOH_100 = labware.load('agilent_1_reservoir_290ml', 4, share=True)
EtOH_70 = labware.load('agilent_1_reservoir_290ml', 2)
# TROUGHS MUST BE CALIBRATED BEFORE USE

# Define tip racks
tiprack_1 = labware.load('opentrons-tiprack-300ul', 6)
tiprack_2 = labware.load('opentrons-tiprack-300ul', 7)
tiprack_3 = labware.load('opentrons-tiprack-300ul', 8)
tiprack_4 = labware.load('opentrons-tiprack-300ul', 9)
tiprack_5 = labware.load('opentrons-tiprack-300ul', 10)
tiprack_6 = labware.load('opentrons-tiprack-300ul', 11)


# pipette
p300 = instruments.P300_Multi(
    mount='right',
    tip_racks=[tiprack_1, tiprack_2, tiprack_3, tiprack_4, tiprack_5, tiprack_6])


# Protocol:

num_columns = len(samples.columns())

# Transfer 450 uL supernatant in each well to a new plate. Tip remains 2 mm
# from the bottom of the well to avoid disturbing the pellet.
for c in range(num_columns):
    p300.pick_up_tip(tiprack_1.columns(c))
    p300.aspirate(300, old_samples.columns(c).bottom(2))
    p300.dispense(300, samples.columns(c))
    p300.aspirate(150, old_samples.columns(c).bottom(2))
    p300.dispense(150, samples.columns(c))
    p300.drop_tip()

# Pause to empty trash
robot.pause()

# Dispense slowly to avoid splashes & contamination
p300.set_flow_rate(dispense=100)  # in uL/s

# Add 1 mL 100% ice cold EtOH to the supernatant at the top of the well
# to avoid contaminating the tips
for c in range(num_columns):
    p300.pick_up_tip(tiprack_2.columns(c))
    p300.aspirate(300, EtOH_100.wells('A1'))
    p300.dispense(300, samples.columns(c).top())
    p300.aspirate(300, EtOH_100.wells('A1'))
    p300.dispense(300, samples.columns(c).top())
    p300.aspirate(300, EtOH_100.wells('A1'))
    p300.dispense(300, samples.columns(c).top())
    p300.aspirate(100, EtOH_100.wells('A1'))
    p300.dispense(100, samples.columns(c).top())
    p300.drop_tip()

# Set dispense rate back to the default
p300.set_flow_rate(dispense=300)

# Spin down plate, then return to robot. Empty trash
robot.pause()

# Remove the supernatant 2mm from the well bottom to avoid disturbing the pellet
for c in range(num_columns):
    p300.pick_up_tip(tiprack_3.columns(c))
    p300.aspirate(300, samples.columns(c).bottom(2))
    p300.dispense(300, trash.wells('A1'))
    p300.aspirate(300, samples.columns(c).bottom(2))
    p300.dispense(300, trash.wells('A1'))
    p300.aspirate(300, samples.columns(c).bottom(2))
    p300.dispense(300, trash.wells('A1'))
    p300.aspirate(100, samples.columns(c).bottom(2))
    p300.dispense(100, trash.wells('A1'))
    p300.drop_tip()

# Pause to empty trash
robot.pause()

# Wash by first adding 0.5 mL of 70% EtOH
for c in range(num_columns):
    p300.pick_up_tip(tiprack_4.columns(c))
    p300.aspirate(300, EtOH_70.wells('A1'))
    p300.dispense(300, samples.columns(c).top())
    p300.aspirate(200, EtOH_70.wells('A1'))
    p300.dispense(200, samples.columns(c).top())
    p300.drop_tip()

# Spin down plate, then return to robot. Empty trash
robot.pause()

# Remove wash liquid 2mm from the well bottom to avoid disturbing the pellet
for c in range(num_columns):
    p300.pick_up_tip(tiprack_5.columns(c))
    p300.aspirate(300, samples.columns(c).bottom(2))
    p300.dispense(300, trash.wells('A1'))
    p300.aspirate(200, samples.columns(c).bottom(2))
    p300.dispense(200, trash.wells('A1'))
    p300.drop_tip()

