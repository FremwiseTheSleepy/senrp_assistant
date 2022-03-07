try:
    from Stats.Stats import StatGroup, Stats
except ModuleNotFoundError:
    import sys
    import os
    base_path_key = 'senrp_assistant'
    path = os.getcwd()
    base_path_index = path.find(base_path_key) + len(base_path_key)
    sys.path.append(path[:base_path_index])
    from Stats.Stats import StatGroup, Stats


class SylStats(Stats):
    def __init__(self, name=None, group=None, description="", value=0, maximum=20):
        super(SylStats, self).__init__(name, description, value, maximum=maximum)
        self.group = group

    def __str__(self):
        return "{}: {}".format(self.name, self.value)


class SylStatOverallGroup(StatGroup):
    def __init__(self, intellect):
        super(SylStatOverallGroup, self).__init__()
        self.stats = {
            'int0': SylStats(name='Encyclopedia',
                             group='Intellect',
                             description='General lookup type knowledge, history, chemistry, biology',
                             value=intellect),
            'int1': SylStats(name='Visual Calculus',
                             group='Intellect',
                             description='Physics, mathematics',
                             value=intellect),
            'int2': SylStats(name='Conceptualization',
                             group='Intellect',
                             description='Arts, acting',
                             value=intellect),
            'int3': SylStats(name='Adaptability',
                             group='Intellect',
                             description='How quickly you can pick up on things',
                             value=intellect),
            'int4': SylStats(name='Interfacing',
                             group='Intellect',
                             description='How well you interact with objects',
                             value=intellect),
            'int5': SylStats(name='Poker Face',
                             group='Intellect',
                             description='Say what you want without tipping your hand (lie)',
                             value=intellect),
        }

    def __str__(self):
        string_output = "\n"
        if self.stats:
            for key, val in self.stats.items():
                string_output += "{} ({}): {}, \n   {}\n".format(val.name, val.group, val.value, val.description)

        string_output += "\nTotal points in stats: {}\n".format(self.stat_summation())

        return string_output

    def stat_summation(self):
        stat_sum = 0
        if self.stats:
            for key, val in self.stats.items():
                stat_sum += val.value
        return stat_sum


if __name__ == '__main__':

    syl_test = SylStatOverallGroup(intellect=5)
    print(syl_test)