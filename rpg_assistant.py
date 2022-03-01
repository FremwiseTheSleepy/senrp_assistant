
if __name__ == "__main__":
    from Configurations.OneRing.Simulations.Combat import Combat, VERSION
    from Configurations.OneRing.Confinguration.OneRing import WeaponStructure, StanceTN
    from Configurations.OneRing.Character.Hero.Hero import Hero
    from Configurations.OneRing.Character.BadGuy.BadGuy import BadGuy
    # TODO: make a (better) command line interface
    # edit here for now
    weapon_type = "Bow"         # Select text from WeaponDatabase
    bad_guy_name = "bg245b"     # select from BadGuyDatabase
    damage_mod = 0              # e.g. Grievous = 2 (reward, pg 116, e-book)
    edge_mod = 0                # e.g. Keen = 1 (reward)
    injury_mod = 0              # e.g. Fell = 2 (reward)
    hit_mod = 0                 # e.g. Bow of the North Downs (bow), 3 (more if valor higher)
    player_basic_body = 3       # adds bonus damage for great/extraordinary successes
    num_success_dice = 2        # skill / success dice of the weapon
    extra_feat_rolls = 0        # e.g. fair shot = 1 (virtue)
    pc_stance = StanceTN.Def    # stance player character is in, affects hit rate (if rearward, use "def")

    combat = Combat(number_of_sims=100000,
                    hero=Hero("Ikari Shinji",
                              weapon_type,
                              weapon_success_dice=num_success_dice,
                              bonus_feat_rolls=extra_feat_rolls,
                              weapon_mods=WeaponStructure(damage=damage_mod,
                                                          edge=edge_mod,
                                                          injury=injury_mod,
                                                          hit_bonus=hit_mod),
                              player_damage=player_basic_body,
                              stance=pc_stance),
                    bad_guy=BadGuy(bad_guy_name),
                    print_all=False,
                    )
    combat.run_simulation()
    print("Version: combat sim: {}".format(VERSION))
    print(combat)
