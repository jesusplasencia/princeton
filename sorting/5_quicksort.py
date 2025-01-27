def quicksort(A, lo, hi):
    # runtime complexity:
    # best-case: O(n log(n))
    # average-case: O(n log(n))
    # worst-case: O(n^2) when it is sorted
    if lo < hi:
        q = partition(A, lo, hi);
        quicksort(A, lo, q - 1);
        quicksort(A, q + 1, hi);

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[hi] = A[hi], A[i + 1]
    return i + 1

arr = [8, 2, 4, 7, 1, 3, 9, 6, 5];
# quicksort(arr, 0, len(arr) - 1);
# print(arr);

import random;
def randomize_partition(A, lo, hi):
    rnd_idx = random.randrange(lo, hi + 1);
    A[hi], A[rnd_idx] = A[rnd_idx], A[hi];
    return partition(A, lo, hi);

def randomize_quicksort(A, lo, hi):
    if lo < hi:
        q = randomize_partition(A, lo, hi);
        randomize_quicksort(A, lo, q - 1);
        randomize_quicksort(A, q + 1, hi);

arr = [8, 2, 4, 7, 1, 3, 9, 6, 5];
randomize_quicksort(arr, 0, len(arr) - 1);
print(arr);
