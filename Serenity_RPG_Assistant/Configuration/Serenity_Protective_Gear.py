from Configuration.Serenity_Config import SerenityArmor, SerenityStats


serenity_armor = {
    "Ballistic Mesh": SerenityArmor(name="Ballistic Mesh",
                                    armor_rating="1W*",
                                    penalty=None,
                                    cost=46,
                                    weight=4,
                                    availability='C',
                                    notes="Absorbs 1 wound from any attack on covered area. Converts 8 wound to stun "
                                          "from normal bullets"
                                    ),

    "Chameleon Suit": SerenityArmor(name="Chameleon Suit",
                                    armor_rating="1W",
                                    penalty=None,
                                    cost=40,
                                    weight=17,
                                    availability='I'
                                    ),

    "Helmet, Infantry": SerenityArmor(name="Helmet, Infantry",
                                      armor_rating="4W",
                                      penalty=SerenityStats(alertness=-1),
                                      cost=16,
                                      weight=2,
                                      availability='E'
                                      ),

    "Helmet, Squad": SerenityArmor(name="Helmet, Squad",
                                   armor_rating="4W",
                                   penalty=SerenityStats(alertness=-2),
                                   cost=35,
                                   weight=3,
                                   availability='C'
                                   ),

    "Mask, NBC": SerenityArmor(name="Mask, NBC",
                               armor_rating="2W",
                               penalty=SerenityStats(alertness=-3),
                               cost=8,
                               weight=3,
                               availability='C'
                               ),

    "NBC Body Suit": SerenityArmor(name="NBC Body Suit",
                                   armor_rating="2W",
                                   penalty=SerenityStats(agility=-2, alertness=-2),
                                   cost=32,
                                   weight=14,
                                   availability='C'
                                   ),

    "Plate Vest": SerenityArmor(name="Plate Vest",
                                armor_rating="4W*",
                                penalty=SerenityStats(agility=-1),
                                cost=30,
                                weight=10,
                                availability='E',
                                notes="Any hits on covered area (torso) are converted to stun. "
                                      "Protects against sharp objects"
                                ),

    "Riot Gear": SerenityArmor(name="Riot Gear",
                               armor_rating="3W*",
                               penalty=SerenityStats(agility=-1, alertness=-1),
                               cost=92,
                               weight=24,
                               availability='C',
                               notes="Effects of mesh apply only to bullets, but AR reduces damage from all attacks"
                               ),

    "HeartLine Health Suit": SerenityArmor(name="HeartLine Health Suit",
                                           armor_rating="–",
                                           penalty=None,
                                           cost=28,
                                           weight=3,
                                           availability='C'
                                           ),

    "Tactical Suit": SerenityArmor(name="Tactical Suit",
                                   armor_rating="5W",
                                   penalty=SerenityStats(agility=-2),
                                   cost=110,
                                   weight=18,
                                   availability='I'
                                   ),

    "Vacuum Suit": SerenityArmor(name="Vacuum Suit",
                                 armor_rating="2W",
                                 penalty=SerenityStats(agility=-2, alertness=-2),
                                 cost=67,
                                 weight=35,
                                 availability='E'
                                 ),

}
