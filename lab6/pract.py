import numpy as np
import random 
import matplotlib.pyplot as plt
import math

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 2 - The Central Limit Theorem
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def problem2(nbooks):
    # Generate the values of the RV X
    N = 10000; a=1; b=4; #nbooks 1,5,10,15
    mu_x = (a+b)/2
    sig_x=np.sqrt((b-1)**2/12)
    X =np.zeros((N,1))
    for k in range(0,N):
        x=np.random.uniform(a,b,nbooks)
        w=np.sum(x)
        X[k] = w

    # Create bins and histogram
    nbins=30 #Number of bins
    edgecolor='w' # Color separating bars in bargraph
    bins=[float(x) for x in np.linspace(nbooks*a,nbooks*b,nbins+1)]
    h1,bin_edges = np.histogram(X,bins,density=True)
    # Define points on horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] #Width of bars in graph
    plt.close('all')

    # Plot the bar graph
    fig1=plt.figure(1)
    plt.bar(b1,h1,width=barwidth,edgecolor=edgecolor)

    # Plot the Gaussian Function
    def gaussian (mu,sig,z):
        f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
        return f

    f = gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
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

# Repeat for 1, 5, 10, and 15 books
problem2( 1)
problem2( 5)
problem2(10)
problem2(15)
