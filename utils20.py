import collections


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
    Wounds="-L_dUEKSkyudwTfRIHV6"  # max
)

maxCases = ("Speed", "Vitality", "Wounds")


def cr_attr(aname, avalue):
    if aname == "Vision/Senses":  # check if name has slash, else normal
        ianame = "VisionSenses"
    else:
        ianame = aname
    return collections.OrderedDict(
        name=aname,
        current=avalue,
        max=avalue if aname in maxCases else "",
        id=listIDs[ianame]
    )


if __name__ == '__main__':
    print("ok")
    print(cr_attr("Vision/Senses", 15))
    print(cr_attr("Speed", 15))
