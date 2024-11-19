# Brute Force Approach --> Using Extra Space
# Time Complexity: O(n) - Single traversal of the array.
# Space Complexity: O(n) - Requires an additional array to store the result.

# Steps:
# Traverse the array and collect all the negative elements in one list.
# Collect all the positive or zero elements in another list.
# Combine the two lists and overwrite the original array.

def move_negatives_brute_force(arr):
    """
    Move all negative elements to one side of the array using extra space.
    
    Parameters:
    arr (list): Input array.
    
    Returns:
    list: The rearranged array.
    """
    negatives = []
    non_negatives = []
    
    # Separate negatives and non-negatives
    for num in arr:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    
    # Combine the two lists
    result = negatives + non_negatives
    return result

# Driver code

arr = [1, -2, 3, -4, -1, 5, -6]
print("Rearranged Array (Brute Force):", move_negatives_brute_force(arr))


# Optimized Approach --> In-Place Partitioning (Two-Pointer Technique)
# Time Complexity: O(n) - Single traversal of the array.
# Space Complexity: O(1) - No extra space used.

# Steps:
# Use two pointers:
# left starts at the beginning of the array.
# right iterates through the array.
# Whenever a negative number is found at the right pointer, swap it with the number at the left pointer and move left forward.
# This partitions the array into negatives on the left and non-negatives on the right.


def move_negatives_optimized(arr):
    """
    Move all negative elements to one side of the array in-place using two-pointer technique.
    
    Parameters:
    arr (list): Input array.
    
    Returns:
    list: The rearranged array.
    """
    left = 0
    for right in range(len(arr)):
        if arr[right] < 0:  # Found a negative number
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    return arr


# Driver code
arr = [1, -2, 3, -4, -1, 5, -6]
print("Rearranged Array (Optimized):", move_negatives_optimized(arr))
