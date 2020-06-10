from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.3',
    'protocolName': 'Make Plate Aliquots',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute plasmid DNA aliquots to a PCR plate for shipping.',
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
    p10rack = protocol.load_labware('geb_96_tiprack_10ul', '11')
    destination = protocol.load_labware("biorad_96_wellplate_200ul_pcr", '10')

    # Source Twist plates
    plate1 = protocol.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate2 = protocol.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate3 = protocol.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate4 = protocol.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate5 = protocol.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate6 = protocol.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate7 = protocol.load_labware("corning_96_wellplate_360ul_flat", '7')
    plate8 = protocol.load_labware("corning_96_wellplate_360ul_flat", '8')

    p10 = protocol.load_instrument('p10_single', 'right', tip_racks=[p10rack])

    # BEGIN PROTOCOL
    # plate1 transfers
    p10.transfer(5, plate1.wells_by_name()['F10'], destination.wells_by_name()['A1'])
    p10.transfer(5, plate1.wells_by_name()['F11'], destination.wells_by_name()['B1'])
    p10.transfer(5, plate1.wells_by_name()['E7'], destination.wells_by_name()['C1'])
    p10.transfer(5, plate1.wells_by_name()['F2'], destination.wells_by_name()['D1'])
    p10.transfer(5, plate1.wells_by_name()['F9'], destination.wells_by_name()['E1'])

    # plate2 transfers
    p10.transfer(5, plate2.wells_by_name()['A9'], destination.wells_by_name()['F1'])
    p10.transfer(5, plate2.wells_by_name()['G8'], destination.wells_by_name()['G1'])
    p10.transfer(5, plate2.wells_by_name()['H8'], destination.wells_by_name()['H1'])
    p10.transfer(5, plate2.wells_by_name()['H3'], destination.wells_by_name()['A2'])
    p10.transfer(5, plate2.wells_by_name()['B2'], destination.wells_by_name()['B2'])

    # plate3 transfers
    p10.transfer(5, plate3.wells_by_name()['D5'], destination.wells_by_name()['C2'])
    p10.transfer(5, plate3.wells_by_name()['C2'], destination.wells_by_name()['D2'])
    p10.transfer(5, plate3.wells_by_name()['B3'], destination.wells_by_name()['E2'])
    p10.transfer(5, plate3.wells_by_name()['H3'], destination.wells_by_name()['F2'])
    p10.transfer(5, plate3.wells_by_name()['F3'], destination.wells_by_name()['G2'])

    # plate4 transfers
    p10.transfer(5, plate4.wells_by_name()['H3'], destination.wells_by_name()['H2'])
    p10.transfer(5, plate4.wells_by_name()['H7'], destination.wells_by_name()['A3'])
    p10.transfer(5, plate4.wells_by_name()['F12'], destination.wells_by_name()['B3'])
    p10.transfer(5, plate4.wells_by_name()['C9'], destination.wells_by_name()['C3'])

    # plate5 transfers
    p10.transfer(5, plate5.wells_by_name()['H6'], destination.wells_by_name()['D3'])
    p10.transfer(5, plate5.wells_by_name()['D5'], destination.wells_by_name()['E3'])
    p10.transfer(5, plate5.wells_by_name()['D9'], destination.wells_by_name()['F3'])

    # plate6 transfers
    p10.transfer(5, plate6.wells_by_name()['B2'], destination.wells_by_name()['G3'])
    p10.transfer(5, plate6.wells_by_name()['F8'], destination.wells_by_name()['H3'])
    p10.transfer(5, plate6.wells_by_name()['B3'], destination.wells_by_name()['A4'])

    # plate7 transfers
    p10.transfer(5, plate7.wells_by_name()['H6'], destination.wells_by_name()['B4'])
    p10.transfer(5, plate7.wells_by_name()['D12'], destination.wells_by_name()['C4'])

    # plate8 transfers
    p10.transfer(5, plate8.wells_by_name()['G6'], destination.wells_by_name()['D4'])
    p10.transfer(5, plate8.wells_by_name()['E5'], destination.wells_by_name()['E4'])
    p10.transfer(5, plate8.wells_by_name()['E3'], destination.wells_by_name()['F4'])
