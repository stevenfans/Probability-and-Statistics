# Steven Phan 
# Function for n-side die
# Write a fucntion that simulates a single roll for a n-side die. 
# Inputs: 
#       the probabilities for each side, given as a vector
#       p = [p1, p2, ... pn]
# Outputs: 
#       The number on the face of the die after a single roll, i.e. 
#       one number from a set of integers {1,2,...n}

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
    # print('Ramdom number generated {:1}'.format(d))
    return d

def experiment(p,N):
    # n=np.size(p)
    s=np.zeros((N,1))
    for i in range(0,N):
        d=nSidedDie(p)
        s[i]=d
    return s

def main(): 
    #create an array of probablities
    p = np.array([0.10,0.15,0.20, 0.05, 0.30, 0.10, 0.10])
    N = 10000
    R = experiment(p,N)
    roll_num, num_of_times_rolled = np.unique(R, return_counts=True)
    plt.stem(roll_num,num_of_times_rolled, use_line_collection=True)
    plt.xlabel("Die Number")
    plt.ylabel("Number of Times Rolled")
    plt.title("Function for N-Side Die")
    plt.show()

if __name__ == "__main__":
    main()