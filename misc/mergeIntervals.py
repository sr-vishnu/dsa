

def mergeIntervals(array):
    array = sorted(array, key=lambda x: x[0])
    result = [array[0]]

    for index in range(1, len(array)):
        if(result[len(result)-1][1] >= array[index][0]):
            result[len(result)-1] = [result[len(result)-1][0],
                                     max(result[len(result)-1][1], array[index][1])]
        else:
            result.append(array[index])

    return result


print(
    mergeIntervals([[1, 4], [3, 5], [100, 200], [150, 190]])
)
