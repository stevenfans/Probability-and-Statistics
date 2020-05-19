# Distrubution of the SUm of Exponential RVs
import numpy as np
import random 
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

def main(): 
    initial = [0.2,0.2,0.2,0.2,0.2] # equal randomness

    # Define the State Transition Matrix P
    P       = [ [1,0,0,0,0],\
                [0.3,0,0.7,0,0],\
                [0,0.5,0,0.5,0],\
                [0,0,0.6,0,0.4],\
                [0,0,0,0,1]]
    n = 15

    # chain can start at any random transient state
    # create single run 
    states = markovChain5(P,initial,n)

    # # Generate and plot 1 markov chain
    plt.figure("Single Run")
    plt.plot(range(n),states,"ro",LINESTYLE='--')
    plt.title("A sample simulation run of a five-state Markov Chain")
    plt.ylabel("State")
    plt.xlabel("Step Number")
    plt.show()


if __name__ == "__main__": 
    main()
