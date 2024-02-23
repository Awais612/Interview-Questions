# In-Order Traversal

- Traverse left tree
- Visit Node
- Traverse right tree

### Pseudo Code

```pseudo
inorder(node):
    if node == null:
        return
    
    inorder(node.left)
    print(node)
    inorder(node.right)
```

### Time Complexity
- O(n)