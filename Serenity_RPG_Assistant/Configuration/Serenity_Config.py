from collections import namedtuple


class SerenityStats(object):
    def __init__(self, strength=4, agility=4, vitality=4, alertness=4, intelligence=4, willpower=4):
        self.strength = strength
        self.agility = agility
        self.vitality = vitality
        self.alertness = alertness
        self.intelligence = intelligence
        self.willpower = willpower

    def __str__(self):
        print_string = "Strength: {}\nAgility: {}\nVitality: {}\nAlertness: {}\nIntelligence: {}\nWillpower: {}".format(
            self.strength, self.agility, self.vitality, self.alertness, self.intelligence, self.willpower)
        return print_string


class SerenitySkills(object):
    def __init__(self,
                 animal_handling=0,
                 artistry=0,
                 athletics=0,
                 covert=0,
                 craft=0,
                 discipline=0,
                 guns=0,
                 heavy_weapons=0,
                 influence=0,
                 knowledge=0,
                 linguist_skilled=0,
                 mechanical_engineering_skilled=0,
                 medical_expertise_skilled=0,
                 melee_weapon_combat=0,
                 perception=0,
                 performance=0,
                 pilot_skilled=0,
                 planetary_vehicles=0,
                 ranged_weapons=0,
                 scientific_expertise_skilled=0,
                 survival=0,
                 technical_engineering_skilled=0,
                 unarmed_combat=0):
        self.Animal_Handling = animal_handling
        self.Artistry = artistry
        self.Athletics = athletics
        self.Covert = covert
        self.Craft = craft
        self.Discipline = discipline
        self.Guns = guns
        self.Heavy_Weapons = heavy_weapons
        self.Influence = influence
        self.Knowledge = knowledge
        self.Linguist_skilled = linguist_skilled
        self.Mechanical_Engineering_skilled = mechanical_engineering_skilled
        self.Medical_Expertise_skilled = medical_expertise_skilled
        self.Melee_Weapon_Combat = melee_weapon_combat
        self.Perception = perception
        self.Performance = performance
        self.Pilot_skilled = pilot_skilled
        self.Planetary_Vehicles = planetary_vehicles
        self.Ranged_Weapons = ranged_weapons
        self.Scientific_Expertise_skilled = scientific_expertise_skilled
        self.Survival = survival
        self.Technical_Engineering_skilled = technical_engineering_skilled
        self.Unarmed_Combat = unarmed_combat


asset_complication_config = namedtuple("name", "minor_major description numeric_effects fx_notes")

serenity_bonus_modifier = namedtuple("serenity_bonus_modifier", "stats skills")


class SerenityTraitLevel:
    Minor = 1
    Major = 2
    Both = 3


class SerenityObject(object):
    def __init__(self, name, cost, weight, availability, notes=None):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.availability = availability
        self.notes = notes


class SerenityWeapon(SerenityObject):
    def __init__(self, name,
                 damage,
                 range_increment_ft,
                 max_rof,
                 magazine_size,
                 cost,
                 weight,
                 availability,
                 notes=None):
        super(SerenityWeapon, self).__init__(name, cost, weight, availability, notes)
        self.damage = damage
        self.rang_increment_ft = range_increment_ft
        self.max_rof = max_rof
        self.magazine_size = magazine_size


class SerenityArmor(SerenityObject):
    def __init__(self,
                 name,
                 armor_rating,
                 penalty,
                 cost,
                 weight,
                 availability,
                 notes=None):
        super(SerenityArmor, self).__init__(name, cost, weight, availability, notes)
        self.armor_rating = armor_rating
        self.agi_alert_penalty = penalty


class SerenityItem(SerenityObject):
    def __init__(self, name, cost, weight, availability, notes):
        super(SerenityItem, self).__init__(name, cost, weight, availability, notes)


def process_step_bonus():
    """
    Process step bonus calculations, initial stat + step_bonus_value * 2 = final stat
    :return:
    """

    # TODO
    pass
