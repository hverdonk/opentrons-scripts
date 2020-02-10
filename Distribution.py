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
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '11')
    p300rack = protocol_context.load_labware('opentrons_96_tiprack_300ul', '10')
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
    p300 = protocol_context.load_instrument('p300_multi', 'left', tip_racks=[p300rack])
    p300.flow_rate.blow_out = 300   # blow out faster to avoid droplets clinging to pipette tips

    plate_list = [plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8, plate9]

    # Distribute volume from deep well plate to flat bottom plates, column by column
    # Only officially take from well 0 in the column, because the multichannel will reach the rest anyway

    # Move right to left (i.e., reverse the list) to avoid contaminating virgin wells
    master_plate = deepwell.columns_by_name()[::-1]

    for col in master_plate:
        p300.distribute(45, master_plate.columns_by_name()[col][0],
                           [plate.columns_by_name()[col][0] for plate in plate_list])
