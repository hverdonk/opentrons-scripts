from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.11',
    'protocolName': 'make_dna_distros_faster',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Create new stock for a FreeGenes distribution',
}


def run(protocol_context):
    # Labware Setup
    master_plate = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '11')
    p10rack = protocol_context.load_labware('opentrons_96_filtertiprack_20ul', '10')

    plate1 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate2 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate3 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate4 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate5 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate6 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate7 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '7')
    plate8 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '8')
    plate9 = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '9')

    # Pipette Setup
    p10 = protocol_context.load_instrument('p10_multi', 'left', tip_racks=[p10rack])
    p10.flow_rate.dispense = 25    # dispense liquid faster so no leftover dripping
    p10.well_bottom_clearance.dispense = 0     # dispense at the very bottom of the well so liquid sticks to well
    p10.flow_rate.blow_out = 400   # blow out faster to avoid droplets clinging to pipette tips

    plate_list = [plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8] #, plate9]

    # Distribute volume from source plate to v-bottom plates, column by column
    # Only officially take from well 0 in the column, because the multichannel will reach the rest anyway
    right = len(master_plate.columns()) - 1
    left = -1
    for col in range(right, left, -1):
        p10.pick_up_tip()
        if len(plate_list)%2==1:
          last_plate = len(plate_list) - 1
          for i in range(0, last_plate, 2):
            p10.aspirate(10, master_plate.columns()[col][0])
            p10.dispense(5, plate_list[i].columns()[col][0])
            p10.touch_tip(radius=0.7, v_offset=-3)
            i = i+1
            p10.dispense(5, plate_list[i].columns()[col][0])
            p10.touch_tip(radius=0.7, v_offset=-3)
          p10.aspirate(5, master_plate.columns()[col][0])
          p10.dispense(5, plate_list[last_plate].columns()[col][0])
          p10.touch_tip(radius=0.7, v_offset=-3)
        else:
          for i in range(0, len(plate_list), 2):
            p10.aspirate(10, master_plate.columns()[col][0])
            p10.dispense(5, plate_list[i].columns()[col][0])
            p10.touch_tip(radius=0.7, v_offset=-3)
            i = i+1
            p10.dispense(5, plate_list[i].columns()[col][0])
            p10.touch_tip(radius=0.7, v_offset=-3)
        p10.drop_tip()

