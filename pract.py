import numpy as np
import matplotlib.pyplot as plt
import random
p=[0.2,  0.1,  0.15, 0.3, 0.2, 0.05] #Given: Probability vector
c=[1,2,3,4,5,6]
n = 1000

# Input: probability vector summing to 1
# Output: side of die based on input probability
def nSideDie(p):
    sides = len(p)
    roll = np.random.random()
    prob_sum = 0
    for i in range(0,sides):
        prob_sum = prob_sum + p[i]
        if i == 0:
            if roll <= prob_sum:
                value = i + 1
            else:
                value = 0
        else:
            if roll > prob_sum - p[i] and roll <= prob_sum:
                value = i + 1
    return value


import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def binomial(k):
    # P(success) = p(1st die == "1" n 2nd die == "2" n 3rd die == "3")
    # = (0.2)(0.1)(0.15) = 0.003
    p = 0.003
    q = 1-p
    binomial = (ncr(1000,k)) * (p**k) * (q**(1000-k))
    return binomial

def problem2():
    xAxis = range(15)
    yAxis = [binomial(x) for x in xAxis]
    # Stem plot graphing
    plt.stem(xAxis,yAxis)
    plt.title('Bernoulli Trials: PMF - Binomial Formula')
    plt.xlabel('Times it took')
    plt.ylabel('Probability')
    plt.xlim(right=15)
    plt.show()
