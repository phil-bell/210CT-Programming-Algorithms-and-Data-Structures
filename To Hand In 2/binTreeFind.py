class BinTreeNode(object):

	def __init__(self, value):
		self.value=value
		self.left=None
		self.right=None

def tree_insert( tree, item):
	if tree==None:
		tree=BinTreeNode(item)
	else:
		if(item < tree.value):
			if(tree.left==None):
				tree.left=BinTreeNode(item)
			else:
				tree_insert(tree.left,item)
		else:
			if(tree.right==None):
				tree.right=BinTreeNode(item)
			else:
				tree_insert(tree.right,item)
	return tree

def bin_tree_find(tree,target):
	while tree != None: # will loop while the is something in the tree
		if tree.value == target: # if the value selected is the target then value is returned
			return tree.value
		elif tree.value > target: # if the value selected is more than the target then the value selected is moved to the left
			tree = tree.left
		else: #if anything else (aiming for selected value less than the target) the selected value is moved right
			tree = tree.right
	return None	# returns none if cant be found or tree is empty

def postorder(tree):
	if(tree.left!=None):
		postorder(tree.left)
	if(tree.right!=None):
		postorder(tree.right)
	print tree.value

def in_order(tree):
	if(tree.left!=None):
		in_order(tree.left)
	print tree.value
	if(tree.right!=None):
		in_order(tree.right)
 
if __name__ == '__main__':
	t=tree_insert(None,6);
	tree_insert(t,10)
	tree_insert(t,5)
	tree_insert(t,2)
	tree_insert(t,3)
	tree_insert(t,4) 
	tree_insert(t,11)
	in_order(t)
	print (bin_tree_find(t,4))
