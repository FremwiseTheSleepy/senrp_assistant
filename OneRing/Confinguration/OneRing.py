from collections import namedtuple
from random import randint
SAURON_FEAT_DIE_VALUE = 11
GANDALF_FEAT_DIE_VALUE = 12
DEFAULT_NUM_FEAT_ROLLS = 1

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
    return "{}: {:0.3f}".format(name, float(count) / total * 100)
