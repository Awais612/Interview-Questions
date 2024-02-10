# Quick Sort

- Selection of Pivot
- Recursive
- Worst case is O(n^2)
- Best Case: O(nlgn)

```
QUICKSORT(A, p, r)
    q = PARTITION(A, p, r)
    QUICKSORT(A, p, q-1)
    QUICKSORT(A, q+1, r)

PARTITION(A, p, r)
    x = A[r]
    i = p - 1 // This is responsible to place the elements to their position after comparing

    for j = 1 to r-1
        if A[j] <= x
            i = i + 1
            Swap A[i] with A[j]
    Swap A[i+1] with A[r]
    return i + 1
```
