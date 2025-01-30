from collections import Counter


def countingSort(arr):
    if not arr:
        return []

    # Count the occurrences of each element
    count = Counter(arr)

    # Sort the unique keys
    sortedKeys = sorted(count.keys())

    # Compute cumulative counts to determine positions
    for i in range(1, len(sortedKeys)):
        currentKey = sortedKeys[i]
        prevKey = sortedKeys[i - 1]
        count[currentKey] += count[prevKey]

    # Prepare the output array
    output = [0] * len(arr)

    # Build the output array by placing elements in their correct positions
    for num in reversed(arr):
        position = count[num] - 1
        output[position] = num
        count[num] -= 1  # Decrement for next occurrence

    return output


A = [1, 0, 1, 3, 1, 5, 3]
sortResult = countingSort(A)
print(sortResult)
