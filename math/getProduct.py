

array = [1, 2, 3, 4, 5]


def calculateProduct(array):
    productArray = [
        {
            "left": 1,
            "right": 1
        } for num in range(len(array))
    ]

    for index in range(1, len(array)):
        productArray[index]["left"] = array[index-1] * \
            productArray[index-1]["left"]
    for index in range(len(array)-2, -1, -1):
        productArray[index]["right"] = array[index+1] * \
            productArray[index+1]["right"]

    return list(map(lambda x: x.get("left")*x.get("right"), productArray))


print(calculateProduct(array))
