from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.3',
    'protocolName': 'Miniprep Plate Part 1',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Automates the Zymo kit "Zyppy-96 Plasmid MagBead Miniprep".',
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware Setup
    tips1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7')
    tips2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '8')
    tips3 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '9')
    tips4 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '10')
    tips5 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11')

    lysis_buffer = protocol.load_labware("agilent_1_reservoir_290ml", '2')
    neutralization_buffer = protocol.load_labware("agilent_1_reservoir_290ml", '4')
    clearing_beads = protocol.load_labware("agilent_1_reservoir_290ml", '5')
    magbeads = protocol.load_labware("agilent_1_reservoir_290ml", '6')

    magdeck = protocol.load_module('Magnetic Module', '1')
    block = magdeck.load_labware("usascientific_96_wellplate_2.4ml_deep", label='culture plate')
    collection_plate = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", '3')

    # Pipette Setup
    p300 = protocol.load_instrument('p300_multi', 'left', tip_racks=[tips1, tips2, tips3, tips4, tips5])

    # BEGIN PROTOCOL
    # set pipette flow rates to 1/2 their normal speed in uL/s, for bubbly lysis buffer
    p300.flow_rate.aspirate = 75
    p300.flow_rate.dispense = 150

    # Add lysis buffer to deepwell block.
    for col in block.columns_by_name():
        p300.transfer(100,
                      lysis_buffer.wells_by_name()['A1'],
                      block.columns_by_name()[col][0],
                      mix_after=(3, 200),
                      new_tip='always')

    # set pipette flow rates back to their default speeds
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 300

    # Pause 5 min for lysis rxn to proceed
    protocol.delay(minutes=5)

    # Add neutralization buffer to deepwell block
    for col in block.columns_by_name():
        p300.pick_up_tip()
        i = 2
        while i > 0:
            p300.move_to(neutralization_buffer.wells_by_name()['A1'])
            p300.aspirate(200)
            p300.move_to(block.columns_by_name()[col][0])
            p300.dispense(200)
            i = i - 1
        p300.move_to(neutralization_buffer.wells_by_name()['A1'])
        p300.aspirate(50)
        p300.move_to(block.columns_by_name()[col][0])
        p300.dispense(50)
        p300.mix(3)
        p300.drop_tip()
        # This version may or may not mix after every dispense, contaminating the neutralization buffer,
        # so for now I'm not gonna risk it.
        # p300.transfer(450,
        #               neutralization_buffer.wells_by_name()['A1'],
        #               block.columns_by_name()[col][0],
        #               mix_after=(4, 200),
        #               new_tip='always')

    # Add clearing beads to deepwell block
    for col in block.columns_by_name():
        p300.transfer(50,
                      clearing_beads.wells_by_name()['A1'],
                      block.columns_by_name()[col][0],
                      mix_before=(2, 200),
                      mix_after=(3, 200),
                      new_tip='always')

    # Activate mag module, let sit for 5 mins
    magdeck.engage()
    protocol.delay(minutes=5)

    # Transfer lysate to collection plate
    for col in block.columns_by_name():
        p300.pick_up_tip()
        i = 3
        while i > 0:
            p300.move_to(block.columns_by_name()[col][0].top(-30))
            p300.aspirate(200)
            p300.move_to(collection_plate.columns_by_name()[col][0])
            p300.dispense(200)
            i = i - 1
        p300.drop_tip()

    # Disengage mag module while not in use
    magdeck.disengage()

    # Add magbeads to collection plate
    for col in block.columns_by_name():
        p300.transfer(30,
                      magbeads.wells_by_name()['A1'],
                      collection_plate.columns_by_name()[col][0],
                      mix_before=(2, 200),
                      mix_after=(3, 200),
                      new_tip='always')

    protocol.comment('Incubate the collection plate at room temperature for 10 minutes before beginning Part 2.')
