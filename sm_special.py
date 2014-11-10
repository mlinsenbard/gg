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

# Burnout
def sm_sp30(values):
	# does damage over time
	# DPS * seconds active
	damage = (80 + values[AD]*0.2) * 3
	cd = 12
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Cull The Meek
def sm_sp31(values):
	# Does altered damage based on fury; disregarding fury
	damage = 180 + values[AD]*0.8
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Slice and Dice
def sm_sp32(values):
	# Does altered damage based on fury; disregarding fury
	# 2-Step Spell, damage = Slice + Dice
	damage = (150 + values[AD]*0.9) * 2
	cd = 14
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Dominus
def sm_sp33(values):
	# Does damage over time
	# Damage = Damage per sec * time active
	damage = (120 + values[AP]*0.1) * 15
	cd = 120
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Blade Waltz
def sm_sp34(values):
	# Has maximum damage cap
	damage = 1000 + values[AD]*2.4
	cd = 110
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Urchin Strike
def sm_sp35(values):
	# Does additional 100% AD dmg not listed in vars
	damage = 130 + values[AP]*0.6 + values[AD]
	cd = 6
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Riftwalk
def sm_sp36(values):
	# Will only be used once every CD period (20s)
	# its not really feasible to calcuate the dps otherwise
	damage = 120
	cd = 20
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Transcendent Blades
def sm_sp37(values):
	# Activated 4 times
	damage = (160 + values[AP]*0.5) * 4
	cd = 50
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Chaos Storm
def sm_sp38(values):
	# Does inital dmg then dmg over time
	# damage = init + (dps * time active)
	damage = (350 + values[AP]*0.55) + ((90 + values[AP]*0.55) * 7)
	cd = 100
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Miasma
def sm_sp39(values):
	# damage given in dps
	# assume target stays in miasma full 7s
	# target is poisoned for total of 9s
	# If CD is less than 9, just give dps
	if (cd - (cd * (values[CDR]/100))) < 9:
		dps = 30 + values[AP]*0.1
	else:
		damage = (30 + values[AP]*0.1) * 9
		cd = 10
		dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Twin Fang
def sm_sp40(values):
	# AP Scaling changes with level
	damage = 155 * values[AP]*0.55
	cd = 5
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Taste Their Fear
def sm_sp41(values):
	# Single targe damage increased
	damage = 221 + values[AD]*1.56
	cd = 3
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Sapling Toss
def sm_sp42(values):
	# Spell has 2 damage periods
	# Damage = landing + exlposion
	damage = (120 + values[AP]*0.4) + (240 + values[AP]*0.6)
	cd = 12
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Vengeful Maelstrom
def sm_sp43(values):
	# Assume no stored bonus damage is done
	damage = 200 + values[AP]*0.5
	cd = 20
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Flay
def sm_sp44(values):
	# Only consider active damage
	damage = 185 + values[AP]*0.4
	cd = 9
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Force of Will
def sm_sp45(values):
	# Cooldown listed as 0 since ability has 2 casts
	damage = 240 + values[AP]*0.7
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Unleashed Power
def sm_sp46(values):
	# Use minimum damage in calculation.
	# All calculations assume no previous spell was cast
	damage = 540 + values[AP]*0.6
	cd = 80
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Burning Agony
def sm_sp47(values):
	# Since spell can be channeled indefinitely
	# damage/sec = dps
	dps = 95 + values[AP]*0.2
	return dps

# Mantra
def sm_sp48(values):
	# Spell modifier. Calculate dps of each modified spell. Return best
	#Inner Flame total dmg
	inner = (260 + values[AP]*0.6) + (175 + values[AP]*0.3) + (350 + values[AP]*0.6)
	# Focused Resolve total dmg
	focused = (260 + values[AP]*0.6) + (300 + values[AP]*0.6)
	# Inspire
	inspire = 300 + values[AP]*0.6
	# Best dps is max damaging mantra spell
	damage = max(inner,focused,inspire)
	cooldown = 36
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Summon: Tibbers
def sm_sp49(values):
	# damage = cast damage + Damage over time
	damage = (425 + values[AP]*0.8) + ((35 + values[AP]*0.2) * 45)
	cd = 80
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Mark of the Assassin
def sm_sp50(values):
	# Only consider casting damage, not activation damage
	damage = 115 + values[AP]*0.4
	cd = 4
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Shadow Dance
def sm_sp51(values):
	# Use 15s generation of 'jumps' for dps cd
	damage = 250 + values[AP]*0.5
	cd = 15
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Sweeping Blade
def sm_sp52(values):
	# Use mark length as CD
	damage = 150 + values[AP]*0.6
	cd = 6
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Last Breath
def sm_sp53(values):
	# API Data doesn't have CD in expected place
	damage = 400 + values[AD]*1.5
	cd = 30
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Slicing Maelstrom
def sm_sp54(values):
	# Hits maximum of 3 times
	damage = (210 + values[AP]*0.4) * 3
	cd = 120
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# None of Rengar's spells have CD's under
# the 'cooldown' key
# Savagery
def sm_sp55(values):
	damage = 150 + values[AD]*1.2
	cd = 4
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Battle Roar
def sm_sp56(values):
	damage = 170 + values[AP]*0.8
	cd = 12
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Bola Strike
def sm_sp57(values):
	damage = 250 + values[AD]*0.7
	cd = 10
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Let's Bounce
def sm_sp58(values):
	# 4 bounces, last 3 do .5 times damage
	damage = (280 + values[AP]*0.4) + ((280 + values[AP]*0.4) * .5) * 3
	cd = 100
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Heartseeker Strike
def sm_sp59(values):
	# 3 strikes, 2x damage to champs = base * 6
	# assume target is champ for max damage
	damage = (53 + values[AD]*0.6) * 6
	cd = 6
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Decrepify
def sm_sp60(values):
	# DOT. Damage = total dot = dps * time active
	damage = (85 + values[AP]*0.3) * 3
	cd = 8
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Ravenous Flock
def sm_sp61(values):
	# Inifinitely Channeled. DPS = Damage per sec
	# Only 1 raven per enemy
	dps = 90 + values[20]
	return dps

# Spirit Fire
def sm_sp62(values):
	# Initial damage + DPS
	damage = (215 + values[AP]*0.6) + ((43 + values[AP]*.12)*5)
	cd = 12
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Fury of the Sands
def sm_sp63(values):
	# aoe damage. Use max damage per sec. value
	# damage = dps * time active
	damage = 240 * 15
	cd = 120
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Feast
def sm_sp64(values):
	# Target is a champion. Using those values
	damage = 650 + values[AP]*0.7
	cd = 60
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Phoenix Stance
def sm_sp65(values):
	# activated pulse damage
	damage = (55 + values[AP]*0.25) * 5
	cd = 6
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Piercing Light
def sm_sp66(values):
	# data parsing failed for this api entry
	# using base dmg + 120% AD
	damage = 200 + values[AD]*1.2
	cd = 5
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# The Culling
def sm_sp67(values):
	# with no attack speed mods, 15 shots are fired
	# damage = dmg per shot * 15
	damage = (60 + values[AP]*.1 + values[AD]*0.25) * 15
	cd = 90
	dps = damage / (cd - (cd * (values[CDR]/100)))
	return dps

# Decimate 
def sm_sp68(values):
	# Using maximum possible damage
	# damage = damage * 1.5 (assume target is hit by blade)
	damage = (210 + values[AD]*0.7) * 1.5
	cd = 5
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
	"Burnout": sm_sp30,
	"Cull the Meek": sm_sp31,
	"Slice and Dice": sm_sp32,
	"Dominus": sm_sp33,
	"Blade Waltz": sm_sp34,
	"Urchin Strike": sm_sp35,
	"Riftwalk": sm_sp36,
	"Transcendent Blades": sm_sp37,
	"Chaos Storm": sm_sp38,
	"Miasma": sm_sp39,
	"Twin Fang": sm_sp40,
	"Taste Their Fear": sm_sp41,
	"Sapling Toss": sm_sp42,
	"Vengeful Maelstrom": sm_sp43,
	"Flay": sm_sp44,
	"Force of Will": sm_sp45,
	"Unleashed Power": sm_sp46,
	"Burning Agony": sm_sp47,
	"Mantra": sm_sp48,
	"Summon: Tibbers": sm_sp49,
	"Mark of the Assassin": sm_sp50,
	"Shadow Dance": sm_sp51,
	"Sweeping Blade": sm_sp52,
	"Last Breath": sm_sp53,
	"Slicing Maelstrom": sm_sp54,
	"Savagery": sm_sp55,
	"Battle Roar": sm_sp56,
	"Bola Strike": sm_sp57,
	"Let's Bounce!": sm_sp58,
	"Heartseeker Strike": sm_sp59,
	"Decrepify": sm_sp60,
	"Ravenous Flock": sm_sp61,
	"Spirit Fire": sm_sp62,
	"Fury of the Sands": sm_sp63,
	"Feast": sm_sp64,
	"Phoenix Stance": sm_sp65,
	"Piercing Light": sm_sp66,
	"The Culling": sm_sp67,
	"Decimate": sm_sp68, 
	"Apprehend"
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
	"Apprehend",
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
	"Consume",
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
	"Twin Bite",
	"Dragon's Descent",
	# Added since dmg is based off of % Enemy hp
	"Twisted Advance",
	# DPS is based of attack speed; an unknown variable
	"Stacked Deck",
	"Tiger Stance",
	"Rolling Thunder",
	"Thunder Claws",
	"Crippling Strike",
]