nodeDict = {0: set([1,3]),1: set([0]),2: set([5]),3: set([0,4]),4: set([3,5]),5: set([2,4])}

	
class nodes():
	"""
	This method must be handed a graph in the form of a dictionary of sets and which node to start on.
	"""
	def graphTraverse(self,nodeDict,startNode):
		self.path = [] #empty list for the path to he added to
		self.visitedNodes, self.stack = set(), [startNode]#created the stack
		while self.stack: #loops though the stack until it is empty (meaning all nodes are visited)
			self.node = self.stack.pop()#makes the current node the top of the stack
			if self.node not in self.visitedNodes: #if that node has not already been visited
				self.visitedNodes.add(self.node) #adds the current node to the visited nodes
				self.stack.extend(nodeDict[self.node] - self.visitedNodes)  #adds the edges in the node to the stack minus the alead visited nodes
				self.path.append(self.node)  # add the current node to the path
		return self.path,self.visitedNodes # returns the path and the nodes visited
		
		
(i,j) = nodes().graphTraverse(nodeDict,4) # calls the method with the parameters graph and starting node. makes it equal to i and j so the 2 items returned by the method can be accessed individually
print "Path used:",", ".join(str(a) for a in i) # prints out the path and removes square brackets
print "Nodes visited:",", ".join(str(a) for a in j) # prints out the visited nodes and removes the square brackets 
	
	
	