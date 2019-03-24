import collections
import json
from NPC import NPClass
from utils20 import cr_attr


def create_main_dict():
    # ID needs to be entered manually, from a JSON export
    # inputid = input("Paste ID:\n")
    inputid = "id"

    # instantiate the class that will store the converted values
    tempnpc = NPClass('Stefan2', 'Teacher', 10, 'Neutral Evil',
                      'Natural Humanoid', 'Small', 15, 10, 16, 8, 14, 18, 5,
                      70, 14, 13, 12, 7, 6, '', 'Common', 5
                      )
    notesiter = (tempnpc.name, tempnpc.size, tempnpc.race, tempnpc.nclass)
    tempnpcnotes = "; ".join(notesiter)

    # create dictionary
    dndict = collections.OrderedDict(
        schema_version=2,
        oldId=inputid,
        name=tempnpc.name,
        avatar="",
        bio="",
        gmnotes="",
        defaulttoken="",
        tags="[]",
        controlledby="-K14mRt7x_ftUXd4NyLH",
        inplayerjournals="-K14mRt7x_ftUXd4NyLH",
        attribs=[
            cr_attr("Alignment", tempnpc.alignment),
            cr_attr("Charisma", tempnpc.charisma),
            cr_attr("Constitution", tempnpc.constitution),
            cr_attr("DRArmour", tempnpc.dr),
            cr_attr("Dexterity", tempnpc.dexterity),
            cr_attr("Fortitude", tempnpc.fortitude),
            cr_attr("Intelligence", tempnpc.intelligence),
            cr_attr("Languages", tempnpc.languages),
            cr_attr("Level", tempnpc.level),
            cr_attr("Notes", tempnpcnotes),
            cr_attr("Reflex", tempnpc.reflex),
            cr_attr("Speed", tempnpc.speed),
            cr_attr("Strength", tempnpc.strength),
            cr_attr("Vision/Senses", tempnpc.senses),
            cr_attr("Vitality", tempnpc.vitality),
            cr_attr("Will", tempnpc.will),
            cr_attr("Wisdom", tempnpc.wisdom),
            cr_attr("Wounds", tempnpc.wounds)
        ],
        abilities=[
            # unused code for abilities due to import issues
            # collections.OrderedDict(
            #     name="Initiative",
            #     decription=" ",
            #     istokenaction=True,
            #     action="/w gm @{selected|token_name} rolls a " +
            #     "[[1d20+?{modifier|0}+"+str(tempnpc.initiative)+
            #     "&{tracker}]]" +
            #     " for initiative!",
            #     order=-1
            # )
        ]
        )
    return dndict


def json_encode():
    # write to a JSON file
    json_dict = create_main_dict()
    with open(json_dict["name"]+".json", "w") as write_file:
        json.dump(json_dict, write_file, indent=4)


if __name__ == '__main__':
    print("OK")
