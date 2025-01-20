# HeapSort Running Time -> O(n*lg(n))
# Sort in Place
# max-heap property -> greatest element is at the root of the tree
# min-heap property -> smallest element is at the root of the tree

# HeapSort --> Max Heap

# Max_Heapify: Function to maintain the max-heap property
def max_heapify(array, n = len(array), idx):
    """
    Ensures the max-heap property for a subtree rooted at index `i`.

    Args:
        arr (list): The heap array.
        n (int): The size of the heap.
        i (int): The index of the root of the subtree.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Example:
    >>> arr = [1, 14, 10, 8, 7, 9, 3, 2, 4, 6]
    >>> max_heapify(arr, len(arr), 1)
    >>> arr
    [14, 8, 10, 6, 7, 9, 3, 2, 4, 1]
    """
    largest = idx;
    left = 2 * idx + 1;
    right = 2 * idx + 2;
    
    # Check if the left child exists and is greater than the root
    if left < n and array[left] > array[largest]:
        largest = left;
    
    # Check if the right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right;

    # If the largest is not the root, swap and continue heapifying
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, len(arr), largest)