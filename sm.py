from urllib2 import urlopen
import json

###########
# GLOBALS #
###########

# Used to access 3-tuple variables by name
AD = 0
AP = 1
CDR = 2

# Obtains all Champion data for use in functions
# API Key would normally be kept secret but is hard-coded to ensure this script works on any machine
result = urlopen(
	"https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?locale=en_US&champData=spells&api_key=84a61ad2-30ec-4067-b06a-2c6cea9fa344")
ALL_CHAMPS = json.loads(result.read())['data']

#############
# FUNCTIONS #
#############

#############################
# mostEfficient
#
# Input: 3-Tuple (AD,AP,CDR)
# Output: Tuple (spellDict, DPS)
# 
# Calculates the spell with
# highest DPS given AD/AP/CDR
#############################
def mostEfficient(values):
	bestSpell = {}
	bestSpellDPS = 0

	for k,v in ALL_CHAMPS.iteritems():
		for s in v['spells']:
			try:
				for i,l in enumerate(s['leveltip']['label']):
					if 'Damage' in l:

						print 'Found a damaging spell: ' + s['name']
						maxLevel = int(s['maxrank'])
						print 'Level:'
						print maxLevel
						# i is our index for leveltip/effect
						# Get the effect index to get damage for our spell
						for c in s['leveltip']['effect'][i]:
							if c.isnumeric():
								damageIndex = int(c)
								break
						print 'Damage Index:'
						print damageIndex
						# Using the maxlevel var and index, get our base damage value for the spell
						damageVal = float(s['effect'][damageIndex][maxLevel-1])
						print "Damage:"
						print damageVal
						cooldown = int(s['cooldown'][maxLevel-1])
						print "Cooldown:"
						print cooldown

						apRatio = 0
						adRatio = 0
						try:
							for var in s['vars']:
								if 'attackdamage' in var['link'] and adRatio == 0:
									adRatio = float(var['coeff'][0])
								elif 'spelldamage' in var['link'] and apRatio == 0:
									apRatio = float(var['coeff'][0])
								elif 'bonusattackdamage' in var['link'] and adRatio == 0:
									adRatio = float(var['coeff'][0])
						except:
							# Spell has no coeffs
							pass

						print "AD Ratio:"
						print adRatio
						print "AP Ratio"
						print apRatio
						# We have our damage, cooldown, and ratios. Time to calculate dps
						totalDamage = damageVal + (apRatio * values[AP]) + (adRatio * values[AD])
						print "Total Damage:"
						print totalDamage
						dps = totalDamage/(cooldown-(cooldown*(values[CDR]/100)))
						print "DPS:"
						print dps
						if dps > bestSpellDPS:
							bestSpellDPS = dps
							bestSpell = s
						break

			except Exception,e:
				print e
	return (bestSpell, bestSpellDPS)









