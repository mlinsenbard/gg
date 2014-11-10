from urllib2 import urlopen
import ast
import json
from sm_special import SPECIAL_SPELLS, DISREGARDED_SPELLS

###########
# GLOBALS #
###########

# User input constants
AFFIRMATIVE = ['y','yes','Yes','Y','sure','ok']
NEGATIVE = ['n','no','No','N','Nope','nope']

# Riot Games API scraping
# Obtains all Champion data for use in functions
result = urlopen(
	"https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?locale=en_US&champData=spells&api_key=84a61ad2-30ec-4067-b06a-2c6cea9fa344")
championData = json.loads(result.read())
allChamps = championData['data']

champSpellDict = {}
for k,v in allChamps.iteritems():
	spellDict = {}
	for s in v['spells']:
		if s['name'] not in DISREGARDED_SPELLS:
			print s['name']