from random import randint
from collections import namedtuple

# Readme: For general usage, go to bottom of file and modify values, run via "python Combat.py"
# tested on python 3.6.1

VERSION = "0.1"

DEFAULT_NUM_FEAT_ROLLS = 1
SAURON_FEAT_DIE_VALUE = 11
GANDALF_FEAT_DIE_VALUE = 12

WeaponStructure = namedtuple('WeaponStructure', 'damage edge injury hit_bonus')
WeaponDatabase = {
    'Dagger':               WeaponStructure(damage=3, edge=GANDALF_FEAT_DIE_VALUE, injury=12, hit_bonus=0),
    'Short sword':          WeaponStructure(damage=5, edge=10, injury=14, hit_bonus=0),
    'Sword':                WeaponStructure(damage=5, edge=10, injury=16, hit_bonus=0),
    'Long sword (1h)':      WeaponStructure(damage=5, edge=10, injury=16, hit_bonus=0),
    'Long sword (2h)':      WeaponStructure(damage=7, edge=10, injury=18, hit_bonus=0),
    'Spear':                WeaponStructure(damage=5, edge=9, injury=14, hit_bonus=0),
    'Great spear (2h)':     WeaponStructure(damage=9, edge=9, injury=16, hit_bonus=0),
    'Axe':                  WeaponStructure(damage=5, edge=GANDALF_FEAT_DIE_VALUE, injury=18, hit_bonus=0),
    'Great axe (2h)':       WeaponStructure(damage=9, edge=GANDALF_FEAT_DIE_VALUE, injury=20, hit_bonus=0),
    'Long-hafted axe (1h)': WeaponStructure(damage=5, edge=GANDALF_FEAT_DIE_VALUE, injury=18, hit_bonus=0),
    'Long-hafted axe (2h)': WeaponStructure(damage=7, edge=GANDALF_FEAT_DIE_VALUE, injury=20, hit_bonus=0),
    'Bow':                  WeaponStructure(damage=5, edge=10, injury=14, hit_bonus=0),
}

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


class StanceTN:
    Forward = 6
    Open = 9
    Def = 12  # Rearward = 12


# General util functions
def parse_numbers_from_string_to_list(string_to_parse):
    """
    Parse a string into a list of numbers: e.g. "This 1 string has 2 numbers." => [1,2]
    :param string_to_parse: str, input string to parse
    :return: list of ints, all numeric values found within string.
    """
    # parse string into parts, add integer value to list if determined to be integer
    return [int(string_integer) for string_integer in string_to_parse.split() if string_integer.isdigit()]


def process_percentage(name, count, total):
    """
    Returns str containing input string and the associated percentage based on count & total inputs.
    :param name: str, contains text to indicate what percent means
    :param count: numeric, numerator, i.e. number of "successes" out of all attempts
    :param total: numeric, denominator, i.e. number of "attempts"
    :return: str, text indicating what percent means followed by percent, separated by ':'
    """
    return "{}: {}".format(name, str(round(float(count) / total * 100, 3)))


def roll_success_dice(number_of_dice, is_weary=False):
    """
    Rolls a number of success dice and returns the total sum of the dice rolls. Handles weary effects if specified.
    :param number_of_dice: int, total number of success dice to roll
    :param is_weary: Boolean, true when the weary effects should affect rolls, false otherwise
    :return: int tuple, total summation of dice rolls (weary affected), number of successes (tengwar or '6' value rolls)
    """
    roll_summation = 0
    number_of_successes = 0
    for _ in range(number_of_dice):
        single_roll_value = randint(1, 6)
        if is_weary and single_roll_value <= 3:
            single_roll_value = 0
        roll_summation += single_roll_value
        if single_roll_value == 6:
            number_of_successes += 1
    return roll_summation, number_of_successes


class Character(object):
    """ Base class for all PCs or NPCs """

    def __init__(self, name, stance=StanceTN.Def):
        self.name = name
        self.stance = stance

    def get_name(self):
        return self.name


class Hero(Character):
    """ Perform tasks that hero can perform """

    def __init__(self,
                 name="",
                 weapon_name="Bow",
                 weapon_mods=WeaponStructure(0, 0, 0, 0),
                 weapon_success_dice=2,
                 bonus_feat_rolls=1,
                 player_damage=0,
                 stance=StanceTN.Def):

        super(Hero, self).__init__(name, stance=stance)
        self.weapon = Weapon(weapon_name, weapon_mods)
        self.weapon_success_dice = weapon_success_dice
        self.num_feat_rolls = DEFAULT_NUM_FEAT_ROLLS + bonus_feat_rolls
        self.player_damage = player_damage
        self.edge_value = self.weapon.edge
        self.damage_value = self.weapon.damage

    def __str__(self):
        output_string = ""
        output_string += " Hero:\n"
        output_string += "   Name: {},   ".format(self.name)
        output_string += "   Number of success dice: {},   ".format(self.weapon_success_dice)
        output_string += "   Number of feat rolls: {}\n".format(self.num_feat_rolls)
        output_string += "{}".format(self.weapon)
        return output_string

    def perform_attack_roll(self):
        """
        Performs feat and success rolls, determines if edge value was met/exceeded.
        :return: tuple of total_attack_value, number_of_successes, achieved_edge, special_feat_text
            total_attack_value, int, is the summation of all dice.
            number of successes, int, is the number of  tengwar (6) rolls on success (1d6) dice.
            achieved_edge, boolean, True when sum of rolls >= edge value (note, attack can miss, negating edge)
            special_feat_text, str, "Gandalf" or "Sauron" if feat roll(s) indicate associated value, "" otherwise.
        """
        total_attack_value, number_of_successes = roll_success_dice(self.weapon_success_dice)

        # perform feat roll(s), end result is a Sauron (failure, 0) only if all rolls are Sauron; add to success rolls
        max_feat_roll = 0
        for _ in range(self.num_feat_rolls):
            feat_roll = randint(1, 12)
            if feat_roll == SAURON_FEAT_DIE_VALUE:
                feat_roll = 0
            max_feat_roll = max(feat_roll, max_feat_roll)
        total_attack_value += max_feat_roll

        # determine whether special outcome (Gandalf/Sauron) occurred
        special_feat_text = ""
        if max_feat_roll == 0:
            special_feat_text = "Sauron"
        elif max_feat_roll == GANDALF_FEAT_DIE_VALUE:
            special_feat_text = "Gandalf"

        # check if edge was reached, this is a preliminary check
        achieved_edge = False
        if max_feat_roll >= self.edge_value:
            achieved_edge = True

        # if weapon adds hit bonus add in now.
        total_attack_value += self.weapon.hit_bonus

        return total_attack_value, number_of_successes, achieved_edge, special_feat_text


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


class Combat:
    """ Perform combat tasks and simulations """

    def __init__(self, hero, bad_guy=BadGuy("bg247b"), number_of_sims=100, print_all=False):
        self.num_of_sims = number_of_sims
        self.hero = hero
        self.bad_guy = bad_guy
        self.simulation_data = ""
        self.print_all = print_all

    def __str__(self):
        output_string = "Combat Results:\n"
        output_string += "{}".format(self.hero)
        output_string += "{}".format(self.bad_guy)
        output_string += " Number of simulations: {}\n".format(self.num_of_sims)

        output_string += self.simulation_data
        return output_string

    def run_simulation(self):
        """

        :return:
        """
        edge_count = 0
        success_count = 0   # TODO: this is overestimating since it can't know hit value
        sauron_count = 0
        gandalf_count = 0
        hit_count = 0
        damage_count = 0
        wound_count = 0
        for sim in range(self.num_of_sims):
            attack_sum, tengwar_rolls, achieved_edge, special_feat_text = self.hero.perform_attack_roll()

            # Player only calculations
            if special_feat_text == "Gandalf":
                gandalf_count += 1

            if special_feat_text == "Sauron":
                sauron_count += 1

            tracking_data = self.calculate_hero_vs_bad_guy_combat_percents(
                (attack_sum, special_feat_text, achieved_edge, tengwar_rolls),
                (hit_count, success_count, edge_count, wound_count, damage_count))
            hit_count, success_count, edge_count, wound_count, damage_count = tracking_data

            if self.print_all:
                self.simulation_data += "{}: Atk: {}, # tengwars: {}, edge?: {}, G/S?: '{}'\n".format(sim+1,
                                                                                                      attack_sum,
                                                                                                      tengwar_rolls,
                                                                                                      achieved_edge,
                                                                                                      special_feat_text)

        damage_percent = process_percentage("Damage per attack", damage_count, self.num_of_sims * 100)
        hit_percent_data = process_percentage("Hit % against {}".format(self.bad_guy.name), hit_count, self.num_of_sims)
        wound_percent = process_percentage("Wound %", wound_count, self.num_of_sims)
        edge_percent = process_percentage("Edge %", edge_count, self.num_of_sims)
        success_avg = process_percentage("Success avg", success_count, self.num_of_sims * 100)
        gandalf_percent = process_percentage("Gandalf %", gandalf_count, self.num_of_sims)
        sauron_percent = process_percentage("Sauron %", sauron_count, self.num_of_sims)

        self.simulation_data += "   {}   {}   {}   {}   {}   {}   {}".format(damage_percent,
                                                                             hit_percent_data,
                                                                             wound_percent,
                                                                             edge_percent,
                                                                             success_avg,
                                                                             gandalf_percent,
                                                                             sauron_percent)

    def process_bad_guy_hit(self, attack_inputs, tracking_data):
        """
        Perform tracking updates after successful hit on bad guy
        :param attack_inputs: bool and int iterator, did the attack reach the weapon's edge, number of tengwar, 6, rolls
        :param tracking_data: iterator, hit, success, edge, wound, damage counts, these are all input/output in function
        :return: iterator, hit, success, edge, wound, damage counts; calculated values against bad guy
        """
        achieved_edge, number_of_successes = attack_inputs
        hit_count, success_count, edge_count, wound_count, damage_count = tracking_data
        # handle detected hit
        hit_count += 1

        # update tracking for hit and damage, calculate it temporarily to perform endurance clamping
        temp_damage = self.hero.weapon.damage

        # update damage based on number of successes
        success_count += number_of_successes
        if success_count == 1:
            temp_damage += self.hero.player_damage
        elif success_count >= 2:
            temp_damage += self.hero.player_damage * 2

        if achieved_edge:
            # roll indicates edge achieved, determine if wound occurred
            edge_count += 1
            armor = self.bad_guy.calculate_armor()
            if self.hero.weapon.injury >= armor:
                wound_count += 1
                # TODO: This is artificially high (assumes player always attacks fresh bad guy,
                # need battle sim to calculate remaining endurance
                temp_damage = self.bad_guy.endurance

        # clamp total damage to bad guy's endurance (levels out wounding damage per turn value)
        if temp_damage > self.bad_guy.endurance:
            temp_damage = self.bad_guy.endurance
        # update damage tracking value
        damage_count += temp_damage

        return hit_count, success_count, edge_count, wound_count, damage_count

    def calculate_hero_vs_bad_guy_combat_percents(self, attack_inputs, tracking_data):
        """
        
        :param attack_inputs: 
        :param tracking_data:
        :return: 
        """
        # unpack input data
        total_attack_value, special_feat_text, is_edge, tengwar_rolls = attack_inputs
        hits, successes, edges, wounds, damage = tracking_data

        # check for hit, either gandalf or attack is greater than defender's TN + parry
        if total_attack_value >= self.bad_guy.calculate_defense(self.hero.stance) or special_feat_text == "Gandalf":
            # handle detected hit
            hits, successes, edges, wounds, damage = self.process_bad_guy_hit((is_edge, tengwar_rolls), tracking_data)
        
        # pack up output data
        tracking_data = hits, successes, edges, wounds, damage
        return tracking_data


class Weapon(object):
    """ Weapon initialization and upgrade handling """
    def __init__(self, name, weapon_mods=WeaponStructure(damage=0, edge=0, injury=0, hit_bonus=0)):

        self.name = name
        base_weapon_attributes = WeaponDatabase.get(self.name)

        if base_weapon_attributes:
            self.base_damage, self.base_edge, self.base_injury, self.hit_bonus = base_weapon_attributes
        else:
            print("Selected weapon of name: {}, not yet supported!".format(self.name))
            self.base_damage = 0
            self.base_edge = 0
            self.base_injury = 0
            self.hit_bonus = 0

        self.damage = self.base_damage + weapon_mods.damage
        self.injury = self.base_injury + weapon_mods.injury
        # Edge is subtractive and has a gap between Gandalf and Sauron; handle both +1 and -1 as subtracting 1.
        if self.base_edge == 12 and weapon_mods.edge >= 1:
            weapon_mods.edge = abs(weapon_mods.edge) + 1
        self.edge = self.base_edge - abs(weapon_mods.edge)
        self.hit_bonus += weapon_mods.hit_bonus

    def __str__(self):
        out_text = "   Weapon:\n"
        out_text += "     Name: {},   ".format(self.name)
        out_text += "Damage: {} ({} + {}),   ".format(self.damage, self.base_damage, (self.damage - self.base_damage))
        out_text += "Injury: {} ({} + {}),   ".format(self.injury, self.base_injury, (self.injury - self.base_injury))
        # Edge is subtractive and has a gap between Gandalf and Sauron; output rationale for extra subtraction
        if self.base_edge == GANDALF_FEAT_DIE_VALUE and self.edge != self.base_edge:
            out_text += "Edge: {} (12 - {} - 1*  (*11 not used))   ".format(self.edge, (self.base_edge-self.edge-1))
        else:
            out_text += "Edge: {} ({} - {})   ".format(self.edge, self.base_edge, (self.base_edge - self.edge))
        out_text += "Hit Bonus: {}   ".format(self.hit_bonus)
        out_text += "\n"
        return out_text


if __name__ == "__main__":
    # TODO: make a (better) command line interface
    # edit here for now
    weapon_type = "Bow"         # Select text from WeaponDatabase
    bad_guy_name = "bg245b"     # select from BadGuyDatabase
    damage_mod = 0              # e.g. Grievous = 2 (reward, pg 116, e-book)
    edge_mod = 0                # e.g. Keen = 1 (reward)
    injury_mod = 0              # e.g. Fell = 2 (reward)
    hit_mod = 0                 # e.g. Bow of the North Downs (bow), 3 (more if valor higher)
    player_basic_body = 3       # adds bonus damage for great/extraordinary successes
    num_success_dice = 2        # skill / success dice of the weapon
    extra_feat_rolls = 0        # e.g. fair shot = 1 (virtue)
    pc_stance = StanceTN.Def    # stance player character is in, affects hit rate (if rearward, use "def")

    combat = Combat(number_of_sims=100000,
                    hero=Hero("Ikari Shinji",
                              weapon_type,
                              weapon_success_dice=num_success_dice,
                              bonus_feat_rolls=extra_feat_rolls,
                              weapon_mods=WeaponStructure(damage=damage_mod,
                                                          edge=edge_mod,
                                                          injury=injury_mod,
                                                          hit_bonus=hit_mod),
                              player_damage=player_basic_body,
                              stance=pc_stance),
                    bad_guy=BadGuy(bad_guy_name),
                    print_all=False,
                    )
    combat.run_simulation()
    print("Version: combat sim: {}".format(VERSION))
    print(combat)

