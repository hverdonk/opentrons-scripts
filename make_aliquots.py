from opentrons import protocol_api,labware, instruments

# metadata
metadata = {
    'apiLevel': '2.2',
    'protocolName': 'Make Aliquots',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute expression plasmids to small tubes for shipping.',
}


def run(protocol_context):
    # Labware Setup
    p10rack = protocol_context.load_labware('geb_96_tiprack_10ul', '11')
    tuberack1 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '1')
    tuberack2 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '2')
    tuberack3 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '3')
    tuberack4 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '4')
    tuberack5 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '5')
    tuberack6 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '6')
    tuberack7 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '7')
    tuberack8 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '8')
    tuberack9 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '9')
    tuberack10 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '10')

    source = tuberack10.wells_by_name()['A1']
    destinations = tuberack1.wells() + tuberack2.wells() + tuberack3.wells() + tuberack4.wells() + tuberack5.wells() +\
        tuberack6.wells() + tuberack7.wells() + tuberack8.wells() + tuberack9.wells() + tuberack10.wells()[1:]



    # Pipette Setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=[p10rack])

    # Instructions
    for dest_well in destinations:
        p10.transfer(5, source, dest_well)
