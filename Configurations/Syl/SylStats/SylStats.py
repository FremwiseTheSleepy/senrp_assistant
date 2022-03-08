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
    def __init__(self, intellect, psyche, physique, motorics):
        super(SylStatOverallGroup, self).__init__()
        self.stats = {
            'Encyclopedia': SylStats(name='Encyclopedia',
                                     group='Intellect',
                                     description='General lookup type knowledge, history, chemistry, biology',
                                     value=intellect),
            'Visual Calculus': SylStats(name='Visual Calculus',
                                        group='Intellect',
                                        description='Physics, mathematics',
                                        value=intellect),
            'Conceptualization': SylStats(name='Conceptualization',
                                          group='Intellect',
                                          description='Arts, acting',
                                          value=intellect),
            'Adaptability': SylStats(name='Adaptability',
                                     group='Intellect',
                                     description='How quickly you can pick up on things',
                                     value=intellect),
            'Interfacing': SylStats(name='Interfacing',
                                    group='Intellect',
                                    description='How well you interact with objects',
                                    value=intellect),
            'Poker Face': SylStats(name='Poker Face',
                                   group='Intellect',
                                   description='Say what you want without tipping your hand (lie)',
                                   value=intellect),

            'Volition': SylStats(name='Volition',
                                 group='Psyche',
                                 description='Energy Point Bonus',
                                 value=psyche),
            'Empathy': SylStats(name='Empathy',
                                group='Psyche',
                                description='Pick up on what people are thinking',
                                value=psyche),
            'Suggestion': SylStats(name='Suggestion',
                                   group='Psyche',
                                   description='Force your ideas on someone else',
                                   value=psyche),
            'Medium': SylStats(name='Medium',
                               group='Psyche',
                               description='Supernatural interface',
                               value=psyche),
            'Mental Shell': SylStats(name='Mental Shell',
                                     group='Psyche',
                                     description='Defense against mental trauma',
                                     value=psyche),
            'Mental Recovery': SylStats(name='Mental Recovery',
                                        group='Psyche',
                                        description='How quickly mental health recovers',
                                        value=psyche),

            'Endurance': SylStats(name='Endurance',
                                  group='Physique',
                                  description='Luck Point Bonus',
                                  value=physique),
            'Physical Instrument': SylStats(name='Physical Instrument',
                                            group='Physique',
                                            description='Strength',
                                            value=physique),
            'Electrochemistry': SylStats(name='Electrochemistry',
                                         group='Physique',
                                         description='Increased effects of drugs',
                                         value=physique),
            'Pain Threshold': SylStats(name='Pain Threshold',
                                       group='Physique',
                                       description='Defense against physical trauma',
                                       value=physique),
            'Physical Presence': SylStats(name='Physical Presence',
                                          group='Physique',
                                          description='How intimidating character is',
                                          value=physique),
            'Physical Recovery': SylStats(name='Physical Recovery',
                                          group='Physique',
                                          description='How quickly physical damage recovers',
                                          value=physique),
            'Hand/eye coordination': SylStats(name='Hand/eye coordination',
                                              group='Motorics',
                                              description='Precise movements',
                                              value=motorics),
            'Perception': SylStats(name='Perception',
                                   group='Motorics',
                                   description='Awareness of surroundings',
                                   value=motorics),
            'Reflexes': SylStats(name='Reflexes',
                                 group='Motorics',
                                 description='React quickly to an event',
                                 value=motorics),
            'Speed': SylStats(name='Speed',
                              group='Motorics',
                              description='Move/Interact quickly with objects',
                              value=motorics),
            'Recovery': SylStats(name='Recovery',
                                 group='Motorics',
                                 description='How quickly you recover from an setback',
                                 value=motorics),
            'Savoir faire': SylStats(name='Savoir faire',
                                     group='Motorics',
                                     description='How smoothly you appear, coolness factor, acrobatics',
                                     value=motorics),
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

    syl_test = SylStatOverallGroup(intellect=5, psyche=2, physique=3, motorics=2)
    print(syl_test)
