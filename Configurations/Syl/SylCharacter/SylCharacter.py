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
                 starting_level=1,
                 stats=None,
                 health=None):
        """

        :param name:
        :param description:
        :param age:
        :param internal_description:
        :param money:
        :param starting_level:
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
        self.level_points_remaining = 1
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
        print("Each stat has the range 1 - 6")
        print("You have {} stat points remaining".format(self.base_stats_remaining))
        print("Press 'enter' once all stats are spent to continue.")
        print("'m' brings up the menu")
        self.print_stats()

    def print_stats(self):
        print("{} - points left: {}".format(self.stats.get_stat_group_string(), self.base_stats_remaining))

    def base_stats_handle_user_input(self, upper_stat_limit=6):

        exit_requested = False

        while not exit_requested:
            print(">", end='', flush=True)
            read_char = msvcrt.getch().decode("utf-8").lower()
            enter_pressed = (13 == ord(read_char))
            if 'q' == read_char or (enter_pressed and self.base_stats_remaining == 0):
                if enter_pressed:
                    print("Stats confirmed.")
                break

            print(read_char)
            error_string = None
            if read_char not in ('a', 's', 'd', 'f', 'j', 'k', 'l', ';', 'm', 'q') and not enter_pressed:
                error_string = "Invalid Key entered, press 'm'/'h' for menu."

            elif enter_pressed:
                error_string = "Points still remain, consume remaining points and hit enter to confirm."

            elif self.base_stats_remaining == 0 and read_char in ('a', 's', 'd', 'f'):
                error_string = "Out of available points, press 'm' for menu"

            elif read_char == 'a':
                if self.stats.intellect < upper_stat_limit:
                    self.stats.intellect += 1
                    self.base_stats_remaining -= 1
                else:
                    error_string = "Intellect is maxed out. 'm' for menu"

            elif read_char == 's':
                if self.stats.psyche < upper_stat_limit:
                    self.stats.psyche += 1
                    self.base_stats_remaining -= 1
                else:
                    error_string = "Psyche is maxed out. 'm' for menu"

            elif read_char == 'd':
                if self.stats.physique < upper_stat_limit:
                    self.stats.physique += 1
                    self.base_stats_remaining -= 1
                else:
                    error_string = "Physique is maxed out. 'm' for menu"

            elif read_char == 'f':
                if self.stats.motorics < upper_stat_limit:
                    self.stats.motorics += 1
                    self.base_stats_remaining -= 1
                else:
                    error_string = "Motorics is maxed out. 'm' for menu"

            elif read_char == 'j':
                if self.stats.intellect > 1:
                    self.stats.intellect -= 1
                    self.base_stats_remaining += 1
                else:
                    error_string = "Minimum Intellect value is 1."

            elif read_char == 'k':
                if self.stats.psyche > 1:
                    self.stats.psyche -= 1
                    self.base_stats_remaining += 1
                else:
                    error_string = "Minimum Psyche value is 1."

            elif read_char == 'l':
                if self.stats.physique > 1:
                    self.stats.physique -= 1
                    self.base_stats_remaining += 1
                else:
                    error_string = "Minimum Physique value is 1."

            elif read_char == ';':
                if self.stats.motorics > 1:
                    self.stats.motorics -= 1
                    self.base_stats_remaining += 1
                else:
                    error_string = "Minimum Motoric value is 1."

            elif read_char == 'm':
                self.intro_stats_menu()

            if error_string is not None:
                print(error_string)
            else:
                self.print_stats()

    def define_base_stats(self):
        self.intro_stats_menu()
        self.base_stats_handle_user_input()
        self.stats.set_stats_to_base_selected()

    def add_level_point_to_stat(self):

        dict_list = [key for key in self.stats.stats.keys()]
        index = 0
        print("Select stat to boost (a, f), space to select")
        while self.level_points_remaining != 0:
            print("> ", end='', flush=True)
            stat_value = self.stats.stats[dict_list[index]].value
            if stat_value == 1:
                point_text = "point"
            else:
                point_text = "points"
            print("{}: {} {}".format(dict_list[index], stat_value, point_text) +
                  " " * 20 + chr(8)*60, end='', flush=True)
            read_char = msvcrt.getch().decode("utf-8").lower()

            if ' ' == read_char:
                self.level_points_remaining -= 1
                self.stats.stats[dict_list[index]].value += 1
            elif 'a' == read_char:
                if index == 0:
                    index = len(dict_list) - 1
                else:
                    index -= 1
            elif 'f' == read_char:
                if index == len(dict_list) - 1:
                    index = 0
                else:
                    index += 1
        return True

    def create_character(self):
        define_base_stats = 0
        add_level_point_to_stat = 1
        finished_creation = 2
        state = define_base_stats
        while state != finished_creation:
            if state == define_base_stats:
                self.define_base_stats()
                state = add_level_point_to_stat
            elif state == add_level_point_to_stat:
                if self.add_level_point_to_stat():
                    print("completed Character startup")
                    break


if __name__ == '__main__':
    syl_character_test = SylCharacter(name="Beeku", description="Eeku's pet bird")
