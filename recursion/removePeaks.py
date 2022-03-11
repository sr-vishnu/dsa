"""
A really really relly Naive solution for the remvoe peaks with minimum replacements problem.

An element is a peak if it succeding and preceding elements are strictly lesser than it
NOTE: peaks doen't exist at the first and last indexes

EXAMPLE:

[1,5,1,5,1,5,1,5] => 1

becuase i can reach state [1,1,1,5,5,5,1,5] which has no peaks with just one replacement by replacing the 1st and 4th elements.

"""


array = [1,5,1,5,1,5,1,5]

from sys import maxsize


def isPeak(array,index):
    return True if(array[index-1]<array[index]>array[index+1]) else False

def doSwapAndCheckPeak(array,indexOne,indexTwo):

    newArray = list.copy(array)

    temp = newArray[indexOne]
    newArray[indexOne] = newArray[indexTwo]
    newArray[indexTwo] = temp

    if(indexOne == len(newArray)-1 or indexOne == 0):
        return newArray
    elif(not isPeak(array,indexOne)):
        return newArray
    else:
        return []


def countReplacements(array,index=1):
    if(index == len(array) - 1):
        return 0
    else:
        if not isPeak(array,index):
            return countReplacements(array,index+1)
        else:
            result = maxsize
            for i in range(0,len(array)):
                swappedArray = doSwapAndCheckPeak(array,i,index)
                if swappedArray:
                    tempResult = 1 + countReplacements(list.copy(swappedArray),index+1)
                else:
                    tempResult = maxsize
                if tempResult < result:
                    result = tempResult
            return result


replacements = countReplacements(array)

print(replacements)