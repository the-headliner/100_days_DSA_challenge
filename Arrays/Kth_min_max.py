# Brute force approach: --> Sorting the Array
# Time Complexity:  O(nlogn), due to sorting the array.
# Space Complexity: O(1), as sorting is done in place.


def kth_min_max_brute(arr, k):
    """
    Finds the kth smallest and kth largest elements in an array using sorting.
    
    Args:
    arr (list): Input array
    k (int): The position (1-based) to find
    
    Returns:
    tuple: (kth_smallest, kth_largest)
    """
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Retrieve kth smallest and kth largest
    kth_smallest = arr[k - 1]  # kth smallest (1-based indexing)
    kth_largest = arr[-k]  # kth largest (negative indexing)
    
    return (kth_smallest, kth_largest)

# Driver code:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print("Kth Min and Max (Brute):", kth_min_max_brute(arr, k))



# Optimized Approach :Using Heaps [Max and Min]
# Time Complexity: O(n+klogn): O(n) to build each heap.O(klogn) to pop k elements from both heaps.
# Space Complexity:  O(n): Two heaps are created (one for smallest, one for largest)


import heapq

def kth_min_max_heap(arr, k):
    """
    Finds the kth smallest and kth largest elements using Min Heap and Max Heap.
    
    Args:
    arr (list): Input array
    k (int): The position (1-based) to find
    
    Returns:
    tuple: (kth_smallest, kth_largest)
    """
    # Step 1: Min Heap for kth smallest
    min_heap = arr.copy()
    heapq.heapify(min_heap)  # O(n) to build the Min Heap
    for _ in range(k - 1):   # Remove k-1 smallest elements
        heapq.heappop(min_heap)
    kth_smallest = heapq.heappop(min_heap)  # kth smallest element
    
    # Step 2: Max Heap for kth largest (simulated with negation)
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)  # O(n) to build the Max Heap
    for _ in range(k - 1):   # Remove k-1 largest elements
        heapq.heappop(max_heap)
    kth_largest = -heapq.heappop(max_heap)  # kth largest element (negated back)
    
    return (kth_smallest, kth_largest)

# Driver code:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print("Kth Min and Max (Heap):", kth_min_max_heap(arr, k))
