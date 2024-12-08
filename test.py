def min_operations(nums):
    nums.sort()  # Sorting is removed since it's unnecessary
    arr = []

    while nums:
        # Using slicing to efficiently remove the first two elements
        alice_value, bob_value = nums[:2]
        nums = nums[2:]

        # Appending values to the result array in the desired order
        arr.append(bob_value)
        arr.append(alice_value)

    return arr

nums = [3, 1, 2, 4]
print(min_operations(nums))