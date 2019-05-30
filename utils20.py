import collections
import math

# list of field IDs
listIDs = dict(
    Alignment="-L_dU6cPcS3iiImpDZrT",
    Charisma="-L_dUDDtm6sdJ1JuPaaB",
    Constitution="-L_dUCYZPRuvrztj6sdG",
    DRArmour="-L_dUGnoVaWOa1e2B01_",
    Dexterity="-L_dUChvlJmfmFogiIB7",
    Fortitude="-L_dUFYbK-4UyZ9J8qLm",
    Intelligence="-L_dUCqiOizHGN1cdHs1",
    Languages="-L_dWUY4zRUKKMO80JlX",
    Level="-L_dU6E8xVHUA5MhmTv5",
    Notes="-L_dWXvrtvR9WhCBX9YT",
    Reflex="-L_dUFhbl5JCpu3JEdz6",
    Speed="-L_dWRtftkSBefqkiLkn",  # max
    Strength="-L_dUBVyWQQxJ8rU6ITn",
    VisionSenses="-L_dWTls8s8AuJG8vHEw",
    Vitality="-L_dUEnM4qam4HRQ5342",  # max
    Will="-L_dUFqEWMmLAqh0lo40",
    Wisdom="-L_dUCz4_tkKepldqgMl",
    Wounds="-L_dUEKSkyudwTfRIHV6",  # max
    FaithsheetPoints="-Lg3BaDehLQ9_Zk_koyK",
    AcrobaticsModifier="-Lg89G4RN_LXtk2MgAIP",
    ArcanaModifier="-Lg89HFDAWb8bZL_9mdH",
    AthleticsModifier="-Lg89HnRely697crJUqy",
    BluffModifier="-Lg89JOuaCgnbicwWA72",
    DiplomacyModifier="-Lg89Jg0If05HyxpNWkq",
    DungeoneeringModifier="-Lg89Joxm3kvKmTlBp0h",
    EnduranceModifier="-Lg89LtVL3PbRhjrL61b",
    HealModifier="-Lg89M4GVQpQy3OPET9h",
    HistoryModifier="-Lg89MA5NhzeQtjeVN92",
    InsightModifier="-Lg89NmZsEMb_4ae3ewA",
    IntimidateModifier="-Lg89OPB8C3FZ7smw0im",
    NatureModifier="-Lg89OUdvnftMjtkDG1x",
    PerceptionModifier="-Lg89QQZjIDdT1XCMyD5",
    ReligionModifier="-Lg89QqkWIfgZRNnT4eH",
    StealthModifier="-Lg89QvVGwWdyz5W6QkR",
    StreetwiseModifier="-Lg89TJzHfTRi1xzXUIF",
    TrickModifier="-Lg89UacRlsNtMZp_nNy"
)

# list of fields with max
maxCases = ("Speed", "Vitality", "Wounds")

# level conversion dict
levels = {
    '1': 1,
    '2': 2,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 6,
    '10': 7,
    '11': 8,
    '12': 8,
    '13': 9,
    '14': 10,
    '15': 10,
    '16': 11,
    '17': 12,
    '18': 12,
    '19': 13,
    '20': 14,
    '21': 14,
    '22': 15,
    '23': 16,
    '24': 16,
    '25': 17,
    '26': 18,
    '27': 18,
    '28': 19,
    '29': 20,
    '30': 20
}

# wounds conversion dict
wounds = dict(
    Tiny=2,
    Small=5,
    Medium=10,
    Large=15,
    Huge=20
)


# create attributes, based on name and value
def cr_attr(aname, avalue):
    if aname == "Vision/Senses":  # check if name has slash, else normal
        ianame = "VisionSenses"
    elif aname == "Faith sheet-Points":  # cover special case for FPs
        ianame = "FaithsheetPoints"
    else:
        ianame = aname
    return collections.OrderedDict(
        name=aname,
        current=str(avalue),
        max=str(avalue) if aname in maxCases else "",
        id=listIDs[ianame]
    )


# function to calc attrib mods
def att_mod(att):
    att = float(att)
    return math.ceil((att-10)/2) if att < 10 else math.floor((att-10)/2)


if __name__ == '__main__':
    print("ok")
