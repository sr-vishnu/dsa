

def getFirstDuplicate(array):
    counterArray = [0 for _ in range(len(array)+1)]

    for element in array:
        elementCount = counterArray[element]

        if(elementCount <= 1):
            counterArray[element] = element+1
        else:
            return element

    return -1
