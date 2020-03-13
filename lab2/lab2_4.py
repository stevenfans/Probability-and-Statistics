# Steven Phan
import numpy as np
import random 
import matplotlib.pyplot as pl

def nSidedDie(p):
    n=np.size(p)
    cs=np.cumsum(p)
    cp=np.append(0,cs)
    r=random.random()
    for k in range(0,n):
        if r>cp[k] and r<=cp[k+1]:
            d=k+1
            break
    return d

def experiment(N):
    # holding values
    sList = []
    rList = []
    R = [] 
    comp  =[]
    # counter for erros
    fails = 0
    # given values
    p0 = [.60,.40]
    e0 = [.95,.05]
    e1 = [.03,.97]

    # perform test N times 
    for test in range(N):
        R = [] # list to hold i
        # perform probability test from assignment
        S = nSidedDie(p0)-1
        for i in range(3):
            if (S==1):
                R.append(nSidedDie(e1)-1)
            else: 
                R.append(nSidedDie(e0)-1)
        # hold all the i values
        sList.append(S)
        rList.append(R)

    # check for athe success
    for i in rList:
        if i.count(1) > i.count(0):
            comp.append(1)
        else:
            comp.append(0)

    # find the number of fails
    for i in range(N):
        if sList[i] != comp[i]:
            fails += 1;

    # calculate the failers 
    fails /= N
    return fails


def main(): 
    N=100000
    #create an array of probablities
    print(experiment(N))

if __name__ == "__main__":
    main()
