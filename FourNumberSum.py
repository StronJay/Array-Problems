def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array)):
        print(i)
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            #print("j-sum:", currentSum)
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
                print(f'Found it {difference}')

        for k in range(0, i):
            currentSum = array[i] + array[k]
            #print("k-sum:", currentSum)
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[i], array[k]]]
                #
            else:
                allPairSums[currentSum].append([array[i], array[k]])

    return quadruplets
    
testArray = [-10, -3, -5, 2, 2, 3, 15, -7, 28, -6, 12, 8, 11, 5]
print(fourNumberSum(testArray, 20))    
# def test():
#         allPairSums = {}
#         quadruplets = []
#         for i in range(1, len(array) - 1):
#             for j in range(i + 1, len(array)):
#                 currentSum = array[i] + array[j]
#                 difference = targetSum - currentSum
#                 if difference in allPairSums:
#                     for pair in allPairSums[difference]:
#                         quadruplets.append(pair + [array[i], array[j]])
#             for k in range(0, i):
#                 currentSum = array[i] + array[k]
#                 if currentSum not in allPairSums:
#                     allPairSums[currentSum] = [[array[k], array[i]]]
#                 else:
#                     allPairSums[currentSum].append([array[k], array[i]])
#         pass
#         return quadruplets