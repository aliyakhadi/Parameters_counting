import math

def initialK(size: int):
    K=[]
    for i in range(size):
        K.append(1)
    return K
def sumOfCosForX(p: int, M: list[int],x: int):
    n=len(M)
    s=0
    for i in range(n):
        s=s+math.cos(2*math.pi*M[i]*x/p)
    return s*s/n/n


def isGood(K: list[int], p:int, eps:float):
    #if max(K)<p:
        s= max(map(lambda x: sumOfCosForX(p,K,x), range(1,p)))
        sett=set()
        for i in K:   sett.add(i)
        if 0 in sett: return None
        if s<eps:
           # print(" k=",K, " eps=", s)
            return s
        else: return None

def errorOfautomaton(K: list[int], p:int, eps:float):
        s= max(map(lambda x: sumOfCosForX(p,K,x), range(1,p)))
        return s

def notpBinary(i, K):
    if i >= 0:
        if K[i] != 1:
            K[i] = K[i] + 1
        else:
            K[i] = 0
            notpBinary(i - 1, K)


def reinitializingBinary(K):
    newK = K
    n = len(newK) - 1
    notpBinary(n, newK)
    return newK


def restKcounting(partialK: list, p:int,nn:int):
    restK = []
    sizeOfBinary=len(partialK)-1
    binaryPartialK = []
    for i in range(sizeOfBinary):
        binaryPartialK.append(0)
    for i in range(2 ** (sizeOfBinary) - 1):
        reinitializingBinary(binaryPartialK)

        ones = 0
        newK = 0
        for j in range(sizeOfBinary):
            ones = ones + binaryPartialK[j]
            if binaryPartialK[j] == 1:
                newK = newK + partialK[j + 1]
        newK = newK - (ones-1) * partialK[0]
        while newK < 0:
            newK = newK + p
        if ones != 1:  restK.append(newK)
    return restK


