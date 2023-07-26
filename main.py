import math
import util
import gradDescendeMethod
import datetime
eps=0.3
d = 32
independentKsize=math.ceil(math.log2(d))+1
restKsize=d-independentKsize-1
n=d
minError=2


def setParamsForOriginalAlgo(Klocal,i,g,p):
    global n
    global minError
    global minErrorK
    if i<n:
        for j in range(g+1,p):
            Klocal[i]=j
            setParamsForOriginalAlgo(Klocal,i+1,j,p)
    else:
        error=util.isGood(Klocal,p,eps)
        if error:
            if minError>error:
                minError=error
                minErrorK=Klocal.copy()



def setParamsForPseudoAlgo(Klocal, i, g, p,restKsize):
    global independentKsize
    global minError
    global minErrorK
    if i < independentKsize:
        for j in range(g + 1, p):
            Klocal[i] = j
            setParamsForPseudoAlgo(Klocal, i + 1, j, p,restKsize)
    else:
        restK = util.restKcounting(Klocal,p,restKsize)
        Klocal = Klocal + restK
        error = util.isGood(Klocal, p, eps)
        if error:
            if minError > error:
                minError = error
                minErrorK = Klocal.copy()


#for p in (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101,103,107,109,113,127,131,137,139):
for p in (
773,1013

):
    KPseudo, minErrorPseudo =  gradDescendeMethod.PseudoResultOfCoordinateDescend(d,p,eps)
    Koriginal, errOriginal = gradDescendeMethod.ResultOfCoordinateDescend(d,p,eps,KPseudo)

    theta=[]
    theta.append(KPseudo[0])
    for i in range(1,independentKsize):
        theta.append(KPseudo[i]-KPseudo[0])
        if theta[i]<0:
            theta[i]=theta[i]+p
    print(p, ";", Koriginal,";", "{:.5f}".format(errOriginal), ";",KPseudo,";", theta,";", "{:.5f}".format(minErrorPseudo), ";","{:.5f}".format(-errOriginal+minErrorPseudo))

