import collections
import json
from NPC import NPClass
from utils20 import cr_attr


# ID needs to be entered manually, from a JSON export
inputId = input("Paste ID:\n")

# instantiate the class that will store the converted values
tempNPC = NPClass('Stefan2', 'Teacher', 10, 'Neutral Evil', 'Natural Humanoid',
                  'Small', 15, 10, 16, 8, 14, 18, 5, 70, 14, 13, 12, 7, 6,
                  '', 'Common', 5
                  )
notesIter = (tempNPC.name, tempNPC.size, tempNPC.race, tempNPC.nclass)
tempNPCNotes = "; ".join(notesIter)

# create dictionary
DnDict = collections.OrderedDict(
    schema_version=2,
    oldId=inputId,
    name=tempNPC.name,
    avatar="",
    bio="",
    gmnotes="",
    defaulttoken="",
    tags="[]",
    controlledby="-K14mRt7x_ftUXd4NyLH",
    inplayerjournals="-K14mRt7x_ftUXd4NyLH",
    attribs=[
        cr_attr("Alignment", tempNPC.alignment),
        cr_attr("Charisma", tempNPC.charisma),
        cr_attr("Constitution", tempNPC.constitution),
        cr_attr("DRArmour", tempNPC.dr),
        cr_attr("Dexterity", tempNPC.dexterity),
        cr_attr("Fortitude", tempNPC.fortitude),
        cr_attr("Intelligence", tempNPC.intelligence),
        cr_attr("Languages", tempNPC.languages),
        cr_attr("Level", tempNPC.level),
        cr_attr("Notes", tempNPCNotes),
        cr_attr("Reflex", tempNPC.reflex),
        cr_attr("Speed", tempNPC.speed),
        cr_attr("Strength", tempNPC.strength),
        cr_attr("Vision/Senses", tempNPC.senses),
        cr_attr("Vitality", tempNPC.vitality),
        cr_attr("Will", tempNPC.will),
        cr_attr("Wisdom", tempNPC.wisdom),
        cr_attr("Wounds", tempNPC.wounds)
    ],
    abilities=[]
    )

# write to a JSON file
with open(tempNPC.name+".json", "w") as write_file:
    json.dump(DnDict, write_file, indent=4)
