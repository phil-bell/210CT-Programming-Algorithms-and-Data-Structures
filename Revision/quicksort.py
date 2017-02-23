import random
def quicksort(listToSort):
    less = []
    more = []
    equal = []
    if len (listToSort) > 1:
        pivot = listToSort[0]
        for i in listToSort:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                more.append(i)
        return quicksort(less)+equal+quicksort(more)
    else:
        return listToSort
randomList = []
for i in range (0,100000):
    randomList.append(random.randint(0,10000000))



print quicksort(randomList)
