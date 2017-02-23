class Node(object): 
	def __init__(self, value):
		self.value=value
		self.next=None
		self.prev=None
 
class List(object):#inserts the given parameters to the list
	def __init__(self):
		self.head=None
		self.tail=None
	def insert(self,n,x):
		if n !=None:
			x.next=n.next
			n.next=x
			x.prev=n
			if x.next!=None:
				x.next.prev=x
		if self.head==None:
			self.head=self.tail=x
			x.prev=x.next=None
		elif self.tail==n:
			self.tail=x
	def delete(self,n): #this will delete a Node
		if n.prev != None: #if previous n isnt empty then the previous next n will become the next n 
			print "test1"
			n.prev.next = n.next
		else: #if not head will become the next n
			print "test2"
			self.head = n.next
		if n.next != None: #if next n is empty then the next previous n will become the previous n 
			print "test3"
			n.next.prev = n.prev
		else: #if not tail will become the previous n
			print "test4"
			self.tail = n.prev
	def display(self): #outputs the list to the screen
		values=[]
		n=self.head
		while n!=None:
			values.append(str(n.value))
			n=n.next
		print "List: ",",".join(values)
	 
if __name__ == '__main__':
	l=List()
	l.insert(None, Node(4))
	l.insert(l.head,Node(6))
	l.insert(l.head,Node(8))
	l.display()
	l.delete()
	l.display()

def test():
