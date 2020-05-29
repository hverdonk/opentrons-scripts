from opentrons import protocol_api, labware, instruments

# metadata
metadata = {
    'apiLevel': '2.3',
    'protocolName': 'Miniprep Plate Part 0',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute media containing antibiotic to distribution deepwell plates.',
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware Setup
    p300rack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11')
    deepwell = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", '4')
    media = protocol.load_labware("agilent_1_reservoir_290ml", '1')

    # Pipette Setup
    p300 = protocol.load_instrument('p300_multi', 'left', tip_racks=[p300rack])

    p300.pick_up_tip()
    for col in deepwell.columns():
        p300.transfer(750, media.wells_by_name()['A1'], col[0], new_tip='never')
