# This file contains a list of spells that have special
# methods of damaging targets, a list of spells that are
# not to be considered in efficiency calculations,
# and functions that deal with the special condition
# spells
from sm import AD,AP,CDR

#############
# FUNCTIONS #
#############

# All constants were taken from their max level
# Cyclone
def sm_sp1(values):
	damage = 800 + values[AD]*1.1 # base + 1.1*AD
	cd = 94 # 4s cast time plus 90s CD
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Infinite Duress
def sm_sp2(values):
	damage = 420 + values[AD]*0.4 # base + 0.4*AD
	cd = 71.8 # 1.8s cast time plus 70s CD
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Tremors
def sm_sp3(values):
	# maximum damage + max 240%ap
	damage = 1560 + values[AP]*2.4
	# 60s CD
	cd = 60
	dps = damge / (cd - (cd * (values[CDR]/100)))
	return dps

# Phosphorus Bomb
# For some reason, the data from the API did not include
# the .5 AD multiplier for the spell's damage
def sm_sp4(values):
	damage = 280 + values[AD]*0.5 + values[AP]*0.5
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Valkyrie
def sm_sp5(values):
	# Damage every .5s for 2.5s
	damage = (180 + values[AP]*0.4) * 5
	cd = 14
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Gatling Gun
def sm_sp6(values):
	# Damage every second for 4s
	damage = (68 + values[AD]*0.4) * 4
	cd = 16
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Missile Barrage
def sm_sp7(values):
	# Damage per normal rocket
	damage = 260 + values[AD]*0.4 + values[AP]*0.3
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Flash Frost
def sm_sp8(values):
	# Damage for the ability passing through
	# plus damage is does on explosion
	damage = (180 + values[AP]*0.5) * 2
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Glacial Storm
def sm_sp8(values):
	# spell can be infinitely channeled
	# so just give dps
	dps = 160 + values[AP]*0.25
	return dps

# Double Up
def sm_sp10(values):
	# Only have 1 target
	dps = 80 + values[AD]*0.85 + values[AP]*0.35
	cd = 3
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Bullet Time
def sm_sp11(values):
	# damage per bullet * 8 bullets
	damage = (125 + values[AP]*0.2) * 8
	cd = 100
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Static Field
def sm_sp12(values):
	# Damage on activation
	damage = 500 + values[AP]
	cd = 30
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Eye of Destruction
def sm_sp13(values):
	# Damage on direct hit
	damage = 270 + values[AP]*0.91
	cd = 10
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Rite of the Arcane
def sm_sp14(values):
	# Maximum damage to 1 target
	damage = 900 + values[AP]*1.29
	cd = 100
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Boomerang Blade
def sm_sp15(values):
	# Damage on 1st hit and 2nd hit
	damage = (105 + values[AD]*1.1) + ((105 + values[AD]*1.1) * .15)
	cd = 9
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Broken Wings
def sm_sp16(values):
	# calc damage for each jump
	damage = (90 + values[AD]*0.6) * 3
	cd = 13
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Blade of the Exile
def sm_sp17(values):
	# Damage of Wind Slash
	damage = 160 + values[AD]*0.6
	cd = 50
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Cannon Barrage
def sm_sp18(values):
	# damage per shot * 7s
	damage = (165 + values[AP]*0.2) * 7
	cd = 95
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Devastating Blow
def sm_sp19(values):
	# Disregarding bonus damage, enemy hp unknown
	damage = 100 + values[AP]*0.6 + values[AD]
	cd = 4
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Heroic Charge
def sm_sp20(values):
	# No assuming we collide with terrain
	damage = 150 + values[AP]*0.4
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Defile
def sm_sp21(values):
	# Needs special case since CD is 0
	# Spell can be constantly channeled, so dmg is dps
	dps = 110 + values[AP]*0.2
	return dps

# Lightning Field / Hyper Charge
def sm_sp22(values):
	# Dual spell, vars not detected properly
	# Total field damage
	damage = 380 + values[AP]*0.25
	cd = 10
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Absolute Zero
def sm_sp23(values):
	# channeled fully, cd time dependent on channel length
	damage = 1000 + values[AP]*2.5
	# 90s CD + 3s channel time
	cd = 93
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Chomp
def sm_sp24(values):
	# ratio scales with level
	damage = 100 + values[AD]*1.2
	cd = 4
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Buckshot
def sm_sp25(values):
	# Target can get hit mult. times
	# Use max damage values for dps
	damage = 364.5 + values[AD]*1.5
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Tormented Soil
def sm_sp26(values):
	# Deals damage over time
	# Damage per second * length = total damage
	damage = (80 + values[AP]*0.22) * 5
	cd = 10
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Soul Shackles
def sm_sp27(values):
	# Has 2 damage periods
	damage = (300 + values[AP]*0.7) * 2
	cd = 100
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Boomerang Throw / Boulder Toss
def sm_sp28(values):
	# dual spell
	# Treating as Boulder Toss for higher #'s
	damage = 170 + values[AD]*1.2
	cd = 10
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Hyper / Wallop
def sm_sp29(values):
	# dual Spell
	# Treat as Wallop, hyper has not activated damage
	damage = 105 + values[AD]
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

	
SPECIAL_SPELLS = {  
	"Cyclone": sm_sp1,
	"Infinite Duress": sm_sp2,
	"Tremors": sm_sp3,
	"Phosphorus Bomb": sm_sp4,
	"Valkyrie": sm_sp5,
	"Gatling Gun": sm_sp6,
	"Missile Barrage": sm_sp7,
	"Flash Frost": sm_sp8,
	"Glacial Storm": sm_sp9,
	"Double Up": sm_sp10,
	"Bullet Time": sm_sp11,
	"Static Field": sm_sp12,
	"Eye of Destruction": sm_sp13,
	"Rite of the Arcane": sm_sp14,
	"Boomerang Blade": sm_sp15,
	"Broken Wings": sm_sp16,
	"Blade of the Exile": sm_sp17,
	"Cannon Barrage": sm_sp18,
	"Devastating Blow": sm_sp19,
	"Heroic Charge": sm_sp20,
	"Defile": sm_sp21,
	"Lightning Field / Hyper Charge": sm_sp22,
	"Absolute Zero": sm_sp23,
	"Chomp": sm_sp24,
	"Buckshot": sm_sp25,
	"Tormented Soil": sm_sp26
	"Soul Shackles": sm_sp27,
	"Boomerang Throw / Boulder Toss": sm_sp28
	"Hyper / Wallop": sm_sp29,
	Hop / Crunch
	GNAR!
	Light Binding
	Lucent Singularity
	Final Spark
	Twin Bite
	Burnout
	Flame Breath
	Dragon's Descent
	Cull the Meek
	Slice and Dice
	Dominus
	Lunge
	Blade Waltz
	Zap!
	Flame Chompers!
	Super Mega Death Rocket!
	Urchin Strike
	Playful / Trickster
	Chum the Waters
	Null Sphere
	Force Pulse
	Riftwalk
	Hymn of Valor
	Crescendo
	Bladesurge
	Equilibrium Strike
	Transcendent Blades
	Siphon Power
	Death Ray
	Chaos Storm
	Noxious Blast
	Miasma
	Twin Fang
	Petrifying Gaze
	Arcane Smash
	Twisted Advance
	Sapling Toss
	Vengeful Maelstrom
	Death Sentence
	Flay
	The Box
	Reckoning
	Rampage
	Spirit of Dread
	Devastating Charge
	Onslaught of Shadows
	Taste Their Fear
	Void Spike
	Leap
	Undertow
	Reckless Swing
	Bouncing Bomb
	Satchel Charge
	Hexplosive Minefield
	Mega Inferno Bomb
	Dark Sphere
	Force of Will
	Scatter the Weak
	Unleashed Power
	Infected Cleaver
	Burning Agony
	Inner Flame
	Focused Resolve
	Mantra
	Disintegrate
	Incinerate
	Summon: Tibbers
	Mark of the Assassin
	Crescent Slash
	Shadow Dance
	Shield of Daybreak
	Eclipse
	Zenith Blade
	Solar Flare
	Steel Tempest
	Sweeping Blade
	Last Breath
	Thundering Shuriken
	Electrical Surge
	Lightning Rush
	Slicing Maelstrom
	Savagery
	Battle Roar
	Bola Strike
	Overload
	Spell Flux
	Vorpal Blade
	Stretching Strike
	Unstable Matter
	Elastic Slingshot
	Let's Bounce!
	Spear Shot
	Aegis of Zeonia
	Heartseeker Strike
	Grand Skyfall
	Decrepify
	Nevermove
	Torment
	Ravenous Flock
	Decimating Smash
	Roar of the Slayer
	Unstoppable Onslaught
	Condemn
	Siphoning Strike
	Spirit Fire
	Fury of the Sands
	Wild Cards
	Pick A Card
	Stacked Deck
	Feral Scream
	Feast
	Tiger Stance
	Phoenix Stance
	Piercing Light
	Ardent Blaze
	The Culling
	Rolling Thunder
	Majestic Roar
	Thunder Claws
	Piltover Peacemaker
	Yordle Snap Trap
	90 Caliber Net
	Ace in the Hole
	Decimate
	Crippling Strike
	Apprehend
	Noxian Guillotine
	Duskbringer
	Unspeakable Horror
	Paranoia
	Time Bomb
	Conquering Sands
	Arise!
	Shifting Sands
	Emperor's Divide
	Flamespitter
	Scrap Shield
	Electro Harpoon
	The Equalizer
	Crystal Slash
	Fracture
	Impale
	Blinding Dart
	Noxious Trap
	Acid Hunter
	Noxian Corrosive Charge
	Bandage Toss
	Despair
	Tantrum
	Curse of the Sad Mummy
	Resolute Smite
	Righteous Gust
	H-28G Evolution Turret
	Hextech Micro-Rockets
	CH-2 Electron Storm Grenade
	UPGRADE!!!
	Volley
	Enchanted Crystal Arrow
	Plasma Fission
	Void Rift
	Tectonic Disruption
	Life Form Disintegration Ray
	Poison Trail
	Fling
	Piercing Arrow
	Hail of Arrows
	Chain of Corruption
	Decisive Strike
	Judgment
	Demacian Justice
	Crescent Strike
	Pale Cascade
	Lunar Rush
	Alpha Strike
	Neurotoxin / Venomous Bite
	Volatile Spiderling / Skittering Frenzy
	Venomous Bite / Neurotoxin
	Skittering Frenzy / Volatile Spiderling
	Pulverize
	Headbutt
	Bouncing Blades
	Sinister Steel
	Shunpo
	Death Lotus
	Mace of Spades
	Creeping Death
	Siphon of Destruction
	Children of the Grave
	Caustic Spittle
	Void Ooze
	Living Artillery
	Dark Flight
	Blades of Torment
	Massacre
	Spinning Axe
	Stand Aside
	Whirling Death
	Drain
	Dark Wind
	Crowstorm
	Noxian Diplomacy
	Rake
	Shadow Assault
	Three Talon Strike
	Audacious Charge
	Crescent Sweep
	Sonic Wave / Resonating Strike
	Tempest / Cripple
	Dragon's Rage
	Shatter
	Dazzle
	Radiance
	Call of the Void
	Null Zone
	Malefic Visions
	Nether Grasp
	Ice Shard
	Ring of Frost
	Glacial Path
	Frozen Tomb
	Rocket Jump
	Explosive Shot
	Buster Shot
	Transfusion
	Sanguine Pool
	Tides of Blood
	Hemoplague
	Dragon Strike
	Demacian Standard
	Cataclysm
	Aqua Prison
	Ebb and Flow
	Tidal Wave
	Starcall
	Equinox
	Baleful Strike
	Dark Matter
	Primordial Burst
	Howling Gale
	Zephyr
	Dredge Line
	Riptide
	Depth Charge
	Hate Spike
	Ravage
	Agony's Embrace
	Barrel Roll
	Drunken Rage
	Body Slam
	Explosive Cask
	Razor Shuriken
	Shadow Slash
	Death Mark
	Vault Breaker
	Excessive Force
	Assault and Battery
	Glitterlance
	Help, Pix!
	Orb of Deception
	Fox-Fire
	Charm
	Spirit Rush
	Blinding Assault
	Vault
	Sigil of Malice
	Distortion
	Ethereal Chains
	Mimic
	Mystic Shot
	Essence Flux
	Arcane Shift
	Trueshot Barrage
}

DISREGARDED_SPELLS = [ 
	"Acceleration Gate",
	"Adrenaline Rush",
	"Aegis Protection",
	"Ambush",
	"Arcane Mastery",
	"Aria of Perseverance",
	"Aspect Of The Cougar",
	"Aspect of the Serpent",
	"Astral Blessing",
	"Astral Infusion",
	"Backstab",
	"Battle Cry",
	"Battle Fury",
	"Bear Stance",
	"Berserker Rage",
	"Bio-Arcane Barrage",
	"Black Shield",
	"Blast Shield",
	"Blighted Quiver",
	"Blood Boil",
	"Blood Price",
	"Blood Rush",
	"Blood Scent",
	"Blood Thirst",
	"Blood Thirst / Blood Price",
	"Blood Well",
	"Bloodlust",
	"Brutal Strikes",
	"Bulwark",
	"Burst of Speed",
	"Camouflage",
	"Cannibalism",
	"Carnivore",
	"Carrion Renewal",
	"Cell Division",
	"Certain Death",
	"Challenge",
	"Chosen of the Storm",
	"Chronoshift",
	"Clockwork Windup",
	"Cocoon",
	"Cocoon / Rappel",
	"Command: Protect",
	"Concussive Blows",
	"Contaminate",
	"Contempt for the Weak",
	"Courage",
	"Crimson Pact",
	"Cripple",
	"Crystalline Exoskeleton",
	"Crystallize",
	"Crystallizing Sting",
	"Cursed Touch",
	"Cutthroat",
	"Damnation",
	"Dark Frenzy",
	"Dark Passage",
	"Deadly Cadence",
	"Deadly Venom",
	"Death Defied",
	"Death Surge",
	"Death's Caress",
	"Cryptic Gaze",
	"Deceive",
	"Decompose",
	"Defensive Ball Curl",
	"Denting Blows",
	"Desperate Power",
	"Destiny",
	"Diplomatic Immunity",
	"Divine Blessing",
	"Double Strike",
	"Dragonborn",
	"Draw a Bead",
	"Dread",
	"Duelist",
	"Empowered Bulwark",
	"Enrage",
	"Equilibrium",
	"Essence Theft",
	"Eternal Thirst",
	"Event Horizon",
	"Evolving Technology",
	"Eye Of The Storm",
	"Feel No Pain",
	"Feint",
	"Final Hour",
	"Fishbones, the Rocket Launcher",
	"Flail of the Northern Winds",
	"Fleet of Foot",
	"Flurry",
	"Focus",
	"Frenzy",
	"Frost Armor",
	"Frost Shot",
	"Frozen Domain",
	"Fury of the Dragonborn",
	"Gathering Fire",
	"Gemcraft",
	"Get Excited!",
	"Glorious Evolution",
	"Glory in Death",
	"Golden Aegis",
	"Grandmaster's Might",
	"Granite Shield",
	"Gravity Field",
	"Grog Soaked Blade",
	"Happy Hour",
	"Harrier",
	"Hawkshot",
	"Headshot",
	"Heightened Learning",
	"Heightened Senses",
	"Hemorrhage",
	"Hextech Capacitor",
	"Hextech Shrapnel Shells",
	"Highlander",
	"Hiten Style",
	"Holy Fervor",
	"Human Form",
	"Hunters Call",
	"Hyper",
	"Hyper Charge",
	"Hyper-Kinetic Position Reverser",
	"Icathian Surprise",
	"Iceborn",
	"Idol of Durand",
	"Illumination",
	"Imbue",
	"Impure Shots",
	"Insanity Potion",
	"Inspire",
	"Intervention",
	"Ionian Fervor",
	"Iron Man",
	"Iron Will",
	"Junkyard Titan",
	"Ki Strike",
	"King's Tribute",
	"League of Draven",
	"Lightslinger",
	"Living Vengeance",
	"Living Shadow",
	"Loaded Dice",
	"Mana Barrier",
	"Mana Surge",
	"Mark of the Storm",
	"Martial Cadence",
	"Masochism",
	"Meditate",
	"Mega Adhesive",
	"Mercury Cannon",
	"Mercury Cannon / Mercury Hammer",
	"Mercury Hammer",
	"Mercy",
	"Mirror Image",
	"Mocking Shout",
	"Molten Shield",
	"Monkey's Agility",
	"Monsoon",
	"Moonfall",
	"Moonsilver Blade",
	"Move Quick",
	"Nether Blade",
	"Night Hunter",
	"Numble Fighter",
	"Omen of Death",
	"Omen of War",
	"On The Hunt",
	"Organic Deconstruction",
	"Overdrive",
	"Paragon of Demacia",
	"Permafrost",
	"Perseverance",
	"Pillar of Ice",
	"Pix, Faerie Companion",
	"Pow-Pow, the Minigun",
	"Power Chord",
	"Primal Surge",
	"Prismatic Barrier",
	"Prowl",
	"Puncturing Taunt",
	"Pyromania",
	"Quickdraw",
	"Rage Gene",
	"Ragnarok",
	"Raise Morale",
	"Rampant Growth",
	"Rapid Fire",
	"Rappel",
	"Rat-Ta-Tat-Tat",
	"Rebirth",
	"Reign of Anger",
	"Relentless Assault",
	"Relentless Pursuit",
	"Remove Scurvy",
	"Rewind",
	"Ricochet",
	"Righteous Fury",
	"Riposte",
	"Rise of the Thorns",
	"Rising Spell Force",
	"Rune Prison",
	"Runic Blade",
	"Runic Skin",
	"Rupture",
	"Ruthless Predator",
	"Sadism",
	"Safeguard",
	"Safeguard / Iron Will",
	"Salvation",
	"Sap Magic",
	"Scrap Sheild",
	"Seastone Trident",
	"Shadow Dash",
	"Shadow Walk",
	"Short Fuse",
	"Shroud of Darkness",
	"Shurima's Legacy",
	"Silver Bolts",
	"Skittering Frenzy",
	"Song of Celerity",
	"Soul Eater",
	"Soul Furnace",
	"Soul Siphon",
	"Spell Shield",
	"Spider Form",
	"Spider Form / Human Form",
	"Spider Swarm",
	"Spiked Shell",
	"Stand Behind Me",
	"Stand United",
	"Stone Skin",
	"Strut",
	"Subjugate",
	"Summon Voidling",
	"Surging Tides",
	"Switcheroo!",
	"Tag Team",
	"Tailwind",
	"Techmaturgical Repair Bots",
	"Terrify",
	"Terror Capacitor",
	"Thrill of the Hunt",
	"Tidecaller's Blessing",
	"Toxic Shot",
	"Time Warp",
	"Titan's Wrath",
	"Trample",
	"Transcendent",
	"Triumphant Roar",
	"True Grit",
	"Tumble",
	"Turtle Stance",
	"Twilight Shroud",
	"Twin Disciplines",
	"Umbra Blades",
	"Unbreakable",
	"Rappel / Cocoon",
	"Unbreakable Will",
	"Unbreakable",
	"Undying Rage",
	"Unholy Covenant",
	"Unseen Predator",
	"Unseen Threat",
	"Valiant Fighter",
	"Valor",
	"Venom Cask",
	"Vicious Strikes",
	"Visionary",
	"Void Assault",
	"Void Stone",
	"Voracity",
	"Vorpal Spikes",
	"Wall of Pain",
	"Warpath",
	"Whimsy",
	"Wicked Blades",
	"Wild Growth",
	"Wind Wall",
	"Wish",
	"Wither",
	"Wuju Style",
	"Zaun-Touched Bolt Augmenter",
	# Added since dmg is based off of % Enemy HP
	"Thundering Blow / Acceleration Gate",
]