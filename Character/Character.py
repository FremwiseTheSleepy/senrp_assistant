import abc


class Character(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self,
                 character_name="Eeku",
                 age=18,
                 description="Let's go",
                 internal_description="Want's to be a folk singer",
                 money=0,
                 stats=None,
                 health=None):
        """
        Character Constructor
        :param character_name: String, name of character
        :param age: int, usually in earth years, could be arbitrary
        :param description: Info others should know about your character
        :param internal_description: Info only you/DM should know about your character
        :param money: int, some number of currency
        :param stats: type defined by subclass, stats skills, etc. Should probably be in a dictionary for parseability
        :param health: type defined by subclass, could be multiple health/mana/stat pools
        """
        self.character_name = character_name
        self.age = age
        self.description = description
        self.internal_description = internal_description
        self.stats = stats
        self.money = money
        self.health = health
        self.inventory = None

    @abc.abstractmethod
    def __str__(self):
        """
        When someone prints this character, what do they see? Recommend use as documentation to what is available
        :return:
        """
        raise NotImplementedError('Subclasses must define how to layout Character printing')

    @abc.abstractmethod
    def get_max_health(self):
        """
        get and return the maximum value one or more health pools.
        :return:
        """
        raise NotImplementedError('Subclasses must define max health')

    def add_to_invetory(self, item_to_add_to_inventory):
        """
        Add an item to the inventory
        :param item_to_add_to_inventory: item to add to inventory
        :return:
        """
        raise NotImplementedError("Subclasses define what adding to the inventory entails")

    def get_invetory(self):
        """
        Return what the character has in their inventory
        :return:
        """
        raise NotImplementedError("Subclasses define what returning the inventory entails")

    def get_current_health(self):
        """
        Can return health as current HP, MP or even status effects
        :return:
        """
        return self.health

    def get_character_name(self):
        """
        Name, can get creative if you want.
        :return:
        """
        return self.character_name

    def set_character_name(self, character_name):
        """
        What others refer to you as
        :param character_name: string, name to call this fine specimen
        :return:
        """
        self.character_name = character_name

    def get_stats(self):
        """
        general return all for stats, skills, etc.
        :return:
        """
        return self.stats

    def get_money(self):
        """
        return amount of money
        :return:
        """
        return self.money