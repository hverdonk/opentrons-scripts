from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.3',
    'protocolName': 'Make Plate Aliquots',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute plasmids to PCR plates for shipping.',
}


def run(protocol: protocol_api.ProtocolContext):
    # Labware Setup
    p50rack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '5')
    destination = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '1')
    buffer = protocol.load_labware("agilent_1_reservoir_290ml", '2')

    p50 = protocol.load_instrument('p50_single', 'right', tip_racks=[p50rack])

    # BEGIN PROTOCOL
    # Final well volume, in uL
    final_volume = 20

    # Volumes of concentrated DNA taken from the Twist plates #TODO: add list of volumes
    volumes = []

    for well in destination.well():
        if volumes:
            additive = volumes.pop()
            p50.transfer(final_volume-additive, buffer, well)
        else:
            break

