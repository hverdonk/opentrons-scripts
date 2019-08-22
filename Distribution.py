from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'Distribute Cultures',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Another simple protocol to get started using OT2',
}

# labware
tiprack = labware.load('opentrons-tiprack-300ul', '1')  # check tip volume for this one later
master_plate = labware.load("usascientific_96_wellplate_2.4ml_deep", '2')
plate1 = labware.load("corning_96_wellplate_360ul_flat", '3')
plate2 = labware.load("corning_96_wellplate_360ul_flat", '4')
plate3 = labware.load("corning_96_wellplate_360ul_flat", '5')
plate4 = labware.load("corning_96_wellplate_360ul_flat", '6')
plate5 = labware.load("corning_96_wellplate_360ul_flat", '7')
plate6 = labware.load("corning_96_wellplate_360ul_flat", '8')
plate7 = labware.load("corning_96_wellplate_360ul_flat", '9')
plate8 = labware.load("corning_96_wellplate_360ul_flat", '10')
plate9 = labware.load("corning_96_wellplate_360ul_flat", '11')
trash = labware.load('trash-box', 'TRASH')  # 'trash-box' name no longer supported

# pipettes
pipette = instruments.P300_Multi(mount='right', tip_racks=[tiprack])
# add trash?

# commands
plate_list = [plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8, plate9]

for p in plate_list:
    pipette.distribute(
        50,
        master_plate,
        p,
        mix_before=(3, 100),
        disposal_vol=10
    )   # include extra liquid "disposal_vol" to make dispenses more accurate

