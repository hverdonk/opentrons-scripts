from opentrons import protocol_api,labware, instruments

metadata = {
    'author': 'Chaz <chaz@opentrons.com',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

def run(protocol):

    ### Deck setup
    # Samples (all in column 12)
    elution_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt','9')
    
    # Reaction plate
    reaction_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt','8')
    
    # Tube rack
    temp_module = protocol.load_module('Temperature Module', '7')
    cold_reagents = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap',
                                     label='Temperature-Controlled Tubes')
    reaction_mix = cold_reagents['A1']
    endogenous_control_mix = cold_reagents['A2']
    water = cold_reagents['A3']
    pcd_dilution = [cold_reagents['B{}'.format(x)] for x in range(1,7)]
    
#    tube_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','7')
#    reaction_mix = tube_rack['A1']
#    endogenus_control_mix = tube_rack['A2']
#    water = tube_rack['A3']
#    pcd_dilution = [tube_rack['B{}'.format(x)] for x in range(1,7)]

    # Set up pipette 
    tips20 = [protocol.load_labware('opentrons_96_filtertiprack_20ul',str(x)) for x in range(11,12)]
    p20 = protocol.load_instrument('p20_single_gen2','right',tip_racks=tips20)

    tips200 = protocol.load_labware('opentrons_96_filtertiprack_200ul','10')
    p200 = protocol.load_instrument('p300_single_gen2','left',tip_racks=[tips200])
    
    ### Protocol run
    # Set up reactions
    [p200.distribute(15,reaction_mix,col,new_tip='always') for col in [reaction_plate.columns_by_name()[str(x)] for x in [1,2,3,5,6]]]

    # Set up Endogenous controls
    p200.distribute(15,endogenus_control_mix,reaction_plate.columns_by_name()['4'],new_tip='always')

    # Place samples in wells
    [p20.transfer(5,elution_plate.columns_by_name()['12'],col,new_tip='always') for col in [reaction_plate.columns_by_name()[str(x)] for x in range(1,5)]]

    # Place controls in wells
    ctrl_col = [reaction_plate.columns_by_name()[str(x)] for x in range(5,7)]
    [[p20.transfer(5,pcd_dilution[num],col[num],new_tip='always') for col in ctrl_col] for num in range(0,6)]
    [[p20.transfer(5,water,col[num],new_tip='always') for col in ctrl_col] for num in range(6,8)]
