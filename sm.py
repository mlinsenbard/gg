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
	champSpellDict = {}

	for k,v in ALL_CHAMPS.iteritems():
		spellDict = {}
		for s in v['spells']:
			try:
				for l in s['leveltip']['label']:
					if 'Damage' in l:
						spellDict[s["name"]] = s
			except Exception:
				pass
		champSpellDict[k] = spellDict

	# TESTING
	for k,v in champSpellDict.iteritems():
		print k
		for s,d in v.iteritems():
			print s
			print [x for x in d['leveltip']['label'] if 'Damage' in x]
			print d['maxrank']
			print d['leveltip']['effect']
			print d['effect']
			print d['cooldown']
		print ''
	return 0









