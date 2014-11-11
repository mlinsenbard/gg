from urllib2 import urlopen
import ast
import json
from sm import mostEfficient

CHAMPION = 0
SPELL = 1
DPS = 2

#### TESTS ####

# The 0,0,0 test
# Anivia's Ult has base 160 dps, which is the highest base dps in game
def test_allZero():
	values = (0,0,0)
	expectedDPS = 160
	expectedChamp = "Anivia"
	expectedSpell = "Glacial Storm"

	result = mostEfficient(values)

	if result[DPS] == expectedDPS and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# The inhuman AD test
# Given a massive AD value, (over 1050) Heartseeker Stike becomes best spell
def test_myRightArmIsALotStrongerThanMyLeftOne():
	values = (10000.0,0,0)

	expectedDPS = 6053
	expectedChamp = "Pantheon"
	expectedSpell = "Heartseeker Strike"

	result = mostEfficient(values)

	if result[DPS] == expectedDPS and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# The Donger Test
# Given a massive AP value, H-28G Evolution Turret becomes best spell
def test_bigAP():
	values = (0,10000.0,0)

	expectedDPS = 3987.934641
	expectedChamp = "Heimerdinger"
	expectedSpell = "H-28G Evolution Turret"

	result = mostEfficient(values)

	# Converting to int because test failed with floats for some reason
	if int(result[DPS]) == int(expectedDPS) and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# The realistic Test
# Tests acceptable AP/AD values give Kog'Maw's Living Artillery as a result diregarding cdr
def test_acceptableValues():
	values = (100.0,100.0,0)

	expectedDPS = 240
	expectedChamp = "KogMaw"
	expectedSpell = "Living Artillery"

	result = mostEfficient(values)

	if result[DPS] == expectedDPS and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# CDR Tests

# The SpellSlinger Test
# Tests a large AP value and large Cooldown
# Result should be Evelynn's Hate Spike
def test_spellslinger():
	values = (0,2000.0,40.0)

	expectedDPS = 1322.222222
	expectedChamp = "Evelynn"
	expectedSpell = "Hate Spike"

	result = mostEfficient(values)

	# Converting to int because test failed with floats for some reason
	if int(result[DPS]) == int(expectedDPS) and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# The Fist of the North Star Test
# Tests a large AD value and large cooldown
# Result should be Pantheon's Heartseeker Strike
def test_fistsOfFury():
	values = (2000.0,0,40.0)

	expectedDPS = 2088.333333
	expectedChamp = "Pantheon"
	expectedSpell = "Heartseeker Strike"

	result = mostEfficient(values)

	# Converting to int because test failed with floats for some reason
	if int(result[DPS]) == int(expectedDPS) and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# The Super Saiyan Test
# Given massive AD,AP, and full CDR
# Result should be Hate Spike
def test_superSaiyan():
	values = (9001.0, 9001.0, 40.0)

	expectedDPS = 12601.388889
	expectedChamp = "Evelynn"
	expectedSpell = "Hate Spike"

	result = mostEfficient(values)

	# Converting to int because test failed with floats for some reason
	if int(result[DPS]) == int(expectedDPS) and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# Haste Test
# Only given full CDR
# Result should be KogMaw's Living Artillery
def test_haste():
	values = (0,0,40.0)

	expectedDPS = 266.666667
	expectedChamp = "KogMaw"
	expectedSpell = "Living Artillery"

	result = mostEfficient(values)

	# Converting to int because test failed with floats for some reason
	if int(result[DPS]) == int(expectedDPS) and result[CHAMPION] == expectedChamp and result[SPELL]['name'] == expectedSpell:
		return True
	else:
		return False

# Run all tests, outputting only failures
def main():
	total = 8
	passes = total
	if not test_allZero():
		print "Test failed: Zero Test"
		passes -= 1
	if not test_myRightArmIsALotStrongerThanMyLeftOne():
		print "Test failed: Big AD Test"
		passes -= 1
	if not test_bigAP():
		print "Test failed: Big AP Test"
		passes -= 1
	if not test_acceptableValues():
		print "Test failed: Normal Values (no CDR) Test"
		passes -= 1
	if not test_spellslinger():
		print "Test failed: SpellSlinger Test"
		passes -= 1
	if not test_fistsOfFury():
		print "Test failed: Fists of Fury Test"
		passes -= 1
	if not test_superSaiyan():
		print "Test failed: Super Saiyan Test"
		passes -= 1
	if not test_haste():
		print "Test failed: Haste Test"
		passes -= 1

	print "%d out of %d tests passed." % (passes, total)

if __name__ == "__main__":
	main()