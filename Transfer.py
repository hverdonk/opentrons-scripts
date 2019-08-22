from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'Transfer From Stock',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Protocol to grow up bacteria from stock plate',
}

# labware
tiprack = labware.load('opentrons-tiprack-300ul', '11')  # check tip volume for this one later
donor_plate = labware.load("corning_96_wellplate_360ul_flat", '7')
recipient_plate = labware.load("usascientific_96_wellplate_2.4ml_deep", '8')
lb_broth = labware.load("agilent_1_reservoir_290ml", '10')
trash = labware.load('trash-box', 'TRASH')  # 'trash-box' name no longer supported

# pipettes
pipette = instruments.P300_Multi(mount='right', tip_racks=[tiprack])

# commands

# fill deepwell plate with broth
pipette.distribute(
    1200,
    lb_broth,
    recipient_plate,
    mix_before=(3, 1500),
    disposal_vol=10
)

# innoculate deepwell plate from donor plate
pipette.distribute(
    5,
    donor_plate,
    recipient_plate,
    mix_before=(3, 5),
    new_tip='always'
)


