

originalLength = 2
size = [1,2,3,4,5,6,7,8]
price = [3,5,8,9,10,17,17,20]

capturePartialResults = [[-1 for i in range((originalLength+1))] for j in range(len(size))]

def maxPrice(index,lengthRemaining):
    if(capturePartialResults[index][lengthRemaining]  != -1):
        print(f"retriving maxPrice({index},{lengthRemaining}) from memory")
        return capturePartialResults[index][lengthRemaining]
    elif(size[index] == lengthRemaining):
        print(f"computing maxPrice({index},{lengthRemaining})")
        capturePartialResults[index][lengthRemaining] = price[index]
        return capturePartialResults[index][lengthRemaining]
    elif (size[index] > lengthRemaining):
        print(f"computing maxPrice({index},{lengthRemaining})")
        capturePartialResults[index][lengthRemaining] = float('-inf')
        return capturePartialResults[index][lengthRemaining]
    else:
        print(f"computing maxPrice({index},{lengthRemaining})")
        capturePartialResults[index][lengthRemaining] = max(
            [price[index] + maxPrice(i,lengthRemaining-size[index]) for i in range(0,len(size))]
        )
        return capturePartialResults[index][lengthRemaining]


result = max(
    [
        maxPrice(i, originalLength) for i in range(0,len(size))
    ]
)


print(f"the result: {result}")