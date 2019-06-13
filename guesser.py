#!/usr/bin/env python
import random
"""
Guesser class is made to be a guessing game. It generates 
a random number between 1 and 100 in run and the user
guesses these in _guessing. It has variables runCount,
bestGame, secrets, and allGuesses for statistical purposes
"""
class Guesser:
	def getRunCount(self):
		return self.runCount

	def getBestGame(self):
		return self.bestGame

	def _guessing(self,guess, number):
		"""
		Takes the correct number and the guess. 
		Compares guess to correct number and tells user
		whether their guess is correct, too high, or too low.
		This runs until the correct guess is found. error checks
		that guesses are valid integers. Also keeps list of guesses. 

		After correct guess is made displays users guesses and number 
		and asks user if they want to play again
		If they do returns true if they don't returns false.
		"""
		gameGuesses= [str(guess)]
		while guess != number:
			if guess > number:	print "\nSorry that is incorrect. The correct number is less than your guess."
			else: print "\nSorry that is incorrect. The correct number is greater than your guess."
			valid = 0
			while not valid:
				try:
					guess=int(raw_input("What is your next guess?"))
					valid = 1
					gameGuesses.append(str(guess))
				except ValueError:
					print ("Invalid number.")
		print ("\nCorrect! It took you " + str(len(gameGuesses)) + " guess(es) to guess correctly. Your guess(es) were/was " +  ", ".join(gameGuesses))
		if self.runCount == 1: self.bestGame = gameGuesses
		elif gameGuesses < self.bestGame: self.bestGame = gameGuesses

		self.allGuesses.append(gameGuesses)
		while True:
			try:	
				again = str(raw_input("\nWould you like to play again (y\\n)?").lower())
				if again != "n" and again != "y":
					raise ValueError("Invalid")
				elif again == 'y': 
					return True
				else: 
					return False		
			except ValueError: 
			 	print "Please enter either y or n."


	def run(self):
		'''
		run generates the secret number and stores it in the 
		secrets list. It then takes the original guess error
		checks and calls guessing
		'''
		self.runCount += 1
		
		print("\nHello, welcome to the guessing game!")
		again = True
		while again:
			number = random.randint(1, 100)
			self.secrets.append(number)
			while 1:
				try:
					guess = int(raw_input("\nPlease guess a number between one and one hundered.\n"))
				except ValueError:
					print ("Invalid number.")
					continue
				break
			again=self._guessing(guess, number)

		print "\nThank you for playing. Good bye!"


		 

	def __init__(self):
		'''
		allGuesses is a list that will contain more lists. The lists
		it contain have the guesses the user made for each game. 

		secrets is a list of ints that keeps track of all the random [secret] numbers
		generated for every game. runCount is an int that keeps track of how many games
		have been played. Best game keeps track of the best game by least number of guesses to win
		'''
		self.allGuesses = []
		self.secrets= []
		self.runCount = 0
		self.bestGame = 0
