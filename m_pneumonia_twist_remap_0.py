from opentrons import protocol_api, labware, instruments
import json

metadata = {

    'protocolName': 'twist_remapping',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'apiLevel': '2.1'}

def run(protocol_context):
    # labware setup
    tiprack_10ul = protocol_context.load_labware('geb_96_tiprack_10ul', '11')
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate_16w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate_15w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate_17w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate_18w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate_14w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate_13w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate_11w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '7')
    plate_12w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '8')

    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=[tiprack_10ul])

    # Do the transfers

