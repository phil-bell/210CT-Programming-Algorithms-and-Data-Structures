# nodeList is a adjacency list of nodes and edges that connect the nodes
nodeList = [[1,2,3],[0,2,4],[0,1,3,4],[0,2,4],[1,2,3,5],[4]]
"""
the nodes class is what operates on the nodes
"""
class nodes():
	"""
	addNode will add new node the the end of nodeList, it will then update the nodes that the new node is connected to with the new edges. It must be 
	"""
	def addNode(self,nodeConnections):
		nodeList.append(nodeConnections)# appends the connections(edges) of the new node to the node list
		for self.i in nodeConnections:# loops though the new connections
			nodeList[self.i].append(len(nodeList)-1) #for the connections in the new node it adds the corresoponding connections to the old nodes
	"""
	addEdge will add ned connections/edges to alreay existing nodes, you hand it the 2 nodes that you would like a new edge between and it will update them
	"""
	def addEdge(self,nodeFrom,nodeTo):
		nodeList[nodeFrom].append(nodeTo) # append the new connection in 1st node
		nodeList[nodeTo].append(nodeFrom) # append the new connection in 2nd node
	"""
	This simply outputs the nodeList so I can check that its has been updated correctly
	"""
	def output(self):
		self.a = 0 # assigns a to zero
		for self.i in nodeList: # loops through list of node
			print "Node",self.a,":", self.i # print the list number and the value in the list
			self.a += 1 # increments a
		#return nodeList
b = nodes()	
b.addNode([0,5])
b.addEdge(3,1)
b.output()