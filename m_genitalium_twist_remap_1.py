from opentrons import protocol_api, labware, instruments

metadata = {

    'protocolName': 'twist_remapping',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'apiLevel': '2.1'}


def run(protocol_context):
    # labware setup
    tiprack_10ul = protocol_context.load_labware('geb_96_tiprack_10ul', '11')
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate_20w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate_24w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate_21w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate_22w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate_18w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate_19w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate_23w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '7')

    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=[tiprack_10ul])

    # Do transfers
