"""
Base file to run from; pulls in what it needs to run app.
"""
# import common files
from Character.Character import *

# Import configuration specific files
from select_project_configuration import select_project_configuration
project_configuration_path = select_project_configuration(project_name="Syl")
from Configuration.Combat import *  # noqa: needs to occur after selecing project configuration path

if __name__ == "__main__":
    # TODO: make a (better) command line interface

    characters_path = os.path.join(project_configuration_path, "Characters")

    if characters_path.find("OneRing") != -1:  # TODO: pull in character information based on configuration.
        from Characters.Hero.Hero import Hero
        from Characters.BadGuy.BadGuy import BadGuy
        # Future TODO: pull in based on configuration
        hero_data = load_character_data(os.path.join(characters_path, "Hero"), "default_character.json")

        bad_guy_data = load_character_data(os.path.join(characters_path, "BadGuy"), "default_badguy.json")

        combat = Combat(number_of_sims=100000,
                        character1=Hero(hero_data),
                        character2=BadGuy(bad_guy_data),  # BadGuy("bg247b")
                        print_all=False, )
    else:
        from Characters.Character import SylCharacter
        combat = Combat(character1=SylCharacter("Eeku", "Let's go"),
                        character2=SylCharacter("Glenn", "How's my hair"), )
    combat.run_simulation()
    print(combat)
