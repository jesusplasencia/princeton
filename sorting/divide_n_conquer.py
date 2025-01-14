# Page 96 (Introduction to Algorithms Third Edition 2009)
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

def max_subarray_problem_brute_force(arr):
    """
    Find the lowest and maximum values and give the profit you win
    i-th lowest < j-th maximum
    T(n) = Θ(n^2)
    >>> Stock = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97];
    >>> max_subarray_problem_brute_force(Stock)
    43
    """
    profit = 0;
    for i in range(len(arr)):
        profit_line = 0;
        key = arr[i];
        for j in range(i + 1, len(arr)):
            local_profit = arr[j] - key;
            if (local_profit > profit_line):
                profit_line = local_profit;
        if (profit_line > profit):
            profit = profit_line;
    return profit;

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf');
    summ = 0;
    max_left = mid
    for i in range(mid, low - 1, -1):
        summ = summ + A[i];
        if summ > left_sum:
            left_sum = summ;
            max_left = i;

    right_sum = float('-inf');
    summ = 0;
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        summ = summ + A[j];
        if summ > right_sum:
            right_sum = summ;
            max_right = j;

    return max_left, max_right, left_sum + right_sum;

def find_maximum_subarray(A, low, high):
    """
    T(n) = { 
                O(1), n = 1
                2T(n/2) + O(n)
            }
    >>> Profits = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7];
    >>> find_maximum_subarray(Profits, 0, len(Profits) - 1);
    (7, 10, 43)
    """
    if high == low: # Base case: only one element
        return low, high, A[low];
    else:
        mid = (low + high) // 2;
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid);
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high);
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high);
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum;
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum;
        else:
            return cross_low, cross_high, cross_sum;