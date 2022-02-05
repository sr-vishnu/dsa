LX1 = 0
LY1 = 0
RX1 = 5
RY1 = 5

LX2 = 1
LY2 = 1
RX2 = 3
RY2 = 3



def findOverlap(A,B,C,D,E,F,G,H):
    if(RX1 < LX2 or RX2 < LX1):
        return False

    if(RY1 < LY2 or RY2 < LY1):
        return False

    return True


print(
    findOverlap(LX1,LY1,RX1,RY1,LX2,LY2,RX2,RY2)
)