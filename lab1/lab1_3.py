# Getting 50 heads when tossing 100 coins
# You toss 100 fair coins and record the number of "heads". This is considered 
# a single experiment. If you get exactly 50 heads, the experiment is considered
# a "success". You repeat the experiment N=100,000 times. After the N experiements 
# are completed count the total success, and calculate the probablity of success
# i.e. the probability of getting exactly 50 heads

import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint

# Function perferoms N experiments
# each experiment has a 100 coin tosses
# a successful experiment is when there are 50 heads
# returns count of how many succesful experiments were performed
def experiements(N):
    success_count = 0
    # perform experiment N times 
    for i in range(0,N): 
        result = coinTossOnHeadSuccess()
        # check if there was a success in that single experiment 
        if result==True:
            success_count += 1
    
    return success_count
        
# function run 100 tossess and returns if there are 50 heads 
def coinTossOnHeadSuccess():
    # intialize the heads and tails
    heads = 0
    tails = 0 
    for i in range(0,100):
        # flip the coin
        coin = randint(0,1)
        #keep tally of heads and tails
        if coin == 0: 
            heads += 1
        else: 
            tails +=1 
    if heads == 50:
        return True
    else:
        return False

def main(): 
    # print(coinTossOnHeadSuccess())
    N = 100000
     # how many experiments to do
    R = experiements(N)
    # get the percentage of the run 
    percentage = R/N * 100
    print("Out of %d tosses, there is a %.2f%% to get success" %(N,percentage))

if __name__ == "__main__":
    main()