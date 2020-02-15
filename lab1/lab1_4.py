# The Password Hacking Problem
# Your computer system uses 4-lettter password for login 
# A hacker creates a list of m rand 4-letter words, as canidates for matching
# the password. Note that it is possibel that some fo the m words may be duplicates. The
# number m that you must use has been given to you.
# You are givin your own 4 letter password and you are going to check if the
# hack's list contains at least one word that matches your password. This process of 
# checking considered one experiment. If a word in the list matches your password, 
# the experiment is considered a success. Repeat the experiment for N=1000 times 
# and find the probability that at least one of the words in the hacker's list will 
# match your password. 
# The hacker creates a long list of k*m random 4-letter words. The numbers k and m 
# have been given to you. repeat the previous experiment for N=1000 times and find the 
# probability that at least one f the words in the hacker's list will match your password
# Repeat the prvious experiment for N=1000 times to find the approximate number (m) of 
# words that must be contained in the hacker's list so that the probability of at least
# one word matching the password is p=0.4. You should this by trial and error: assume a 
# value for (m) and calculate the corresponding probability as you did in the previous part.
# The answer will value of (m) that makes this probability approximately equal to p=0.5

import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint, choice
from string import ascii_lowercase

def createPassList(m,E):
    pass_list = []
    
    for i in range(0,m):
        password = createPass()
        pass_list.append(password)
        print("Experiment:%d Iteration: %d, Password: %s" %(E,i,password))
    return pass_list

# function creates random 4 letter word password
def createPass():
    password = ""
    for i in range (0,4):
        letter = choice(ascii_lowercase)
        # print(letter)
        password += letter

    return password

def experiment(N):
    success_count = 0

    for i in range(0,N):
        # create your random password
        print("Experiment: %d" %i)
        user_pass = createPass()
        # create hacker password list
        m = 80000
        k = 7
        km = k*m
        T = 319955
        hacker_pass_list = createPassList(km,i)

        if user_pass in hacker_pass_list:
            success_count += 1
    
    return success_count

def main():
    success_count  = experiment(1000)
    p1 = success_count / 1000
    print("Probabiliy of user password in hacker's list: %.2f" %p1)

if __name__ == "__main__":
    main()
