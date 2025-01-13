"""

"""
from Simulations.Combat import Combat


class Combat(Combat):

    def perform_attack_simulations(self, num_of_sims, character1, character2, print_all):
        """

        :param num_of_sims:
        :param character1:
        :param character2:
        :param print_all:
        :return:
        """
        edge_count = 0
        success_count = 0  # TODO: this is overestimating since it can't know hit value
        sauron_count = 0
        gandalf_count = 0
        hit_count = 0
        damage_count = 0
        wound_count = 0
        simulation_data = ""
        for sim in range(num_of_sims):
            attack_sum, tengwar_rolls, achieved_edge, special_feat_text = character1.perform_attack_roll()

            # Characters only calculations
            if special_feat_text == "Gandalf":
                gandalf_count += 1

            if special_feat_text == "Sauron":
                sauron_count += 1

            tracking_data = self.calculate_hero_vs_bad_guy_combat_percents(
                (attack_sum, special_feat_text, achieved_edge, tengwar_rolls),
                (hit_count, success_count, edge_count, wound_count, damage_count))
            hit_count, success_count, edge_count, wound_count, damage_count = tracking_data

            if print_all:
                simulation_data += "{}: Atk: {}, # tengwars: {}, edge?: {}, G/S?: '{}'\n".format(sim + 1,
                                                                                                      attack_sum,
                                                                                                      tengwar_rolls,
                                                                                                      achieved_edge,
                                                                                                      special_feat_text)
        damage_percent = self.process_percentage("Damage per attack", damage_count, num_of_sims * 100)
        hit_percent_data = self.process_percentage("Hit % against {}".format(character2.name), hit_count,
                                                   num_of_sims)
        wound_percent = self.process_percentage("Wound %", wound_count, num_of_sims)
        edge_percent = self.process_percentage("Edge %", edge_count, num_of_sims)
        success_avg = self.process_percentage("Success avg", success_count, num_of_sims * 100)
        gandalf_percent = self.process_percentage("Gandalf %", gandalf_count, num_of_sims)
        sauron_percent = self.process_percentage("Sauron %", sauron_count, num_of_sims)
        simulation_data += "   {}   {}   {}   {}   {}   {}   {}".format(damage_percent,
                                                                         hit_percent_data,
                                                                         wound_percent,
                                                                         edge_percent,
                                                                         success_avg,
                                                                         gandalf_percent,
                                                                         sauron_percent)
        return simulation_data

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
        temp_damage = self.character1.weapon.damage

        # update damage based on number of successes
        success_count += number_of_successes
        if success_count == 1:
            temp_damage += self.character1.player_damage
        elif success_count >= 2:
            temp_damage += self.character1.player_damage * 2

        if achieved_edge:
            # roll indicates edge achieved, determine if wound occurred
            edge_count += 1
            armor = self.character2.calculate_armor()
            if self.character1.weapon.injury >= armor:
                wound_count += 1
                # TODO: This is artificially high (assumes player always attacks fresh bad guy,
                # need battle sim to calculate remaining endurance
                temp_damage = self.character2.endurance

        # clamp total damage to bad guy's endurance (levels out wounding damage per turn value)
        if temp_damage > self.character2.endurance:
            temp_damage = self.character2.endurance
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
        if total_attack_value >= self.character2.calculate_defense(
                self.character1.stance) or special_feat_text == "Gandalf":
            # handle detected hit
            hits, successes, edges, wounds, damage = self.process_bad_guy_hit((is_edge, tengwar_rolls),
                                                                              tracking_data)

        # pack up output data
        tracking_data = hits, successes, edges, wounds, damage
        return tracking_data

    def process_percentage(self, name, count, total):
        """
        Returns str containing input string and the associated percentage based on count & total inputs.
        :param name: str, contains text to indicate what percent means
        :param count: numeric, numerator, i.e. number of "successes" out of all attempts
        :param total: numeric, denominator, i.e. number of "attempts"
        :return: str, text indicating what percent means followed by percent, separated by ':'
        """
        return "{}: {:0.3f}".format(name, float(count) / total * 100)
