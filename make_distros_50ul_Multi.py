from opentrons import protocol_api,labware, instruments

# metadata
metadata = {
    'apiLevel': '2.1',
    'protocolName': 'make_distros',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Create new stock for a FreeGenes distribution',
}


def run(protocol_context):
    # Labware Setup
    master_plate = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '11')
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
    p50 = protocol_context.load_instrument('p50_multi', 'left', tip_racks=[p300rack])
    p50.flow_rate.blow_out = 400   # blow out faster to avoid droplets clinging to pipette tips

    plate_list = [plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8, plate9]


    # Distribute volume from deep well plate to flat bottom plates, column by column
    # Move right to left (i.e., start at column 12) to avoid contaminating virgin wells
    # Only officially take from well 0 in the column, because the multichannel will reach the rest anyway
    right = len(master_plate.columns()) - 1
    left = -1
    for col in range(right, left, -1):
        p50.distribute(45, master_plate.columns()[col][0],
                           [plate.columns()[col][0] for plate in plate_list])
