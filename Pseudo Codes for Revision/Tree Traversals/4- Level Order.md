# Level-Order Traversal
`Educative`

- Breadth-First: Queue approach

- Traverse left tree
- Traverse right tree
- Visit Node

### Pseudo Code

```pseudo
levelorder(rootnode):
    q = empty queue
    q.enqueue(rootnode)

    while (not q.isEmpty()):
        node = q.dequeue()
        print(node)

        if node.left != null:
            q.enqueue(node.left)

        if(node.right != null):
            q.enqueue(node.right) 
```

### Time Complexity
- O(n)