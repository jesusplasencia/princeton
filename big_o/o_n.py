### family of algos that run in O(n)
def findElement(arr, n: int, key: int) -> bool:
    for i in range(n):
        if arr[i] == key:
            return True
    return False


def sumList(lst):
    total = 0
    for value in lst:
        total = total + value
    return total


def minimum(lst):
    if len(lst) == 0:
        return -1
    mini = lst[0]  # 1 instruction
    for i in range(1, len(lst)):  # n - 1 instructions
        mini = min(mini, lst[i])
    return mini  # 1 instruction
