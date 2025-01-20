# HeapSort Running Time -> O(n*lg(n))
# Sort in Place
# max-heap property -> greatest element is at the root of the tree
# min-heap property -> smallest element is at the root of the tree

# HeapSort --> Max Heap

# Max_Heapify: Function to maintain the max-heap property
def max_heapify(arr, n, i):
    """
    Ensures the subtree rooted at index `i` satisfies the max-heap property.
    A max-heap means every parent node is greater than or equal to its children.

    Parameters:
    - arr: List[int], the array representing the heap.
    - n: int, the size of the heap.
    - i: int, the index of the root of the subtree to heapify.

    The function modifies the input array in place.

    Running Time:
    - Best Case: O(1) (when the subtree rooted at `i` is already a valid max-heap)
    - Worst Case: O(log n) (when the element at `i` is moved all the way down the tree)
    - Average Case: O(log n) (depends on the height of the tree)

    Why it's important:
    - This function is the foundation of the heap sort algorithm and other heap-based algorithms.
    - It maintains the heap structure, ensuring efficient operations like `insert` and `extract-max`.
    - The max-heap property enables quick access to the maximum element (root of the heap) in O(1) time.

    Doctest:
    >>> arr = [3, 19, 1, 14, 8, 7, 4]
    >>> n = len(arr)
    >>> max_heapify(arr, n, 1)
    >>> arr
    [3, 19, 7, 14, 8, 1, 4]

    Explanation:
    - Initially, the subtree rooted at index 1 (value 19) violates the max-heap property
      because one of its children (index 5, value 8) is smaller than its sibling (index 3, value 14).
    - After heapify, the subtree satisfies the max-heap property.

    """
    largest = i  # Initialize the largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

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
    # Start from the last non-leaf node and move upward
    for i in range((n // 2) - 1, -1, -1):
        max_heapify(arr, n, i)
