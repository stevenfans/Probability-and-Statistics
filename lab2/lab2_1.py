# Steven Phan 
# Function for n-side die
# Write a fucntion that simulates a single roll for a n-side die. 
# Inputs: 
#       the probabilities for each side, given as a vector
#       p = [p1, p2, ... pn]
# Outputs: 
#       The number on the face of the die after a single roll, i.e. 
#       one number from a set of integers {1,2,...n}

import numpy as np
import random 
import matplotlib.pyplot as plt

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
    # create list to hold bit values for S and R
    sList = []
    rList = []
    fail = 0
    #create an array of probablities
    p0 = [0.6, 0.4]
    e0 = [0.95,0.05]
    e1 = [0.03, 0.97]

    # perform experiment N times
    for test in range(N):
        # use function param from assignment
        S = nSidedDie(p0)-1
        if (S == 1):
            R = nSidedDie(e1)-1
        else:
            R = nSidedDie(e0)-1

        # add to S and R list
        sList.append(S)
        rList.append(R)

    # calculate the errors
    for bit in range(N):
        if sList[bit] != rList[bit]:
            fail += 1
    fail /= N
    
    return fail

def main(): 
    N = 100000
    print(experiment(N))

if __name__ == "__main__":
    main()