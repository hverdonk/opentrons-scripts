from opentrons import protocol_api,labware, instruments

metadata = {
    'author': 'Chaz <chaz@opentrons.com',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

def run(protocol):

    # Deck Setup #
    # Samples (all in column 12) - the extracted RNA from the last step
    elution_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '9')
    
    # Reaction plate
    # the final destination for all this stuff
    reaction_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '8')
    
    # Temp deck
    # where all the reagents we're adding live. Must be cold
    temp_module = protocol.load_module('Temperature Module', '7')
    cold_reagents = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap',
                                     label='Temperature-Controlled Tubes')
    # TODO: set temp module temperature to something like 4C
    reaction_mix = cold_reagents['A1']
    endogenous_control_mix = cold_reagents['A2']
    water = cold_reagents['A3']
    pcr_dilution = [cold_reagents['B{}'.format(x)] for x in range(1, 7)]

    # Set up pipette 
    tips20 = [protocol.load_labware('opentrons_96_filtertiprack_20ul', str(x)) for x in range(10, 12)]
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=tips20)

    # Protocol Run #
    # Set up reactions
    [p20.distribute(15, reaction_mix, col, new_tip='always')
        for col in [reaction_plate.columns_by_name()[str(x)] for x in [1, 2, 3, 5, 6]]]

    # Set up Endogenous controls
    p20.distribute(15, endogenous_control_mix, reaction_plate.columns_by_name()['4'], new_tip='always')

    # Place samples in wells
    [p20.transfer(5, elution_plate.columns_by_name()['12'], col, new_tip='always')
        for col in [reaction_plate.columns_by_name()[str(x)] for x in range(1, 5)]]

    # Place controls in wells
    ctrl_col = [reaction_plate.columns_by_name()[str(x)] for x in range(5, 7)]
    [[p20.transfer(5, pcr_dilution[num], col[num], new_tip='always') for col in ctrl_col] for num in range(0, 6)]
    [[p20.transfer(5, water, col[num], new_tip='always') for col in ctrl_col] for num in range(6, 8)]
