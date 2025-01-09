# Page 60 (Introduction to Algorithms Third Edition 2009)
# python -m doctest divide_n_conquer.py -v
def merge(A, p, q, r):
    """
    Merge Array by bisecting in two arrays [p..q] [q + 1..r] (both sorted prior the execution of the algorithm)
    >>> A = [3, 26, 41, 52, 9, 38, 49, 57];
    >>> p = 1;
    >>> r = len(A);
    >>> q = r // 2;
    >>> OUT = merge(A, p, q, r);
    >>> print(OUT);
    [3, 9, 26, 38, 41, 49, 52, 57]
    """
    N1 = q - p + 1;
    N2 = r - q;

    L = [0 for _ in range(N1)];
    R = [0 for _ in range(N2)];

    for i in range(N1):
        L[i] = A[p + i - 1];
    for j in range(N2):
        R[j] = A[q + j];

    i = j = k = 0;
    while i < N1 and j < N2:
        if L[i] <= R[j]:
            A[k] = L[i];
            i = i + 1;
        else:
            A[k] = R[j];
            j = j + 1;
        k = k + 1;

    if i < N1:
        A[k] = L[i];
        i = i + 1;
        k = k + 1;

    if j < N2:
        A[k] = R[j];
        j = j + 1;
        k = k + 1;

    return A;

def merge_sort(arr):
    """
    Merge Sort Array Algorithm In-Place
    >>> A = [3, 41, 52, 26, 38, 57, 9, 49]
    >>> merge_sort(A);
    >>> A
    [3, 9, 26, 38, 41, 49, 52, 57]
    """
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        i = j = k = 0
        
        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1