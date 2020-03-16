from opentrons import protocol_api, labware, instruments

# metadata
metadata = {
    'apiLevel': '2.1',
    'protocolName': 'Prep Deepwells',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute media containing antibiotic to distribution deepwell plates.',
}


def run(protocol_context):
    # Labware Setup
    p300rack = protocol_context.load_labware('opentrons_96_tiprack_300ul', '11')
    plate1 = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '4')
    plate2 = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '5')
    plate3 = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '6')
    trough1 = protocol_context.load_labware("agilent_1_reservoir_290ml", '1')
    trough2 = protocol_context.load_labware("agilent_1_reservoir_290ml", '2')
    trough3 = protocol_context.load_labware("agilent_1_reservoir_290ml", '3')

    # Pipette Setup
    p300 = protocol_context.load_instrument('p300_multi', 'left', tip_racks=[p300rack])


    # Transfer media in troughs to deepwell plates
    # Only officially take from well 0 in the column, because the multichannel will reach the rest anyway

    p300.pick_up_tip()
    for col in plate1.columns_by_name():
        p300.transfer(1200, trough1.wells_by_name()['A1'], plate1.columns_by_name()[col][0], new_tip='never')

    for col in plate1.columns_by_name():
        p300.transfer(1200, trough2.wells_by_name()['A1'], plate2.columns_by_name()[col][0], new_tip='never')

    for col in plate1.columns_by_name():
        p300.transfer(1200, trough3.wells_by_name()['A1'], plate3.columns_by_name()[col][0], new_tip='never')
    p300.drop_tip()
