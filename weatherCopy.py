#!/usr/bin/env python
"""
wether.py takes a 5 digit zip code from user and 
displays a current weather for that zip code
"""
import urllib2
import json
class weather:
	#
	# api.openweathermap.org/data/2.5/forecast?zip={zip code},{country code}
	#
	def getRunCount(self):
		return self.runCount
	def _getTemp(self):
		"""
		getTemp takes self.zipCode and sends it to the 
		openweathermap api. It parses through the json data
		from openweathermap to get the temperature and displays
		the current temparture as a whole number. Also adds currentTemp as int to the 
		the zipsToTemps dictionary and stores zip as a value. Will erase previous value if applicable
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
		#print json.dumps(json_data, sort_keys=True, indent=2, separators= (',', ': '))

	def run(self):
		'''
		Run gets 5 digit number from user and error checks 
		to make sure. It then stores that number in self.zipCode and
		calls getTemp()
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

		


	def __init__(self):
		'''
		zipsToTemps is a dictionary that keeps zip
		codes as the value and their temperatures as key.
		zipCode is used to keep track of the current zipCode
		'''
		self.zipsToTemps = {}
		self.zipCode = ''
		self.runCount = 0
		