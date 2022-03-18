from sys import maxsize

"""
given two arrays finds the pair with the smallest absolute difference between them.

([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]) => [28, 26]
"""

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]


def findSmallestAbsoluteDifference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)

    minDiff = maxsize
    minDiffArray = []
    arrayOnePtr = 0
    arrayTwoPtr = 0

    while(((arrayOnePtr <= len(arrayOne) - 1 and arrayTwoPtr <= len(arrayTwo) - 1))):

        currentMinDiff = abs(arrayOne[arrayOnePtr] - arrayTwo[arrayTwoPtr])

        if currentMinDiff < minDiff:
            minDiff = currentMinDiff
            minDiffArray = [arrayOne[arrayOnePtr], arrayTwo[arrayTwoPtr]]

        if((arrayTwo[arrayTwoPtr] < arrayOne[arrayOnePtr])):
            arrayTwoPtr += 1
        elif(arrayTwo[arrayTwoPtr] > arrayOne[arrayOnePtr]):
            arrayOnePtr += 1
        else:
            break

    return minDiffArray


print(findSmallestAbsoluteDifference(arrayOne, arrayTwo))
