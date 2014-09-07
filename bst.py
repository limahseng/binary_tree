class BST(object):
  ''' Binary search tree class '''

  def __init__(self, data):
    ''' Binary search tree initialiser '''
    self.data = data
    self.left = None
    self.right = None

  def insert(self, data):
    ''' Binary search tree insert '''    
    if data < self.data: 
      if self.left is None: # insert as left leaf node
        self.left = BST(data)
      else: # insert to left subtree
        self.left.insert(data)
    else:
      if self.right is None: # insert as left leaf node
        self.right = BST(data)
      else: # insert to right subtree
        self.right.insert(data)

  def search(self, data):
    ''' Binary search '''    
    if self.data == data:
      return "Found"
    elif self.left is None and self.right is None:
      return "Not found"
    elif data < self.data: # go left
      if self.left is None:
        return "Not found"
      else:
        return self.left.search(data)
    else: # data > self.data i.e. go right
      if self.right is None:
        return "Not found"
      else:
        return self.right.search(data)

  def print_inorder(self):
    ''' Binary search tree inorder traversal '''    
    if self.left:
      self.left.print_inorder()
    print(self.data, end=' ')
    if self.right:
      self.right.print_inorder()  

  def print_preorder(self):
    ''' Binary search tree preorder traversal '''
    print(self.data, end=' ')
    if self.left:
      self.left.print_preorder()
    if self.right:
      self.right.print_preorder()    

  def print_postorder(self):
    ''' Binary search tree postorder traversal '''
    if self.left:
      self.left.print_postorder()
    if self.right:
      self.right.print_postorder()  
    print(self.data, end=' ')

  def print_reverse(self):
    ''' Binary search tree reverse traversal '''
    if self.right:
      self.right.print_reverse()
    print(self.data, end=' ')
    if self.left:
      self.left.print_reverse()

  def find_min(self):
    ''' Binary search tree find minimum value '''    
    if self.left is None:
      print("Minimum is", self.data)
    else:
      self.left.find_min()

  def find_max(self):
    ''' Binary search tree find maximum value '''
    if self.right is None:
      print("Maximum is", self.data)
    else:
      self.right.find_max()

  def lookup(self, data, parent=None):
    ''' Binary search tree lookup, similar to search
        but keeps track of parent (used for delete) '''
    if self.data == data:
      # return current node and its parent
      return self, parent
    elif data < self.data: # go left
      if self.left is None:
        return None, None
      else:
        return self.left.lookup(data, self)
    else: # data > self.data, go right
      if self.right is None:
        return None, None
      else:
        return self.right.lookup(data, self)

  def delete(self, data):
    ''' Binary search tree delete '''    
    # get node containing data and its parent
    node, parent = self.lookup(data)
    if node is not None:
      # node has not child, just delete
      if (node.left is None) and (node.right is None):
        # check if it is not the root node
        if parent.left is node:
          parent.left = None
        else:
          parent.right = None
        del node
      # node has 1 child, replace node by its child
      elif (node.left is None) != (node.right is None):
        if node.left:
          n = node.left
        else:
          n = node.right
        if parent.left is node:
          parent.left = n
        else:
          parent.right = n
        del node
      else:
        # node has 2 children, replace with inorder successor
        # i.e. smallest value in right subtree
        parent = node
        successor = node.right
        while successor.left:
          parent = successor
          successor = successor.left
        # replace node data by its successor data
        node.data = successor.data
        # fix successor's parent node child
        if parent.left == successor:
          parent.left = successor.right
        else:
          parent.right = successor.right
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
