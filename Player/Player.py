
class Player(object):
    """ Base class for all PCs or NPCs """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
