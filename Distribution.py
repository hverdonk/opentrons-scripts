from opentrons import protocol_api,labware, instruments

# metadata
metadata = {
    'apiLevel': '2.1',
    'protocolName': 'Distribute Cultures',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Another simple protocol to get started using OT2',
}


def run(protocol_context):
    # Labware Setup
    tiprack = labware.load('opentrons_96_tiprack_300ul', '11')
    master_plate = labware.load("usascientific_96_wellplate_2.4ml_deep", '10')
    plate1 = labware.load("corning_96_wellplate_360ul_flat", '1')
    plate2 = labware.load("corning_96_wellplate_360ul_flat", '2')
    plate3 = labware.load("corning_96_wellplate_360ul_flat", '3')
    plate4 = labware.load("corning_96_wellplate_360ul_flat", '4')
    plate5 = labware.load("corning_96_wellplate_360ul_flat", '5')
    plate6 = labware.load("corning_96_wellplate_360ul_flat", '6')
    plate7 = labware.load("corning_96_wellplate_360ul_flat", '7')
    plate8 = labware.load("corning_96_wellplate_360ul_flat", '8')
    plate9 = labware.load("corning_96_wellplate_360ul_flat", '9')

    # Pipette Setup
    p300 = protocol_context.load_instrument('p300_multi', 'right', tip_racks=tiprack)

    plate_list_1 = [plate1, plate2, plate3, plate4, plate5, plate6]
    plate_list_2 = [plate7, plate8, plate9]

    # Distribute volume from deep well plate to flat bottom plates, column by column
    for col in master_plate.columns_by_name():
        p300.pick_up_tip()
        p300.aspirate(275, master_plate[col])
        p300.dispense(45, [plate.columns_by_name()[col] for plate in plate_list_1])
        p300.aspirate(135, master_plate[col])
        p300.dispense(45, [plate.columns_by_name()[col] for plate in plate_list_2])
        p300.drop_tip()

    # from master_plate, aspirate 275uL from column 1
    # Dispense 45uL into column 1 of plates 1-6 (270uL total)
    # from master_plate, aspirate 135uL from column 1 (140uL total)
    # dispense 45uL into column 1 of plates 7-9 (135uL total)
    # drop tips
    # repeat with other columns
