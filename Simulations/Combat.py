
class Combat:
    """ Perform combat tasks and simulations """
    # TODO: Abstact to be character 1 and character 2.
    def __init__(self, character1, character2, number_of_sims=100, print_all=False):
        self.num_of_sims = number_of_sims
        self.character1 = character1
        self.character2 = character2
        self.simulation_data = ""
        self.print_all = print_all

    def __str__(self):
        output_string = "Combat Results:\n"
        output_string += "{}".format(self.character1)
        output_string += "{}".format(self.character2)
        output_string += " Number of simulations: {}\n".format(self.num_of_sims)

        output_string += self.simulation_data
        return output_string

    def run_simulation(self):
        """

        :return:
        """

        self.simulation_data = self.perform_attack_simulations(self.num_of_sims,
                                                               self.character1,
                                                               self.character2,
                                                               self.print_all)

    def perform_attack_simulations(self, num_of_sims, character1, character2, print_all):
        """

        :param num_of_sims:
        :param character1:
        :param character2:
        :param print_all:
        :return:
        """
        return ""
