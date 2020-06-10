from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.2',
    'protocolName': 'Miniprep Plate Part 3',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Automates the Zymo kit "Zyppy-96 Plasmid MagBead Miniprep".',
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware Setup
    tips1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11')
    tips2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '10')
    tips3 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '9')

    elution_buffer = protocol.load_labware("agilent_1_reservoir_290ml", '2')
    elution_plate = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '5')

    # Part way through the protocol, the collection plate must be moved by hand from the temp deck to the mag deck.
    # The plates loaded onto both modules represent the same plate in real life.
    magdeck = protocol.load_module('Magnetic Module', '1')
    collection_plate = magdeck.load_labware("usascientific_96_wellplate_2.4ml_deep", label='same collection plate')

    tempdeck = protocol.load_module('Temperature Module', '4')
    c_plate_2 = magdeck.load_labware("usascientific_96_wellplate_2.4ml_deep", label='collection plate')

    # Pipette Setup
    p300 = protocol.load_instrument('p300_multi', 'left', tip_racks=[tips1, tips2, tips3])

    # BEGIN PROTOCOL
    # Check that collection plate is on top of tempdeck prior to start.
    protocol.pause("Is the collection plate on the temp deck?")

    # Set tempdeck to 65C
    tempdeck.set_temperature(65)

    # Add Elution Buffer & incubate on tempdeck for 5 mins
    for col in c_plate_2.columns():
        p300.transfer(40,
                      elution_buffer.wells_by_name()['A1'],
                      col[0],
                      mix_after=(3, 35),
                      new_tip='always')
    protocol.delay(minutes=5)

    # Physically move the collection plate back onto the magdeck
    protocol.pause("Move the collection plate onto the magdeck, then continue.")

    # Let magdeck work its magic for 1 min.
    magdeck.engage()
    protocol.delay(minutes=1)

    # Transfer eluted DNA to elution plate
    for col in collection_plate.columns_by_name():
        p300.pick_up_tip()
        p300.move_to(collection_plate.columns_by_name()[col][0].top(-40))
        p300.aspirate(30)
        p300.move_to(elution_plate.columns_by_name()[col][0])
        p300.dispense(30)
        p300.drop_tip()
