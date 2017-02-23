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
	r=tree
	while r != None:
		if r.value == target:
			return r.value
		elif r.value > target:
			
			r = r.left
		else:
			r = r.right
	return None

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
