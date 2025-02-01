### family of algos that run in O(n^2)
def bubbleSort(arr):
    """
    >>> A = [10, 2, 4, 5, 74, 21, 45]
    >>> bubbleSort(A)
    >>> A
    [2, 4, 5, 10, 21, 45, 74]
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped is False:
            break


def selectionSort(lst):
    sortedLst = []  # 1 instruction
    for _ in range(len(lst)):
        mini = min(lst)  # n instructions
        lst.remove(mini)  # n instructions
        sortedLst.append(mini)  # n instructions
    return sortedLst  # 1 instruction
