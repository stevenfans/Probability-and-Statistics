# Approximation of Binomial by Poisson Distribution 
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


def poisson(n,x):
    # p = 0.2*0.1*0.15
    p = 0.003
    lambduh = n*p
    # poinson formula
    numerator = (lambduh**x)*(m.e**(-lambduh))
    denominator = m.factorial(x)
    result = numerator/denominator
    return result
    
def experiment(): 

    # experiment trials
    n = 1000
    # the bernoulli trial had 12 successe
    exp = range(13)
    # perform the poisson distribution
    poisson_distribution = [poisson(n,x) for x in exp]

    # plot the success
    plt.stem(exp,poisson_distribution)
    plt.xlabel("Number of Successes in n=1000 trials")
    plt.ylabel("Probability")
    plt.title("Bernoulli Trials: PMF- Poisson Approximation")
    plt.show()


def main(): 
    # run experiment
    experiment()


if __name__ == "__main__":
    main()