def twoSum(nums, target):
    # Initialize an empty hash map
    hashmap = {}

    # Iterate through the list with index and value
    for i, v in enumerate(nums):
        # Calculate the difference needed to reach the target
        diff = target - v

        # Check if the difference is already in the hash map
        if diff in hashmap:
            # If found, return the indices of the two numbers
            return hashmap[diff], i
        else:
            # Otherwise, store the current value and its index in the hash map
            hashmap[v] = i

    # If no pair is found, return False
    return False


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))  # Output: (0, 1)

# Time Complexity: O(n)
# Space Complexity: O(n)
