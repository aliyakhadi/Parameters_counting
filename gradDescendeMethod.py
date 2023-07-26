import util
import random
import math

descendStopError=0.0001

def ParameterIMinError(parameters:list, i:int, p, eps):
    minerrKvalue = 1
    parameters[i] = minerrKvalue
    minerr=util.errorOfautomaton(parameters, p, eps)
    if minerr==None:
        minerr=1

    for j in range(2,p):
        parameters[i]=j
        temperr=util.errorOfautomaton(parameters, p, eps)
        if temperr==None:
            temperr=3
        if minerr>temperr:
            minerr=temperr
            minerrKvalue=j
    parameters[i]=minerrKvalue
    return (parameters, minerr)

def CoordinateDescendIteration(parameters:list, p, eps):
    n=len(parameters)
    for i in range(n):
        parameters, err=ParameterIMinError(parameters, i, p, eps)
    return (parameters,err)

def CoordinateDescend(parameters: list, p, eps):
    err = 1
    nextErr=10000
    while nextErr==10000 or err-nextErr > descendStopError:
        err = nextErr
        parameters, nextErr = CoordinateDescendIteration(parameters, p, eps)
    return (parameters, nextErr)

def randomK(size,p):
    K=[]
    for i in range(size):
        K.append(random.randrange(p)+1)
    return K

def ResultOfCoordinateDescend(sizeOfParametersSet:int, p: int, eps:float, InitialParameters:list):
    params=util.initialK(sizeOfParametersSet)
    minparams,minerr=CoordinateDescend(params, p, eps)

    for i in range(10):
        params = randomK(sizeOfParametersSet, p)
        params, err=CoordinateDescend(params, p, eps)
        if minerr>err:
            minerr=err
            minparams=params
    params, err=CoordinateDescend(InitialParameters, p, eps)
    if minerr > err:
        minerr = err
        minparams = params
    return (minparams,minerr)


def wholePseudoSetComputing(parameters:list, p, n, independentPartSize):
    restPartK = util.restKcounting(parameters[0:independentPartSize], p, n - independentPartSize - 1)
    parameters = parameters[0:independentPartSize] + restPartK
    return parameters

def PseudoParameterIMinError(parameters:list, i:int, p, eps, independentPartSize):
    minerrKvalue = 1
    n=len(parameters)
    parameters[i] = minerrKvalue
    wholePseudoSetComputing(parameters, p, n, independentPartSize)

    minerr=util.errorOfautomaton(parameters, p, eps)
    if minerr==None:
        minerr=1

    for j in range(2,p):
        parameters[i]=j
        wholePseudoSetComputing(parameters, p, n, independentPartSize)
        temperr=util.errorOfautomaton(parameters, p, eps)
        if temperr==None:
            temperr=3
        if minerr>temperr:
            minerr=temperr
            minerrKvalue=j
    parameters[i]=minerrKvalue
    wholePseudoSetComputing(parameters, p, n, independentPartSize)
    return (parameters, minerr)

def PseudoCoordinateDescendIteration(parameters:list, p, eps, independentPartSize):
    n=len(parameters)
    for i in range(independentPartSize):
        parameters, err=PseudoParameterIMinError(parameters, i, p, eps,independentPartSize )
    return (parameters,err)

def PseudoCoordinateDescend(parameters: list, p, eps,independentPartSize):
    err = 1
    nextErr=10000
    while nextErr==10000 or err-nextErr > descendStopError:
        err = nextErr
        parameters, nextErr = PseudoCoordinateDescendIteration(parameters, p, eps,independentPartSize)
    return (parameters, nextErr)


def PseudoRandomK(independentPartSize,restPartSize, p):
    K=[]
    for i in range(independentPartSize):
        K.append(random.randrange(p)+1)
    restPartK = util.restKcounting(K, p, restPartSize)
    return K + restPartK


def PseudoResultOfCoordinateDescend(sizeOfParametersSet:int, p: int, eps:float):

    independentPartSize = math.ceil(math.log2(sizeOfParametersSet)) + 1
    restPartSize=sizeOfParametersSet-independentPartSize-1
    params=PseudoRandomK(independentPartSize, restPartSize,p)
    minparams,minerr=PseudoCoordinateDescend(params,p,eps,independentPartSize)
    for i in range(6):
        params = PseudoRandomK(independentPartSize, restPartSize,p)
        params, err=PseudoCoordinateDescend(params, p, eps,independentPartSize)
        if minerr>err:
            minerr=err
            minparams=params
    return (minparams,minerr)



