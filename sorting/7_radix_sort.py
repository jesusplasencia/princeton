def countingSort(arr, exp1):
    n = len(arr)

    # the output array elements that will have the sorted array
    output = [0] * n

    # initialize count array as 0
    count = [0] * (10)

    # store count of ocurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # change count[i] so that count[i] now contains actual position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    maxItem = max(arr)
    exp = 1
    while maxItem / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
    return arr


# Driver code
arr = [171, 48, 75, 91, 804, 23, 1, 66]

# Function Call
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
