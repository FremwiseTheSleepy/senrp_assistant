from Stats.Stats import Stats


class SylStats(Stats):
    def __init__(self, name=None, description="", value=0, maximum=20):
        super(SylStats, self).__init__(name, description, value, maximum=maximum)

    def __str__(self):
        return "{}: {}".format(self.name, self.value)
