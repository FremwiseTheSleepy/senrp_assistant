try:
    import msvcrt
    from Character.Character import Character
    from Configurations.Syl.SylStats.SylStats import SylStatOverallGroup
except ModuleNotFoundError:
    import sys
    import os
    base_path_key = 'senrp_assistant'
    path = os.getcwd()
    base_path_index = path.find(base_path_key) + len(base_path_key)
    sys.path.append(path[:base_path_index])
    from Character.Character import Character
    from Configurations.Syl.SylStats.SylStats import SylStatOverallGroup


class SylCharacter(Character):
    BASE_LUCK = 10
    MAX_INVENTORY_ITEMS = 10
    STARTING_STAT_POINTS = 8  # minimum 1 for each

    def __init__(self, name,
                 description,
                 age=18,
                 internal_description="",
                 money=0,
                 stats=None,
                 health=None):
        """

        :param name:
        :param description:
        :param age:
        :param internal_description:
        :param money:
        :param stats:
        :type stats:
        :param health:
        """
        super(SylCharacter, self).__init__(name=name,
                                           age=age,
                                           description=description,
                                           internal_description=internal_description,
                                           money=money,
                                           stats=stats,
                                           health=health)
        # base class mods
        self.inventory = []
        self.base_stats_remaining = self.STARTING_STAT_POINTS
        if self.stats is None:
            self.stats = SylStatOverallGroup(1, 1, 1, 1)
        self.create_character()

    def __str__(self):
        character_string = "Name: {}\n  Stats: {}".format(self.name, self.stats)

    def get_max_health(self):
        return self.BASE_LUCK

    def add_to_inventory(self, item_to_add_to_inventory):
        if len(self.inventory) < self.MAX_INVENTORY_ITEMS:
            # only allow a certain number of items, choose which
            self.inventory.append(item_to_add_to_inventory)

    def get_inventory(self):
        return self.inventory

    def drop_item_from_inventory(self, item_to_drop_from_inventory):
        try:
            self.inventory.remove(item_to_drop_from_inventory)
        except ValueError:
            pass

    def intro_stats_menu(self):
        print("")
        print("Intellect: press 'a' to increase, 'j' to decrease")
        print("Psyche: Press 's' to increase, 'k' to decrease")
        print("Physique: Press 'd' to increase, 'l' to decrease")
        print("Motorics: Press 'f' to increase, ';' to decrease")
        print("You have {} stat points remaining".format(self.base_stats_remaining))
        print("Press 'enter' once all stats are spent to continue.")
        print("'m' brings up the menu")
        self.print_stats()

    def print_stats(self):
        self.stats.print_stat_groups()

    def define_base_stats(self):
        self.intro_stats_menu()
        char_code = None
        while char_code != 13:
            print(">", end='', flush=True)
            read_char = msvcrt.getch().decode("utf-8").lower()
            print(read_char)
            char_code = ord(read_char)


    def create_character(self):
        self.define_base_stats()



if __name__ == '__main__':

    syl_character_test = SylCharacter(name="Beaku", description="Eeku's pet bird")
