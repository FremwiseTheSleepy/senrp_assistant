from Configuration.Serenity_Config import asset_complication_config, SerenityTraitLevel, serenity_bonus_modifier, \
    SerenityStats, SerenitySkills


serenity_assets = {
    "Allure": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="partially or completely sexyfied",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=SerenitySkills(influence=2)),
        fx_notes="(minor) +2 skill to appearance actions (seduction, negotiation,etc) "
                 "(major) any plot points spent have +2 plot points (+d4)",
    ),

    "Athlete": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="push body past normal limits for physical activity (may pay price later w/ sore muscles)",
        numeric_effects=None,
        fx_notes="(minor) pick one athletics specialty can take damage to more likely succeed; "
                 "per point of damage, get plot point worth of rolls (can't spend more than going unconscious)"
                 "(major) plot points spent on physical activities get +d4 (2 plot points)",
    ),

    "Born Behind the Wheel": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="like a fish in water, but instead of water it is a vehicle and instead of a fish it is you",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(agility=2), skills=None),
        fx_notes="(minor) +2 step bonus to agility when at controls of your chosen vehicle type "
                 "(major) plot points spent on actions improve by +2 plot points (d4)",
    ),

    "Cortex Specter": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="living off the grid",
        numeric_effects=None,
        fx_notes="(minor) anybody trying to find your past has +8 difficulty added"
                 "(major) no official docket of you exists anywhere (may have trouble renting a car)",
    ),

    "Fightin' Type": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="handle combat situations of any type well",
        numeric_effects=None,
        fx_notes="Can take one non-attack action each combat turn without penalty "
                 "(i.e. moving & shooting doesn't get a penalty)",
    ),

    "Friends in High Places": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="you know important people",
        numeric_effects=None,
        fx_notes="Once per session you can spend 1 or more Plot points to call in a favor or secure a quick loan "
                 "(more points for more money)",
    ),

    "Friends in Low Places": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="you know shady people",
        numeric_effects=None,
        fx_notes="Once per session you can spend plot point(s) to call in a favor from a criminal contact",
    ),

    "Good Name": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="you have street cred (in whatever circle)",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=SerenitySkills(influence=2)),
        fx_notes="(minor) +2 step bonus to any social action where your name comes into play "
                 "(i.e. if people know who you are) "
                 "(major) kinda a big deal (everyone knows about you, +2 bonus applies all the time)",
    ),

    "Healthy as a Horse": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="don't get sick",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(vitality=2), skills=None),
        fx_notes="(minor) +2 vitality attribute bonus against illness or infections "
                 "(major) heal damage 2x the usual rate; when using plot points, add 2 plot points worth of die (d4)",
    ),

    "Heavy Tolerance": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="drugs don't affect you",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(vitality=2), skills=None),
        fx_notes="gain +2 Vitality attrib bonus against drugs/alcohol/poison/gases)",
    ),

    "Highly Educated": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="good at school",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(intelligence=2), skills=None),
        fx_notes="gain +2 intelligence to knowledge based roll (e.g. when recalling information)",
    ),

    "Intimidatin' Manner": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="folks think twice before crossing you",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(willpower=2), skills=None),
        fx_notes="gain +2 willpower on action that involves intimidation, interrogation, bullying, frightening, etc. "
                 "can be used to resist similar attempts against",
    ),

    "Leadership": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="you're an inspiration to others",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) once per session, can assign goal for receiving leadership bonus; "
                 "anyone working towards this goal can gain a single +2 to any skill check for accomplishing the goal"
                 "(major) can give/spend plot points for others to achieve your goals"
                 "(must be used at the next turn)",
    ),

    "Lightnin' Reflexes": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="Quick Draw McGraw",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(agility=2), skills=None),
        fx_notes="gain +2 attribute to agility on initiative rolls",
    ),

    "Math Whiz": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="good at the maths",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(intelligence=2), skills=None),
        fx_notes="gain +2 attribute bonus to intelligence for accounting, engineering, navigation, etc actions)",
    ),

    "Mean Left Hook": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="good at fighting (bruce lee/chuck norris)",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="unarmed attack damage is split between stun and wound",
    ),

    "Mechanical Empathy": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="good at fixing mechanical devices",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=SerenitySkills(mechanical_engineering_skilled=2)),
        fx_notes="can intuitively know the issue (with plot points); "
                 "skill +2 mechanical engineering for fixing the problem",
    ),

    "Military Rank": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="known as being military (along with the good and bad that come with it)",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(enlisted man) gain +2 willpower on discipline based actions "
                 "(officer) gain +2 influence based actions",
    ),

    "Moneyed Individual": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="I'm rich b...",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="1.5x starting credits; "
                 "once per session, can roll Intelligence + Influence (or other similar) to make purchases from "
                 "trust fund (diff:3 for 2k, 11 for 6k, 19 for 10k)",
    ),

    "Natural Linguist": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="can quickly learn and blend in with new languages, can tell where people are from, from dialect",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="learn linguist specialties at half normal cost. imitate and detect specific accents and dialects "
                 "(+2 influence / performance (or similar) whenever trying to pass as a native)",
    ),

    "Nature Lover": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="in harmony with nature",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="gain +2 attribute to all alertness based rolls in an outdoor setting & equivalent bonus to "
                 "survival skill die when applied to natural environments",
    ),

    "Nose for Trouble": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="Spidey sense tingling ability (second sense about when things are going to go wrong",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) make an intelligence or alertness based roll to sense trouble even when circumstances may "
                 "not normally permit it. gain +2 to either intelligence or alertness "
                 "(major) can spend 1 plot point to negate all effects of surprise (sense trouble in nick of time "
                 "to avoid being caught off guard)",
    ),

    "Reader": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="mind is open to thoughts and emotions of folk nearby",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) learn general feelings and moods of those around you; + 2 Attribute bonus to Alertness "
                 "whenever observing someone "
                 "(major) increases to +4 and can spend plot points (once per session) to gain clues/info",
    ),

    "Registered Companion": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="licensed to be a companion",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="gain +2 influence based actions for those who respect your station",
    ),

    "Religiosity": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="faithful practitioner or bona fide person of your particular god(s)",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) one +2 attribute bonus to any willpower based action "
                 "(major) respected leader & can wear garbs; all plot points spent on influence (for those who "
                 "respect your station) gain an extra +2 plot point die (d4)",
    ),

    "Sharp Sense": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="one of your senses is very keen",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="gain +2 Alertness for any action utilizing that sense (this trait can be chosen multiple "
                 "times for different senses)",
    ),

    "Steady Calm": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="clear headed in difficult situations",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) +2 willpower to avoid being shaken, frightened "
                 "(major) never frightened unless under extremely unusual circumstances "
                 "(story requires it for example/under the influence/etc)",
    ),

    "Sweet and Cheerful": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="cheerful to the max",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="gain +2 skill bonus to any action that your sweetness works in your favor",
    ),

    "Talented": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="you're better than others at a given skill (paired with other skill)",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) pick a specialty, gain +2 skill bonus on every use of that skill "
                 "(major) during advancement to a higher die for that skill, costs 2 points less than usual",
    ),

    "Things Go Smooth": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="lucky!",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) can re-roll any action (except botches) once per session "
                 "(major) can re-roll any action (including botches) twice per session",
    ),

    "Total Recall": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="good at remembering things you've seen/heard",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="gain +2 skill bonus to any action where remembering things helps. "
                 "Can spend a plot point to remember (exactly) every detail of a past event/encounter "
                 "(may have some story exceptions)",
    ),

    "Tough as Nails": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="good at taking a beating & keep smiling",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) +2 health (major) +4 health",
    ),

    "Trustworthy Gut": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="learned to trust your hunches to keep you out of trouble (or into opportunity)",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) +2 bonus to any mental attribute when you're relying on intuition "
                 "(major) can spend plot points to ask GM yes/no questions (first:-1, 2nd:-2, 3rd:-3 (total 6))",
    ),

    "Two-Fisted": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="ambidextrous",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="can perform any task with either hand without penalty",
    ),

    "Walking Timepiece": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="never need to look at watch for time",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="under normal circumstances, you know the time of day or how much time has passed; "
                 "if KO'd it takes a full turn Intelligence + Alertness action at average difficulty "
                 "to get it back to normal",
    ),

    "Wears a Badge": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="the law",
        numeric_effects=serenity_bonus_modifier(stats=None, skills=None),
        fx_notes="(minor) +2 skill bonus to all influence based actions when dealing with those that respect your "
                 "position (local law enforcement - to planet or region) "
                 "(major) authority is increased from local to most of the 'verse",
    ),

}

serenity_complications = {
    "Allergy": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="food, sting, pollen, etc. give you issues",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(agility=-2, strength=-2, vitality=-2),
                                                skills=None),
        fx_notes="Pick an allergy (minor) -2 penalty to physical attributes (agi, str, vit) "
                 "until medicated (major) suffer d2 damage (stun) each turn until no more stun "
                 "remain, then take shock/wound damage. Most likely carry an emergency "
                 "injection/medication that will stop effects in d4 turns."
    ),

    "Amorous": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="sexytimes on the mind near all the time",
        numeric_effects=serenity_bonus_modifier(stats=SerenityStats(willpower=-2),
                                                skills=SerenitySkills(influence=-2)),
        fx_notes="make a pass at almost all people of your sexual preference and don't put up barriers when "
                 "someone is coming on to you causes -2 skill penalty to Influence based actions when other "
                 "party is offended by your actions causes -2 to Willpower attribute penalty when trying to "
                 "resist someone of your 'type'"
    ),

    "Amputee": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="missing an arm or leg; may have prosthetic, but it isn't a nice model",
        numeric_effects=serenity_bonus_modifier(stats=None, skills="See notes"),
        fx_notes="(if arm) -2 penalty (attribute?) to action requiring use of hands/arms "
                 "(if leg) base movement reduced to 5 feet per turn, -4 step penalty on movement actions"
    ),

    "Bleeder": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="hemophiliac (once bleeding don't stop easily)",
        numeric_effects=None,
        fx_notes="once cut take 1 wound damage until bleeding stopped, (hard level: int + medical expertise)"
    ),

    "Blind": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="<-... at least you can have a guide dog, but you have to take care of it",
        numeric_effects=serenity_bonus_modifier(stats=None, skills="See notes"),
        fx_notes="has difficulty moving in unfamiliar surroundings -4 skill penalty on any action that requires vision "
                 "-8 skill penalty on any ranged combat "
                 "(bonus) get 'Sharp senses' for touch and hearing at no cost"
    ),

    "Branded": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="you're a bad person and everyone knows it (bad reputation)",
        numeric_effects=None,
        fx_notes="(minor) -2 skill to social interactions when the story of your terrible misdeeds come into play "
                 "(major) penalty applies nearly all the time (you're famous!) "
                 "(exception) people that know you personally or know you got a raw deal don't apply"
    ),

    "Chip on the Shoulder": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="short fuse to violence",
        numeric_effects=None,
        fx_notes="ready to fight at slightest provocation "
                 "(minor) -2 skill to peaceable social actions with even a hint of tension "
                 "(major) Any time suffering wound damage, go completely berserk, "
                 "only focusing on that person who hurt you until someone else hurts you"
    ),

    "Credo": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="follow your own set of rules regardless of the situation",
        numeric_effects=None,
        fx_notes="(minor) pick a credo that will get you into minor trouble (e.g. never run from a fight) "
                 "(major) credo will put you in danger if situation arises (captiain goes down with ship)"
    ),

    "Combat Paralysis": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="freeze up in combat situations",
        numeric_effects=None,
        fx_notes="(minor) at combat start, unable to take action for d2 turns (can plot points off (1 point per turn) "
                 "(major) helpless for d4 turns (exception) may be able to lower value with another character's "
                 "'leadership' asset to inspire you to act sooner (may consume both character's turns as well)"
    ),

    "Coward": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="when fight breaks out, look for nearest exit",
        numeric_effects=None,
        fx_notes="suffer -2 skill penalty on combat actions which you are in danger and suffer -2 Willpower attribute "
                 "penalty on any action to resist fear, intimidation, torture, or other threats. "
                 "(exception) when backed into a corner may fight without penalty until exit appears"
    ),

    "Crude": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="one crude dude spittin lewd chewed food",
        numeric_effects=None,
        fx_notes="suffer -2 skill penalty on Influence based actions whenever refined social behavior is called for"
    ),

    "Dead Broke": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="never has money, when receiving money, spent immediately",
        numeric_effects=None,
        fx_notes="start out at 50% normal money. must spend remaining immediately on whatever you think you need "
                 "lose 50% of income the first day in a town/location/etc (how is up to the player and/or GM)"
    ),

    "Deadly Enemy": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="you have an enemy that is out to capture/kill you",
        numeric_effects=None,
        fx_notes="don't have to specify who; personal background may supply GM with ideas; "
                 "enemy may be powerful and dangerous, posing threat ever 3 to 5 adventures (at GM's discretion) "
                 "until buying off this complication... "
                 "even killing enemy may trigger friend/sibling/etc to take their place as the enemy."
    ),

    "Deaf": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="wha?",
        numeric_effects=None,
        fx_notes="Automaticall fail any alertness based action involving sound; "
                 "Immune to sonic attacts intended to disrupt hearing; "
                 "(bonus) understand sign language and receive +2 skill bonus to perception/read lips"
    ),

    "Dull Sense": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="one sense is fried",
        numeric_effects=None,
        fx_notes="pick one sense (smell, touch, sight, taste, hearing). "
                 "suffer -2 to alertness attribute for any action utilizing that sense; "
                 "This can be taken multiple times"
    ),

    "Easy Mark": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="guillible/succeptible to trickery",
        numeric_effects=None,
        fx_notes="believe what you're told; "
                 "suffer -4 mental attribute penalty when trying to distinguish if others telling the truth "
                 "(bonus) can get plot points for going along with beliveing other's lies"
    ),

    "Ego Signature": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="wet/sticky bandits (home alone) always leaving behind evidence/marking of what you've done",
        numeric_effects=None,
        fx_notes="Always leave evidence that at least indirectly leads back to you"
    ),

    "Filcher": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="Stealy McGee",
        numeric_effects=None,
        fx_notes="Anything that catches your eye, you will attempt to steal"
    ),

    "Forked Tongue": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="Will lie when it benefits the character, will lie when it doesn't",
        numeric_effects=None,
        fx_notes="anyone who knows you trusts you as much as they can throw you; "
                 "suffer -4 skill penalty to Influence based actions in such situations"
    ),

    "Greedy": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="get stupid if money is good enough",
        numeric_effects=None,
        fx_notes="take almost any opportunity to acquire money; Bendable ethics when money is involved, "
                 "will sell out friends, crew, family if the money is good enough"
    ),

    "Hero Worship": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="have a person (living or dead) you idolize whether they deserve it or not",
        numeric_effects=None,
        fx_notes="Emulate this idol in dress and speech and will go to great lengths to feel close to this person. "
                 "Suffer -2 skill penalty to Influence based actions when people around you aren't as "
                 "enthralled to this person as you are."
    ),

    "Hooked": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="Addicted to drug and must get fix on a regular basis",
        numeric_effects=None,
        fx_notes="(minor) addicted to something not immediately dangerous and/or have your addiction somewhat "
                 "under control; suffer -2 to all Attributes for one week or until you get your fix; "
                 "(major) abusing dangerous substance or non-functional "
                 "(strains relationships and/or chances of living) without your fix, suffer -4 to all Attributes "
                 "for two weeks until you get your fix. Cannot quit until you buy off this complication"
    ),

    "Leaky Brainpan": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="A couple of screws loose",
        numeric_effects=None,
        fx_notes="(minor) prone to occoasional delusions and random, nonsensical outbursts; "
                 "suffer - 2 skill penalty to Influence based social interactions; "
                 "(major) very weird and creepyfied; may perceive the world in a different view "
                 "(GM may detail scene differently for character); perform strange/dangerous actions randomly. "
                 "suffer -4 skill penalty to Influence based social interactions"
    ),

    "Lightweight": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="don't deal well to threats to your health",
        numeric_effects=None,
        fx_notes="suffer -2 Vitality penalty to attempts to resist effects of alcohol, diseases, "
                 "environmental hazards, poison, etc."
    ),

    "Little Person": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="not a tall person (3' to 4' tall)",
        numeric_effects=None,
        fx_notes="Base movement is 8 feet per turn, -2 skill penalty on movement actions "
                 "(bonus) opponents attacking you from more than 10 feet away suffer a +4 to difficulty"
    ),

    "Loyal": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="will do anything for those you are loyal to",
        numeric_effects=None,
        fx_notes="Pick a group that can count on your loyalty (or person/npc that is constantly in campaign). "
                 "You will do anything short of sacrificing your own life to help/protect them"
    ),

    "Memorable": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="people remember you (i.e. you're easily identified)",
        numeric_effects=None,
        fx_notes="Others gain +2 Alertness attribute when attempting to spot or recognize your likeness."
    ),

    "Mute": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="don't speak verbally",
        numeric_effects=None,
        fx_notes="Communicate only via sign language, writing, gestures. (Whenever this causes you "
                 "significant challenges, GM should reward you with plot points)"
    ),

    "Non-Fightin' Type": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="only willing to engage in violence under the most dire of circumstances",
        numeric_effects=None,
        fx_notes="When forced to fight, suffer -2 skill penalty to any combat actions."
    ),

    "Overconfident": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="think you're smarter, stronger, tougher than others (overconfident)",
        numeric_effects=None,
        fx_notes="you'll run into deadly altercations; fight when you're outnumbered; "
                 "bet all credits on single throw of dice; "
                 "risk attempting a dangerous actions even if you're not the least bit skilled at it"
    ),

    "Paralyzed": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="spinal cord injury, spend time in wheelchair",
        numeric_effects=None,
        fx_notes="w/o assistance, 2 ft/turn; in wheelchair, 5 ft/turn; -4 step penalty to movement actions "
                 "(with electric wheelchair can move normal) -4 step penalty when fighting hand to hand"
    ),

    "Phobia": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="object gives you the shivers",
        numeric_effects=None,
        fx_notes="Specify your phobia, object should be either: uncommon and extreme reaction or more common "
                 "(with less extreme reaction) suffer -2 Attribute penalty on all actions related to this object"
    ),

    "Portly": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="overweight to some degree",
        numeric_effects=None,
        fx_notes="(minor) somewhat overweight; suffer -2 Attribute penalty to all Athletics (except swimming) "
                 "and Influence based actions dealing with fitness/physical appearance. "
                 "(major) morbidly obese; suffer -4 attribute; base movement is 5 ft/turn; suffer -2 Skill penalty "
                 "for covert actions such as hiding and disguise"
    ),

    "Predjudice": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="can't stand a certain group of people",
        numeric_effects=None,
        fx_notes="pick a group of people (race, religion, region of space, side of war, etc) - "
                 "must be people with whom you could have business dealings; Avoid interacting with these people "
                 "whenever possible, if not possible won't be able to hide disdain for them, may go out of your "
                 "way to insult them. "
                 "Influence based social interactions with the object of your prejudice suffer -2 Skill penalty"
    ),

    "Sadistic": asset_complication_config(
        minor_major=SerenityTraitLevel.Major,
        description="love hurting people",
        numeric_effects=None,
        fx_notes="don't pass up chances to maim or torture those under your power (usually reserved for bad guys, "
                 "not big damn heroes)"
    ),

    "Scrawny": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="skin and bones",
        numeric_effects=None,
        fx_notes="Suffer -2 Strength attribute penalty to all Athletics based actions; "
                 "suffer -2 Skill penalty on influence based actions dealing with fitness and physical appearance"
    ),

    "Slow Learner": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="bad at learning certain things",
        numeric_effects=None,
        fx_notes="Choose one general skill, pay 2 additional points for any improvement to the skill or specialties; "
                 "suffer -2 penalty whenever trying to use said Skill"
    ),

    "Soft": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="sensitive/squishy when it comes to pain",
        numeric_effects=None,
        fx_notes="Take an additional 1 stun damage every time you take damage at all; must succeed on AVERAGE "
                 "Willpower + Discipline to keep from weeping and wailing each time you take wound damage."
    ),

    "Stingy": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="mr thrifty",
        numeric_effects=None,
        fx_notes="don't part with money you don't have to; buy off brand merch, haggle down shopkeepers, "
                 "only friends would be able to get a loan (with interest)"
    ),

    "Straight Shooter": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="extremely honest (to a fault)",
        numeric_effects=None,
        fx_notes="speak the truth without regard to other's feelings or circumstances; might consider "
                 "lying in emergencies, but suffer -2 Skill penalty to Influence based actions as your "
                 "lie is written all over your face"
    ),

    "Superstitious": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="don't break mirrors, believe in omens, treat everything as luck based.",
        numeric_effects=None,
        fx_notes="wide set of superstitious beliefs that affect everyday behavior (may become "
                 "self-fufilling prophecies.) Whenever you receive an omen of bad luck you receive a -2 penalty "
                 "to all of your Attributes for a set of actions determined by the GM. (bonus) if you receive an"
                 " omen of good luck GM will determine a group of actions to receive a +2 Attribute bonus"
    ),

    "Things Don't Go Smooth": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="anti-lucky",
        numeric_effects=None,
        fx_notes="(minor) Once per session, GM can force you to re-roll an action & take the lower of the two results."
                 " (major) Twice"
    ),

    "Traumatic Flashes": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="have reoccurring unplesant flashbacks / visions / dreams",
        numeric_effects=None,
        fx_notes="(minor) Once per session, the GM will cause you to suffer a traumatic flash - leaves you incoherent, "
                 "shaking, screaming, incapable of actions for d2 turns - suffer -2 Attribute penalty on all "
                 "actions for 10min following the flash "
                 "(major) Twice"
    ),

    "Twitchy": asset_complication_config(
        minor_major=SerenityTraitLevel.Minor,
        description="paranoid",
        numeric_effects=None,
        fx_notes="everyone is whispering about you, don't believe people that state they're on your side. "
                 "Convinced someone is watching you all the time; suffer -2 Skill to all Influence based actions "
                 "in social situations"
    ),

    "Ugly as Sin": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="whether from genetics or life events, you're relatively hideous",
        numeric_effects=None,
        fx_notes="(minor) unattractive, suffer -2 Skill penalty to all actions keyed to appearance such as seduction, "
                 "negotiation, and persuasion "
                 "(major) ugly to the bone, all plot points spent on actions listed above cause 2x the normal amount"
    ),

    "Weak Stomach": asset_complication_config(
        minor_major=SerenityTraitLevel.Both,
        description="get woozy from the oozy (blood)",
        numeric_effects=None,
        fx_notes="(minor) can't stand to be in the presense of blood, entrails, or dead bodies; "
                 "suffer -2 to all Attributes until either the source of your discomfort is removed or until "
                 "you leave on your own. "
                 "(major) have to make AVERAGE VIT + WILL for each five minute interval you are exposed to gory scenes "
                 "to avoid falling unconsious for 2d4 minutes"
    ),

}