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

def markovChain5(P,initial,length): 

    # crate array to hold all states
    allState = []
    # get the initial state
    state = nSidedDie(initial)-1
    allState.append(state)
    
    # sub length by 1, b/c index starts at 0
    length -= 1
    
    # create chain up to the length size
    for i in range(length):
        #check the previous state
        if allState[-1] == 0:
            allState.append(nSidedDie(P[0])-1)
        elif allState[-1] == 1:
            allState.append(nSidedDie(P[1])-1)
        elif allState[-1] == 2:
            allState.append(nSidedDie(P[2])-1)
        elif allState[-1] == 3:
            allState.append(nSidedDie(P[3])-1)
        else: 
            allState.append(nSidedDie(P[4])-1)

    # return all the states
    return allState

def markovExperiment(P,initial,N):

    # create a chain of length 15, for N times
    experiment = [markovChain5(P,initial,15) for i in range(N)]

    # transponse the matrix to count the occurences 
    transposed = np.transpose(experiment)

    state0 = [list(i).count(0)/N for i in transposed]
    state1 = [list(i).count(1)/N for i in transposed]
    state2 = [list(i).count(2)/N for i in transposed]
    state3 = [list(i).count(3)/N for i in transposed]
    state4 = [list(i).count(4)/N for i in transposed]

    return (state0,state1,state2,state3,state4)

def main(): 
    initial = [0,0,1,0,0]

    # Define the State Transition Matrix P
    P       = [ [1,0,0,0,0],\
                [0.3,0,0.7,0,0],\
                [0,0.5,0,0.5,0],\
                [0,0,0.6,0,0.4],\
                [0,0,0,0,1]]
    n = 15
    N = 10000

    state0,state1,state2,state3,state4 = markovExperiment(P,initial,N)

    plt.figure("Multiple Runs")
    plt.plot(range(n),state0,'o',label="State 0",LINESTYLE='--')
    plt.plot(range(n),state1,'o',label="State 1",LINESTYLE='--')
    plt.plot(range(n),state2,'o',label="State 2",LINESTYLE='--')
    plt.plot(range(n),state3,'o',label="State 3",LINESTYLE='--')
    plt.plot(range(n),state4,'o',label="State 4",LINESTYLE='--')
    plt.title("Simulate five-state Markov Chain")
    plt.ylabel("Probability")
    plt.xlabel("Step Number")
    plt.legend()
    plt.show()

if __name__ == "__main__": 
    main()