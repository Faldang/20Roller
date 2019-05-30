import utils20
import math


class NPClass:
    def __init__(self, name, nclass, level, alignment, race, size, strength,
                 constitution, dexterity, intelligence, wisdom, charisma,
                 wounds, fortitude, reflex, will, ac, speed, senses,
                 languages, faith, acrobatics, arcana, athletics, bluff,
                 diplomacy, dungeoneering, endurance, heal, history, insight,
                 intimidate, nature, perception, religion, stealth, streetwise,
                 trick):
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
        self.fortitude = fortitude
        self.reflex = reflex
        self.will = will
        self.dr = math.ceil(max((float(ac)-10)/2, (float(self.level)/2)+2))
        self.speed = speed
        self.senses = senses
        self.languages = languages
        self.faith = faith
        self.vitality = self.level * 7 + utils20.att_mod(self.constitution)
        self.acrobatics = int(acrobatics) - utils20.att_mod(self.dexterity)
        self.arcana = int(arcana) - utils20.att_mod(self.intelligence)
        self.athletics = int(athletics) - utils20.att_mod(self.strength)
        self.bluff = int(bluff) - utils20.att_mod(self.charisma)
        self.diplomacy = int(diplomacy) - utils20.att_mod(self.charisma)
        self.dungeoneering = int(dungeoneering)\
            - utils20.att_mod(self.intelligence)
        self.endurance = int(endurance) - utils20.att_mod(self.constitution)
        self.heal = int(heal) - utils20.att_mod(self.wisdom)
        self.history = int(history) - utils20.att_mod(self.intelligence)
        self.insight = int(insight) - utils20.att_mod(self.wisdom)
        self.intimidate = int(intimidate) - utils20.att_mod(self.strength)
        self.nature = int(nature) - utils20.att_mod(self.intelligence)
        self.perception = int(perception) - utils20.att_mod(self.wisdom)
        self.religion = int(religion) - utils20.att_mod(self.wisdom)
        self.stealth = int(stealth) - utils20.att_mod(self.dexterity)
        self.streetwise = int(streetwise) - utils20.att_mod(self.charisma)
        self.trick = int(trick) - utils20.att_mod(self.dexterity)

# Stores the NPC class used in other modules


if __name__ == '__main__':
    print("NPC.py")
