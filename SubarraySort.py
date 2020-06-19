# def subarraySort(array):
#     minOutOfOrder = float("inf")
#     maxOutOfOrder = float("-inf")
#     print(array)
#     for i in range(len(array)):
#         num = array[i]
#         print(isOutOfOrder(i, num, array), i, num)
#         if isOutOfOrder(i, num, array):
#             minOutOfOrder = min(minOutOfOrder, num)
#             maxOutOfOrder = max(maxOutOfOrder, num)
#     if maxOutOfOrder == float("-inf"):
#         return [-1, -1]
#     print(minOutOfOrder, maxOutOfOrder)
#     subarrayLeftIdx = 0
#     while minOutOfOrder >= array[subarrayLeftIdx]:
#         subarrayLeftIdx += 1
#         print("Left:",array[subarrayLeftIdx])
#     subarrayRightIdx = len(array) - 1
#     while maxOutOfOrder <= array[subarrayRightIdx]:
#         print("Right:", array[subarrayRightIdx])
#         subarrayRightIdx -= 1
#     return[subarrayLeftIdx, subarrayRightIdx]

# def isOutOfOrder(i, num, array):
#     if i == 0:
#         return num > array[i + 1]
#     if i == len(array) - 1:
#         return num < array[i - 1]
#     return num > array[i + 1] or num < array [i - 1]

# test2 = [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
# test = [-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]
# print(subarraySort(test2))