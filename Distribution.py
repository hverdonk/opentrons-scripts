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
    p300rack = protocol_context.load_labware('opentrons_96_tiprack_300ul', '11')
    master_plate = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate1 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate2 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate3 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate4 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate5 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate6 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate7 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '7')
    plate8 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '8')
    plate9 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '9')

    # Pipette Setup
    p300 = protocol_context.load_instrument('p300_multi', 'right', tip_racks=[p300rack])

    plate_list_1 = [plate1, plate2, plate3, plate4, plate5, plate6]
    plate_list_2 = [plate7, plate8, plate9]

    # Distribute volume from deep well plate to flat bottom plates, column by column
    for col in master_plate.columns_by_name():
        p300.pick_up_tip()
        p300.aspirate(275, master_plate.columns_by_name()[col][0])
        p300.dispense(45, [plate.columns_by_name()[col][0] for plate in plate_list_1])
        p300.aspirate(135, master_plate.columns_by_name()[col][0])
        p300.dispense(45, [plate.columns_by_name()[col][0] for plate in plate_list_2])
        p300.drop_tip()
        
