# Calculations using the Binomial Distribution  
# Perform experiment 1000 times

import numpy as np
import random 
import matplotlib.pyplot as plt
import math as m


# function returns the answer to nCr
def combo(n,r):
    # n!/(n!(n-r)!)
    numerator = m.factorial(n)
    r_fact = m.factorial(r)
    n_minus_r_fact = m.factorial(n-r)
    denominator = r_fact * n_minus_r_fact
    result = numerator / denominator 
    return result

def binom(n,x):
    p = 0.66
    q = 1-p
    # binomial distribution formulas
    result = combo(n,x) * (p**x) * (q**(n-x))
    return result
    

def experiment(): 

    # experiment trials
    n = 100
    # the bernoulli trial had 12 successe
    exp = range(1000)

    # perform the binomial distribution
    binomial_distribution = [binom(n,x) for x in exp]
    print(binomial_distribution)
    # plot the success
    plt.stem(exp,binomial_distribution)
    plt.xlabel("Number of Successes in n=1000 trials")
    plt.ylabel("Probability")
    plt.title(" PMF- Binomial Forumla for 66% Success")
    plt.show()


def main(): 

    # run experiment 
    experiment()



if __name__ == "__main__":
    main()