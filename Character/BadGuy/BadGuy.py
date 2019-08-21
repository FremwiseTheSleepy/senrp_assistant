from collections import namedtuple
from random import randint
from Character.Character import Character
from Configuration.OneRing import StanceTN, parse_numbers_from_string_to_list

BadGuyStructure = namedtuple('BadGuyStructure', 'attribute_level endurance hate parry armor')
BadGuyDatabase = {
    # names are taken from page numbers + general location in page top left is a, bottom right b, c, etc.
    # for parry, use string, one char by itself will assume no shield, specified '+ 0' mostly for readability
    # for armor, U means that attribute bonus is added to protection check
    'bg237a': BadGuyStructure(attribute_level=7, endurance=48, hate=8, parry="5 + 2", armor="4dU"),
    'bg238a': BadGuyStructure(attribute_level=4, endurance=18, hate=5, parry="4 + 0", armor="2d"),
    'bg238b': BadGuyStructure(attribute_level=2, endurance=8,  hate=2, parry="3 + 0", armor="2d"),
    'bg238c': BadGuyStructure(attribute_level=5, endurance=20, hate=4, parry="5 + 2", armor="2dU"),
    'bg239a': BadGuyStructure(attribute_level=5, endurance=20, hate=5, parry="4 + 3", armor="3d"),
    'bg240a': BadGuyStructure(attribute_level=3, endurance=12, hate=1, parry="3 + 1", armor="3d"),
    'bg240b': BadGuyStructure(attribute_level=2, endurance=8,  hate=1, parry="2 + 0", armor="2d"),
    'bg240c': BadGuyStructure(attribute_level=4, endurance=16, hate=3, parry="4 + 2", armor="2dU"),
    'bg242a': BadGuyStructure(attribute_level=3, endurance=12, hate=2, parry="4 + 0", armor="2d"),
    'bg242b': BadGuyStructure(attribute_level=4, endurance=36, hate=3, parry="5 + 0", armor="3d"),
    'bg244a': BadGuyStructure(attribute_level=7, endurance=76, hate=8, parry="5 + 0", armor="3dU"),
    'bg244b': BadGuyStructure(attribute_level=7, endurance=84, hate=7, parry="5 + 1", armor="3d"),
    'bg244c': BadGuyStructure(attribute_level=8, endurance=90, hate=10, parry="6 + 1", armor="4d"),
    'bg245a': BadGuyStructure(attribute_level=9, endurance=96, hate=9, parry="7 + 0", armor="4d"),
    'bg245b': BadGuyStructure(attribute_level=6, endurance=72, hate=5, parry="5 + 0", armor="3d"),
    'bg246a': BadGuyStructure(attribute_level=3, endurance=12, hate=1, parry="5 + 0", armor="2d"),
    'bg247a': BadGuyStructure(attribute_level=5, endurance=16, hate=3, parry="6 + 0", armor="3d"),
    'bg247b': BadGuyStructure(attribute_level=8, endurance=68, hate=12, parry="9 + 0", armor="4d"),
    'bg248a': BadGuyStructure(attribute_level=6, endurance=20, hate=5, parry="6 + 0", armor="3d"),
    'bg249a': BadGuyStructure(attribute_level=3, endurance=10, hate=2, parry="5 + 0", armor="2d"),
    'bg249b': BadGuyStructure(attribute_level=5, endurance=35, hate=6, parry="7 + 0", armor="3d"),
}


class BadGuy(Character):
    """ Perform tasks that bad guys can perform
    @type parry: str
    @type armor: str
    """
    def __init__(self, name):
        super(BadGuy, self).__init__(name)
        bad_guy_data = BadGuyDatabase.get(self.name)
        if bad_guy_data:
            self.attribute_level, self.endurance, self.hate, self.parry, self.armor = bad_guy_data
        else:
            self.attribute_level = 0
            self.endurance = 0
            self.hate = 0
            self.parry = 0
            self.armor = 0
        self.stance = StanceTN.Def

    def __str__(self):
        out_string = " Bad Guy:\n"
        out_string += "   Name: {},  ".format(self.name)
        out_string += "Parry: {},  ".format(self.parry)
        out_string += "Armor: {},  ".format(self.armor)
        out_string += "Endurance: {},  ".format(self.endurance)
        out_string += "Stance TN: {},  ".format(self.stance)
        out_string += "Attribute level: {}\n".format(self.attribute_level)
        return out_string

    def get_parry(self, shield_present):
        parry_values = parse_numbers_from_string_to_list(self.parry)
        parry_output = parry_values[0]
        if shield_present and len(parry_values) == 2:
            parry_output += parry_values[1]
        return parry_output

    def calculate_defense(self, incoming_tn, shield_present=True):
        parry_value = incoming_tn + self.get_parry(shield_present)
        return parry_value

    def calculate_armor(self):
        armor_parse = self.armor.split('d')
        armor_dice = int(armor_parse[0])

        armor_value = 0
        for _ in range(armor_dice):
            armor_value += randint(1, 6)

        if armor_parse[-1].upper() == 'U':
            armor_value += self.attribute_level
        return armor_value
