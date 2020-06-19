# def ValidateSS(array, sequence):
#     arrayPointer = 0
#     sequencePointer = 0
#     print(array, len(array), len(sequence))
#     while sequencePointer < len(sequence) and arrayPointer < len(array):
#         if sequence[sequencePointer] == array[arrayPointer]:
#             print(sequence[sequencePointer], array[arrayPointer])
#             sequencePointer += 1
#         arrayPointer += 1
#         print(sequencePointer, "sequencePointer", arrayPointer)
#     return sequencePointer == len(sequence)

# def test(array, sequence):
#     seqIdx = 0
#     i = 0
#     print(array)
#     for i in range(len(array) - 1):
#         print(i, f"{array[i]}")
#         print(seqIdx)
#         i += 1
#         if seqIdx == len(sequence):
#             break
#         if array[i] == sequence[seqIdx]:
#             seqIdx += 1
#             print(seqIdx)
#     return seqIdx == len(sequence)
    


# array = [5, 1, 22, 25, 1, 6, -1, 10]
# sequence = [1, 6, -1, 10]

# print(test(array, sequence))