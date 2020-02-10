metadata = {

    'protocolName': 'p300_test',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Test to see if reassembled p300 works correctly',
    'apiLevel': '2.1'}


def run(protocol_context):
    # labware setup
    tiprack = protocol_context.load_labware('opentrons_96_tiprack_300ul', '11')
    trough = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')

    # instrument setup
    p300 = protocol_context.load_instrument('p300_multi', 'left', tip_racks=[tiprack])

    # Transfer water into plate, watching for poor volume control
    for col in plate:
        p300.distribute(45, trough.columns_by_name()[0][0], plate.columns_by_name()[col][0])
