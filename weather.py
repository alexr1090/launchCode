#!/usr/bin/env python
"""
weather class is a class which has the purpose of getting the current
temperature from a zipcode that the user enters and displaying it back to them.
It uses the openweathermap api to get the temperature. It also has
variables that keep track of statistics if more than one zip code is entered.

API info:https://openweathermap.org/current
"""
import urllib2
import json
class Weather:

	def getRunCount(self):
		return self.runCount
	def getZipsToTemps(self):
		return self.zipsToTemps
	def _playAgain(self):
		'''
		Play again is a method that asks user if they want
		to play again and error checks that user entered 
		either y or n. It returns False for n and True for y
		'''
		while True:
			try:	
				again = str(raw_input("Would you like to search another zip code? (y\\n)?").lower())
				if again != "n" and again != "y":
					raise ValueError("Invalid")
				elif again == 'y': 
					return True
				else: 
					return False		
			except ValueError: 
			 	print "Please enter either y or n."

	def _getTemp(self):
		"""
		getTemp takes self.zipCode and sends it to the openweathermap 
		api. It parses through the json data from openweathermap to get 
		the temperature and displays the current temparture as a whole 
		number. Also adds currentTemp as int to the the zipsToTemps key 
		and stores zip as a value. Will erase previous value if 
		applicable. Asks user if they want to search again and returns 
		True for y and False for n.
		"""
		try:
			req = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?zip='+self.zipCode+'&units=imperial&APPID=d14d83eda3ee830fce2583dce1fbf755')
			json_data = json.loads(urllib2.urlopen(req).read())
			j = json_data["main"]
			current_temp = int( j['temp'] )
			self.zipsToTemps[current_temp] = self.zipCode
			print "The current temperature in "+ self.zipCode + " is " + str(current_temp) +" degrees Fahrenheit."
			return 1
		except Exception as e:
			print str(e) + ", Please try again."
			return False
		return True
		
		

	def run(self):
		'''
		Run gets 5 digit number from user and error checks it. 
		It then stores that number in self.zipCode and
		calls getTemp(). If getTemp returns an error (False) it 
		will ask user for another zip code. After get temp runs
		successfully (True) it will ask user if they want to play again.
		It will add 1 to run count for every time it is called. 
		'''
		self.runCount += 1
		while True:
			try:
				self.zipCode = raw_input("Please enter a five digit zip code to get the forecast\n")
				if len(self.zipCode) != 5: raise ValueError("invalid length")
				else: zipCodeInt = int(self.zipCode)
			except Exception :
				print ("Invalid input.\n")
				continue
			if not self._getTemp(): continue
			else: break
		if self._playAgain(): self.run()
		


	def __init__(self):
		'''
		zipsToTemps is a dictionary that keeps zip
		codes as the value and their temperatures as key.
		zipCode is used to keep track of the current zipCode
		'''
		self.zipsToTemps = {}
		self.zipCode = ''
		self.runCount = 0
		
