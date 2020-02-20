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
    plate_12w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')

    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=[tiprack_10ul])

    # Do the transfers
    p10.transfer(5, plate_12w.wells_by_name()["D5"], deepwell.wells_by_name()["A3"])
    p10.transfer(5, plate_12w.wells_by_name()["C5"], deepwell.wells_by_name()["A4"])
    p10.transfer(5, plate_12w.wells_by_name()["G6"], deepwell.wells_by_name()["A5"])
    p10.transfer(5, plate_12w.wells_by_name()["C8"], deepwell.wells_by_name()["A6"])
    p10.transfer(5, plate_12w.wells_by_name()["D7"], deepwell.wells_by_name()["A7"])
    p10.transfer(5, plate_12w.wells_by_name()["E7"], deepwell.wells_by_name()["A8"])
    p10.transfer(5, plate_12w.wells_by_name()["B8"], deepwell.wells_by_name()["A9"])
    p10.transfer(5, plate_12w.wells_by_name()["F5"], deepwell.wells_by_name()["A10"])
    p10.transfer(5, plate_12w.wells_by_name()["A9"], deepwell.wells_by_name()["A11"])
    p10.transfer(5, plate_12w.wells_by_name()["C6"], deepwell.wells_by_name()["A12"])
    p10.transfer(5, plate_12w.wells_by_name()["F1"], deepwell.wells_by_name()["B1"])
    p10.transfer(5, plate_12w.wells_by_name()["F8"], deepwell.wells_by_name()["B2"])
    p10.transfer(5, plate_12w.wells_by_name()["G7"], deepwell.wells_by_name()["B3"])
    p10.transfer(5, plate_12w.wells_by_name()["G5"], deepwell.wells_by_name()["B4"])
    p10.transfer(5, plate_12w.wells_by_name()["F6"], deepwell.wells_by_name()["B5"])
    p10.transfer(5, plate_12w.wells_by_name()["E8"], deepwell.wells_by_name()["B6"])
    p10.transfer(5, plate_12w.wells_by_name()["E5"], deepwell.wells_by_name()["B7"])
    p10.transfer(5, plate_12w.wells_by_name()["H7"], deepwell.wells_by_name()["B8"])
    p10.transfer(5, plate_12w.wells_by_name()["D6"], deepwell.wells_by_name()["B9"])
    p10.transfer(5, plate_12w.wells_by_name()["H6"], deepwell.wells_by_name()["B10"])
