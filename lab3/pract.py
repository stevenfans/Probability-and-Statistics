

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
    p0 = [.60,.40]
    e0 = [.95,.05]
    e1 = [.03,.97]

    sList = []
    rList = []
    R = [] 
    bits3 = []
    decoded  =[]
    
    
    for test in range(100000):
        R = []
        # bits3=[]
        # R = [nSidedDie(e1)-1 if (S == 1) else nSidedDie(e0)-1 for _ in range(3)]
        S = nSidedDie(p0)-1
        for i in range(3):
            if (S==1):
                R.append(nSidedDie(e1)-1)
            else: 
                R.append(nSidedDie(e0)-1)
            # R.append(bits3)
        sList.append(S)
        rList.append(R)

    # decoded = [1 if bits.count(1) > bits.count(0) else 0 for bits in rList]
    for bits in rList:
        if bits.count(1) > bits.count(0):
            decoded.append(1)
        else:
            decoded.append(0)

    probability = sum(1 for bit in range(100000) if sList[bit] != decoded[bit])/100000
    
    return probability


def main(): 
    N=100000
    #create an array of probablities
    print(experiment(N))

if __name__ == "__main__":
    main()
