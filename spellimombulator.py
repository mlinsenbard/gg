from urllib2 import urlopen
import ast
import json

###########
# GLOBALS #
###########

# User input constants
AFFIRMATIVE = ['y','yes','Yes','Y','sure','ok']
NEGATIVE = ['n','no','No','N','Nope','nope']

# Obtains all Champion data for use in functions
# API Key would normally be kept secret but is hard-coded to ensure this script works on any machine
result = urlopen(
	"https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?locale=en_US&champData=spells&api_key=84a61ad2-30ec-4067-b06a-2c6cea9fa344")
ALL_CHAMPS = json.loads(result.read())['data']


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
# getInputValues
#
# Input:
# Output: a 3-tuple of AD, AP, and CDR values 
# 
# Obtains and sanitizes user input
#############################
def getInputValues():
	ad = raw_input('\nEnter an integer for your desired AD: ')
	while any(char.isalpha() for c in ad) or ad < 0:
		ad = raw_input('\nPlease enter a positive integer for your AD: ')
	ap = raw_input('\nEnter an integer for your desired AP: ')
	while any(char.isalpha() for c in ap) or ap < 0:
		ap = raw_input('\nPlease enter a positive integer for your AP: ')
	cdr = raw_input('\nEnter a value from 0 to 100 representing your CDR: ')
	while any(char.isalpha() for c in cdr) or cdr < 0 or cdr > 100:
		cdr = raw_input('\nPlease enter an integer in the range 0-100 representing your CDR: ')
	return (ad,ap,cdr)

#############################
# smMostEfficient
#
# Input: a 3-tuple of AD,AP,CDR
# Output: A dictionary representing a LoL spell
# 
# given ad, ap, and cdr, finds the most 'efficient' champion spell in the game
#############################
def smMostEfficient(dataTuple):
	pass

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
			variableTuple = getInputValues()
			spell = smMostEfficient(variableTuple)
			userInput = raw_input('Once more? With pizzaz!? (y/n): ')
		else:
			userInput = raw_input('... Can you try answering "yes" or "no", summoner?: ')

	print "Please come back again, for great science!"
	print "		- Heimerdinger"

# One function to rule them all
smRunner()