# Pre-Order Traversal

### Tree Traversal

A systematic way of visiting nodes in a tree

There are two types:
- Depth-First: Stack
- Breadth-First: Queue

| Depth First | Breadth First |
|-------------|---------------|
| Pre-order   | Level order   |
| In-order    |               |
| Post-order  |               |

### Mechanism

- Visit Node
- Traverse Left
- Traverse Right

### Pseudo Code

```pseudo
preorder(node):
    if node == null:
        return
    
    print(node)
    preorder(node.left)
    preorder(node.right)
```

### Time Complexity
- O(n<sup>2</sup>)