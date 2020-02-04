from opentrons import protocol_api,labware, instruments

metadata = {

    'protocolName': 'twist_remapping',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'apiLevel':'2.1'}


def run(protocol_context):

    # labware setup
    tipracks_10ul = [protocol_context.load_labware('geb_96_tiprack_10ul', slot) for slot in [1, 2, 3, 4]]
    tiprack_300ul = protocol_context.load_labware('opentrons_96_tiprack_300ul', 5)


    rt_reagents = protocol_context.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 6)


    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=tipracks_10ul)
    p50 = protocol_context.load_instrument('p50_single', 'right', tip_racks=tiprack_300ul)


    # reagent setup

    mastermix = rt_reagents.columns()[0][0]
    primer_1 = rt_reagents.columns()[1][0]
    primer_2 = rt_reagents.columns()[1][1]
    water = rt_reagents.columns()[2][0]
    dna = rt_reagents.columns()[3][0]
