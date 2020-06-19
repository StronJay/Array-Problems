# def apartmentHunting(blocks, reqs):
#     print([["Block:", block] for block in blocks])
#     print("Requirements:", reqs)
#     maxDistancesAtBlocks = [float("-inf") for block in blocks]
#     for i in range(len(blocks)):
#         for req in reqs:
#             print(req)
#             closestReqDistance = float("inf")
#             for j in range(len(blocks)):
#                 if blocks[j][req]:
#                     closestReqDistance = min(
#                         closestReqDistance, distanceBetween(i, j))
#                     print(blocks[j][req], "i:", i, "j:", j,
#                           "Closest Requirement Distance:", closestReqDistance)
#             maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
#             print(maxDistancesAtBlocks)
#     print(getIdxAtMinValue(maxDistancesAtBlocks))


# def getIdxAtMinValue(array):
#     idxAtMinValue = 0
#     minValue = float("inf")
#     print(array)
#     for i in range(len(array)):
#         currentValue = array[i]
#         if currentValue < minValue:
#             minValue = currentValue
#             idxAtMinValue = i
#     return idxAtMinValue


# def distanceBetween(a, b):
#     return abs(a - b)

# def apartmentHunting(blocks, reqs):
#     print(blocks)
#     print(reqs)
#     minDistancesFromBlocks = list(
#         map(lambda req: getMinDistances(blocks, req), reqs))
#     print("MINIMUM DISTANCE FROM REQ:", minDistancesFromBlocks)
#     maxDistancesAtBlocks = getMaxDistancesAtBlocks(
#         blocks, minDistancesFromBlocks)
#     print("MAX DISTANCE AT BLOCKS:", maxDistancesAtBlocks)
#     print(getIdxAtMinValue(maxDistancesAtBlocks))


# def getMinDistances(blocks, req):
#     minDistances = [0 for block in blocks]
#     closestReqIdx = float("inf")
#     for i in range(len(blocks)):
#         print(minDistances)
#         if blocks[i][req]:
#             print(req)
#             closestReqIdx = i
#         minDistances[i] = distanceBetween(i, closestReqIdx)
#     for i in reversed(range(len(blocks))):
#         print("i2", minDistances)
#         if blocks[i][req]:
#             closestReqIdx = i
#         minDistances[i] = min(
#             minDistances[i], distanceBetween(i, closestReqIdx))
#     return minDistances


# def distanceBetween(a, b):
#     return abs(a - b)


# def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
#     maxDistancesAtBlocks = [0 for block in blocks]
#     for i in range(len(blocks)):
#         minDistancesAtBlock = list(
#             map(lambda distances: distances[i], minDistancesFromBlocks))
#         maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
#     return maxDistancesAtBlocks


# def getIdxAtMinValue(array):
#     idxAtMinValue = 0
#     minValue = float("inf")
#     for i in range(len(array)):
#         currentValue = array[i]
#         if currentValue < minValue:
#             minValue = currentValue
#             idxAtMinValue = i
#     return idxAtMinValue


# blocks = [
#     {"gym": True, "pool": False, "school": True, "store": False},
#     {"gym": False, "pool": False, "school": False, "store": False},
#     {"gym": False, "pool": False, "school": True, "store": False},
#     {"gym": False, "pool": False, "school": False, "store": False},
#     {"gym": False, "pool": False, "school": False, "store": True},
#     {"gym": True, "pool": False, "school": False, "store": False},
#     {"gym": False, "pool": False, "school": False, "store": False},
#     {"gym": False, "pool": False, "school": False, "store": False},
#     {"gym": False, "pool": False, "school": False, "store": False},
#     {"gym": False, "pool": False, "school": True, "store": False},
#     {"gym": False, "pool": True, "school": False, "store": False}
# ]
# reqs = ["gym", "pool", "school", "store"]
# apartmentHunting(blocks, reqs)
