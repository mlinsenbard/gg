from urllib2 import urlopen
import sm

###########
# GLOBALS #
###########

# User input constants
AFFIRMATIVE = ['y','yes','Yes','Y','sure','ok']
NEGATIVE = ['n','no','No','N','Nope','nope']

# Result tuple index names
CHAMPION = 0
SPELL = 1
DPS = 2

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
	print "and Cooldown Reduction (CDR).\n"
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
		try:
			ad = int(ad)
			if ad < 0:
				ad = raw_input('\nEnter a positive number for your desired AD: ')
			else:
				inputValid = True
		except Exception:
			ad = raw_input('\nEnter a positive number (not a letter!) for your desired AD: ')

	inputValid = False
	ap = raw_input('\nEnter a positive number for your desired AP: ')
	while not inputValid:
		try:
			ap = int(ap)
			if ap < 0:
				ap = raw_input('\nEnter a positive number for your desired AP: ')
			else:
				inputValid = True
		except Exception:
			ap = raw_input('\nEnter a positive number (not a letter!) for your desired AP: ')

	inputValid = False
	cdr = raw_input('\nEnter a number from 0-40 representing your desired CDR %: ')
	while not inputValid:
		try:
			cdr = float(cdr)
			if cdr < 0 or cdr > 40:
				cdr = raw_input('\nEnter a positive number from 0-40 representing your desired CDR %: ')
			else:
				inputValid = True
		except:
			cdr = raw_input('\nEnter a positive number from 0-40 (not a letter!) representing your desired CDR %: ')

	return (ad,ap,cdr)

#############################
# printResult
#
# Input: a 3-Tuple (champion [dict], spell [dict], dps [float])
# Output:
# 
# Prints out the result of calculating the most efficient spell
#############################
def printResult(result):
	print "After running some meticulous calculations..."
	print "%s's spell, %s is the most efficient spell with %f DPS.\n" % (result[CHAMPION], result[SPELL]['name'], result[DPS])

#############################
# main
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
			printResult(sm.mostEfficient(variableTuple))
			userInput = raw_input('Once more? (y/n): ')
		else:
			userInput = raw_input('... Can you try answering "yes" or "no", summoner?: ')

	print "Please, come back again for great science!"
	print "		- Heimerdinger"

# One function call to rule them all
if __name__ == "__main__":
    main()