from opentrons import protocol_api, labware, instruments

# metadata
metadata = {
    'apiLevel': '2.2',
    'protocolName': 'Make Plate Aliquots',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Distribute plasmids to PCR plates for shipping.',
}


def run(protocol_context):
    # Labware Setup
    p50rack = protocol_context.load_labware('opentrons_96_filtertiprack_200ul', '11')
    rack1 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '7')
    rack2 = protocol_context.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", '10')
    plate1 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '1')
    plate2 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '2')
    plate3 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '3')
    plate4 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '4')
    plate5 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '5')
    plate6 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '6')
    plate7 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '8')
    plate8 = protocol_context.load_labware("biorad_96_wellplate_200ul_pcr", '9')

    plates = [plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8]

    # Tubes should be pulled and also inserted into tuberack left to right, top to bottom, to correspond to this code.
    # (E.g., A1, A2... B1, B2...)
    # Key = destination well in PCR plate, Value = source tube in tube rack. E.g., rack1[A1] has the plasmid aliquot
    # for the A1 wells in all the PCR plates.
    # A3, A4, B6, and H3 do not have content. TUBES A8, B8, C6, E5, & E11 WERE MANUALLY ALIQUOTTED due to low source
    # volume and lack of space on the OT2.
    tube_to_well_map = {'A1': rack1['A1'],
                        'A2': rack1['A2'],

                        'A5': rack1['A3'],
                        'A6': rack1['A4'],
                        'A7': rack1['A5'],

                        'A9': rack1['A6'],
                        'A10': rack1['B1'],
                        'A11': rack1['B2'],
                        'A12': rack1['B3'],
                        'B1': rack1['B4'],
                        'B2': rack1['B5'],
                        'B3': rack1['B6'],
                        'B4': rack1['C1'],
                        'B5': rack1['C2'],

                        'B7': rack1['C3'],

                        'B9': rack1['C4'],
                        'B10': rack1['C5'],
                        'B11': rack1['C6'],
                        'B12': rack1['D1'],
                        'C1': rack1['D2'],
                        'C2': rack1['D3'],
                        'C3': rack1['D4'],
                        'C4': rack1['D5'],
                        'C5': rack1['D6'],

                        'C7': rack2['A1'],
                        'C8': rack2['A2'],

                        'E1': rack2['A3'],
                        'E2': rack2['A4'],
                        'E3': rack2['A5'],
                        'E4': rack2['A6'],

                        'E6': rack2['B1'],
                        'E7': rack2['B2'],
                        'E8': rack2['B3'],
                        'E9': rack2['B4'],
                        'E10': rack2['B5'],

                        'E12': rack2['B6'],
                        'F1': rack2['C1'],
                        'F2': rack2['C2'],
                        'F3': rack2['C3'],
                        'F4': rack2['C4'],
                        'F5': rack2['C5'],
                        'F6': rack2['C6'],
                        'H1': rack2['D1'],
                        'H2': rack2['D2'],

                        'H4': rack2['D3'],
                        'H5': rack2['D4'],
                        'H6': rack2['D5'],
                        'H7': rack2['D6'],
                        }

    # Pipette Setup
    p50 = protocol_context.load_instrument('p10_single', 'right', tip_racks=[p50rack])

    # Blow out liquid at 100,000 uL/s. Ideally, speed increased from default to prevent drips/
    # trapping extra volume in pipette. Actually has no effect on water, but I leave it here to show I tried.
    p50.flow_rate.blow_out = 100000

    # Instructions
    for source in tube_to_well_map:
        dest_well = tube_to_well_map[source]
        destinations = [p[dest_well] for p in plates]
        p50.distribute(5, source, destinations, touch_tip=True, disposal_volume=5)
