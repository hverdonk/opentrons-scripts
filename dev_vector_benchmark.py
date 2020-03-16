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
    p200rack = protocol_context.load_labware('opentrons_96_filtertiprack_200ul', '11')
    p10rack = protocol_context.load_labware('geb_96_tiprack_10ul', '10')
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '4')
    OD_plate = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '5')
    trough = protocol_context.load_labware("agilent_1_reservoir_290ml", '1')

    # Pipette Setup
    p300 = protocol_context.load_instrument('p300_multi', 'left', tip_racks=[p200rack])
    p10 = protocol_context.load_instrument('p10_multi', 'right', tip_racks=[p10rack])

    # Change these every time you do a dilution
    prior_col = '1'
    destination_col = '2'

    # Add selective media to new column
    p300.transfer(1200, trough.wells_by_name()['A1'], deepwell.columns_by_name()[destination_col][0],
                  new_tip='always')

    # # Uncomment for morning OD
    # p300.transfer(100, deepwell.columns_by_name()[prior_col][0], OD_plate.columns_by_name()[prior_col][0],
    #               new_tip='always')

    # # Uncomment for morning dilution (1:400)
    # p10.transfer(3, deepwell.columns_by_name()[prior_col][0], deepwell.columns_by_name()[destination_col][0],
    #               new_tip='always')

    # # Uncomment for evening dilution (1:1,200)
    # p10.transfer(1, deepwell.columns_by_name()[prior_col][0], deepwell.columns_by_name()[destination_col][0],
    #               new_tip='always')
