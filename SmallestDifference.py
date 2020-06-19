def smallestDifferenceBetweenTwoArrays(array1, array2):
    array1.sort()
    array2.sort()
    print(array1)
    print(array2)
    print(len(array1))
    print(len(array2))
    smallestPair = []
    current = float("inf")
    smallest = float("inf")
    index1 = 0
    index2 = 0
    while index1 < len(array1) and index2 < len(array2):
        num1 = array1[index1]
        num2 = array2[index2]
        print(f"num1: {num1}")
        print(f"num2: {num2}")
        if num1 < num2:
            current = num2 - num1
            index1 += 1
        elif num2 < num1:
            current = num1 - num2
            index2 += 1
        else:
            return [num2, num1]
        #you can check for multiple variables and update them
        #all in the same loop! That's fucking cool
        if smallest > current:
            smallest = current
            print(f"smallest: {smallest}, index 1: {index1}, index 2: {index2}, current: {current}")
            smallestPair = [num1, num2]
            print(smallestPair)
            
    return smallestPair

array1 = [240, 124, 86, 111, 500, 84, 953, 3000, 89]
array2 = [1, 3, 954, 19, 8]
print(smallestDifferenceBetweenTwoArrays(array1, array2))