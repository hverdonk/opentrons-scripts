from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.2',
    'protocolName': 'Miniprep Plate Part 2',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Automates the Zymo kit "Zyppy-96 Plasmid MagBead Miniprep".',
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware Setup
    tips1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '5')
    tips2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '6')
    tips3 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7')
    tips4 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '8')
    tips5 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '9')
    tips6 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '10')
    tips7 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11')

    endo_wash = protocol.load_labware("agilent_1_reservoir_290ml", '2')
    zyppy_wash = protocol.load_labware("agilent_1_reservoir_290ml", '3')

    magdeck = protocol.load_module('Magnetic Module', '1')
    collection_plate = magdeck.load_labware("usascientific_96_wellplate_2.4ml_deep", label='collection plate')

    # Pipette Setup
    p300 = protocol.load_instrument('p300_multi', 'left', tip_racks=[tips1, tips2, tips3, tips4, tips5, tips6, tips7])

    # BEGIN PROTOCOL
    # Pause 5 min for magdeck to pellet the magbeads
    magdeck.engage()
    protocol.delay(minutes=5)

    # Aspirate and discard cleared lysates. # TODO: Double check volume math on this one.
    for col in collection_plate.columns():
        p300.pick_up_tip()
        i = 3
        while i > 0:
            p300.move_to(col[0].top(-30))
            p300.aspirate(200)
            # dispense into trash
            i -= 1
        p300.drop_tip()

    # Endo Wash
    magdeck.disengage()
    for col in collection_plate.columns():
        p300.transfer(200,
                      endo_wash.wells_by_name()['A1'],
                      col[0],
                      mix_after=(3, 200),
                      new_tip='always')
    magdeck.engage()
    protocol.delay(minutes=2)
    for col in collection_plate.columns():
        p300.pick_up_tip()
        p300.move_to(col[0].top(-30))
        p300.aspirate(200)
        # move to trash & dispense into trash
        p300.drop_tip()


    # Zyppy Wash 1 & 2
    washes_left = 2
    while washes_left > 0:
        magdeck.disengage()
        for col in collection_plate.columns():
            i = 2
            p300.pick_up_tip()
            while i > 0:
                p300.move_to(zyppy_wash.wells_by_name()['A1'])
                p300.aspirate(200)
                p300.move_to(col[0])
                p300.dispense(200)
                i -= 1
            p300.mix(2)
            p300.drop_tip()
        magdeck.engage()
        protocol.delay(minutes=2)
        for col in collection_plate.columns():
            p300.pick_up_tip()
            while i > 0:
                p300.move_to(col[0].top(-30))
                p300.aspirate(200)
                # move to trash & dispense
                i -= 1
            p300.drop_tip()
        washes_left -= 1

    protocol.comment('Let the collection plate dry at room temperature for 30 minutes before beginning Part 3.')
