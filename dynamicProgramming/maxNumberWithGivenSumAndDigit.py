N = 22

DIGITS = [5,7]

DP_TABLE = [[None for x in range(len(DIGITS))] for i in range(N+1)]

for _sum in range(N,-1,-1):
    for _index in range(len(DIGITS)):
        if _sum + DIGITS[_index] > N:
            DP_TABLE[_sum][_index] = -1
        elif _sum + DIGITS[_index] == N:
            DP_TABLE[_sum][_index] = DIGITS[_index]
        else:
            zero = DP_TABLE[_sum+DIGITS[_index]][0]
            one = DP_TABLE[_sum+DIGITS[_index]][1]
            result = max(zero, one)

            if result == -1:
                DP_TABLE[_sum][_index] = -1
            else:
                DP_TABLE[_sum][_index] = int(f"{DIGITS[_index]}{result}")


result = max(
    DP_TABLE[0][0],
    DP_TABLE[0][1]
)

print(result)
print("#"*100)
print(DP_TABLE)