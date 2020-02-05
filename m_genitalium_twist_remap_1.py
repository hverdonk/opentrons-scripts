from opentrons import protocol_api, labware, instruments
import json

metadata = {

    'protocolName': 'twist_remapping',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'apiLevel': '2.1'}

json1_file = open('data.json', 'r')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
json1_file.close()

'''
json1_data is a list of dicts. Each dict has key = old plate name, value = list of dicts 
governing moves to make.
json1_data['M.gentalium_1']

take len of this to find out how many plates to take FROM
len(json1_data['M.gentalium_1'])

8 plates used to build 'M.gentalium_0'
7 plates used to build 'M.gentalium_1'

Find plate names & the order in which they appear:
for plate in json1_data['M.gentalium_0']:
    print(plate)


Calculating # of tips used (aka number of move operations)
Find the number of dicts per old plate. Each dict is a move, and each move 
requires a new tip to avoid contamination.

moves = 0
for plate in json1_data['M.gentalium_1']:
    moves = moves + len(plate)

print("moves = {}".format(moves))

Creating plate 1 will require 21 tips - one box will suffice.
'''


def run(protocol_context):
    # labware setup
    tiprack_10ul = protocol_context.load_labware('geb_96_tiprack_10ul', '11')
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate_20w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate_24w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate_21w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate_22w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate_18w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate_19w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate_23w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '7')

    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=tiprack_10ul)

    # Extract source and destination wells from json, then do the transfer
    for plate in json1_data['M.gentalium_1']:
        p_name = "plate_" + plate
        print(p_name)
        for move in plate:
            source_well = move['from']['address']
            dest_well = move['to']['address']
            p10.transfer(5, p_name.wells_by_name()[source_well], deepwell.wells_by_name()[dest_well])
