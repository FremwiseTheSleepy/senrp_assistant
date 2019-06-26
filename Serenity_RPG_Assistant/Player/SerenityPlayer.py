from Player.RPPlayer import RPPlayer
import re


def process_weapon_damage(weapon_config):
    weapon_damage_text = weapon_config.damage
    if "*" in weapon_damage_text:
        total_damage, dam_text = input("See manual for how to handle '*'. Enter total damage, damage type "
                                       "as 'S'tun, 'W'ound, or 'B'asic (or both)")

    else:
        dam_text = weapon_damage_text
        numeric_values = re.findall(r'\d+', weapon_damage_text)
        if len(numeric_values) == 1:
            num_dice = 1
            dice_value = numeric_values[0]
        elif len(numeric_values) == 2:
            num_dice = numeric_values[0]
            dice_value = numeric_values[1]
        else:
            exit_signal = False
            dice_value = 0
            num_dice = 0
            while not exit_signal:
                try:
                    num_dice = int(input("See manual for description, specify number of dice + enter"))
                    dice_value = int(input("See manual for description, specify dice values + enter"))
                    break
                finally:
                    pass

        total_damage = 0
        exit_signal = False
        while not exit_signal:
            try:
                dice_roll_text = input("Please enter results of {} d{} rolls:".format(num_dice, dice_value))
                dice_rolls = [int(dice_roll) for dice_roll in re.findall(r'\d+', dice_roll_text)]
                if len(dice_rolls) == num_dice:
                    for die in dice_rolls:
                        total_damage += die
                    exit_signal = True
            finally:
                pass

    damage_type = HealthSystem.BASIC_TYPE
    if "S" in dam_text:
        damage_type = HealthSystem.STUN_TYPE
    elif "W" in dam_text:
        damage_type = HealthSystem.WOUND_TYPE

    return total_damage, damage_type


class HealthSystem(object):
    STUN_TYPE = 0x1
    WOUND_TYPE = 0x2
    BASIC_TYPE = 0x3

    HEALTHY = 0x10      # no ailments, in good health

    # passed out, roll endurance checks to stay awake, more damage after this causes shock points.
    # Shock points take one hour for chance to go away (average endurance)
    UNCONSCIOUS = 0x20

    SERIOUSLY_WOUNDED = 0x40    # more than half damage is wounds, stats go down by 2 steps, -4d
    GETTING_WORSE = 0x80    # As you get more wounded, to
    BURNED = 0x100
    POISONED = 0x200
    DYING = 0x400
    MOSTLY_DEAD = 0x800
    ALL_DEAD = 0x1000

    ROLL_DIFFICULTY_INCREASE = 4

    def __init__(self, total_hitpoints=0, current_stun_damage=0, current_wound_damage=0):
        self.total_hitpoints = total_hitpoints
        self.current_stun_damage = current_stun_damage
        self.current_wound_damage = current_wound_damage
        self.remaining_health_points = total_hitpoints - current_stun_damage - current_wound_damage
        self.state = self.HEALTHY
        self.unconscious_roll = 7
        self.dead_roll = 3

    def __str__(self):
        print_string = "Remaining hit points: {} of {}\nStun Damage: {}\nWound Damage = {}\n".format(
            self.remaining_health_points, self.total_hitpoints, self.current_stun_damage, self.current_wound_damage)
        return print_string


class SerenityPlayer(RPPlayer):
    def __init__(self, player_name,
                 character_name=None,
                 age=0,
                 description="",
                 stats=None,
                 money=50,
                 health=HealthSystem()):
        super(SerenityPlayer, self).__init__(player_name, character_name, age, description, stats, money, health)

    def __str__(self):
        print_string = "Player Name: {}\nCharacter Name: {}\nAge: {}\nBack-story: {}\nCurrent Stats: {}".format(
            self.player_name, self.character_name, self.age, self.description, self.get_stats())
        return print_string

    def get_max_health(self):
        _, _, vitality, _, _, willpower = self.get_stats()
        return vitality + willpower

    def process_incoming_damage(self, attack, defense, weapon_config):
        """
        1) Basic damage; essentially damage simply for succeeding rolls
        Basic damage = attack - defense
        Divide between stun and wounds (favor stun on odd number)

        2) Weapon damage; only when succeeding rolls

        :param attack:
        :param defense:
        :param weapon_config:
        :return:
        """
        if defense > attack:
            # attack was unsuccessful
            return

        else:
            # attack successful, determine damage amount
            basic_damage = attack - defense

            stun_damage = int((basic_damage + 1) / 2)
            wound_damage = int(basic_damage / 2)

            damage_amount, damage_type = process_weapon_damage(weapon_config)

            if damage_type == HealthSystem.STUN_TYPE:
                stun_damage += damage_amount
            elif damage_type == HealthSystem.WOUND_TYPE:
                wound_damage += damage_amount
            elif damage_type == HealthSystem.BASIC_TYPE:
                stun_damage += int((damage_amount + 1) / 2)
                wound_damage += int(damage_amount / 2)

            self.health.current_stun_damage += stun_damage
            self.health.current_wound_damage += wound_damage

            if self.health.current_wound_damage >= self.get_max_health():
                # fall dead if wound damage >= max health
                self.health.state = self.health.MOSTLY_DEAD

                passed_endurance_roll = None
                while passed_endurance_roll is None:
                    try:
                        pass_fail = input("Enter 'P'ass or 'F'ail for ({}) difficulty (vit + will)".format(
                            self.health.unconscious_roll))
                        if 'P' in pass_fail.upper():
                            passed_endurance_roll = True
                            self.health.dead_roll += 4
                        elif 'F' in pass_fail.upper():
                            passed_endurance_roll = False
                            self.health.state = self.health.MOSTLY_DEAD
                            self.health.dead_roll = 3
                    finally:
                        pass

            elif self.health.current_stun_damage + self.health.current_wound_damage >= self.get_max_health():
                # fall unconscious if summation of stun & wound >= total health (roll to stay conscious)

                passed_endurance_roll = None
                while passed_endurance_roll is None:
                    try:
                        pass_fail = input("Enter 'P'ass or 'F'ail for ({}) difficulty (vit + will)".format(
                            self.health.unconscious_roll))
                        if 'P' in pass_fail.upper():
                            passed_endurance_roll = True
                            self.health.unconscious_roll += 4
                        elif 'F' in pass_fail.upper():
                            passed_endurance_roll = False
                            self.health.state = self.health.UNCONSCIOUS
                            self.health.unconscious_roll = 7
                    finally:
                        pass

    def heal_player(self, amount_to_heal, heal_type):
        stun_heal_amount = 0
        wound_heal_amount = 0
        if heal_type == HealthSystem.STUN_TYPE:
            stun_heal_amount = amount_to_heal
        elif heal_type == HealthSystem.WOUND_TYPE:
            wound_heal_amount = amount_to_heal
        elif heal_type == HealthSystem.BASIC_TYPE:
            # favor healing wounds first on odd "both" heal values
            wound_heal_amount = int((amount_to_heal + 1) / 2)
            stun_heal_amount = int(amount_to_heal / 2)

        self.health.current_stun_damage -= stun_heal_amount
        if self.health.current_stun_damage < 0:
            self.health.current_stun_damage = 0

        self.health.current_wound_damage -= wound_heal_amount
        if self.health.current_wound_damage < 0:
            self.health.current_wound_damage = 0


# TESTING
if __name__ == "__main__":
    from Configuration.Serenity_Config import SerenityStats

    bayek_stats = SerenityStats(strength=10, agility=6, vitality=6, alertness=8, intelligence=8, willpower=6)
    bayek_health = HealthSystem(total_hitpoints=bayek_stats.vitality+bayek_stats.willpower,
                                current_stun_damage=0,
                                current_wound_damage=0)
    bayek = SerenityPlayer(player_name="Andy",
                           character_name="Bayek",
                           age=28,
                           description="Protect the weak",
                           stats=bayek_stats,
                           money=750,
                           health=bayek_health)

    print("Bayek's Health = {}".format(bayek_health))
