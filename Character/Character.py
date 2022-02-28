import abc


class Character(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, character_name=None, age=0, description="", stats=None, money=0, health=None):
        self.character_name = character_name
        self.age = age
        self.description = description
        self.stats = stats
        self.money = money
        self.health = health

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError('This must be defined by derived classes')

    @abc.abstractmethod
    def get_max_health(self):
        raise NotImplementedError('This must be defined by derived classes')

    def get_character_name(self):
        return self.character_name

    def set_character_name(self, character_name):
        self.character_name = character_name

    def get_current_health(self):
        return self.health

    def get_stats(self):
        return self.stats

    def get_money(self):
        return self.money
