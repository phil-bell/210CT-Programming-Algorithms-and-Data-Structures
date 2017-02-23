def isSbString(a,b):
	def strIncre(i,j,k,l):
		print "i: ",i
		print "j: ",j
		print "k: ",k
		print "l: ",l
		print "\n \n"
		if j==l:
			print "Is not substring"
		elif i==k and listA[i-1] == listB[j-1]:
			print "Is substring"
		elif listA[i] == listB[j]:
			if j==l:
				print "Is not substring"
			else:
				i += 1
				j += 1
				strIncre(i,j,k,l)
		else:
			j += 1
			strIncre(i,j,k,l)
	listA = list(a)
	listB = list(b)
	i = 0
	j = 0
	k = len(listA)
	l = len(listB)
	return strIncre(i,j,k,l)
b = isSbString("cat","tybs")


		

