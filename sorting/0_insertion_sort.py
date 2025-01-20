def insertion_sort(arr):
    """
    In-place insertion sort implementation.
    O(n^2)
    Args:
        arr (list): The list to be sorted.

    >>> arr = [12, 11, 13, 5, 6]
    >>> insertion_sort(arr)
    >>> arr
    [5, 6, 11, 12, 13]

    >>> arr = [31, 41, 59, 26, 41, 58]
    >>> insertion_sort(arr)
    >>> arr
    [26, 31, 41, 41, 58, 59]

    >>> arr = []
    >>> insertion_sort(arr)
    >>> arr
    []

    >>> arr = [1]
    >>> insertion_sort(arr)
    >>> arr
    [1]
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key