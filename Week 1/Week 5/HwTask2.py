  import random

  class BinTreeNode(object):

      def __init__(self, value):
          self.value=value
          self.left=None
          self.right=None
      def __str__(self):

          return "BinTreeNode(%d)"%self.value

      def dot(self):
        if self.left!=None:
          print "%s -> %d;"%(self.value, self.left.value)
          self.left.dot()
        if self.right!=None:
          print "%s -> %d;"%(self.value, self.right.value)
          self.right.dot()
     

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
      order1=range(10)
      #random.shuffle(order1)
      t=BinTreeNode(order1[0])
      for i in order1[1:]:
          tree_insert(t,i)
      #print order1
      print "digraph g{"
      t.dot()
      print "}"