## [1,2,3,4,5] ==> [120,60,40,30,24] without using divide

You can achieve this by first calculating the total product of all elements in the list and then dividing this total product by each element to get the desired output. However, since you mentioned not using division, we can use a different approach by multiplying elements selectively.

Here's a Python implementation without using division:

```python
def product_except_self(nums):
    n = len(nums)
    # Initialize two arrays to store products to the left and right of each element
    left_products = [1] * n
    right_products = [1] * n
    
    # Calculate products to the left of each element
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    # Calculate products to the right of each element
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    # Multiply corresponding elements from both arrays to get the final result
    result = [left_products[i] * right_products[i] for i in range(n)]
    return result

# Example usage
nums = [1, 2, 3, 4, 5]
print(product_except_self(nums))  # Output: [120, 60, 40, 30, 24]
```

In this implementation:

- We first calculate the products of all elements to the left and right of each element separately.
- Then, we multiply the corresponding elements from both arrays to get the final result.
- This approach avoids using division while still achieving the desired output.