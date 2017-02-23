#this functions tries to find and item in the array "arrayA" that is more the "L" and less than "U"
def moreLessChecker(arrayA,l,u):
	for i in range (0,len(arrayA)): #loops though for loop until
		if arrayA[i] > l: #makes the bool "moreThenL" true if the item in the array is more then l if note makes it false
			moreThenL = True
		else:
			moreThenL = False 
		if arrayA < u: #make the bool "lessThenL" true of the item in the array is less then u if note makes it false
			lessThanU = True
		else:
			lessThanU = False
	if moreThenL = True and lessThanU = True: #if both lessThenL and moreThenL is both true then the item in the array is more the L and less the U it retruns true if not return false
		return True
	else:
		return False