def functCalc(k,l):
	results = ((4**l)+k)/(3*(k**3)+l)
	return results
	
def mean(numList):
	numListTot = 0
	for i in range (0,len(numList)):
		numListTot = numListTot + numList[i]
	numListMean = numListTot/len(numList)
	return numListMean

myList = [32,425,125,262,2,15,523]
meanOutput = mean(myList)
print meanOutput

output = functCalc(12,16)
print output