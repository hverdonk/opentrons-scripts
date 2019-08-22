from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'Criss-Cross Innoculation',
    'author': 'Hannah Verdonk <hverdonk@stanford.edu>',
    'description': 'Simple protocol to get started using OT2',
}

# labware
tiprack = labware.load('opentrons-tiprack-300ul', '1')  # check tip volume for this one later
lb_broth = labware.load("TROUGH_NAME", '2')  # figure out what the name of a trough is
wolbachia = labware.load("TROUGH_NAME", '3')  # figure out what the name of a trough is
plate = labware.load("usascientific_96_wellplate_2.4ml_deep", '4')
trash = labware.load('trash-box', 'TRASH')  # 'trash-box' name no longer supported

# pipettes
pipette = instruments.P300_Multi(mount='right', tip_racks=[tiprack])
# add trash?

# commands
pipette.distribute(
    1200,
    lb_broth,
    plate,
    mix_before=(3, 1500),
    disposal_vol=10
)   # include extra liquid "disposal_vol" to make dispenses more accurate


CULTURE_VOL = 300
INNOCULATIONS = [
  CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0,
  0,  CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL,
  CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0,
  0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL,
  CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0,
  0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL,
  CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0,
  0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL,
  CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0,
  0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL,
  CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0,
  0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL, 0, CULTURE_VOL
]


pipette.distribute(
    INNOCULATIONS,
    wolbachia,
    plate,
    mix_before=(3, 500)
)
# mix 3 times with 500uL before aspirating into each well
