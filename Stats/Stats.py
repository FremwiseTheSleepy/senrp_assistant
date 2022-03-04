import abc


class Stats(object):
    """ Stats, Skills, Traits, Weaknesses """
    __metaclass__ = abc.ABCMeta

    def __init__(self,
                 name=None,
                 description="",
                 value=0,
                 maximum=None):
        self.name = name
        self.description = description
        self.value = value
        self.maximum = maximum

    @abc.abstractmethod
    def __str__(self):
        """
        When someone prints this character, what do they see? Recommend use as documentation to what is available
        :return:
        """
        raise NotImplementedError('Subclasses must define how to layout Character printing')


class StatGroup(object):
    """ a collection of stats """
    def __init__(self, name="Stats", stats_to_add=None, stat_groups_to_add=None):
        """


        :param name:
        :param stats_to_add:
        :type stats_to_add: tuple of Stats
        :param stat_groups_to_add:
        :type stat_groups_to_add: tuple of StatGroup
        """

        self.name = name
        self.stats = stats_to_add

    def stat_summation(self):
        stat_sum = 0
        if self.stats:
            for stat in self.stats:
                stat_sum += stat.value

        return stat_sum


