from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'TENS Plasmid Purification - Part 1',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': "Automated plasmid purification using the TENS method "
                   "(https://openwetware.org/wiki/Miniprep/TENS_miniprep)",
}

# Define sample labware
samples = labware.load("usascientific_96_wellplate_2.4ml_deep", 5)
trash = labware.load('agilent_1_reservoir_290ml', 1)

# Define reagents
LB = labware.load('agilent_1_reservoir_290ml', 9)
TENS = labware.load('agilent_1_reservoir_290ml', 4)
NaAC = labware.load('agilent_1_reservoir_290ml', 6)

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
columns = 12

# Find number of transfers per well
full_transfers = well_volume // 300
remainder = (well_volume/300) - full_transfers
partial_transfer_volume = round(300*remainder)

# Discard full supernatant volume in 300 uL increments
for c in range(columns):
    p300.pick_up_tip()
    n = full_transfers
    while n > 0:
        p300.aspirate(300, samples.columns(c))
        p300.dispense(300, trash.wells('A1').top())
        p300.blow_out()
        n -= 1
    if partial_transfer_volume > 0:
        p300.aspirate(partial_transfer_volume, samples.columns(c))
        p300.dispense(partial_transfer_volume, trash.wells('A1').top())
        p300.blow_out()
    p300.drop_tip()

# Set dispense rate back to the default
p300.set_flow_rate(dispense=300)


# Resuspend either in 50 μL of LB or P1 buffer or TE/RNAse
for c in range(columns):
    p300.transfer(50,
                  LB.wells('A1'),
                  samples.columns(c),
                  mix_after=(10, 300),
                  new_tip='always'
                  )

# p300.distribute(50, LB.wells('A1'), samples, pipette_after=(10, 300), new_tip='always')

# Add TENS buffer
for c in range(columns):
    p300.transfer(300,
                  TENS.wells('A1'),
                  samples.columns(c),
                  mix_after=(10, 300),
                  new_tip='always'
                  )

# p300.distribute(300, TENS.wells('A1'), samples, pipette_after=(10, 300), new_tip='always')

# Add NaAC
for c in range(columns):
    p300.transfer(100,
                  NaAC.wells('A1'),
                  samples.columns(c),
                  mix_after=(10, 300),
                  new_tip='always')

# p300.distribute(100, NaAC.wells('A1'), samples, pipette_after=(10, 300), new_tip='always')
