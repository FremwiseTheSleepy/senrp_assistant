from random import randint
from Configurations.OneRing.Confinguration.OneRing import GANDALF_FEAT_DIE_VALUE, SAURON_FEAT_DIE_VALUE, \
    DEFAULT_NUM_FEAT_ROLLS, StanceTN, roll_success_dice
from Configurations.OneRing.Equipment.Weapon import WeaponStructure
from Configurations.OneRing.Equipment.Weapon import Weapon
from Character.Character import Character


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

        super(Hero, self).__init__(name)
        self.name = name
        self.weapon = Weapon(weapon_name, weapon_mods)
        self.weapon_success_dice = weapon_success_dice
        self.num_feat_rolls = DEFAULT_NUM_FEAT_ROLLS + bonus_feat_rolls
        self.player_damage = player_damage
        self.edge_value = self.weapon.edge
        self.damage_value = self.weapon.damage
        self.stance = stance
        self.inventory = []

    def __str__(self):
        output_string = ""
        output_string += " Hero:\n"
        output_string += "   Name: {},   ".format(self.name)
        output_string += "   Number of success dice: {},   ".format(self.weapon_success_dice)
        output_string += "   Number of feat rolls: {}\n".format(self.num_feat_rolls)
        output_string += "{}".format(self.weapon)
        return output_string

    def get_max_health(self):
        """
        get and return the maximum value one or more health pools.
        :return:
        """
        return 0

    def add_to_inventory(self, item_to_add_to_inventory):
        """
        Add an item to the inventory
        :param item_to_add_to_inventory: item to add to inventory
        :return:
        """

        self.inventory.append(item_to_add_to_inventory)

    def get_inventory(self):
        """
        Return what the character has in their inventory
        :return:
        """
        return self.inventory

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
