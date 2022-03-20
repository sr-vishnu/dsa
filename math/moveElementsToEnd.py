
array = [4, 5, 4, 6, 4, 1, 45, 1, 3543, 1, 4543, 3, 1, 4, 33, 1, 1, 1]
element = 1


def moveElementsToEndOfArrayInPlace(array, element):
    leftPtr = 0
    rightPtr = len(array) - 1

    while(leftPtr <= rightPtr):
        if(array[leftPtr] != element):
            leftPtr += 1
        elif(array[rightPtr] == element):
            rightPtr -= 1
        else:
            array[leftPtr], array[rightPtr] = array[rightPtr], array[leftPtr]
            leftPtr += 1
            rightPtr -= 1

    return array


print(
    moveElementsToEndOfArrayInPlace(array, element)
)
