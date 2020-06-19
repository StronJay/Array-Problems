# def zigZagTraverse(array):
#     results = []
#     row, col = 0, 0
#     height = len(array) - 1
#     width = len(array[0]) - 1
#     goingDown = True
#     while not isOutOfBounds(row, col, width, height):
#         results.append(array[row][col])
#         if goingDown:
#             if row == height or col == 0:
#                 goingDown = False
#                 if row == height:
#                     col += 1
#                 else:
#                     row += 1
#             else:
#                 row += 1
#                 col -= 1
#         else:
#             if row == 0 or col == width:
#                 goingDown = True
#                 if col == width:
#                     row += 1
#                 else:
#                     col += 1
#             else:
#                 col += 1
#                 row -= 1
#     print(results)

# def isOutOfBounds(row, col, width, height):
#     return row < 0 or col < 0 or row > height or col > width

# array = [
#     [1, 3, 4, 10, 11],
#     [2, 5, 9, 12, 19],
#     [6, 8, 13, 18, 20],
#     [7, 14, 17, 21, 24],
#     [15, 16, 22, 23, 25]
# ]

# array2 = [
#     [1, 3, 4, 10, 11, 20],
#     [2, 5, 9, 12, 19, 21],
#     [6, 8, 13, 18, 22, 27],
#     [7, 14, 17, 23, 26, 28],
#     [15, 16, 24, 25, 29, 30]
#   ]

# zigZagTraverse(array)
