k = 0
rounds = 0
n = 16
for i in range(n // 2, n):
    step = 2
    while step < n:
        k = k + n // 2
        rounds = rounds + 1
        step *= 2
print("rounds: {0}".format(rounds))
print("k: {0}".format(k))


## this is an algorithm that runs in O(log(n))
# def binarySearch(arr, left: int, right: int, x: int) -> int:
#     if right >= left:
#         mid = (left + (right - left)) // 2
#         if arr[mid] == x:
#             return mid
#         if arr[mid] > x:
#             return binarySearch(arr, left, mid, x)
#         return binarySearch(arr, mid, right, x)
#     return -1
#
#
# ## Time complexity -> O(logN)
# # N = 18
# # i = N
# # a = 0
# #
# # while i > 0:
# #     print(a, end=" ")
# #     a = a + i
# #     i = i // 2

# N = int(input("Range to guess: "))
# jackpot = random.randint(0, N)
#
# iter = 0
# left = 0
# right = N
#
# while right >= left:
#     mid = left + (right - left) // 2
#     iter = iter + 1
#     if mid == jackpot:
#         print("jackpot:", jackpot)
#         break
#     elif mid > jackpot:
#         right = mid - 1
#     else:
#         left = mid + 1
# print("iterations:", iter)
