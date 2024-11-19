# find the Union and Intersection of two sorted arrays

# Union: A list of unique elements present in either of the arrays.
# Intersection: A list of common elements present in both arrays.

# Brute Force Approach --> Using Sets
# Time Complexity:
# Union: O(m + n) - Convert arrays to sets and merge them.
# Intersection: O(m * n) - Nested loop for finding common elements.
# Space Complexity: O(m + n) - For storing sets or results.


def union_brute_force(arr1, arr2):
    """
    Find the union of two sorted arrays using sets.
    
    Parameters:
    arr1, arr2 (list): Input sorted arrays.
    
    Returns:
    list: The union of the two arrays.
    """
    return sorted(set(arr1) | set(arr2))  # Union of sets


def intersection_brute_force(arr1, arr2):
    """
    Find the intersection of two sorted arrays using nested loops.
    
    Parameters:
    arr1, arr2 (list): Input sorted arrays.
    
    Returns:
    list: The intersection of the two arrays.
    """
    result = []
    for num in arr1:
        if num in arr2 and num not in result:  # Avoid duplicates
            result.append(num)
    return result

# Driver code

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
print("Union (Brute Force):", union_brute_force(arr1, arr2))
print("Intersection (Brute Force):", intersection_brute_force(arr1, arr2))


# Optimized Approach --> Using Two-Pointer Technique
# Time Complexity: O(m + n) - Traverse both arrays once.
# Space Complexity: O(m + n) - Store results in separate lists.

# Steps:
# Use two pointers i and j starting at the beginning of arr1 and arr2.

# For Union:
# Add the smaller element to the result and increment the respective pointer.
# Skip duplicates by ensuring the element isn't already in the result.

# For Intersection:
# If the elements are equal, add to the result and increment both pointers.


"""
def union_optimized(arr1, arr2):
    # """
    # Find the union of two sorted arrays using two-pointer technique.
    
    # Parameters:
    # arr1, arr2 (list): Input sorted arrays.
    
    # Returns:
    # list: The union of the two arrays.
    """
    i, j = 0, 0
    union_result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union_result or union_result[-1] != arr1[i]:
                union_result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not union_result or union_result[-1] != arr2[j]:
                union_result.append(arr2[j])
            j += 1
        else:  # arr1[i] == arr2[j]
            if not union_result or union_result[-1] != arr1[i]:
                union_result.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements
    while i < len(arr1):
        if not union_result or union_result[-1] != arr1[i]:
            union_result.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not union_result or union_result[-1] != arr2[j]:
            union_result.append(arr2[j])
        j += 1

    return union_result


def intersection_optimized(arr1, arr2):
    """
   ''' Find the intersection of two sorted arrays using two-pointer technique.
    
    Parameters:
    arr1, arr2 (list): Input sorted arrays.
    
    Returns:
    list: The intersection of the two arrays.
    """
    i, j = 0, 0
    intersection_result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:  # arr1[i] == arr2[j]
            if not intersection_result or intersection_result[-1] != arr1[i]:
                intersection_result.append(arr1[i])
            i += 1
            j += 1

    return intersection_result

# Driver code

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
print("Union (Optimized):", union_optimized(arr1, arr2))
print("Intersection (Optimized):", intersection_optimized(arr1, arr2))





"""













