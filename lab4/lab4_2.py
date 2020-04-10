# The Central Limit Theorem

import numpy as np
import random 
import matplotlib.pyplot as plt


# Plot the Gaussian Function
def gaussian(mu,sig,z):
    f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f

def CentralLim(nbooks): 
    # Generate the values of the RV x
    N = 100000; a = 1.0; b = 4.0; 
    mu_x = (a+b)/2; sig_x=np.sqrt((b-a)**2/12)
    X = np.zeros((N,1))
    for k in range (0,N):
        x=np.random.uniform(a,b,nbooks)
        w=np.sum(x)
        X[k]=w

    # Create bins and historgram
    nbins=30;       # Number of bins
    edgecolor='w'   # Color separating bars in the bargraph
    bins=[float(x) for x in np.linspace(nbooks*a, nbooks*b, nbins+1)]
    h1, bin_edges = np.histogram(X,bins,density=True)
    # Define poits on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2

    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    # Plot the Bar Graph
    fig1=plt.figure(1)
    plt.bar(b1,h1,width=barwidth,edgecolor=edgecolor)

    f=gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
    plt.plot(b1,f,'r')
    plt.title('Gaussian Distribution: Books={}'.format(nbooks))
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.show()

    # Calculate mean and standard deviation
    mu_x=(a+b)/2 * nbooks
    sig_x=np.sqrt((b-a)**2/12) * np.sqrt(nbooks)

    print("Calculations for {} books".format(nbooks))
    print("Median: " + str(mu_x))
    print("Standard Deviation: " + str(sig_x))
    print("")


def main():

    n = (1,5,15); 

    CentralLim(1)

if __name__== "__main__":
    main()