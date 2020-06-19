# def twoNumberSum(array, tSum):
#     for i in range(len(array) - 1):
#         num1 = array[i]
#         print(num1, )
#         for j in range(i + 1, len(array)):
#             num2 = array[j]
#             print(num2, "num2")
#             if num1 + num2 == tSum:
#                 return [num1, num2]
#     return []
# def twoNumberSum(array, tSum):
#     nums = {}
#     print(nums)
#     for num in array:
#         print(num)
#         pMatch = tSum - num
#         print(pMatch)
#         if pMatch in nums:
#              return [pMatch, num]
#         else:
#             nums[num] = True
#             print(nums[num])
#             print(nums)
#     return []
# def twoNumberSum(arr, tSum):
#     arr.sort()
#     print(arr)
#     left = 0
#     right = len(arr) - 1
#     print(left, right)
#     while left < right:
#         currSum = arr[left] + arr[right]
#         print(currSum)
#         if currSum == tSum:
#             return [arr[left], arr[right]]
#         elif currSum < tSum:
#             left += 1
#             print(left, "left")
#         elif currSum > tSum:
#             right -= 1
#             print(right, "right")
#     return []
    

# arr = [3, 5, -4, 33, 11, 1, -1, 6]
# tSum = 5
# print(twoNumberSum(arr, tSum))

# test2 = {"a": "apples", "b": [2,3, 4, 5, 6], "c": 42}
# test.values()
# # test2.values()
# def test(array):
#    return (array)

#print(test(array))
