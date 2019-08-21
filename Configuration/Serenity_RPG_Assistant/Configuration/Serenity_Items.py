from Configuration.Serenity_Config import SerenityItem


serenity_tools = {
    "Fire Jelly": SerenityItem(name="Fire Jelly",
                               cost=0.2,
                               weight=2,
                               availability='E',
                               notes="Heating element for cooking"
                               ),

    "Garden Bunk": SerenityItem(name="Garden Bunk",
                                cost=18,
                                weight=45,
                                availability='C',
                                notes="Shipboard mini-garden"
                                ),

    "Gun Vac Case": SerenityItem(name="Gun Vac Case",
                                 cost=2.6,
                                 weight=4,
                                 availability='C',
                                 notes="Allows a firearm to function in a vacuum"
                                 ),

    "Gun Cleaning Kit": SerenityItem(name="Gun Cleaning Kit",
                                     cost=2.4,
                                     weight=4,
                                     availability='E',
                                     notes="Gun and knife cleaning care and gear"
                                     ),

    "Multiband": SerenityItem(name="Multiband",
                              cost=4.8,
                              weight="–",
                              availability='C',
                              notes="Multi-function watch"
                              ),

    "Patch Tape": SerenityItem(name="Patch Tape",
                               cost=1.2,
                               weight=3,
                               availability='E',
                               notes="10-yard roll of airtight cloth patching"
                               ),

    "Purification Crystals": SerenityItem(name="Purification Crystals",
                                          cost=0.4,
                                          weight="–",
                                          availability='E',
                                          notes="Prepares 20 gallons of water to drink"
                                          ),

    "Trash Incinerator": SerenityItem(name="Trash Incinerator",
                                      cost=7.4,
                                      weight=20,
                                      availability='E',
                                      notes="Disposes of organic trash"
                                      ),

}

serenity_food = {
    "Crop Supplements": SerenityItem(name="Crop Supplements",
                                     cost=300,
                                     weight=0,
                                     availability='C',
                                     notes="Fertilizer and growth-stimulating chemicals for most crop plants"
                                     ),

    "Drink, Fine Wine": SerenityItem(name="Drink, Fine Wine",
                                     cost=6.4,
                                     weight=0,
                                     availability='C',
                                     notes="One case"
                                     ),

    "Drink, Good Whiskey": SerenityItem(name="Drink, Good Whiskey",
                                        cost=5.6,
                                        weight=0,
                                        availability='C',
                                        notes="One decanter"
                                        ),

    "Foodstuffs, Canned": SerenityItem(name="Foodstuffs, Canned",
                                       cost=5,
                                       weight=0,
                                       availability='E',
                                       notes="Average cost for one person/week"
                                       ),

    "Foodstuffs, Fresh": SerenityItem(name="Foodstuffs, Fresh",
                                      cost=8,
                                      weight=0,
                                      availability='E',
                                      notes="Average cost for one person/week"
                                      ),

    "Foodstuffs, Luxury": SerenityItem(name="Foodstuffs, Luxury",
                                       cost=2,
                                       weight=0,
                                       availability='C',
                                       notes="Average cost for one ‘unit’"
                                       ),

    "Foodstuffs, Nutrient Bars": SerenityItem(name="Foodstuffs, Nutrient Bars",
                                              cost=570,
                                              weight=0,
                                              availability='C',
                                              notes="Case of 100 bars"
                                              ),

    "Foodstuffs, Protein Packs": SerenityItem(name="Foodstuffs, Protein Packs",
                                              cost=2.5,
                                              weight=0,
                                              availability='E',
                                              notes="Average cost for one person/week"
                                              ),

    "Spices, Common": SerenityItem(name="Spices, Common",
                                   cost=2,
                                   weight=0,
                                   availability='C',
                                   notes="½ lb package"
                                   ),

    "Spices, Rare": SerenityItem(name="Spices, Rare",
                                 cost=5,
                                 weight=0,
                                 availability='C',
                                 notes="Five ounce package"
                                 ),

}

serenity_computer_tools = {
    "Cortex Terminal, Black Box": SerenityItem(name="Cortex Terminal, Black Box",
                                               cost=747.2,
                                               weight=20,
                                               availability='I',
                                               notes="Illegal, nonstandard Cortex access terminal"
                                               ),

    "Cortex Terminal, Personal Access": SerenityItem(name="Cortex Terminal, Personal Access",
                                                     cost=100,
                                                     weight=15,
                                                     availability='C',
                                                     notes="Allows access to profiles on Cortex for data storage"
                                                     ),

    "Cortex Terminal, Public Access": SerenityItem(name="Cortex Terminal, Public Access",
                                                   cost=52,
                                                   weight=15,
                                                   availability='E',
                                                   notes="Allows access to profiles on Cortex for data storage"
                                                   ),

    "Data-library, Standard": SerenityItem(name="Data-library, Standard",
                                           cost=22.8,
                                           weight="–",
                                           availability='E',
                                           notes="Annual renewal costs ¼ original price"
                                           ),

    "Data-library, Professional": SerenityItem(name="Data-library, Professional",
                                               cost=92,
                                               weight="–",
                                               availability='C',
                                               notes="Annual renewal costs ¼ original price; "
                                                     "may require Alliance certification"
                                               ),

    "DataBook": SerenityItem(name="DataBook",
                             cost=30,
                             weight=2,
                             availability='E',
                             notes="Low-storage display unit; "
                                   "reads data discs and can interface with Cortex terminals"
                             ),

    "Data Disc": SerenityItem(name="Data Disc",
                              cost=0.2,
                              weight="-",
                              availability='E',
                              notes="Stores electronic data or recordings"
                              ),

    "Dedicated Sourcebox": SerenityItem(name="Dedicated Sourcebox",
                                        cost=154,
                                        weight=30,
                                        availability='C',
                                        notes="Allows access to Cortex, "
                                              "but also acts as a local Cortex hub and database"
                                        ),

    "Encyclopedia": SerenityItem(name="Encyclopedia",
                                 cost=60,
                                 weight=2,
                                 availability='C',
                                 notes="Official Encyclopedic Data-library (OED)"
                                 ),

    "Holo-Image Development Suite": SerenityItem(name="Holo-Image Development Suite",
                                                 cost=64,
                                                 weight=5,
                                                 availability='C',
                                                 notes="A software bundle with additional computer hardware"
                                                 ),

    "SubKelvin": SerenityItem(name="SubKelvin",
                              cost=80,
                              weight="–",
                              availability='I',
                              notes="A security-destroying software link"
                              ),

    "XerO Security": SerenityItem(name="XerO Security",
                                  cost=7.2,
                                  weight="–",
                                  availability='C',
                                  notes="Computer security software; 5 credit annual fee"
                                  ),

}

serenity_communications_and_security_equipment = {
    "Barrier Field": SerenityItem(name="Barrier Field",
                                  cost=1062,
                                  weight=450,
                                  availability='C',
                                  notes="Up to 50 feet of force-barrier fencing"
                                  ),

    "Commpack, Long Range": SerenityItem(name="Commpack, Long Range",
                                         cost=37.8,
                                         weight=10,
                                         availability='C',
                                         notes="Allows communication up to 300 miles"
                                         ),

    "Commpack, Short Range": SerenityItem(name="Commpack, Short Range",
                                          cost=22.4,
                                          weight=7,
                                          availability='E',
                                          notes="Allows communication up to 20 miles"
                                          ),

    "Distress Beacon": SerenityItem(name="Distress Beacon",
                                    cost=31,
                                    weight=14,
                                    availability='C',
                                    notes="Automated distress signal, range of 750 miles, self-powered for 10 hours"
                                    ),

    "Emergency Signal Ring": SerenityItem(name="Emergency Signal Ring",
                                          cost=300,
                                          weight='-',
                                          availability='C',
                                          notes="A Newtech, miniaturized distress beacon, worn as a ring"
                                          ),

    "Fedband Scanner": SerenityItem(name="Fedband Scanner",
                                    cost=19.8,
                                    weight=3,
                                    availability='I',
                                    notes="Reads most official frequencies"
                                    ),

    "Gunscanner": SerenityItem(name="Gunscanner",
                               cost=132.8,
                               weight=220,
                               availability='C',
                               notes="Security device"
                               ),

    "Micro Transmitter": SerenityItem(name="Micro Transmitter",
                                      cost=8,
                                      weight='–',
                                      availability='C',
                                      notes="Wearable comm. unit"
                                      ),

    "Motion Sensor Array": SerenityItem(name="Motion Sensor Array",
                                        cost=22,
                                        weight=12,
                                        availability='C',
                                        notes="Redeployable security system"
                                        ),

    "Ship-linked Handset": SerenityItem(name="Ship-linked Handset",
                                        cost=3.2,
                                        weight=1,
                                        availability='E',
                                        notes="Handset linked to ship’s comm. system, 10 mile range"
                                        ),

    "Surveyor’s Box": SerenityItem(name="Surveyor’s Box",
                                   cost=230,
                                   weight=65,
                                   availability='C',
                                   notes="Scanning and detection equipment for laying out mine-shafts"
                                   ),

    "Transmission Station": SerenityItem(name="Transmission Station",
                                         cost=2200,
                                         weight=3000,
                                         availability='C',
                                         notes="License: ₡1,000/year; can process Telofonix and other Cortex signals"
                                         ),

    "Jabberwocky Signal Blocker": SerenityItem(name="Jabberwocky Signal Blocker",
                                               cost=13.3,
                                               weight=10,
                                               availability='I',
                                               notes="Powerful communication jamming unit"
                                               ),

}

serenity_medical_equipment = {
    "Blastomere Organs": SerenityItem(name="Blastomere Organs",
                                      cost=18000,
                                      weight=5,
                                      availability='I',
                                      notes="Newtech replacement organs; can extend lifespan"
                                      ),

    "Cryo Chamber": SerenityItem(name="Cryo Chamber",
                                 cost=1300,
                                 weight=275,
                                 availability='I',
                                 notes="Suspended animation unit"
                                 ),

    "Dermal Mender": SerenityItem(name="Dermal Mender",
                                  cost=800,
                                  weight=15,
                                  availability='C',
                                  notes="Newtech wound-sealing equipment"
                                  ),

    "Doctor’s Bag": SerenityItem(name="Doctor’s Bag",
                                 cost=27.4,
                                 weight=7,
                                 availability='R',
                                 notes="Simple case with tools and supplies"
                                 ),

    "Doctor’s Bag (MedAcad)": SerenityItem(name="Doctor’s Bag (MedAcad)",
                                           cost=210,
                                           weight=8,
                                           availability='C',
                                           notes="A full set of portable Core MedAcad tools and supplies"
                                           ),

    "First-Aid Kit": SerenityItem(name="First-Aid Kit",
                                  cost=0.6,
                                  weight=3,
                                  availability='E',
                                  notes="A basic first-aid kit"
                                  ),

    "Immunization Packet": SerenityItem(name="Immunization Packet",
                                        cost=3,
                                        weight='–',
                                        availability='C',
                                        notes="Powerful but short-lived inoculation against most common diseases"
                                        ),

    "MedComp": SerenityItem(name="MedComp",
                            cost=312,
                            weight=23,
                            availability='C',
                            notes="Vital-status diagnostic computer"
                            ),

    "Medical Supplies, Emergency": SerenityItem(name="Medical Supplies, Emergency",
                                                cost=110,
                                                weight=20,
                                                availability='C',
                                                notes="Most commonly needed emergency supplies for one month"
                                                ),

    "Medical Supplies, Standard": SerenityItem(name="Medical Supplies, Standard",
                                               cost=46,
                                               weight=15,
                                               availability='C',
                                               notes="Standard medical supplies to keep an infirmary "
                                                     "stocked for one month"
                                               ),

    "Operating Theatre, Modular": SerenityItem(name="Operating Theatre, Modular",
                                               cost=346,
                                               weight=1250,
                                               availability='C',
                                               notes="Base camp or shipboard infirmary; installation costs ₡ 25"
                                               ),

}

serenity_engineering_supplies = {
    "CAD Board": SerenityItem(name="CAD Board",
                              cost=27.2,
                              weight=5,
                              availability='C',
                              notes="Design and schematic display tablet"
                              ),

    "Cutting Torch": SerenityItem(name="Cutting Torch",
                                  cost=4,
                                  weight=8,
                                  availability='E',
                                  notes="Will cut through most metal"
                                  ),

    "Gravcart": SerenityItem(name="Gravcart",
                             cost=485,
                             weight=150,
                             availability='C',
                             notes="Can carry up to one ton"
                             ),

    "Scrapware": SerenityItem(name="Scrapware",
                              cost=5,
                              weight=50,
                              availability='E',
                              notes="Junked parts, for repair materials"
                              ),

    "Sticky Scrapper’s Gel": SerenityItem(name="Sticky Scrapper’s Gel",
                                          cost=2,
                                          weight=2,
                                          availability='C',
                                          notes="Used to cut sheet metal, bulkheads, etc; price per 10 yards of gel"
                                          ),

    "Tool Kit, Basic": SerenityItem(name="Tool Kit, Basic",
                                    cost=14.4,
                                    weight=15,
                                    availability='E',
                                    notes="A full set of basic hand-tools"
                                    ),

    "Tool Set, Electronic": SerenityItem(name="Tool Set, Electronic",
                                         cost=138,
                                         weight=45,
                                         availability='C',
                                         notes="Used for computer and electronic device or circuit work"
                                         ),

    "Tool Set, Mechanic’s": SerenityItem(name="Tool Set, Mechanic’s",
                                         cost=284,
                                         weight=130,
                                         availability='E',
                                         notes="A moderately well-furnished workshop"
                                         ),

}

serenity_covert_ops_gear = {
    "Debugger": SerenityItem(name="Debugger",
                             cost=20,
                             weight=1,
                             availability='C',
                             notes="Single scrambling hub; 15’ radius"
                             ),

    "Disguise Kit": SerenityItem(name="Disguise Kit",
                                 cost=65.6,
                                 weight=5,
                                 availability='C',
                                 notes="Refill for ₡ 5 per 10 uses"
                                 ),

    "Eavesdrops": SerenityItem(name="Eavesdrops",
                               cost=47.2,
                               weight=3,
                               availability='I',
                               notes="Includes 4 bugs and transmission hub"
                               ),

    "Fake IdentCard": SerenityItem(name="Fake IdentCard",
                                   cost=4000,
                                   weight='–',
                                   availability='I',
                                   notes="Illegal and hard to obtain"
                                   ),

    "Laserlight Mist": SerenityItem(name="Laserlight Mist",
                                    cost=1.8,
                                    weight=1,
                                    availability='1',
                                    notes="C One can, good for about 25 cubic feet"
                                    ),

    "Lock Picks": SerenityItem(name="Lock Picks",
                               cost=14,
                               weight='–',
                               availability='I',
                               notes="Required for mechanical locks"
                               ),

    "Lock Picks, Electronic": SerenityItem(name="Lock Picks, Electronic",
                                           cost=35.4,
                                           weight=1,
                                           availability='I',
                                           notes="Required for electronic locks"
                                           ),

    "Mag Charge": SerenityItem(name="Mag Charge",
                               cost=27,
                               weight=1,
                               availability='I',
                               notes="Shorts out electronic devices"
                               ),

    "Optical Bomb": SerenityItem(name="Optical Bomb",
                                 cost=16,
                                 weight=1,
                                 availability='I',
                                 notes="Wide-spectrum; may disable cameras"
                                 ),

    "Poison, Kortine (Debilitating)": SerenityItem(name="Poison, Kortine (Debilitating)",
                                                   cost=11,
                                                   weight='–',
                                                   availability='I',
                                                   notes="Price per dose"
                                                   ),

    "Poison, Cyanol (Lethal)": SerenityItem(name="Poison, Cyanol (Lethal)",
                                            cost=12.6,
                                            weight='–',
                                            availability='I',
                                            notes="Price per dose"
                                            ),

}

serenity_robots = {
    "AgriCultivator": SerenityItem(name="AgriCultivator",
                                   cost=2240,
                                   weight=1300,
                                   availability='C',
                                   notes="Automated farming robot"
                                   ),

    "Automated Secretary": SerenityItem(name="Automated Secretary",
                                        cost=1600,
                                        weight=100,
                                        availability='C',
                                        notes="Receptionist; can take & transfer Telofonix calls, greet visitors, etc."
                                        ),

    "LoveBot": SerenityItem(name="LoveBot",
                            cost=1960,
                            weight=120,
                            availability='*',
                            notes="Personal companion robot... black market, anyone owning one has a black mark "
                                  "from the Companion Registry"
                            ),

    "Excavator": SerenityItem(name="Excavator",
                              cost=2350,
                              weight=950,
                              availability='R',
                              notes="Designed for mining and digging"
                              ),

    "Household Assistant": SerenityItem(name="Household Assistant",
                                        cost=1344,
                                        weight=55,
                                        availability='C',
                                        notes="Cleans floors thoroughly"
                                        ),

    "Scout Drone": SerenityItem(name="Scout Drone",
                                cost=640,
                                weight=12,
                                availability='I',
                                notes="Military reconnaissance robot"
                                ),

}
