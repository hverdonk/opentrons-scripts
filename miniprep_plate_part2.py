from opentrons import protocol_api,labware, instruments

# metadata
metadata = {
    'apiLevel': '2.2',
    'protocolName': 'Miniprep Plate',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Automates the Zymo kit "Zyppy-96 Plasmid MagBead Miniprep".',
}


def run(protocol_context):
    # Labware Setup
    tips1 = protocol_context.load_labware('opentrons_96_filtertiprack_200ul', '11')
    tips2 = protocol_context.load_labware('opentrons_96_filtertiprack_200ul', '10')
    tips3 = protocol_context.load_labware('opentrons_96_filtertiprack_200ul', '10')
    block = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '4')
    collection_plate = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '4')
    elution_plate = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '9')
    lysis_buffer = protocol_context.load_labware("agilent_1_reservoir_290ml", '1')
    neutralization_buffer = protocol_context.load_labware("agilent_1_reservoir_290ml", '2')
#     trough3 = protocol_context.load_labware("agilent_1_reservoir_290ml", '3')

    # put block on top of mag module to begin with

    # Pipette Setup
    p300 = protocol_context.load_instrument('p300_multi', 'left', tip_racks=[tips1, tips2, tips3])

    # Add a mix step after transfer
    # Add lysis buffer to deepwell block.
    for col in block.columns_by_name():
        p300.transfer(100, lysis_buffer.wells_by_name()['A1'], block.columns_by_name()[col][0], new_tip='always')

    # Pause 5 min

    for col in block.columns_by_name():
        p300.transfer(100, lysis_buffer.wells_by_name()['A1'], block.columns_by_name()[col][0], new_tip='always')
