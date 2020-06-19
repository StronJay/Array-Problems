# def LongestPeak(array):
#     longestPeakLength = 0
#     i = 1
#     while i < len(array) - 1:
#         #         leftIdx + 1               rightIdx - 1
#         isPeak = array[i - 1] < array[i] > array[i + 1]
        
#         if not isPeak:
#             i += 1
#             continue

#         leftIdx = i - 2
#         while leftIdx >= 0 and array[leftIdx + 1] > array[leftIdx]:
#             leftIdx -= 1
#             print("left", leftIdx)
#         rightIdx = i + 2
#         while rightIdx < len(array) and array[rightIdx - 1] > array[rightIdx]:
#             rightIdx += 1
#             print("right", rightIdx)
#         currentPeakLength = rightIdx - leftIdx - 1
#         print(currentPeakLength)
#         longestPeakLength = max(currentPeakLength, longestPeakLength)
#         i = rightIdx
    
#     return longestPeakLength

# testArr = [
#     1,
#     1,
#     1,
#     2,
#     3,
#     10,
#     12,
#     -3,
#     -3,
#     2,
#     3,
#     45,
#     800,
#     99,
#     98,
#     0,
#     -1,
#     -1,
#     2,
#     3,
#     4,
#     5,
#     0,
#     -1,
#     -1
# ]
# print(LongestPeak(testArr))