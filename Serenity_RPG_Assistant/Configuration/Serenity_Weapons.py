from Configuration.Serenity_Config import SerenityWeapon


serenity_hand_to_hand_weapons = {
    "Baton, Security": SerenityWeapon(name="Baton, Security",
                                      damage="d2S",
                                      range_increment_ft=4,
                                      max_rof=1,
                                      magazine_size=0,
                                      cost=1.2,
                                      weight=2,
                                      availability='E'
                                      ),

    "Baton, Stun": SerenityWeapon(name="Baton, Stun",
                                  damage="d2S*",
                                  range_increment_ft=4,
                                  max_rof=1,
                                  magazine_size=0,
                                  cost=12,
                                  weight=2,
                                  availability='C',
                                  notes="All damage is converted to stun. Batteries cost 1g and last 10 shocks"
                                  ),

    "Brass Knuckles": SerenityWeapon(name="Brass Knuckles",
                                     damage="*",
                                     range_increment_ft=4,
                                     max_rof=1,
                                     magazine_size=0,
                                     cost=0.8,
                                     weight=1,
                                     availability='E'
                                     ),

    "Club": SerenityWeapon(name="Club",
                           damage="d6B",
                           range_increment_ft=4,
                           max_rof=1,
                           magazine_size=0,
                           cost=0.2,
                           weight=3,
                           availability='E'
                           ),

    "Hatchet": SerenityWeapon(name="Hatchet",
                              damage="d6W",
                              range_increment_ft=4,
                              max_rof=1,
                              magazine_size=0,
                              cost=16,
                              weight=4,
                              availability='E'
                              ),

    "Knife, Combat": SerenityWeapon(name="Knife, Combat",
                                    damage="d4W",
                                    range_increment_ft=4,
                                    max_rof=1,
                                    magazine_size=0,
                                    cost=1.6,
                                    weight=1,
                                    availability='E'
                                    ),

    "Knife, Utility": SerenityWeapon(name="Knife, Utility",
                                     damage="d2W",
                                     range_increment_ft=4,
                                     max_rof=1,
                                     magazine_size=0,
                                     cost=0.8,
                                     weight=0,
                                     availability='E'
                                     ),

    "Machete": SerenityWeapon(name="Machete",
                              damage="d4W",
                              range_increment_ft=4,
                              max_rof=1,
                              magazine_size=0,
                              cost=3.2,
                              weight=3,
                              availability='E'
                              ),

    "Sword, Combat": SerenityWeapon(name="Sword, Combat",
                                    damage="d6W",
                                    range_increment_ft=4,
                                    max_rof=1,
                                    magazine_size=0,
                                    cost=24,
                                    weight=6,
                                    availability='E'
                                    ),

    "Sword, Gentleman’s": SerenityWeapon(name="Sword, Gentleman’s",
                                         damage="d4W",
                                         range_increment_ft=4,
                                         max_rof=1,
                                         magazine_size=0,
                                         cost=26,
                                         weight=1,
                                         availability='C'
                                         ),

}

serenity_explosive_weapons = {

    "ChemPlast (CP-HE) Charge": SerenityWeapon(name="ChemPlast (CP-HE) Charge",
                                               damage="3d12W",
                                               range_increment_ft=5,
                                               max_rof=1,
                                               magazine_size=1,
                                               cost=6,
                                               weight=1,
                                               availability='I'
                                               ),

    "Grenade, Concussion": SerenityWeapon(name="Grenade, Concussion",
                                          damage="4d6B",
                                          range_increment_ft=10,
                                          max_rof=1,
                                          magazine_size=1,
                                          cost=1.4,
                                          weight=1,
                                          availability='I'
                                          ),

    "Grenade, Flashbang": SerenityWeapon(name="Grenade, Flashbang",
                                         damage="2d6B*",
                                         range_increment_ft=5,
                                         max_rof=1,
                                         magazine_size=1,
                                         cost=0.8,
                                         weight=1,
                                         availability='I',
                                         notes="Everyone within 20 ft automatically gets stunned for 1 turn."
                                               "have to make a Survival Roll, difficulty 15, otherwise stunned for "
                                               "2d6 more turns. If succeeding, only stunned 2 more turns"),

    "Grenade, Fragmentation": SerenityWeapon(name="Grenade, Fragmentation",
                                             damage="5d6 W",
                                             range_increment_ft=15,
                                             max_rof=1,
                                             magazine_size=1,
                                             cost=1.8,
                                             weight=1,
                                             availability='I'
                                             ),

    "Grenade, Smoke": SerenityWeapon(name="Grenade, Smoke",
                                     damage="d4S",
                                     range_increment_ft=20,
                                     max_rof=1,
                                     magazine_size=1,
                                     cost=0.6,
                                     weight=1,
                                     availability='C'
                                     ),

    "Grenade, Gas": SerenityWeapon(name="Grenade, Gas",
                                   damage="3d6S",
                                   range_increment_ft=5,
                                   max_rof=1,
                                   magazine_size=1,
                                   cost=1.2,
                                   weight=1,
                                   availability='I'
                                   ),

    "Mining Charge": SerenityWeapon(name="Mining Charge",
                                    damage="5d10B",
                                    range_increment_ft=2,
                                    max_rof=1,
                                    magazine_size=1,
                                    cost=20,
                                    weight=5,
                                    availability='E'
                                    ),

    "Seeker Missile": SerenityWeapon(name="Seeker Missile",
                                     damage="2d8W",
                                     range_increment_ft=5,
                                     max_rof=1,
                                     magazine_size=1,
                                     cost=95,
                                     weight=4,
                                     availability='I',
                                     notes="Range: tend to move toward movement & heat. Explode when thinking they're "
                                           "near target (not transmitting appropriate transponder signal). Can be "
                                           "tricked by flares."
                                     ),

    "Squadkiller": SerenityWeapon(name="Squadkiller",
                                  damage="4d12W",
                                  range_increment_ft=15,
                                  max_rof=1,
                                  magazine_size=1,
                                  cost=48,
                                  weight=8,
                                  availability='I'
                                  ),

}

serenity_ranged_weapons = {
    "Bow": SerenityWeapon(name="Bow",
                          damage="d4W",
                          range_increment_ft=70,
                          max_rof=1,
                          magazine_size=9999,
                          cost=6,
                          weight=6,
                          availability='E'
                          ),

    "Crossbow": SerenityWeapon(name="Crossbow",
                               damage="d4W",
                               range_increment_ft=150,
                               max_rof=0.5,
                               magazine_size=2,
                               cost=8,
                               weight=13,
                               availability='E'
                               ),

    "Crossbow, Powered":  SerenityWeapon(name="Crossbow, Powered",
                                         damage="d4W",
                                         range_increment_ft=175,
                                         max_rof=2,
                                         magazine_size=6,
                                         cost=24,
                                         weight=15,
                                         availability='C'
                                         ),

    "Derringer":  SerenityWeapon(name="Derringer",
                                 damage="d4W",
                                 range_increment_ft=30,
                                 max_rof=1,
                                 magazine_size=2,
                                 cost=14,
                                 weight=1,
                                 availability='E'
                                 ),

    "Grenade Launcher":  SerenityWeapon(name="Grenade Launcher",
                                        damage="*",
                                        range_increment_ft=40,
                                        max_rof=1,
                                        magazine_size=8,
                                        cost=106,
                                        weight=12,
                                        availability='I',
                                        notes="Damage is equal to the grenade type used. Range increment "
                                              "penalties are doubled"),

    "Pistol":  SerenityWeapon(name="Pistol",
                              damage="d6W",
                              range_increment_ft=100,
                              max_rof=3,
                              magazine_size=8,
                              cost=18,
                              weight=2,
                              availability='E'
                              ),

    "Pistol, Laser":  SerenityWeapon(name="Pistol, Laser",
                                     damage="d10W*",
                                     range_increment_ft=100,
                                     max_rof=3,
                                     magazine_size=10,
                                     cost=330,
                                     weight=1.5,
                                     availability='I',
                                     notes="Causes burn damage upon successful hit"),

    "Rifle":  SerenityWeapon(name="Rifle",
                             damage="d8W",
                             range_increment_ft=225,
                             max_rof=3,
                             magazine_size=30,
                             cost=30,
                             weight=9,
                             availability='E'
                             ),

    "Rifle, Assault":  SerenityWeapon(name="Rifle, Assault",
                                      damage="d8W",
                                      range_increment_ft=150,
                                      max_rof=3,
                                      magazine_size=40,
                                      cost=40,
                                      weight=11,
                                      availability='I'
                                      ),

    "Rifle, Sniper":  SerenityWeapon(name="Rifle, Sniper",
                                     damage="d8W",
                                     range_increment_ft=1000,
                                     max_rof=3,
                                     magazine_size=20,
                                     cost=160,
                                     weight=15,
                                     availability='C',
                                     notes="Range listed is only when bracing & using scope, otherwise 225 ft."
                                     ),

    "Rifle, Sonic":  SerenityWeapon(name="Rifle, Sonic",
                                    damage="d8S",
                                    range_increment_ft=15,
                                    max_rof=2,
                                    magazine_size=50,
                                    cost=140,
                                    weight=6,
                                    availability='I*',
                                    notes="Likely contains a transponder chip to allow it to be tracked."),

    "Shotgun":  SerenityWeapon(name="Shotgun",
                               damage="d10W",
                               range_increment_ft=10,
                               max_rof=2,
                               magazine_size=10,
                               cost=50,
                               weight=10,
                               availability='E'
                               ),

    "Sub-machine Gun":  SerenityWeapon(name="Sub-machine Gun",
                                       damage="d6W",
                                       range_increment_ft=60,
                                       max_rof=3,
                                       magazine_size=35,
                                       cost=36,
                                       weight=4,
                                       availability='I'
                                       ),

}
