# The GOogle PageRank Algorithm

import numpy as np
import random 
import matplotlib.pyplot as plt


def markovCalculated5(P,initial,n):

    # array to hold all the state values
    state0 = []
    state1 = []
    state2 = []
    state3 = []
    state4 = []

    state0.append(initial[0])
    state1.append(initial[1])
    state2.append(initial[2])
    state3.append(initial[3])
    state4.append(initial[4])

    for i in range(1,n):
        state0.append((state0[i-1]*P[0][0])+(state1[i-1]*P[1][0])+(state2[i-1]*P[2][0])+(state3[i-1]*P[3][0])+(state4[i-1]*P[4][0]))
        state1.append((state0[i-1]*P[0][1])+(state1[i-1]*P[1][1])+(state2[i-1]*P[2][1])+(state3[i-1]*P[3][1])+(state4[i-1]*P[4][1]))
        state2.append((state0[i-1]*P[0][2])+(state1[i-1]*P[1][2])+(state2[i-1]*P[2][2])+(state3[i-1]*P[3][2])+(state4[i-1]*P[4][2]))
        state3.append((state0[i-1]*P[0][3])+(state1[i-1]*P[1][3])+(state2[i-1]*P[2][3])+(state3[i-1]*P[3][3])+(state4[i-1]*P[4][3])) 
        state4.append((state0[i-1]*P[0][4])+(state1[i-1]*P[1][4])+(state2[i-1]*P[2][4])+(state3[i-1]*P[3][4])+(state4[i-1]*P[4][4]))
    
    return (state0,state1,state2,state3,state4)


def main():
    P =([[  0,   1,   0,   0,   0], \
            [1/2,   0, 1/2,   0,   0], \
            [1/3, 1/3,   0,   0, 1/3], \
            [  1,   0,   0,   0,   0], \
            [  0, 1/3, 1/3, 1/3,   0]]) 
    n = 20

    v1 = [0.2,0.2,0.2,0.2,0.2]
    v2 = [0, 0, 0, 0, 1]

    v1S0,v1S1,v1S2,v1S3,v1S4 = markovCalculated5(P,v1,n)
    v2S0,v2S1,v2S2,v2S3,v2S4 = markovCalculated5(P,v2,n)

    plt.figure("Calc Run V1")
    plt.plot(range(n),v1S0,'o',label="State 0",LINESTYLE='--')
    plt.plot(range(n),v1S1,'o',label="State 1",LINESTYLE='--')
    plt.plot(range(n),v1S2,'o',label="State 2",LINESTYLE='--')
    plt.plot(range(n),v1S3,'o',label="State 3",LINESTYLE='--')
    plt.plot(range(n),v1S4,'o',label="State 4",LINESTYLE='--')
    plt.title("Calculated five-state Markov Chain")
    plt.ylabel("Probability")
    plt.xlabel("Step Number")
    plt.legend()
    plt.show()

    plt.figure("Calc Run V2")
    plt.plot(range(n),v2S0,'o',label="State 0",LINESTYLE='--')
    plt.plot(range(n),v2S1,'o',label="State 1",LINESTYLE='--')
    plt.plot(range(n),v2S2,'o',label="State 2",LINESTYLE='--')
    plt.plot(range(n),v2S3,'o',label="State 3",LINESTYLE='--')
    plt.plot(range(n),v2S4,'o',label="State 4",LINESTYLE='--')
    plt.title("Calculated five-state Markov Chain")
    plt.ylabel("Probability")
    plt.xlabel("Step Number")
    plt.legend()
    plt.show()

if __name__== "__main__":
    main()