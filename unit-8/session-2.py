# build_tree()

from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
# problem 1

'''
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
'''
'''
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def count_odd_splits(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        if root.val % 2 != 0:
            return 1 
    
    left = count_odd_splits(root.left)
    right = count_odd_splits(root.right)

    return left + right
    
    
    
    


"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""
# 1

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

'''


# problem 2
'''
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if inventory == None:
        return False
    if inventory.val == name:
        return True
    
    if name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)


"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) '''

# problem 3

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower"))  