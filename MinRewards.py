# def minRewards(scores):
#     #print(scores)
#     rewards = [1 for x in scores]
#     #print(rewards)
#     for i in range(1, len(scores)):
#         j = i - 1
#         print("iteration", i, "scores", scores)
#         print("rewards           ", rewards)
#         print("Passed", scores[i], scores[j])
#         if scores[i] > scores[j]:
#             rewards[i] = rewards[j] + 1
#             print(rewards[i], scores[i])
#         else:
#             while j >=0 and scores[j] > scores[j + 1]:
#                 rewards[j] = max(rewards[j], rewards[j + 1] + 1)
#                 j -= 1
#                 print("rewards j:",rewards[j], rewards[j + 1], "scores j:", scores[j])
#     print(rewards)
#     print(sum(rewards))

# def minRewards(scores):
#     print(scores)
#     rewards = [1 for x in scores]
#     localMinIdc = getLocalMinIdc(scores)
#     print(localMinIdc)
#     for localMinIdx in localMinIdc:
#         expandFromLocalMinIdx(localMinIdx, scores, rewards)
#     print(sum(rewards))
#     print(rewards)


# def getLocalMinIdc(scores):
#     if len(scores) == 1:
#         return [0]
#     localMinIdc = []
#     for i in range(len(scores)):
#         if i == 0 and scores[i] < scores[i + 1]:
#             localMinIdc.append(i)
#         if i == len(scores) - 1 and scores[i] < scores[i - 1]:
#             localMinIdc.append(i)
#         if i == 0 or i == len(scores) - 1:
#             continue
#         if scores[i] < scores[i - 1] and scores[i] < scores[i + 1]:
#             localMinIdc.append(i)
    
#     return localMinIdc


# def expandFromLocalMinIdx(minIdx, scores, rewards):
#     leftIdx = minIdx - 1
#     while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
#         rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
#         leftIdx -= 1
#     rightIdx = minIdx + 1
#     while rightIdx <= len(scores) - 1 and scores[rightIdx] > scores[rightIdx - 1]:
#         rewards[rightIdx] = rewards[rightIdx - 1] + 1
#         rightIdx += 1

# def minRewards(scores):
#     print(scores)
#     rewards = [1 for x in scores]
#     for i in range(1, len(scores)):
#         If you are comparing indices, make sure you account for
#         first and last idx. e.g. range(1, len(scores)) and
#         reversed(range(len(scores) - 1))
#         if scores[i] > scores[i - 1]:
#             rewards[i] = rewards[i - 1] + 1
#     for i in reversed(range(len(scores) - 1)):
#         if scores[i] > scores[i + 1]:
#             rewards[i] = max(rewards[i], rewards[i + 1] + 1)
#         print(i)
#     print(sum(rewards))
#     print(rewards)

# scores2 = [0, 4, 2, 1, 3]
# scores1 = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
# scores = [800,
#           400,
#           20,
#           10,
#           30,
#           61,
#           70,
#           90,
#           17,
#           21,
#           22,
#           13,
#           12,
#           11,
#           8,
#           4,
#           2,
#           1,
#           3,
#           6,
#           7,
#           9,
#           0,
#           68,
#           55,
#           67,
#           57,
#           60,
#           51,
#           661,
#           50,
#           65,
#           53]
# minRewards(scores)
