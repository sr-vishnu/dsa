
def merge(listOne,listTwo):
    """
    Function performs merging of two lists
    """
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


def sort(_list):
    if(len(_list)) == 1:
        return _list
    elif(len(_list)) == 2:
        if(_list[0] > _list[1]):
            return [_list[1],_list[0]]
        else:
            return _list
    else:
        left = 0
        mid = len(_list)//2
        right = len(_list) - 1

        leftSorted = sort(_list[left:mid+1])
        rightSorted = sort(_list[mid+1:])
        return merge(leftSorted,rightSorted)

print(
    sort(
        [5,4,3,2,1]
    )
)

print(
    sort(
        [5,4,3,2]
    )
)

print(
    sort(
        [5,4,3,2,1,1,1,1,3,4,5,6,100,-1,34,0]
    )
)

print(
    sort(
        [1]*1000000
    )
)
