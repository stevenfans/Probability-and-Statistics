# Perform experiments to see whether or not to switch doors

import numpy as np
import random 
import matplotlib.pyplot as plt
import math as m
import xlwt
from xlwt import Workbook

def switchDoor(old, revealed): 
    if (old == 0 and revealed == 1) or (old == 1 and revealed ==0) : 
        return 2
    elif (old == 0 and revealed == 2) or (old == 2 and revealed ==0) : 
        return 1
    elif (old == 1 and revealed == 2) or (old == 2 and revealed ==1) : 
        return 0
    
def generateDoor(): 

    doors = []
    
    # get random location for car
    car = random.randrange(3)

    for i in range(3):
        if i == car: 
            doors.append("Car")
        else: 
            doors.append("Sheep")

    return doors

def monty(pickedDoor, switch): 

    sheepLoc = []
    success = 0; 

    # create an array for the doors
    doors = generateDoor(); 

    for i in range(len(doors)): 
        if i != pickedDoor and doors[i] == "Sheep": 
            sheepLoc.append(i)
    l = random.randrange(len(sheepLoc))
    # choose a sheep location
    # this is an idex that will not be used
    rLoc = sheepLoc[l]
    # print(sheepLoc)

    # choose to switch or not to switch
    if switch == False: 
        if doors[pickedDoor] == 'Car': 
            success = 1
    else: 
        newdoor = switchDoor(pickedDoor,rLoc)
        if doors[newdoor] == "Car": 
            success = 1; 

    return success


def experiment(n,switch): 

    success = 0; 

    for i in range(n):
        pick = random.randrange(3)
        success += monty(pick,switch)
    
    return success

def main():

    n = 200
    # print(experiment(20))
    exp = range(50000)

    wb = Workbook()
    sheet = wb.add_sheet('Sheet')
    sheet2 = wb.add_sheet('Sheet2')

    test  = [experiment(n,True) for x in exp]
    # print(test)
    test2 = [experiment(n,False) for x in exp]
    
    val, cnt = np.unique(test, return_counts=True)
    pmf = cnt/len(test)

    val2,cnt2 = np.unique(test2,return_counts=True)
    pmf2 = cnt2/len(test2)

    # print(np.column_stack((val, pmf)))

    for i in range(len(val)):
        sheet.write(i,0,int(val[i]))
        sheet.write(i,1,int(cnt[i])
        )
    wb.save('xlwt example.xls')
    for i in range(len(val2)): 
        sheet2.write(i,0,int(val2[i]))
        sheet2.write(i,1,int(cnt2[i]))
    wb.save('xlwt example2.xls')


    # plot the success
    # plt.stem(exp,test)
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title("Binomial PMF: Switch Door")
    plt.stem(val,pmf, use_line_collection=True)
    plt.plot(val,pmf)
    plt.xlabel("Number of Successes in n="+str(n)+" trials")
    plt.ylabel("Probability")    

    plt.subplot(2,1,2)
    plt.stem(val2,pmf2)
    plt.plot(val2,pmf2)
    plt.xlabel("Number of Successes in n="+str(n)+" trials")
    plt.ylabel("Probability")
    plt.title("Binomial PMF: Don't Switch Door")

    # plt.subplot(3,1,3)
    plt.figure(2)
    plt.stem(val,pmf, use_line_collection=True,markerfmt='ro',linefmt='r',label='switch')
    plt.stem(val2,pmf2,use_line_collection=True,markerfmt='bo',linefmt='b',label="don't switch")
    plt.plot(val,pmf,'r')
    plt.plot(val2,pmf2,'b')
    plt.xlabel("Number of Successes in n="+str(n)+" trials")
    plt.ylabel("Probability")
    plt.title("Binomial PMF: Don't Switch Door")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main(); 