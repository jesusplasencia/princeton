# Recursive Insertion Sort Time Complexity Recurrence
def insertion_sort_recurrence(n):
    if n == 1: return 0; # Base case: no cost for a single element
    return insertion_sort_recurrence(n - 1) + n;

# Verify the recurrence for insertion sort
def verify_insertion_sort(max_n):
    for n in range(1, max_n + 1):
        T_n = insertion_sort_recurrence(n)
        print(f"n = {n}, T(n) = {T_n}")

verify_insertion_sort(10)