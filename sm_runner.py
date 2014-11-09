from urllib2 import urlopen
import sm

###########
# GLOBALS #
###########

# User input constants
AFFIRMATIVE = ['y','yes','Yes','Y','sure','ok']
NEGATIVE = ['n','no','No','N','Nope','nope']

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
	inputValid = False
	ad = raw_input('\nEnter a positive number for your desired AD: ')
	while not inputValid:
		if any(c.isalpha() for c in ad):
			ad = raw_input('\nEnter a positive number (not a letter!) for your desired AD: ')
		else:
			ad = int(ad)
			if ad < 0:
				ad = raw_input('\nEnter a positive number for your desired AD: ')
			else:
				inputValid = True

	inputValid = False
	ap = raw_input('\nEnter a positive number for your desired AP: ')
	while not inputValid:
		if any(c.isalpha() for c in ap):
			ap = raw_input('\nEnter a positive number (not a letter!) for your desired AP: ')
		else:
			ap = int(ap)
			if ap < 0:
				ap = raw_input('\nEnter a positive number for your desired AP: ')
			else:
				inputValid = True

	inputValid = False
	cdr = raw_input('\nEnter a number from 0-100 representing your desired CDR %: ')
	while not inputValid:
		if any(c.isalpha() for c in cdr):
			cdr = raw_input('\nEnter a number (not a letter!) from 0-100 representing your desired CDR %: ')
		else:
			cdr = float(cdr)
			if cdr < 0 or cdr > 100:
				cdr = raw_input('\nEnter a positive number from 0-100 representing your desired CDR %: ')
			else:
				inputValid = True

	return (ad,ap,cdr)

#############################
# smRunner
#
# Input:
# Output:
# 
# The 'main' of this program. Handles user input and calls helper functions
#############################
def main():
	printIntroText()

	userInput = raw_input('Give it a whirl? (y/n): ')

	while userInput not in NEGATIVE:
		if userInput in AFFIRMATIVE:
			variableTuple = getInputValues()
			try:
				result = sm.mostEfficient(variableTuple)
				print "For the given values, " + result[0]['name'] + " is the most efficient spell with " + str(result[1]) + ' DPS.'
			except Exception,e:
				print "Something went terribly wrong!"
				print e
			userInput = raw_input('Once more? (y/n): ')
		else:
			userInput = raw_input('... Can you try answering "yes" or "no", summoner?: ')

	print "Please, come back again for great science!"
	print "		- Heimerdinger"

# One function to rule them all
main()