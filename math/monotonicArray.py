
"""
Function tells if a given array is Monotonously increasing or decreasing
"""


def isMonotonic(array):
    state = None
    for index in range(0, len(array)-1):
        if(array[index] == array[index+1]):
            continue
        elif(array[index] < array[index+1]):
            currentState = "increasing"
            if((state is not None) and (currentState != state)):
                return False
            else:
                state = currentState
        else:
            currentState = "decreasing"
            if((state is not None) and (currentState != state)):
                return False
            else:
                state = currentState

    return True
