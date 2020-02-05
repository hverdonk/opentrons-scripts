import json

json1_file = open('data.json', 'r')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
json1_file.close()


'''
Keeping these notes for later code improvements.

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

t = open('transfers.txt','w')

# Extract source and destination wells from json, then write them to new file for transfer.

for plate in json1_data['M.gentalium_1']:
    p_name = "plate_" + plate
    for move in json1_data['M.gentalium_1'][plate]:
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

