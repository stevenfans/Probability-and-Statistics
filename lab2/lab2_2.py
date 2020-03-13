# Steven Phan
# Using the same probablities of p0, e0, and e1
# create and transmit a one-i message S and calculate the conditional 
# succProb P(R=1|S=1)
# For all events that signal S=1, look at i R. If R=1, the experiment
# is a success_count
# Repeate 100000 times and count the number of success_count. Find th conditional
# probablity of P(R=1|S=1)
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
    # create S and R holding lists
    sList = []
    rList = []
    # counters for sucess
    success_count = 0
    total = 0
    # given values
    p0 = [0.6, 0.4]
    e0 = [0.95,0.05]
    e1 = [0.03, 0.97]

    for test in range(N):
        # use function param from assignment
        S = nSidedDie(p0)-1
        if (S == 1):
            R = nSidedDie(e1)-1
        else:
            R = nSidedDie(e0)-1
        # add to the list
        sList.append(S)
        rList.append(R)

    # count the times for when P(R=1|S=1)
    for i in range(N):
        if sList[i] == 1:
            total+=1
            if rList[i] == 1:
                success_count+=1
    # calcuate the succesful times
    succProb = success_count/total
    return succProb

def main(): 
    N=100000
    #create an array of probablities
    print(experiment(N))

if __name__ == "__main__":
    main()
