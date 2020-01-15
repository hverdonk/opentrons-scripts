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
    p300 = protocol_context.load_instrument('p300_multi', 'right',
                                            tip_racks=tiprack)

    # commands
    plate_list = [plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8, plate9]

    for p in plate_list:
        pipette.distribute(
            50,
            master_plate,
            p,
            mix_before=(3, 100),
            disposal_vol=10
        )   # include extra liquid "disposal_vol" to make dispenses more accurate

