class NPClass:
    def __init__(self, name, nclass, level, alignment, race, size, strength,
                 constitution, dexterity, intelligence, wisdom, charisma,
                 wounds, vitality, fortitude, reflex, will, dr, speed, senses,
                 languages, initiative):
        self.name = name
        self.nclass = nclass
        self.level = level
        self.alignment = alignment
        self.race = race
        self.size = size
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.wounds = wounds
        self.vitality = vitality
        self.fortitude = fortitude
        self.reflex = reflex
        self.will = will
        self.dr = dr
        self.speed = speed
        self.senses = senses
        self.languages = languages
        self.initiative = initiative

# Stores the NPC class used in other modules


if __name__ == '__main__':
    print("NPC.py")
