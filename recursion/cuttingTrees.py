from sys import maxsize

"""
The problem: Given an array find the min number of edits needed to be done to make the array strictly alternating

examples:
[5, 4, 3, 2, 6] => 1
[3, 7, 4, 5] => 0

This implementation is the realization of the recurrence relation given at 
https://cs.stackexchange.com/questions/116854/minimum-number-of-tree-cuts-so-that-each-pair-of-trees-alternates-between-strict
"""


def stepUp(CurrentIndex,array,LastIndex):
    if(CurrentIndex == LastIndex):
        return 0
    elif(array[CurrentIndex] < array[CurrentIndex +1]):
        return stepDown(CurrentIndex+1, array, LastIndex)
    else:
        return maxsize

def stepUpAndCut(CurrentIndex,array,LastIndex):
    if(CurrentIndex == LastIndex):
        return 1
    elif(array[CurrentIndex + 1] > 2):
        return 1 + stepDown(CurrentIndex+1, array, LastIndex)
    else:
        return maxsize

def stepDown(CurrentIndex,array,LastIndex):
    if(CurrentIndex == LastIndex):
        return 0
    elif(array[CurrentIndex] > array[CurrentIndex +1]):
        return min(
            stepUp(CurrentIndex+1,array,LastIndex),
            stepUpAndCut(CurrentIndex+1,array,LastIndex)
        )
    else:
        return maxsize



array = [3, 7, 4, 5]
lastIndex = len(array) -1 


print(min(
    stepUp(0,array,lastIndex),
    stepUpAndCut(0,array,lastIndex),
    stepDown(0,array,lastIndex)
))




