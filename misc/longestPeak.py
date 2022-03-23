import math

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


def getLongestPeak(array):
    longestPeak = -math.inf
    index = 1

    while(index <= len(array) - 2):
        if not(array[index-1] < array[index] > array[index+1]):
            index += 1
            continue

        leftPtr = index-2
        while((leftPtr >= 0) and array[leftPtr+1] > array[leftPtr]):
            leftPtr -= 1

        rightPtr = index+2
        while((rightPtr <= len(array)-1) and array[rightPtr-1] > array[rightPtr]):
            rightPtr += 1

        currentLongestPeak = (rightPtr - leftPtr) - 1
        longestPeak = currentLongestPeak if(
            currentLongestPeak > longestPeak) else longestPeak

        index = rightPtr

    return longestPeak


print(
    getLongestPeak(array)
)
