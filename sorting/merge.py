"""
Function performs merging of two lists
"""

def merge(listOne,listTwo):
    mergedList = []

    while(listOne and listTwo):
        if listOne[0] <= listTwo[0]:
            mergedList.append(listOne[0])
            del listOne[0]
        else:
            mergedList.append(listTwo[0])
            del listTwo[0]

    if(listOne):
        return mergedList + listOne
    else:
        return mergedList + listTwo

print(
    merge(
        [1,3,5,7,9],
        [2,4,6,8,10]
    )
)


print(
    merge(
        [1,2,3],
        [4,5,6]
    )
)
