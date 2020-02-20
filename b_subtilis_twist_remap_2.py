from opentrons import protocol_api, labware, instruments
import json

metadata = {

    'protocolName': 'twist_remapping',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'apiLevel': '2.2'}


def run(protocol_context):
    # labware setup
    tiprack_10ul = protocol_context.load_labware('geb_96_tiprack_10ul', '11')
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate_inc_18 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')

    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=[tiprack_10ul])

    # Do the transfers
    p10.transfer(5, plate_inc_18.wells_by_name()["B09"], deepwell.wells_by_name()["A1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F01"], deepwell.wells_by_name()["B1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A12"], deepwell.wells_by_name()["C1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B08"], deepwell.wells_by_name()["D1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A02"], deepwell.wells_by_name()["E1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D07"], deepwell.wells_by_name()["F1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["G01"], deepwell.wells_by_name()["G1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B02"], deepwell.wells_by_name()["H1"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D02"], deepwell.wells_by_name()["A2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["G12"], deepwell.wells_by_name()["B2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C05"], deepwell.wells_by_name()["C2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A08"], deepwell.wells_by_name()["D2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D09"], deepwell.wells_by_name()["E2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["G02"], deepwell.wells_by_name()["F2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F09"], deepwell.wells_by_name()["G2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B10"], deepwell.wells_by_name()["H2"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C12"], deepwell.wells_by_name()["A3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F06"], deepwell.wells_by_name()["B3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F08"], deepwell.wells_by_name()["C3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E05"], deepwell.wells_by_name()["D3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D11"], deepwell.wells_by_name()["E3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H12"], deepwell.wells_by_name()["F3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D08"], deepwell.wells_by_name()["G3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C09"], deepwell.wells_by_name()["H3"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A10"], deepwell.wells_by_name()["A4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H01"], deepwell.wells_by_name()["B4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A03"], deepwell.wells_by_name()["C4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E01"], deepwell.wells_by_name()["D4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E04"], deepwell.wells_by_name()["E4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C03"], deepwell.wells_by_name()["F4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B07"], deepwell.wells_by_name()["G4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A06"], deepwell.wells_by_name()["H4"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E10"], deepwell.wells_by_name()["A5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C04"], deepwell.wells_by_name()["B5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B06"], deepwell.wells_by_name()["C5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A09"], deepwell.wells_by_name()["D5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A11"], deepwell.wells_by_name()["E5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E11"], deepwell.wells_by_name()["F5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H03"], deepwell.wells_by_name()["G5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B04"], deepwell.wells_by_name()["H5"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E08"], deepwell.wells_by_name()["A6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E02"], deepwell.wells_by_name()["B6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H07"], deepwell.wells_by_name()["C6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H05"], deepwell.wells_by_name()["D6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["A07"], deepwell.wells_by_name()["E6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F12"], deepwell.wells_by_name()["F6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B03"], deepwell.wells_by_name()["G6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D05"], deepwell.wells_by_name()["H6"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E09"], deepwell.wells_by_name()["A7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["E03"], deepwell.wells_by_name()["B7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["G07"], deepwell.wells_by_name()["C7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C01"], deepwell.wells_by_name()["D7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["G09"], deepwell.wells_by_name()["E7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F03"], deepwell.wells_by_name()["F7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D10"], deepwell.wells_by_name()["G7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H10"], deepwell.wells_by_name()["H7"])
    p10.transfer(5, plate_inc_18.wells_by_name()["G06"], deepwell.wells_by_name()["A8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["G03"], deepwell.wells_by_name()["B8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H04"], deepwell.wells_by_name()["C8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C02"], deepwell.wells_by_name()["D8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C07"], deepwell.wells_by_name()["E8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F02"], deepwell.wells_by_name()["F8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B01"], deepwell.wells_by_name()["G8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H02"], deepwell.wells_by_name()["H8"])
    p10.transfer(5, plate_inc_18.wells_by_name()["H08"], deepwell.wells_by_name()["A9"])
    p10.transfer(5, plate_inc_18.wells_by_name()["C11"], deepwell.wells_by_name()["B9"])
    p10.transfer(5, plate_inc_18.wells_by_name()["B11"], deepwell.wells_by_name()["C9"])
    p10.transfer(5, plate_inc_18.wells_by_name()["F05"], deepwell.wells_by_name()["D9"])
    p10.transfer(5, plate_inc_18.wells_by_name()["D12"], deepwell.wells_by_name()["E9"])
