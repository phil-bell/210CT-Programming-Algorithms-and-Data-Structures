def nameDisplay(name):
	for i in range(10):
		print name
		
def squeareDraw(size):
	lineList=[]
	for i in range(size):
		lineList.append("*")
	lineStr = ''.join(lineList)
	for i in range(size):
		print lineStr
		
def userInputList(listLength):
	tempWord=[]
	for i in range(listLength):
		temp = raw_input ("Enter Word: ")
		tempWord.append(temp)
	return tempWord
	
def writeToFile(text,fileName):
	fileOpen = open(fileName,"w")
	for i in range(len(text)):
		fileOpen.write(text[i])
		
def fileCapital(fileName):
	fileText = open(fileName,"w")
	print fileText.lower()


b=userInputList(10)
writeToFile(b,"Letter.txt")
fileCapital("Letters.txt")
squeareDraw(10)
nameDisplay("Phil")