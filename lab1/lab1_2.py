#   Number of rolls needed to get a "7" with two dice
#   You roll a pair of fair dice  and calculate the sum of the faces. 
#   You are interested in th enumber of rolls it takes until  you get
#   a sum of "7". The first time you get a "7" the experiment is 
#   considered a success. You record the number of rolls and you stop the 
#   experiment. You repeat the experiment N=100,000 times. Each time
# you keep track of the number of rolls it takes to have "success"

import numpy as np
import random 
import matplotlib.pyplot as plt
from random import randint

def experiment(N):
    s=np.zeros((N,1))
    # peform experiment N times and store in array s
    for i in range(0,N):
        count_of_rolls = rollsTo7()
        s[i] = count_of_rolls
    return s

def rollsTo7():
    count = 1
    #roll until sum of 2 random dice is 7
    while(sum2dice()!=7):
       count += 1 #increment count if sum is not 7
    
    return count


def sum2dice(): 
    #create dice variables and get random value from 1~6
    dice_1 = randint(1,6)
    dice_2 = randint(1,6)
    # get the sum of the two dices
    sum_of_dice = dice_1+dice_2
    # return the sum
    return sum_of_dice


def main():
    R = experiment(10)
    # print(randint(1,6,6))
    
    # stem plot 
    roll_num, num_of_times_rolled = np.unique(R, return_counts=True)
    # print(str(roll_num)+ "    " + str(num_of_times_rolled))
    # NOTE: Plot times of rolls vs the probaility of it being a success in totality
    plt.stem(roll_num, (num_of_times_rolled * 0.0001), use_line_collection=True)
    plt.xlabel("Number of Rolls to have a Success")
    plt.ylabel("Probability")
    plt.title("Number of Rolls Needed to Get a '7' with Two Dice")
    plt.show()

if __name__ == "__main__": 
    main()