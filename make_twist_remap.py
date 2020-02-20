import json

# change as necessary for different distros
json1_file = open('mflorum.json', 'r')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
json1_file.close()

'''
Keeping these notes for later code improvements.

json1_data is a list of dicts. Each dict has key = old plate name, value = list of dicts 
governing moves to make.
json1_data['M.genitalium_1']
'''

# Uncomment to find new plate names.
# print("New Plate Names: ")
# print(json1_data.keys())

new_plate = 'M.florum_5'

# Uncomment to find old plate names, and how many there are.
# Could theoretically exceed what can fit on the deck (max 9 plates fit in addition to tips/deepwell),
# but in practice doesn't actually happen
# Nvm, it happened
# print("Number of old plates: {}".format(len(json1_data[new_plate])))
# for plate in json1_data[new_plate]:
#     print(plate)

# Uncomment to calculate # of tips used (aka number of move operations)
# Find the number of dicts per old plate. Each dict is a move, and each move
# requires a new tip to avoid contamination.
# Keoni has provided me with data that will ALWAYS be 96 tips or fewer, since
# that's the most tips it could require to fill one plate. SO, no need to run this.

# moves = 0
# for plate in json1_data[new_plate]:
#     moves = moves + len(json1_data[new_plate][plate])
#
# print("moves = {}".format(moves))


t = open('transfers.txt','w')

# Extract source and destination wells from json, then write them to new file for transfer.
for p in json1_data[new_plate]:
    p_name = "plate_" + p
    for move in json1_data[new_plate][p]:
        source_well = move['from']['address']
        dest_well = move['to']['address']
        command = "p10.transfer(5, " \
                  + p_name \
                  + ".wells_by_name()[\"" \
                  + source_well \
                  + "\"], deepwell.wells_by_name()[\"" \
                  + dest_well \
                  + "\"])" + "\n"
        t.write(command)
t.close()
