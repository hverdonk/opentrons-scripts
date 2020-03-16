"""
Required: set up the PCD dilution series before running this protocol.
Tube with highest concentration of Positive Control Template (RED) goes in B1
of the temp deck. Tube with second highest concentration goes in B2, etc.

By hand, add 5uL control RNA to H1, G4, H4, G5, and H5. Add 2.5uL control RNA 2 to H2 and H3.
"""

from opentrons import protocol_api, labware, instruments

metadata = {
    'author': 'Chaz <chaz@opentrons.com',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

def run(protocol):

    # Deck Setup #
    # Samples (all in column 12) - the extracted RNA from Station B
    elution_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '9')
    
    # Reaction plate - the plate returned by this protocol
    reaction_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '8')
    
    # Temp deck
    temp_module = protocol.load_module('Temperature Module', '7')
    temp_module.set_temperature(20)   # for testing
    # temp_module.set_temperature(4)   # for the real run

    # Cold Reagents
    cold_reagents = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap',
                                     label='Temperature-Controlled Tubes')
    reaction_mix = cold_reagents['A1']
    endogenous_control_mix = cold_reagents['A2']
    water = cold_reagents['A3']
    std_template = cold_reagents['A4']
    pcd_dilution = [cold_reagents['B{}'.format(x)] for x in range(1, 7)]

    # Set up pipette 
    tips20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 4)
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=tips20)

    # Protocol Run #
    # Set up reactions
    [p20.distribute(15, reaction_mix, col, new_tip='always')
        for col in [reaction_plate.columns_by_name()[str(x)] for x in [2, 3, 4]]]

    # Set up Endogenous controls
    p20.distribute(15, endogenous_control_mix, reaction_plate.columns_by_name()['1'], new_tip='always')

    # Place samples in wells
    sample_col = [reaction_plate.columns_by_name()[str(x)] for x in range(1, 4)]
    [p20.transfer(5, elution_plate.columns_by_name()['12'], col, new_tip='always') for col in sample_col]

    # Place controls in wells for PCD dilution curve (THIS is the standard template?)
    ctrl_col = [reaction_plate.columns_by_name()[str(x)] for x in range(4, 7)]
    [[p20.transfer(5, pcd_dilution[num], col[num], new_tip='always') for col in ctrl_col] for num in range(0, 6)]

    # put water in bottom two wells for all PCD dilution cols
    [p20.transfer(5, water, reaction_plate.columns_by_name()['6'][num], new_tip='always') for num in range(6, 8)]
