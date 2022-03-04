import abc


class Equipment(object):
    """ Everything related to equipment, items that can take up slots on a character """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self,
                 name=None,
                 stats=None,
                 slot=None,
                 weight=0):
        self.name = name
        self.stats = stats
        self.slot = slot
        self.weight = weight

    @abc.abstractmethod
    def __str__(self):
        """
        When someone prints this character, what do they see? Recommend use as documentation to what is available
        :return:
        """
        raise NotImplementedError('Subclasses must define how to layout Character printing')
