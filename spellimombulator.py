from urllib2 import urlopen
import ast

###########
# GLOBALS #
###########

# User input constants
AFFIRMATIVE = ['y','yes','Yes','Y','sure','ok']
NEGATIVE = ['n','no','No','N','Nope','nope']

# Riot Games API scraping
# Obtains all Champion data for use in functions
result = urlopen(
	"https://na.api.pvp.net/api/lol/na/v1.2/champion?api_key=84a61ad2-30ec-4067-b06a-2c6cea9fa344")
championList = ast.literal_eval(result.read().replace('false', 'False').replace('true','True'))
championIDList = [x['id'] for x in championList['champions']]


#############
# FUNCTIONS #
#############

#############################
# printIntroText
#
# Input:
# Output:
# 
# Prints out the introduction text to the Spellimobulator
#############################
def printIntroText():
	print "Welcome, Summoner, to my newest invention, the Spellimobulator!\n"
	print "This device takes in the variables of Attack Damage (AD), Ability Power (AP),"
	print "and Cooldown Reduction (CDR)."
	print "Then, via magical donger technology, calculates the most 'efficient' spell between all champions."

#############################
# smRunner
#
# Input:
# Output:
# 
# The 'main' of this program. Handles user input and calls helper functions
#############################
def smRunner():
	printIntroText()

	userInput = raw_input('Give it a whirl? (y/n): ')

	while userInput not in NEGATIVE:
		if userInput in AFFIRMATIVE:
			# DO the thing, get the input, yay!
			userInput = raw_input('Once more? With pizzaz!? (y/n): ')
		else:
			userInput = raw_input('... Can you try answering "yes" or "no", summoner?: ')

	print "Please come back again, for great science!"
	print "		- Heimerdinger"

# One function to rule them all
smRunner()