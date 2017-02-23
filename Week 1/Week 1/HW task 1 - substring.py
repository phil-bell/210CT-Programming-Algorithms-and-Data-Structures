def isSubString(userWord1,userWord2): 
	if(len(userWord1) >= len(userWord2)):
		userA = userWord2
		userB = userWord1
	else:
		userA = userWord1
		userB = userWord2
	length = (len(userB) - len(userA))+1
	for i in range(0,length):
		if(userB[i:i + len(userA)] == userA):
			print "Is a substring"
		else:
			print "Is not a substring"
usersWord1 = raw_input ("Word 1: ")
usersWord2 = raw_input ("Word 2: ")
isSubString(usersWord1,usersWord2)
