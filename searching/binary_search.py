def binary_search_recursive(arr, target, left, right):
    if left > right: return -1;
    mid = (left + right) // 2;
    if (arr[mid] == target): return mid;
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1);
    else:
        return binary_search_recursive(arr, target, mid + 1, right);

# Binary Search Implementation (Iterative)
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage of binary search
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
index_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
index_iterative = binary_search_iterative(arr, target)
print(f"Recursive Binary Search: Target {target} found at index {index_recursive}")
print(f"Iterative Binary Search: Target {target} found at index {index_iterative}")