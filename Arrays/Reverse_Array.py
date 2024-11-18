
# Brute force approach: --> Creating a New Array
# Time Complexity: O(n), Traverse the array once from the last element to the first.
# Space Complexity: O(n), because a new array is created to store the reversed elements. Appending takes constant time, so the overall time remains O(n)



def reverse_array_brute(arr):
    """
    Reverses an array using brute force by creating a new array.
    
    Args:
    arr (list): Input array
    
    Returns:
    list: Reversed array
    """
    # Initialize an empty array to store reversed elements
    reversed_arr = []
    
    # Traverse the input array from the last element to the first
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])  # Append the current element to the new array
    
    return reversed_arr

# Driver code:

arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)
print("Reversed Array (Brute):", reverse_array_brute(arr))



# Optimized Approach ---> Two-Pointer Technique
# Time Complexity: Step 1: Use a while loop to swap elements at two indices (left and right).
# Step 2: Each swap operation takes constant time, and the loop runs n/2 times (where n is the size of the array).
# Overall Time Complexity: O(n)

# Space Complexity: No extra array or data structure is used. The reversal is done in place.
# Overall Space Complexity: O(1)



def reverse_array_optimized(arr):
    """
    Reverses an array in place using two-pointer technique.
    
    Args:
    arr (list): Input array (modified in place)
    
    Returns:
    list: Reversed array
    """
    # Initialize two pointers
    left = 0  # Start pointer
    right = len(arr) - 1  # End pointer
    
    # Swap elements until the pointers meet
    while left < right:
        # Swap the elements at the 'left' and 'right' indices
        arr[left], arr[right] = arr[right], arr[left]
        # Move the pointers closer to each other
        left += 1
        right -= 1
    
    return arr

# Driver code:
arr = [1, 2, 3, 4, 5]

print("Original Array:", arr)
print("Reversed Array (Optimized):", reverse_array_optimized(arr))



