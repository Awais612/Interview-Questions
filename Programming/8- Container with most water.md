<h3> You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. </h3>


![alt text](image.png)

`Educative`

```python
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    water = 0 
    left = 0 
    right = len(height) - 1
    while left < right:
        current_water = min(height[left], height[right]) * (right - left) 
        water = max(water, current_water)
        
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return water
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
```