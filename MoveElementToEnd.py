# def moveElementToEnd(array, numToMove):
#     i = 0
#     j = len(array) - 1
#     print(i, j)
#     while i < j:
        
#         while i < j and array[j] == numToMove:
#             j -= 1
#         # pull out i < j to see it all fall apart
#             print("j at", j)
#             print("i at", i)
#         if array[i] == numToMove:
#             swap(i, j, array)
#         i += 1
#     return array


# def swap(i, j, array):
#     array[i], array[j] = array[j], array[i]


# array = [2, 1, 2, 2, 2, 3, 4, 2]
# numToMove = 2
# print(moveElementToEnd(array, numToMove))
