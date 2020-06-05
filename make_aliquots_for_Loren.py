from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.3',
    'protocolName': 'Make Plate Aliquots',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute plasmids to PCR plates for shipping.',
}


def run(protocol: protocol_api.ProtocolContext):
    """
    plate1 = pSHPs0414B582235TN
    plate2 = pSHPs0414B582238TN
    plate3 = pSHPs0423B636483SH
    plate4 = pSHPs0826B521701SH
    plate5 = pSHPs0826B521704SH
    plate6 = pSHPs0828B645135SH
    plate7 = pSHPs0828B645138SH
    plate8 = pSHPs0828B645144SH
    """

    # Labware Setup
    p50rack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11')
    destination = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '10')

    # Source Twist plates #TODO: change labware definition to reflect actual Twist DNA plate type
    plate1 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '1')
    plate2 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '2')
    plate3 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '3')
    plate4 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '4')
    plate5 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '5')
    plate6 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '6')
    plate7 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '7')
    plate8 = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '8')

    p50 = protocol.load_instrument('p50_single', 'right', tip_racks=[p50rack])

    # BEGIN PROTOCOL
    # plate1 transfers
    p50.transfer(vol, plate1.wells_by_name()['F10'], destination.wells_by_name()['A1'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['F11'], destination.wells_by_name()['B1'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['E7'], destination.wells_by_name()['C1'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['F2'], destination.wells_by_name()['D1'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['F9'], destination.wells_by_name()['E1'], mix_after=True)

    # plate2 transfers
    p50.transfer(vol, plate1.wells_by_name()['A9'], destination.wells_by_name()['F1'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['G8'], destination.wells_by_name()['G1'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['H8'], destination.wells_by_name()['H1'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['H3'], destination.wells_by_name()['A2'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['B2'], destination.wells_by_name()['B2'], mix_after=True)

    # plate3 transfers
    p50.transfer(vol, plate1.wells_by_name()['D5'], destination.wells_by_name()['C2'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['C2'], destination.wells_by_name()['D2'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['B3'], destination.wells_by_name()['E2'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['H3'], destination.wells_by_name()['F2'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['F3'], destination.wells_by_name()['G2'], mix_after=True)

    # plate4 transfers
    p50.transfer(vol, plate1.wells_by_name()['H3'], destination.wells_by_name()['H2'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['H7'], destination.wells_by_name()['A3'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['F12'], destination.wells_by_name()['B3'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['C9'], destination.wells_by_name()['C3'], mix_after=True)

    # plate5 transfers
    p50.transfer(vol, plate1.wells_by_name()['H6'], destination.wells_by_name()['D3'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['D5'], destination.wells_by_name()['E3'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['D9'], destination.wells_by_name()['F3'], mix_after=True)

    # plate6 transfers
    p50.transfer(vol, plate1.wells_by_name()['B2'], destination.wells_by_name()['G3'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['F8'], destination.wells_by_name()['H3'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['B3'], destination.wells_by_name()['A4'], mix_after=True)

    # plate7 transfers
    p50.transfer(vol, plate1.wells_by_name()['H6'], destination.wells_by_name()['B4'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['D12'], destination.wells_by_name()['C4'], mix_after=True)

    # plate8 transfers
    p50.transfer(vol, plate1.wells_by_name()['G6'], destination.wells_by_name()['D4'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['E5'], destination.wells_by_name()['E4'], mix_after=True)
    p50.transfer(vol, plate1.wells_by_name()['E3'], destination.wells_by_name()['F4'], mix_after=True)
