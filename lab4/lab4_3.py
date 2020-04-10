# Distrubution of the SUm of Exponential RVs
import numpy as np
import random 
import matplotlib.pyplot as plt
import math

# Generate the values of the RV x
beta = 40; N = 10000; a = 1; b = 2000

carton = [None]*24 # pre allocate array to hold 24 elements
all_cartons = []    # hold all the sum of the 24 elements

for k in range(N):
    # each one of 24 elements is exponentially distrubted random variable T
    carton = np.random.exponential(beta,24)
    # C = T1+T2+...T24
    C = sum(carton)
    all_cartons.append(C)

# Create bins and histogram
    nbins=30;       # Number of bins
    edgecolor='w'   # Color separating bars in the bargraph
    bins=[float(x) for x in np.linspace(a, b, nbins+1)]
    h1, bin_edges = np.histogram(all_cartons,bins,density=True)

# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges) - 1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1+be2)/2
barwidth = b1[1] - b1[0] #Width of bars in the bargraph
plt.close('all')

# Plot the Bar Graph
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

# Plot the Normal PDF
def NormPDF(mu,sigma,x):
    f=((1/(sigma*math.sqrt(2*math.pi)))*(np.exp((-1*((x-mu)**2))/(2*(sigma**2)))*np.ones(np.size(x))))
    return f

# Calculate the mean and std
mu_x = 24 * beta
sig_x = math.sqrt(24) * beta

f = NormPDF(mu_x, sig_x, b1)
plt.plot(b1,f,'r')
plt.title('Normal Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')
plt.show()

# Create a new figure for CDF plot
fig2=plt.figure(2)

# Plot the CDF
def plotCDF(mu,sigma,carton,b1):
    fnorm = NormPDF(mu,sigma,b1)
    fcdf = np.cumsum(barwidth * f)
    return fcdf

h1 = np.cumsum(h1*barwidth)
f = plotCDF(mu_x,sig_x,carton,b1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
plt.plot(b1,f,'r')
plt.title('Normal Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')
plt.show()


