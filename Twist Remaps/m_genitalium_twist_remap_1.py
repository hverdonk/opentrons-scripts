from opentrons import protocol_api, labware, instruments

metadata = {

    'protocolName': 'twist_remapping',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'apiLevel': '2.1'}


def run(protocol_context):
    # labware setup
    tiprack_10ul = protocol_context.load_labware('geb_96_tiprack_10ul', '11')
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate_23w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate_21w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate_24w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '3')

    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=[tiprack_10ul])

    # Do transfers
    p10.transfer(5, plate_23w.wells_by_name()["C11"], deepwell.wells_by_name()["B1"])
    p10.transfer(5, plate_23w.wells_by_name()["F1"], deepwell.wells_by_name()["B2"])
    p10.transfer(5, plate_23w.wells_by_name()["E10"], deepwell.wells_by_name()["B3"])
    p10.transfer(5, plate_23w.wells_by_name()["D10"], deepwell.wells_by_name()["B4"])
    p10.transfer(5, plate_23w.wells_by_name()["G10"], deepwell.wells_by_name()["B5"])
    p10.transfer(5, plate_23w.wells_by_name()["D12"], deepwell.wells_by_name()["B6"])
    p10.transfer(5, plate_23w.wells_by_name()["B11"], deepwell.wells_by_name()["B7"])
    p10.transfer(5, plate_23w.wells_by_name()["H11"], deepwell.wells_by_name()["B8"])
    p10.transfer(5, plate_23w.wells_by_name()["H10"], deepwell.wells_by_name()["B9"])
    p10.transfer(5, plate_23w.wells_by_name()["F10"], deepwell.wells_by_name()["B10"])
    p10.transfer(5, plate_23w.wells_by_name()["D1"], deepwell.wells_by_name()["B11"])
    p10.transfer(5, plate_23w.wells_by_name()["E11"], deepwell.wells_by_name()["B12"])
    p10.transfer(5, plate_21w.wells_by_name()["A8"], deepwell.wells_by_name()["A1"])
    p10.transfer(5, plate_21w.wells_by_name()["F8"], deepwell.wells_by_name()["A2"])
    p10.transfer(5, plate_21w.wells_by_name()["C9"], deepwell.wells_by_name()["A3"])
    p10.transfer(5, plate_21w.wells_by_name()["G8"], deepwell.wells_by_name()["A4"])
    p10.transfer(5, plate_21w.wells_by_name()["H7"], deepwell.wells_by_name()["A5"])
    p10.transfer(5, plate_21w.wells_by_name()["E8"], deepwell.wells_by_name()["A6"])
    p10.transfer(5, plate_21w.wells_by_name()["A9"], deepwell.wells_by_name()["A7"])
    p10.transfer(5, plate_21w.wells_by_name()["B7"], deepwell.wells_by_name()["A8"])
    p10.transfer(5, plate_21w.wells_by_name()["B8"], deepwell.wells_by_name()["A9"])
    p10.transfer(5, plate_21w.wells_by_name()["B9"], deepwell.wells_by_name()["A10"])
    p10.transfer(5, plate_21w.wells_by_name()["C7"], deepwell.wells_by_name()["A11"])
    p10.transfer(5, plate_21w.wells_by_name()["F6"], deepwell.wells_by_name()["A12"])
    p10.transfer(5, plate_24w.wells_by_name()["G2"], deepwell.wells_by_name()["C1"])
    p10.transfer(5, plate_24w.wells_by_name()["B2"], deepwell.wells_by_name()["C2"])
    p10.transfer(5, plate_24w.wells_by_name()["G6"], deepwell.wells_by_name()["C3"])
    p10.transfer(5, plate_24w.wells_by_name()["G3"], deepwell.wells_by_name()["C4"])
    p10.transfer(5, plate_24w.wells_by_name()["F6"], deepwell.wells_by_name()["C5"])
    p10.transfer(5, plate_24w.wells_by_name()["H7"], deepwell.wells_by_name()["C6"])
    p10.transfer(5, plate_24w.wells_by_name()["G7"], deepwell.wells_by_name()["C7"])
    p10.transfer(5, plate_24w.wells_by_name()["H3"], deepwell.wells_by_name()["C8"])
    p10.transfer(5, plate_24w.wells_by_name()["F7"], deepwell.wells_by_name()["C9"])
    p10.transfer(5, plate_24w.wells_by_name()["D7"], deepwell.wells_by_name()["C10"])
    p10.transfer(5, plate_24w.wells_by_name()["A1"], deepwell.wells_by_name()["C11"])
    p10.transfer(5, plate_24w.wells_by_name()["E7"], deepwell.wells_by_name()["C12"])
    p10.transfer(5, plate_24w.wells_by_name()["A2"], deepwell.wells_by_name()["D1"])
    p10.transfer(5, plate_24w.wells_by_name()["D8"], deepwell.wells_by_name()["D2"])
    p10.transfer(5, plate_24w.wells_by_name()["F1"], deepwell.wells_by_name()["D3"])
    p10.transfer(5, plate_24w.wells_by_name()["G1"], deepwell.wells_by_name()["D4"])
    p10.transfer(5, plate_24w.wells_by_name()["C1"], deepwell.wells_by_name()["D5"])
    p10.transfer(5, plate_24w.wells_by_name()["C7"], deepwell.wells_by_name()["D6"])
    p10.transfer(5, plate_24w.wells_by_name()["B1"], deepwell.wells_by_name()["D7"])
