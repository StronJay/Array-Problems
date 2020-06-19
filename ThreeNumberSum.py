def test(array, targetSum):
    # sort your arrayay Jay nlog(n)
    array.sort()
    print(array)
    triplets = []
    for i in range(len(array) - 2):
        leftPointer = i + 1
        rightPointer = len(array) - 1
        print(f"{leftPointer}, `leftPointer` {rightPointer} `rightPointer`")
        while leftPointer < rightPointer:
            currentSum = array[i] + array[leftPointer] + array[rightPointer]
            print(f"currentSum: {currentSum}" )
            print(f"leftPointer: {leftPointer}" )
            print(f"rightPointer: {rightPointer}" )
            if currentSum == targetSum:
                triplets.append([array[i], array[rightPointer], array[leftPointer]])
                print(triplets, leftPointer, rightPointer, i)
                leftPointer += 1
                rightPointer -= 1
            elif currentSum < targetSum:
                leftPointer += 1
                #if currentSum > targetSum:
            else:
                rightPointer -= 1
    return triplets


array = [12, 3, 1, 2, -6, 5, 0, -8, -1, 6]
targetSum = 0
print(test(array, targetSum))