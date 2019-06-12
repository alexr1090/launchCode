#!/usr/bin/env python
"""
main.py imports weather and guesser programs. It displays a menu
asking user which they would like to do and error checks
and runs the correct program until user exits
"""
import weatherCopy, guesserCopy

def main():
	
	guessingGame = guesserCopy.Guesser()
	weatherCheck = weatherCopy.weather()

	currentChoice = 0
	guess = 0
	weather = 0
	while currentChoice != 3:
		while 1:
			try:
				currentChoice = int(raw_input("Please enter 1 for weather, 2 for the guessing game or 3 to exit. "))
				if currentChoice == 1:weatherCheck.run()
				elif currentChoice == 2: guessingGame.run()
				elif currentChoice == 3: break
				elif currentChoice > 3: raise ValueError 
			except Exception as e:
				print e, "Please re-enter."

	weatherRuns = weatherCheck.getRunCount()
	
	print "\nYou ran the weather check " + str(weatherRuns) + " me(s)."


	if weatherRuns >= 1:
		'''
		get the hottest temperture and zip code
		'''
		hottest = sorted(weatherCheck.zipsToTemps.keys())[-1]
		print "The hottest temperature you searched was in " + weatherCheck.zipsToTemps[hottest] + " and it was "+ str(hottest)+" degrees Fahrenheit."
	guessCount = guessingGame.getRunCount()
	print "You played the guessing game " + str(guessCount) + " time(s)."
	if guessCount >= 1:
		'''
		display the best game 
		'''
		guesses = str(guessingGame.getRunCount())
		bestCount = str(len(guessingGame.getBestGame()))
		
		print "In your best game it took you " + bestCount+ " guesses to win."

	print "\nHave a nice day!"
	
	
if __name__ == '__main__':
	main()
