def largestRange(array):
    print("Array", array)
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    print("Hash Table of input Array:", nums)
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        while left in nums:
            print(left)
            nums[left] = False
            currentLength += 1
            left -= 1
        right = num + 1
        while right in nums:
            print(right)
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
        print(nums)
    print(bestRange)


test2 = [0,
         -5,
         9,
         19,
         -1,
         18,
         17,
         2,
         -4,
         -3,
         10,
         3,
         12,
         5,
         16,
         4,
         11,
         7,
         -6,
         -7,
         6,
         15,
         12,
         12,
         2,
         1,
         6,
         13,
         14,
         -2
         ]
test = [
    0,
    9,
    19,
    -1,
    18,
    17,
    2,
    10,
    3,
    12,
    5,
    16,
    4,
    11,
    8,
    7,
    6,
    15,
    12,
    12,
    2,
    1,
    6,
    13,
    14
]
largestRange(test2)
