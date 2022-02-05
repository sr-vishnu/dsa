X = 7
Y = 5
N = 22

DIGITS = [X,Y]

def findMax(toggle,currentSum=0):
    if((currentSum + DIGITS[toggle]) == N):
        return f"{DIGITS[toggle]}"
    elif(currentSum + DIGITS[toggle] > N):
        return ""
    else:
        one = int(str(DIGITS[toggle]) + str(findMax(0,currentSum + DIGITS[toggle]))),
        two = int(str(DIGITS[toggle]) + str(findMax(1,currentSum + DIGITS[toggle])))



print(
    max(
        findMax(0),
        findMax(1)
    )
)