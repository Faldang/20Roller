import collections
import json
from NPC import NPClass
from utils20 import crdict


# ID needs to be entered manually, from a JSON export
inputId = input("Paste ID:\n")

# instantiate the class that will store the converted values
tempNPC = NPClass('Stefan1', 'Teacher', 10, 'Neutral Evil', 'Natural Humanoid',
                  'Small', 15, 10, 16, 8, 14, 18, 5, 70, 14, 13, 12, 7, 6,
                  '', 'Common', 5
                  )

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
        crdict("Alignment", tempNPC.alignment),
        crdict("Charisma", tempNPC.charisma),
        collections.OrderedDict(
            name="Constitution",
            current=tempNPC.constitution,
            max="",
            id="-L_dUCYZPRuvrztj6sdG"
        ),
        collections.OrderedDict(
            name="DRArmour",
            current=tempNPC.dr,
            max="",
            id="-L_dUGnoVaWOa1e2B01_"
        ),
        collections.OrderedDict(
            name="Dexterity",
            current=tempNPC.dexterity,
            max="",
            id="-L_dUChvlJmfmFogiIB7"
        ),
        collections.OrderedDict(
            name="Fortitude",
            current=tempNPC.fortitude,
            max="",
            id="-L_dUFYbK-4UyZ9J8qLm"
        ),
        collections.OrderedDict(
            name="Intelligence",
            current=tempNPC.intelligence,
            max="",
            id="-L_dUCqiOizHGN1cdHs1"
        ),
        collections.OrderedDict(
            name="Languages",
            current=tempNPC.languages,
            max="",
            id="-L_dWUY4zRUKKMO80JlX"
        ),
        collections.OrderedDict(
            name="Level",
            current=tempNPC.level,
            max="",
            id="-L_dU6E8xVHUA5MhmTv5"
        ),
        collections.OrderedDict(
            name="Notes",
            current=tempNPC.race,
            max="",
            id="-L_dWXvrtvR9WhCBX9YT"
        ),
        collections.OrderedDict(
            name="Reflex",
            current=tempNPC.reflex,
            max="",
            id="-L_dUFhbl5JCpu3JEdz6"
        ),
        collections.OrderedDict(
            name="Speed",
            current=tempNPC.speed,
            max=tempNPC.speed,
            id="-L_dWRtftkSBefqkiLkn"
        ),
        collections.OrderedDict(
            name="Strength",
            current=tempNPC.strength,
            max="",
            id="-L_dUBVyWQQxJ8rU6ITn"
        ),
        collections.OrderedDict(
            name="Vision/Senses",
            current=tempNPC.senses,
            max="",
            id="-L_dWTls8s8AuJG8vHEw"
        ),
        collections.OrderedDict(
            name="Vitality",
            current=tempNPC.vitality,
            max=tempNPC.vitality,
            id="-L_dUEnM4qam4HRQ5342"
        ),
        collections.OrderedDict(
            name="Will",
            current=tempNPC.will,
            max="",
            id="-L_dUFqEWMmLAqh0lo40"
        ),
        collections.OrderedDict(
            name="Wisdom",
            current=tempNPC.wisdom,
            max="",
            id="-L_dUCz4_tkKepldqgMl"
        ),
        collections.OrderedDict(
            name="Wounds",
            current=tempNPC.wounds,
            max=tempNPC.wounds,
            id="-L_dUEKSkyudwTfRIHV6"
        )
    ],
    abilities=[]
    )

# write to a JSON file
with open(tempNPC.name+".json", "w") as write_file:
    json.dump(DnDict, write_file, indent=4)
