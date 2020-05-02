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
    n = list(range(1,201,1))
    allMean = [] # hold all the mean values from the experiment
    step = np.linspace(1,200) # create even spaces from 1~200
    # create random normal
    pop = np.random.normal(u,o,N)

    # get all the mean values
    for num in range(len(n)):
        # create sample points
        x = pop[random.sample(range(N),num)]
        #  get the mean 
        mean = np.mean(x)
        allMean.append(mean)

    # Get the standard deviation curve for 95%
    pos_std_95 = u+1.96*(o/(step**(0.5)))
    neg_std_95 = u-1.96*(o/(step**(0.5)))

    # Get the standard deviation curve for 99%
    pos_std_99 =  u+2.58*(o/(step**(0.5))) 
    neg_std_99 =  u-2.58*(o/(step**(0.5)))

    # Plot the 95% Sample
    # Create a new figure
    plt.figure("Sample_95")
    # Plot the Standard Deviation
    plt.plot(step,pos_std_95,color="red",linestyle='--')
    plt.plot(step,neg_std_95,color="red",linestyle='--')
    # Plot the sample means
    plt.plot(n,allMean,color='blue',marker='x',linestyle='none')
    # Plot the average
    plt.plot(n,[mean for step in n]) 

    plt.title("Sample Means and 95% Confidence Intervals")
    plt.ylabel("X bar")
    plt.xlabel("Sample Size")

    # Plot 99%
    # Create a new figure
    plt.figure("Sample_99")

    # Plot the Standard Deviation
    plt.plot(step,pos_std_99,linestyle=':',color="green")
    plt.plot(step,neg_std_99,linestyle=':',color="green")

    # Plot the sample means
    plt.plot(n,allMean,color="blue",marker='x',linestyle='none')
    # Plot the average
    plt.plot(n,[mean for step in n]) 
    plt.title("Sample Means and 99% Confidence Intervals")
    plt.ylabel("X bar")
    plt.xlabel("Sample Size")

    plt.show()
    print('done')

if __name__ == "__main__":
    main()  