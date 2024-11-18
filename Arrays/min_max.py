# Brute force approach: --> Traverse the Array Twice
# Time Complexity:  O(2n), as we traverse the array twice to find min and max.
# Space Complexity: O(1), no additional space is used.


def find_min_max_brute(arr):
    """
    Finds the minimum and maximum value in an array using brute force.
    
    Args:
    arr (list): Input array
    
    Returns:
    tuple: (min_value, max_value)
    """
    # Find the minimum value in the array
    min_value = float('inf')  # Initialize with infinity
    for num in arr:
        if num < min_value:
            min_value = num

    # Find the maximum value in the array
    max_value = float('-inf')  # Initialize with negative infinity
    for num in arr:
        if num > max_value:
            max_value = num

    return (min_value, max_value)

# Driver code:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Min and Max (Brute):", find_min_max_brute(arr))



# Optimized Approach : Single Traversal
# Time Complexity:  O(n), as we traverse the array once to find both min and max.
# Space Complexity: O(1), no additional space is used.


def find_min_max_optimized(arr):
    """
    Finds the minimum and maximum value in an array using a single traversal.
    
    Args:
    arr (list): Input array
    
    Returns:
    tuple: (min_value, max_value)
    """
    # Initialize min and max with the first element of the array
    min_value = max_value = arr[0]

    # Traverse the array and update min and max
    for num in arr:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    return (min_value, max_value)

# Driver code:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print("Min and Max (Optimized):", find_min_max_optimized(arr))
