# Effect of Sample Size on Confidence Intervals
import numpy as np
import random 
import matplotlib
import matplotlib.pyplot as plt
import math


def main():
    N = 1500000
    u = 55
    o = 5
    n = list(range(1,200,1))

    # create random normal
    pop = np.random.normal(u,o,N)

    avg = []

    for num in range(len(n)):
        x = pop[random.sample(range(N),num)]
        #  get the mean 
        mean = x.mean()
        avg.append(mean)

    x = np.linspace(1,200)
    pos_std = u+1.96*o/(n**(1/2))
    neg_std = u-1.96*o/(n**(1/2))

    plt.figure("1A")
    plt.title("Sample means and 95% confidence intervals")
    plt.xlabel("Sample Size")
    plt.ylabel("average weight (X bar)")
    plt.plot(n,avg,"ob",marker='x',linestyle='none')
    plt.plot(n,[mean for x in n]) # Plot average line
   
    plt.plot(x,pos_std,color="red",linestyle='--')
    plt.plot(x,neg_std,color="red",linestyle='--')
    plt.ylim(top=55+10)
    plt.ylim(bottom=55-10)
    plt.show()
    print('done')

if __name__ == "__main__":
    main()  