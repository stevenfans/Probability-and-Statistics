# Compute the probability of absorption usin gthe simulated chain

import numpy as np
import random 
import matplotlib
import matplotlib.pyplot as plt
import math

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

def markovChain3(P,initial,length): 

    # crate array to hold all states
    allState = []
    # get the initial state
    state = nSidedDie(initial)-1
    allState.append(state)
    
    # sub length by 1, b/c index ssstarts at 0
    length -= 1
    
    # create chain up to the length size
    for i in range(length):
        #check the previous state
        if allState[-1] == 0:
            allState.append(nSidedDie(P[0])-1)
        elif allState[-1] == 1:
            allState.append(nSidedDie(P[1])-1)
        else: 
            allState.append(nSidedDie(P[2])-1)

    # return all the states
    return allState

def main(): 
    initial = [0,0,1,0,0] # always state 2
    P       = [ [1,0,0,0,0],\
                [ ],[],[],[]]
    N = 10000

if __name__ == "__main__": 
    main()