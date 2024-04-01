# MOVE ZEROES TO RIGHT SIDE OF THE ARRAY IN O(N)
`Pentaloop`

To move all zeroes to the right side of an array in O(n) time complexity, you can use the two-pointer approach. Here's a simple algorithm in Python:

```python
def move_zeroes_to_right(arr):
    n = len(arr)
    
    # Initialize two pointers
    left = 0
    right = 0

    # Iterate through the array
    while right < n:
        # If the current element is non-zero
        if arr[right] != 0:
            # Swap the non-zero element with the left pointer
            arr[left], arr[right] = arr[right], arr[left]
            
            # Move the left pointer forward
            left += 1

        # Move the right pointer forward
        right += 1

# Example Usage
arr = [0, 2, 0, 3, 4, 0, 5, 0]
move_zeroes_to_right(arr)
print(arr)
```

This algorithm uses two pointers (left and right) to iterate through the array. The left pointer points to the position where the next non-zero element should be placed, and the right pointer scans the array for non-zero elements. When a non-zero element is found, it is swapped with the element at the left pointer's position, and both pointers are moved forward. This process continues until the end of the array is reached. The zeroes are effectively moved to the right side of the array while maintaining the relative order of non-zero elements.

Consider the array: [0, 2, 0, 3, 4, 0, 5, 0]

Initially, the two pointers (left and right) are at the beginning of the array:

```
left
 ↓
[0, 2, 0, 3, 4, 0, 5, 0]
 ↑
right
```

Now, let's iterate through the array:

- right at index 0, value 0 (zero). No change.
- right at index 1, value 2 (non-zero). Swap with the element at left (index 0).

```
   left
    ↓
[2, 0, 0, 3, 4, 0, 5, 0]
       ↑
      right
```

- right at index 2, value 0 (zero). No change.
- right at index 3, value 3 (non-zero). Swap with the element at left (index 1).

```
       left
       ↓
[2, 3, 0, 0, 4, 0, 5, 0]
             ↑
           right
```

Continue this process until the end of the array.
After the complete iteration: [2, 3, 4, 5, 0, 0, 0, 0]

