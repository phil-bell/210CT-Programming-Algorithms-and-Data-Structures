import random 
def randIntList():
	randomList1=[0]
	randomList2=[0]
	for x in range(0,40):
		randomList1.append(random.randint(0,1))
		randomList2.append(0)
	for x in range(0,40):
		if randomList1[x-1]+randomList1[x+1]==1 or randomList1[x-1]+randomList1[x+1]==2:
			randomList2[x]=1
		else:
			randomList2[x]=0
	print randomList1
	print randomList2
a=randIntList()


