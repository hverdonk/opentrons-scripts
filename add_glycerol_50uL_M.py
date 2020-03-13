from opentrons import protocol_api,labware, instruments

# metadata
metadata = {
    'apiLevel': '2.1',
    'protocolName': 'Add Glycerol - 50uL Multichannel',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute media containing antibiotic to distribution deepwell plates.',
}


def run(protocol_context):
    # Labware Setup
    p300rack = protocol_context.load_labware('opentrons_96_tiprack_300ul', '11')
    plate1 = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '4')
    plate2 = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '5')
    #plate3 = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '6')
    trough1 = protocol_context.load_labware("agilent_1_reservoir_290ml", '1')
    trough2 = protocol_context.load_labware("agilent_1_reservoir_290ml", '2')
    #trough3 = protocol_context.load_labware("agilent_1_reservoir_290ml", '3')

    # Pipette Setup
    p50 = protocol_context.load_instrument('p50_multi', 'left', tip_racks=[p300rack])
    p50.flow_rate.aspirate = 75    # half of the default speed
    p50.flow_rate.dispense = 150   # half of the default speed


    # Transfer media in troughs to deepwell plates
    # Only officially take from well 0 in the column, because the multichannel will reach the rest anyway

    for col in plate1.columns_by_name():
        p50.transfer(300, trough1.wells_by_name()['A1'], plate1.columns_by_name()[col][0], mix_after=(4, 300), new_tip='always')

    for col in plate1.columns_by_name():
        p50.transfer(300, trough2.wells_by_name()['A1'], plate2.columns_by_name()[col][0], mix_after=(4, 300), new_tip='always')

    '''
    for col in plate1.columns_by_name():
        p50.transfer(300, trough3.wells_by_name()['A1'], plate3.columns_by_name()[col][0], mix_after=(4, 300), new_tip='always')
    '''
