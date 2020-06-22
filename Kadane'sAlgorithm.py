test = [
    8,
    5,
    -9,
    1,
    3,
    -2,
    3,
    4,
    7,
    2,
    -18,
    6,
    3,
    1,
    -5,
    6,
    20,
    -23,
    15,
    1,
    -3,
    4
]


def kadanesAlgorithm(array):
    currentSubarraySum = array[0]
    largestSubarraySum = array[0]
    for i in range(1, len(array)):
        currentElement = array[i]
        currentSubarraySum = max(
            currentSubarraySum + currentElement, currentElement)
        largestSubarraySum = max(largestSubarraySum, currentSubarraySum)
    return largestSubarraySum

print(kadanesAlgorithm(test))