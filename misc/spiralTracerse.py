"""
Function traverses a 2D array in a spiral
"""


array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]


def spiralTraverse(array):
    firstRowPtr = 0
    lastRowPtr = len(array) - 1
    firstColPtr = 0
    lastColPtr = len(array[0]) - 1

    targetList = []

    print(f"""
        firstRowPtr: {firstRowPtr}
        firstColPtr: {firstColPtr}
        lastRowPtr: {lastRowPtr}
        lastColPtr: {lastColPtr}
        """)

    while(firstRowPtr <= lastRowPtr and firstColPtr <= lastColPtr):

        # traverse the top row
        targetList += array[firstRowPtr][firstColPtr:lastColPtr+1]

        # traverse the last col except the element which is already traversed during the toprow operation
        targetList += [array[row][lastColPtr]
                       for row in range(firstRowPtr+1, lastRowPtr+1)]

        # traverse the bottom row execept the element read in the previous step

        if(firstRowPtr != lastRowPtr):
            targetList += [array[lastRowPtr][col]
                           for col in range(lastColPtr-1, firstColPtr-1, -1)]

        # traverse the first col

        if(firstColPtr != lastColPtr):
            targetList += [array[row][firstColPtr]
                           for row in range(lastRowPtr-1, firstRowPtr, -1)]

        firstRowPtr += 1
        lastRowPtr -= 1
        firstColPtr += 1
        lastColPtr -= 1

        print(f"""
        firstRowPtr: {firstRowPtr}
        firstColPtr: {firstColPtr}
        lastRowPtr: {lastRowPtr}
        lastColPtr: {lastColPtr}
        """)

    return targetList


print(spiralTraverse(array))
