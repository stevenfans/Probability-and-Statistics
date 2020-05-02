# Steven Phan

# Using the sample mean to estimate the population mean
import numpy as np
import random 
import matplotlib
import matplotlib.pyplot as plt
import math

N = 1500000
u = 55
o = 5
n = range(1,201)

# create random normal
pop = np.random.normal(u,o,N)


def experiment95(size):
    norm95_succ =0
    norm95_t_succ = 0

    for i in range(10000):
        # Part A.1 Calculate sample mean and sample std
        x = pop[random.sample(range(N),size)]
        mean = np.mean(x)
        stdd = np.std(x,ddof=1)
        
        # Part A.2 Create 95% confidence itnerval
        lower95 = mean - (1.96*(stdd/(math.sqrt(size))))
        upper95 = mean + (1.96*(stdd/(math.sqrt(size))))

        # Part A.3 Check if the confidence interval includes the actual mean of the population
        if lower95 < u < upper95:
            norm95_succ+=1
        
        # Part A.4  Get Appropriated distrbution 
        lower95_t = mean - (2.78*(stdd/(math.sqrt(size))))
        upper95_t = mean + (2.78*(stdd/(math.sqrt(size))))
        
        # Part A.5 Check confidence
        if lower95_t < u < upper95_t:
            norm95_t_succ += 1

    result = [norm95_succ,norm95_t_succ]
    return result

def experiment99(size):
    norm99_succ=0
    norm99_t_succ=0
    for i in range(10000):
        # Part A.1 Calculate sample mean and sample std
        x = pop[random.sample(range(N),size)]
        mean = np.mean(x)
        std = np.std(x)

        # Part A.2 Create 99% 
        lower99 = mean - (2.58*(std/(math.sqrt(size))))
        upper99 = mean + (2.58*(std/(math.sqrt(size))))

        # Part A.3
        if lower99 < u <upper99:
            norm99_succ+= 1
        
        # Part A.4  Get Appropriated distrbution 
        lower99_t = mean - (4.60*(std/(math.sqrt(size))))
        upper99_t = mean + (4.60*(std/(math.sqrt(size))))
        
        # Part A.5 Check confidence
        if lower99_t < u < upper99_t:
            norm99_t_succ += 1

    results = [norm99_succ,norm99_t_succ]
    return results


def main():
    sizes = [5,40,120]
    for size in sizes: 
        # run the experiments
        results95 = experiment95(size)
        results99 = experiment99(size)
        # get the percentages
        norm95 = results95[0]/10000
        stud95 = results95[1]/10000
        norm99 = results99[0]/10000
        stud99 = results99[1]/10000
        print("95%% Size:%1d   Normal:%5.2f   Student's:%5.2f" %(size,norm95,stud95))
        print("99%% Size:%1d   Norma:%5.2f   Student's:%5.2f" %(size,norm99,stud99))

if __name__ == "__main__":
    main()