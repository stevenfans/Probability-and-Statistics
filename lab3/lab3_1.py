# Experimental Bernoulli Trials
# You have 3 identical mulit-side unfair dice with probability p.
# One roll is a success if you get a one for the first die; two 
# for the second die; three for the third die
# Perform experiment 1000 times

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

def rolls():
    # probability
    p = np.array([0.2, 0.1, 0.15, 0.3, 0.2, 0.05])
    success = 0

    # roll 3 dices 
    for times in range(0,1000):
        die1 = nSidedDie(p)
        die2 = nSidedDie(p)
        die3 = nSidedDie(p)

        # calculate when there is a success
        success+= 1 if die1==1 and die2==2 and die3==3 else 0
    
    return success

def experiment(N): 

    # store the number of success into the array
    success_array = [rolls() for i in range(0,N)]

    roll_num, num_of_times_rolled = np.unique(success_array, return_counts=True)
    plt.stem(roll_num, (num_of_times_rolled * 0.0001), use_line_collection=True)
    plt.xlabel("Number of Successes in n=1000 trials")
    plt.ylabel("Probability")
    plt.title("Bernoulli Trials: PMF-Experimental Results")
    plt.show()


def main(): 
    # experiment times 
    N = 10000
    # run experiment
    experiment(N)

if __name__ == "__main__":
    main()
