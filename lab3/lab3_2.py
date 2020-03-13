# Calculations using the Binomial Distribution  
# You have 3 identical mulit-side unfair dice with probability p.
# One roll is a success if you get a one for the first die; two 
# for the second die; three for the third die
# Perform experiment 1000 times

import numpy as np
import random 
import matplotlib.pyplot as plt
import math as m

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

    for times in range(0,1000):
        die1 = nSidedDie(p)
        die2 = nSidedDie(p)
        die3 = nSidedDie(p)

        success+= 1 if die1==1 and die2==2 and die3==3 else 0
    
    return success

def combo(n,r):
    numerator = m.factorial(n)
    r_fact = m.factorial(r)
    n_minus_r_fact = m.factorial(n-r)
    denominator = r_fact * n_minus_r_fact
    result = numerator / denominator 

def binom(n,x):
    p = 0.003
    q = 1-p

    result = combo(n,x) * (p**x) * (q**(n-x))
    

def experiment(N): 

    n = 1000
    exp = range(15)
    binomial_distribution = [binom(x) for x in exp]

    roll_num, num_of_times_rolled = np.unique(success_array, return_counts=True)
    
    # plot the dice number by its probability of showing up
    plt.stem(roll_num, (num_of_times_rolled * 0.0001), use_line_collection=True)
    plt.xlabel("Number of Successes in n=1000 trials")
    plt.ylabel("Probability")
    plt.title("Bernoulli Trials: PMF-Experimental Results")
    plt.show()


def main(): 
    # experiment times 
    N = 10000

    experiment(N)


if __name__ == "__main__":
    main()
