def insertion_sort_asc(arr):
    # Running time O (n²) - theta n - squared
    for j in range(1, len(arr)):
        key = arr[j];
        # insert A[j] into the sorted sequence A[0 - k] -> k = j - 1
        i = j - 1;
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i];
            i = i - 1;
        arr[i + 1] = key;
    return arr;

def insertion_sort_desc(arr):
    # Running time O (n²) - theta n - squared
    for j in range(1, len(arr)):
        key = arr[j];
        # insert A[j] into the sorted sequence A[0 - k] -> k = j - 1
        i = j - 1;
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i];
            i = i - 1;
        arr[i + 1] = key;
    return arr;

def cubic_function(n):
    # Running time O (n^3) - theta n - cubic
    return ((n ** 3) / 1000) - (100 * (n ** 2)) - (100 * n) + 3;

def sum_binary_array(A, B):
    # Running time O (n)
    n = len(A);
    C = [0 for _ in range(n + 1)];
    carry = 0;
    for i in range(n, 0, -1): # [n -- 1]
        summ = A[i - 1] + B[i - 1] + carry;
        carry = summ // 2;
        C[i] = summ % 2;
    C[0] = carry;
    return C;

def linear_search(arr, v):
    # Running Time O(n) - theta n
    # Best case scenario O(1) -> item is in the first position
    # Worst case scenario O(n) -> item is in the last position of the array or not present
    for idx, item in enumerate(arr):
        if (item == v): return idx;
    return -1; # NIL

# arr = [5, 2, 4, 6, 1, 3];
# arr = [31, 41, 59, 26, 41, 58];
# sorted = insertion_sort_asc(arr);
# print(sorted);

# v = 59;
# print(linear_search(sorted, v));


# A = [1,0,1,1];
# 𝐵 = [1,1,0,1];
# C = sum_binary_array(A, B);
# print(C);


def selective_sort(A):
    # Running Time O (n³) - theta n-squared
    N = len(A);
    for j in range(0, N - 1):
        key = A[j];
        i = j + 1;
        idxSmallest = j;
        while i <= N - 1:
            if (A[i] < A[idxSmallest]):
                idxSmallest = i;
            i = i + 1;
        A[j], A[idxSmallest] = A[idxSmallest], key; # nice swap :)
    return A;

A = [13, 15, 8, 9, 4, 5];
B = selective_sort(A);
print(B);