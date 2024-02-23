# Post-Order Traversal

- Traverse left tree
- Traverse right tree
- Visit Node

### Pseudo Code

```pseudo
postorder(node):
    if node == null:
        return
    
    postorder(node.left)
    print(node)
    postorder(node.right)
```

### Time Complexity
- O(n)