def isSbString(a,b):
	def strIncre(i,j,k):
		if listA[i] = listB[j] && j-i=k:
			return True
		elif listA[i] = listB[j]:
			if i=j:
				return False
			else:
				i =+ 1
				j =+ 1
				stringIcre(i,j)
		else:
			j =+ 1
			stringIcre(i,j)
	listA = list(a)
	listB = list(b)
	i = 0
	j = 0
	k = len(listA)
	return strIncre(i,j,k)


		

