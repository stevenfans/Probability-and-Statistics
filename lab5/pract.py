import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 1. Effect of sample size on confience intervals
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
N = 1500000 # Bearings
m = 55 # Mean
sd = 5 # Standard deviation
n = range(1,201) # Sample size 1,2,...200

B = np.random.normal(m,sd,N) # Generate population

averages = []

for num in n:
    x = B[random.sample(range(N),num)]
    mean = x.mean()
    # sd = np.std(x,ddof=1)
    averages.append(mean)


plt.figure("1A")
plt.title("Sample means and 95% confidence intervals")
plt.xlabel("Sample Size")
plt.ylabel("average weight (X bar)")
plt.plot(n,averages,"ob",marker='x',linestyle='none')
plt.plot(n,[mean for x in n]) # Plot average line
x = np.linspace(1,200)
plt.plot(x,m+1.96*sd/(x**(1/2)),color="red",linestyle='--')
plt.plot(x,m-1.96*sd/(x**(1/2)),color="red",linestyle='--')
plt.ylim(top=55+10)
plt.ylim(bottom=55-10)

plt.figure("1B")
plt.title("Sample means and 99% confidence intervals")
plt.xlabel("Sample Size")
plt.ylabel("average weight (X bar)")
plt.plot(n,averages,"ob",marker='x',linestyle='none')
plt.plot(n,[mean for x in n]) # Plot average line
x = np.linspace(1,200)
plt.plot(x,m+2.58*sd/(x**(1/2)),color="green",linestyle='--')
plt.plot(x,m-2.58*sd/(x**(1/2)),color="green",linestyle='--')
plt.ylim(top=55+10)
plt.ylim(bottom=55-10)
plt.show()
