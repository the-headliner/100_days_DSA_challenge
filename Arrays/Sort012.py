# Brute force approach: --> Counting Frequencies
# Time Complexity:  O(n) - Traverse the array once to count frequencies.
# Space Complexity:   O(n) - Create a new array for the result.

def sort_012_brute_force_new_array(arr):   # Using For Loops and by Creating a New Array
    """

    Sort an array of 0, 1, and 2 using a new array and for loops.

    Parameters:
    arr (list): The input array containing 0s, 1s, and 2s.
    
    Returns:
    list: A newly created sorted array.

    """
    count_0 = count_1 = count_2 = 0

    # Count frequencies of 0, 1, and 2
    for num in arr:

        if num == 0:
            count_0 += 1

        elif num == 1:
            count_1 += 1

        else:
            count_2 += 1

    # Construct the sorted array

    sorted_array = []

    for k in range(count_0):
        sorted_array.append(0)

    for k in range(count_1):
        sorted_array.append(1)

    for k in range(count_2):
        sorted_array.append(2)

    return sorted_array

# Driver code
example = [2, 0, 2, 1, 1, 0]
print("Sorted Array (New Array):", sort_012_brute_force_new_array(example))




# Optimized Approach: --> Dutch National Flag Algorithm
# Time Complexity: O(n) - Each element is traversed once.
# Space Complexity: O(1) - Sorting is done in-place.

def sort_012_optimized(arr):
    """
    Sort an array consisting of 0, 1, and 2 using Dutch National Flag Algorithm.
    
    Parameters:
    arr (list): The input array containing 0s, 1s, and 2s.
    
    Returns:
    list: The sorted array.
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Driver code :

example = [2, 0, 2, 1, 1, 0]
print("Sorted Array (Optimized):", sort_012_optimized(example))

