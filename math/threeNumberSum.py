"""
gets the triplets which sums up to a given targetSum

([12, 3, 1, 2, -6, 5, -8, 6],0) => [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""


array = [12, 3, 1, 2, -6, 5, -8, 6]


def getThreeNumSum(array, targetSum):
    array = sorted(array)
    result = []
    for index in range(0, len(array)-2):
        leftPtr = index+1
        rightPtr = len(array)-1

        while(leftPtr < rightPtr):
            _sum = array[index] + array[leftPtr] + array[rightPtr]
            if(_sum < targetSum):
                leftPtr += 1
            elif(_sum > targetSum):
                rightPtr -= 1
            else:
                result.append(
                    [array[index], array[leftPtr], array[rightPtr]]
                )
                leftPtr += 1
                rightPtr -= 1
    return result


print(getThreeNumSum(array, 0))
