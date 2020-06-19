# def isMonotonicArray(arr):
#     direction = arr[1] - arr[0]
#     for i in range(2, len(arr)):
#         if direction == 0:
#             direction = arr[i] - arr[i - 1]
#             print(direction, i)
#             continue
#         print("index:", i)
#         print(breaksDirection(direction, arr[i - 1], arr[i]))
#         if breaksDirection(direction, arr[i - 1], arr[i]):
#             return False          
#     return True


# def breaksDirection(direction, prevNum, currNum):
#     diff = currNum - prevNum
#     print("diff:", diff)
#     print("direction:", direction)
#     if direction > 0:
#         return diff < 0
#     return diff > 0
# def isMonotonicArray(arr):
#     isNonDecreasing = True
#     isNonIncreasing = True
#     for i in range(1, len(arr)):
#         if arr[i] < arr[i - 1]:
#             isNonIncreasing = False
#         if arr[i] > arr[i - 1]:
#             isNonDecreasing = False
#     return isNonDecreasing or isNonIncreasing


# arr = [134, 134, 2345, 3353, 4555, 5335, 5555, 5556, 6344, 74677, 88788, 88788, 98778, 105665, 11567788]
# negativeArr = [-x for x in arr]
# print(isMonotonicArray(negativeArr))