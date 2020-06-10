from opentrons import protocol_api

# metadata
metadata = {
    'apiLevel': '2.3',
    'protocolName': 'Resuspend Twist DNA',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Resuspend specific wells of lyophilized DNA from Twist Biosciences.',
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
    water = protocol.load_labware("agilent_1_reservoir_290ml", '10')

    # Source Twist plates
    plate1 = protocol.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate2 = protocol.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate3 = protocol.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate4 = protocol.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate5 = protocol.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate6 = protocol.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate7 = protocol.load_labware("corning_96_wellplate_360ul_flat", '7')
    plate8 = protocol.load_labware("corning_96_wellplate_360ul_flat", '8')

    p50 = protocol.load_instrument('p50_single', 'right', tip_racks=[p50rack])

    # BEGIN PROTOCOL
    # plate1 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate1.wells_by_name()['F10'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate1.wells_by_name()['F11'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate1.wells_by_name()['E7'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate1.wells_by_name()['F2'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate1.wells_by_name()['F9'], mix_after=(3, 10))

    # plate2 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate2.wells_by_name()['A9'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate2.wells_by_name()['G8'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate2.wells_by_name()['H8'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate2.wells_by_name()['H3'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate2.wells_by_name()['B2'], mix_after=(3, 10))

    # plate3 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate3.wells_by_name()['D5'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate3.wells_by_name()['C2'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate3.wells_by_name()['B3'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate3.wells_by_name()['H3'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate3.wells_by_name()['F3'], mix_after=(3, 10))

    # plate4 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate4.wells_by_name()['H3'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate4.wells_by_name()['H7'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate4.wells_by_name()['F12'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate4.wells_by_name()['C9'], mix_after=(3, 10))

    # plate5 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate5.wells_by_name()['H6'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate5.wells_by_name()['D5'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate5.wells_by_name()['D9'], mix_after=(3, 10))

    # plate6 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate6.wells_by_name()['B2'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate6.wells_by_name()['F8'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate6.wells_by_name()['B3'], mix_after=(3, 10))

    # plate7 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate7.wells_by_name()['H6'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate7.wells_by_name()['D12'], mix_after=(3, 10))

    # plate8 transfers
    p50.transfer(10, water.wells_by_name()['A1'], plate8.wells_by_name()['G6'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate8.wells_by_name()['E5'], mix_after=(3, 10))
    p50.transfer(10, water.wells_by_name()['A1'], plate8.wells_by_name()['E3'], mix_after=(3, 10))
