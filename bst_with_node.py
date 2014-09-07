class Node(object):
  ''' Binary search tree node class '''

  def __init__(self, data):
    ''' Binary search tree node initialiser  '''
    self.data = data
    self.left = None
    self.right = None


class BST(object):
  ''' Binary search tree class '''

  def __init__(self, data):
    ''' Binary search tree initialiser '''    
    self.node = Node(data)

  def insert(self, data):
    ''' Binary search tree insert '''
    if data < self.node.data: 
      if self.node.left is None: # insert as left leaf node
        self.node.left = BST(data)
      else: # insert to left subtree
        self.node.left.insert(data)
    else:
      if self.node.right is None: # insert as right leaf node
        self.node.right = BST(data)
      else: # insert to right subtree
        self.node.right.insert(data)

  def search(self, data):
    ''' Binary search '''    
    if self.node.data == data:
      return "Found"
    elif self.node.left is None and self.node.right is None:
      return "Not found"
    elif data < self.node.data: # go left
      if self.node.left is None:
        return "Not found"
      else:
        return self.node.left.search(data)
    else: # data > self.data i.e. go right
      if self.node.right is None:
        return "Not found"
      else:
        return self.node.right.search(data)

  def print_inorder(self):
    ''' Binary search tree inorder traversal '''
    if self.node.left:
      self.node.left.print_inorder()
    print(self.node.data, end=' ')
    if self.node.right:
      self.node.right.print_inorder()  

  def print_preorder(self):
    ''' Binary search tree preorder traversal '''
    print(self.node.data, end=' ')
    if self.node.left:
      self.node.left.print_preorder()
    if self.node.right:
      self.node.right.print_preorder()    

  def print_postorder(self):
    ''' Binary search tree postorder traversal '''    
    if self.node.left:
      self.node.left.print_postorder()
    if self.node.right:
      self.node.right.print_postorder()  
    print(self.node.data, end=' ')

  def print_reverse(self):
    ''' Binary search tree reverse traversal '''    
    if self.node.right:
      self.node.right.print_reverse()
    print(self.node.data, end=' ')
    if self.node.left:
      self.node.left.print_reverse()

  def find_min(self):
    ''' Binary search tree find minimum value '''    
    if self.node.left is None:
      print("Minimum is", self.node.data)
    else:
      self.node.left.find_min()

  def find_max(self):
    ''' Binary search tree find maximum value '''
    if self.node.right is None:
      print("Maximum is", self.node.data)
    else:
      self.node.right.find_max()

  def lookup(self, data, parent=None):
    ''' Binary search tree lookup, similar to search
        but keeps track of parent (used for delete) '''
    if self.node.data == data:
      # return current node and its parent
      return self, parent
    elif data < self.node.data: # go left
      if self.node.left is None:
        return None, None
      else:
        return self.node.left.lookup(data, self)
    else: # data > self.node.data, go right
      if self.node.right is None:
        return None, None
      else:
        return self.node.right.lookup(data, self)

  def delete(self, data):
    ''' Binary search tree delete '''
    # get node containing data and its parent
    node, parent = self.lookup(data)
    if node is not None:
      # node has not child, just delete
      if (node.node.left is None) and (node.node.right is None):
        # check if it is not the root node
        if parent.node.left is node:
          parent.node.left = None
        else:
          parent.node.right = None
        del node
      # node has 1 child, replace node by its child
      elif (node.node.left is None) != (node.node.right is None):
        if node.node.left:
          n = node.node.left
        else:
          n = node.node.right
        if parent.node.left is node:
          parent.node.left = n
        else:
          parent.node.right = n
        del node
      else:
        # node has 2 children, replace with inorder successor
        # i.e. smallest value in right subtree
        parent = node
        successor = node.node.right
        while successor.node.left:
          parent = successor
          successor = successor.node.left
        # replace node data by its successor data
        node.data = successor.node.data
        # fix successor's parent node child
        if parent.node.left == successor:
          parent.node.left = successor.node.right
        else:
          parent.node.right = successor.node.right
    else:
      print("Not found")

# main
bst = BST(50)
bst.insert(30)
bst.insert(80)
bst.insert(10)
bst.insert(40)
bst.insert(70)
bst.insert(90)

bst.print_inorder()
print()

bst.print_preorder()
print()

bst.print_postorder()
print()

bst.print_reverse()
print()

bst.find_min()
bst.find_max()

print(bst.search(70))  # successful search
print(bst.search(100)) # unsuccessful search

bst.insert(20)
bst.print_inorder()
print()

bst.delete(90) # delete node with 0 children
bst.delete(10) # delete node with 1 child
bst.delete(50)# delete node with 2 children, root
bst.print_inorder()
print()
