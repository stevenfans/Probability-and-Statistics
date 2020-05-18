# A 3-State markov Chain

import numpy as np
import random 
import matplotlib
import matplotlib.pyplot as plt
import math


initial = [1/4,0,3/4]
P       = [[1/2, 1/4, 1/4],[1/4,1/8, 5/8],[1/3,2/3,0]]

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

def nSideDie0(p):
    return nSidedDie(p) - 1

def makeMarkov(chainLength):
    S = [nSideDie0(initial)]
    for i in range(chainLength-1):
        if S[-1] == 0:
            S.append(nSideDie0(P[0]))
        elif S[-1] == 1:
            S.append(nSideDie0(P[1]))
        elif S[-1] == 2:
            S.append(nSideDie0(P[2]))
    return S

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

def markovExperiment(P,initial,N):

    # create a chain of length 15, for N times
    experiment = [markovChain3(P,initial,15) for i in range(N)]

    # transponse the matrix to count the occurences 
    transposed = np.transpose(experiment)

    # state0 = [] 
    # state1 = [] 
    # state2 = []
    # state3 = []

    # for i in transposed:
    #     state0.append(list(i).count(0)/N)
    #     state1.append(list(i).count(1)/N)
    #     state2.append(list(i).count(2)/N)

    state0 = [list(i).count(0)/N for i in transposed]
    state1 = [list(i).count(1)/N for i in transposed]
    state2 = [list(i).count(2)/N for i in transposed]

    print('test')

    return (state0,state1,state2)

def main(): 
    P       = [[1/2,1/4,1/4],[1/4,1/8, 5/8],[1/3,2/3,0]]
    initial = [1/4,0,3/4]
    n = 15    # chain length
    N = 10000 # experiments

    
    states = markovChain3(P,initial,n)
    state0,state1,state2 = markovExperiment(P,initial,100)

    # # Generate and plot 1 markov chain
    plt.figure("Single Run")
    plt.plot(range(n),states,"ro",LINESTYLE='--')
    plt.title("A sample simulation run of a three-state Markov Chain")
    plt.ylabel("State")
    plt.xlabel("Step Number")
    plt.show()

    plt.figure("Multiple Runs")
    plt.plot(range(n),state0,'o',label="State 0",LINESTYLE='--')
    plt.plot(range(n),state1,'o',label="State 1",LINESTYLE='--')
    plt.plot(range(n),state2,'o',label="State 2",LINESTYLE='--')
    plt.title("Simulate three-stae Markov Chain")
    plt.ylabel("Probability")
    plt.xlabel("Step Number")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main(); 