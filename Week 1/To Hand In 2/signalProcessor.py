import math
class numStore(): 
	
	"""
	self iniateing method that creates the series list and the length of the series list, it must be handed the lengh of the series as a integer
	"""
	def __init__(self,seriesLength):
		self.series = [] #list the other methods use for the series of numbers
		self.seriesLength = seriesLength #defines the length of the series from the parameter that is handed to the method

	"""
	This method generates a series of numbers between -1 and 1 using sin. It will the the length that is set in the constructor
	"""
	def genSeries(self):
		self.incrementor = 10 #screates the value that will be incremented
		for self.i in range (0,self.seriesLength): #loops for the required length of the series of numbers
			self.series.append(math.sin(math.radians(self.incrementor)))# appends a sin value between -1 and 1
			self.incrementor += 10 # increments the value the sin uses by 10
		return self.series #returns the series
	
	"""
	This method will display a list(what the other functuons return) is a readable format (lines of hashes)
	"""	
	def display(self,listToOutput):
		self.scale = 30 # this sets the scale for the graph
		for self.i in listToOutput:#loops for the length of the list handed to the method
			self.j = int(self.i*self.scale) # changes the values to ints from a floats to integers
			self.str = "" #creates the string to fill with spaces or #
			if self.j > 0: # if the value is value is positive
				for self.a in range (0,self.scale): #for 30 spaces a white space will be created
					self.str = self.str + " "
				for self.a in range(0,self.j): # for the length of the value hashs will be printed
					self.str = self.str + "#"
			else: # if its is a negative number
				for self.a in range (0,self.j+self.scale): #for the empty space print white space
					self.str = self.str + " "
				for self.a in range(0,-self.j): # for the remaining space between white space created and the mid point, print hashs
					self.str = self.str + "#"
			print self.str #print the line of hashs produced
	"""
	This method get a series of numbers from genSeries() and then alters them using a lambda so they are all in the positive region
	"""
	def valChanger(self):
		self.listToReturn =[] #creates the list that will be returned
		self.values = numStore(self.seriesLength).genSeries() #gets a series of values from the genSeries
		f = lambda x : x+1 if x<=1 else x #lambda that makes adds 1 to any value less than 1 which will create a wave only in positive
		for self.i in self.series: #for the length of the series
			self.listToReturn.append(f(self.i)) # appends the value that is changed by the lambda to the list that is returned
		return self.listToReturn #returns the list
		
a = numStore(100) #makes the class equal to a, send 10 as the series length
a.display(a.genSeries()) # displays what is returned by genSeries()
print " "
a.display(a.valChanger())# displays what is returned by valChanger()