from Character.Character import Character


class SylCharacter(Character):
    BASE_LUCK = 10
    MAX_INVENTORY_ITEMS = 10

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
