# Iterative In-order Traversal of Binary Tree

`Educative`

```python
from collections import deque
from binary_tree import *
from binary_tree_node import *

# Function that prints the in-order traversal of the binary tree
def inorder_iterative(root):
  result = ""
  if not root:
      # If the root is None, we simply print None
      print("None", end = "")
  else:
      # Initializing the stack
      stk = deque()
      curr_node = root

      # This loop will keep printing the tree node in "L N R" fashion
      # until the current node is None or the stack becomes empty
      while stk or curr_node:
          # If the current node is not None, we push it into the stack and point it
          # to its left child and skip to the next iteration
          if curr_node:
              stk.append(curr_node)
              curr_node = curr_node.left
              continue

          # Current node is None, meaning that it's time to print the nodes in the "L"
          # sub-tree
          # So, printing and popping the top-most element of the stack
          result += str(stk[-1].data) + ", "
          curr_node = stk[-1].right
          stk.pop()

      # Truncating right most comma
      result_ = result[:-2]
      print(str(result_), end = "")
```