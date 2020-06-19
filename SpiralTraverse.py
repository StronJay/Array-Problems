# def test(arr):
#     # RECURSION SUXX
#     # need start/ end row/ col
#     results = []
#     spiralFill(arr, 0, len(arr) - 1, 0, len(arr[0]) - 1, results)
#     return results


# def spiralFill(arr, startRow, endRow, startCol, endCol, results):
#     if startRow > endRow or startCol > endCol:
#         return
#     for col in range(startCol, endCol + 1):
#         results.append(arr[startRow][col])
#     for row in range(startRow + 1, endRow + 1):
#         results.append(arr[row][endCol])
#     for col in reversed(range(startCol, endCol)):
#         #we already accounted for this in the for loop above
#         if startRow == endRow:
#             break
#         results.append(arr[endRow][col])
#     for row in reversed(range(startRow + 1, endRow)):
# #we already accounted for this in the for loop above
#         if startCol == endCol:
#             break
#         results.append(arr[row][startCol])

#     spiralFill(arr, startRow + 1, endRow - 1, startCol + 1, endCol - 1, results)


# def test(array):
#     results = []
#     startRow, endRow = 0, len(array) - 1
#     startCol, endCol = 0, len(array[0]) - 1
#     print(startRow, endRow, startCol, endCol)

#     while startRow <= endRow and startCol <= endCol:
#         for col in range(startCol, endCol + 1):
#             results.append(array[startRow][col])
#         for row in range(startRow + 1, endRow + 1):
#             results.append(array[row][endCol])
#         for col in reversed(range(startCol, endCol)):
#             if startRow == endRow:
#                 break
#             results.append(array[endRow][col])
#         for row in reversed(range(startRow + 1, endRow)):
#             if startCol == endCol:
#                 break
#             results.append(array[row][startCol])

#         startRow += 1
#         endRow -= 1
#         startCol += 1
#         endCol -= 1
#         print (results)
#         return results

# def spiralTraverse(array):
# 	results = []
# 	startRow, endRow = 0, len(array) - 1
# 	startCol, endCol = 0, len(array[0]) - 1
	
# 	while startRow <= endRow and startCol <= endCol:
# 		for col in range(startCol, endCol + 1):
# 			results.append(array[startRow][col])

# 		for row in range(startRow + 1, endRow + 1):
# 			results.append(array[row][endCol])
# 		for col in reversed(range(startCol, endCol)):
# 			if startRow == endRow:
# 				break
# 			results.append(array[endRow][col])
# 		for row in reversed(range(startRow + 1, endRow)):
# 			if startCol == endCol:
# 				break
# 			results.append(array[row][startCol])
# 		startRow += 1
# 		endRow -= 1
# 		startCol += 1
# 		endCol -= 1
# 	return results

# testArray2 = [
#     [1, 2, 3, 4],
#     [10, 11, 12, 5],
#     [9, 8, 7, 6]]

# testArray = [
#     [1, 2, 3],
#     [12, 13, 4],
#     [11, 14, 5],
#     [10, 15, 6],
#     [9, 8, 7]]

# print(test(testArray))