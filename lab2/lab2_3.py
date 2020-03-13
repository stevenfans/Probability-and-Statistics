# Steven Phan
# Using the same probablities of p0, e0, and e1
# create and transmit a one-i message S and calculate the conditional 
# succProb P(S=1|R=1)
# For all events that signal R=1, look at i S. If S=1, the experiment
# is a success_count
# Repeate 100000 times and count the number of success_count. Find th conditional
# probablity of P(S=1|R=1)
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
    # counter variables
    success = 0
    total = 0
    succProb = 0

    # create list to hold s and r bits
    sList = []
    rList = []

    # given values
    p0 = [.60,.40]
    e0 = [.95,.05]
    e1 = [.03,.97]
    for test in range(N):
        # succcess frm assignment
        S = nSidedDie(p0)-1
        if (S == 1):
            R = nSidedDie(e1)-1
        else: 
            R = nSidedDie(e0)-1
        # store it in the list
        sList.append(S)
        rList.append(R)

    # check for P(S=1|R=1) 
    for i in range(N):
        if rList[i] == 1:
            total+=1
            if sList[i] == 1:
                success+=1
    # calculate the number of success
    succProb = success/total
    return succProb

def main(): 
    N=100000
    #create an array of probablities
    print(experiment(N))

if __name__ == "__main__":
    main()
