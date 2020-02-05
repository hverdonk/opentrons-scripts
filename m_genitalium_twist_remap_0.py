from opentrons import protocol_api,labware, instruments
import json

metadata = {

    'protocolName': 'twist_remapping',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'apiLevel':'2.1'}


json1_file = open('data.json', 'r')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
json1_file.close()

#print('keys')  # Each key is a new plate to be filled
#print(json1_data.keys())

#print("values")
#print(len(json1_data['M.gentalium_1']))


'''
a list of dicts. each dict has key = old plate name, value = list of dicts 
governing moves to make.
json1_data['M.gentalium_1']

take len of this to find out how many plates to take FROM
len(json1_data['M.gentalium_1'])

8 plates used to build 'M.gentalium_0'
7 plates used to build 'M.gentalium_1'


Calculating # of tips used (aka number of move operations)
Find the number of dicts per old plate. Each dict is a move, and each move 
requires a new tip to avoid contamination.

'''
moves = 0
plates = []
for plate in json1_data['M.gentalium_0']:
    plates.append(plate)
    moves = moves + len(plate)

print(plates)
print("moves = {}".format(moves))

'''
Creating plate 0 will require 24 tips - one box will suffice.
'''

def run(protocol_context):

    # labware setup
    tiprack_10ul = protocol_context.load_labware('geb_96_tiprack_10ul', '11')
    deepwell = protocol_context.load_labware("usascientific_96_wellplate_2.4ml_deep", '10')
    plate_16w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '1')
    plate_15w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '2')
    plate_17w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '3')
    plate_18w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '4')
    plate_14w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '5')
    plate_11w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '6')
    plate_12w = protocol_context.load_labware("corning_96_wellplate_360ul_flat", '7')





    # instrument setup
    p10 = protocol_context.load_instrument('p10_single', 'left', tip_racks=tipracks_10ul)
    p50 = protocol_context.load_instrument('p50_single', 'right', tip_racks=tiprack_300ul)