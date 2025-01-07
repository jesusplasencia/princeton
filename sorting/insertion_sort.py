# Page 43: Introduction to Algorithms 3rd Edition
def insertion_sort_asc(arr):
    for j in range(1, len(arr)):
        key = arr[j];
        # insert A[j] into the sorted sequence A[1.. j - 1]
        i = j - 1;
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i];
            i = i - 1;
        arr[i + 1] = key;
    return arr;

def insertion_sort_desc(arr):
    for j in range(1, len(arr)):
        key = arr[j];
        # insert A[j] into the sorted sequence A[1.. j - 1]
        i = j - 1;
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i];
            i = i - 1;
        arr[i + 1] = key;
    return arr;

# linear search
def linear_search(arr, v):
    for idx, item in enumerate(arr):
        if (item == v): return idx;
    return -1; # NIL

arr = [5, 2, 4, 6, 1, 3];
arr = [31, 41, 59, 26, 41, 58];
sorted = insertion_sort_asc(arr);
print(sorted);

v = 59;
print(linear_search(sorted, v));
