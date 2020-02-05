import json

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
