# Write a program to cyclically rotate an array by one.

# # arr=[1,2,3,4,5]

# Time Complexity: O(n) : Shifting elements requires iterating through the array once, which takes O(n) time.
# Space Complexity: O(1) : Only a constant amount of extra space is used to store the temporary element.

# Steps:
# Store the Last Element: Temporarily store the last element.
# Shift Elements: Move each element to the next position.
# Insert the Last Element: Place the stored last element at the beginning of the array.

def cyclic_rotate_arr_by1(arr):
    # Calculate the length of the array
    n = len(arr)
    temp = arr[n-1] # Store the last element of the array in a temporary variable

    # Loop from the last element to the first (excluding the first element)

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]   # Shift each element one position to the right
    arr[0] = temp  # Place the stored last element in the first position

    # Return the modified array
    return arr


# Driver code:
arr = [1, 2, 3, 4, 5]
print(cyclic_rotate_arr_by1(arr))  # Expected Output: [5, 1, 2, 3, 4]



# Optimized Approach  :  Using Reversal Algorithm
# Time Complexity: O(n) :Reversing parts of the array still involves iterating through the array elements, leading to O(n) time. 
# Space Complexity: O(1) :No additional space is required beyond a few variables, so it's constant.

# Steps:
# Reverse the Entire Array: Reverse the entire array.
# Reverse the First Part: Reverse the first part of the array (from start to the end of what was the last element).
# Reverse the Second Part: Reverse the second part of the array (from the start of what was the original array, minus one).

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def cyclic_rotate_arr_by1(arr):
    n = len(arr)
    # Step 1: Reverse the entire array
    reverse(arr, 0, n-1)
    # Step 2: Reverse the first part (first element only, since it's one rotation)
    reverse(arr, 0, 0)
    # Step 3: Reverse the second part (rest of the array)
    reverse(arr, 1, n-1)
    return arr



# Driver code:
arr = [1, 2, 3, 4, 5]
print(cyclic_rotate_arr_by1(arr)) 