# Max_Heapify: Function to maintain the max-heap property
def heapify(arr, n, i):
    """
    Ensures the subtree rooted at index `i` satisfies the max-heap property.
    A max-heap means every parent node is greater than or equal to its children.

    Parameters:
    - arr: List[int], the array representing the heap.
    - i: int, the index of the root of the subtree to heapify.

    The function modifies the input array in place.

    Running Time:
    - Best Case: O(1) (when the subtree rooted at `i` is already a valid max-heap)
    - Worst Case: O(log n) (when the element at `i` is moved all the way down the tree)
    - Average Case: O(log n) (depends on the height of the tree)

    Doctest:
    >>> arr = [3, 14, 1, 19, 8, 7, 4]
    >>> n = len(arr)
    >>> heapify(arr, n, 1)
    >>> arr
    [3, 19, 1, 14, 8, 7, 4]
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Converts an array into a max-heap.

    Parameters:
    - arr: List[int], the array to be heapified.

    Running Time:
    - O(n), where n is the size of the array. Although `max_heapify` is O(log n),
      this process applies it in a way that the total cost sums to O(n).

    Doctest:
    >>> arr = [3, 19, 1, 14, 8, 7, 4]
    >>> build_max_heap(arr)
    >>> arr
    [19, 14, 7, 3, 8, 1, 4]

    Explanation:
    - After heapifying the entire array, the root (index 0) is the largest element.
    """
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    """
    Sorts an array using the HeapSort algorithm.

    Parameters:
    arr (list): The list of elements to sort.

    Time Complexity:
    - Worst-case: O(n log n)
    - Average-case: O(n log n)
    - Best-case: O(n log n)

    Space Complexity:
    - O(1) (in-place sorting)

    Returns:
    None: The input array is sorted in-place.

    Doctests:
    >>> arr1 = [4, 10, 3, 5, 1]
    >>> heapsort(arr1)
    >>> arr1
    [1, 3, 4, 5, 10]

    >>> arr2 = [12, 11, 13, 5, 6, 7]
    >>> heapsort(arr2)
    >>> arr2
    [5, 6, 7, 11, 12, 13]

    >>> arr3 = []
    >>> heapsort(arr3)
    >>> arr3
    []

    >>> arr4 = [1]
    >>> heapsort(arr4)
    >>> arr4
    [1]

    >>> arr5 = [3, 3, 3, 3]
    >>> heapsort(arr5)
    >>> arr5
    [3, 3, 3, 3]
    """
    n = len(arr)

    # Build Max Heap
    build_max_heap(arr);

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)