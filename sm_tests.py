from urllib2 import urlopen
import ast
import json

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

for k,v in allChamps.iteritems():
	print k
	for s in v['spells']:
		print "Name" 
		print s['name']
		print "Cooldown" 
		print s['cooldown']
		try:
			print 'Vars' 
			print s['vars']
		except Exception:
			print "Spell has no Variables"
		try:
			print "Level Info" 
			print s['leveltip']
		except Exception:
			print "Spell has no effects"
		try:
			print "Effects per level" 
			print s['effectBurn']
		except Exception:
			print "Spell has no effect vals"
		print ''