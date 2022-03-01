from Configurations.OneRing.Confinguration.OneRing import process_percentage
from Configurations.OneRing.Character.BadGuy.BadGuy import BadGuy

# Readme: For general usage, go to bottom of file and modify values, run via "python Combat.py"
# tested on python 3.6.1

VERSION = "0.2"


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

            # Character only calculations
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
