import numpy as np
import random 
import matplotlib.pyplot as plt
import math

a=1; b= 2000; beta = 40; N = 10000

n=24
carton = []
cartonSums = []

for i in range(N):
    carton = np.random.exponential(beta, n)

    C = (sum(carton)) # b = sum(a)
    cartonSums.append(C)


# Calculate average and standard deviation
mu_c = 24 * beta
sig_c = beta * math.sqrt(24)

# Create bins and histogram
nbins=30; # Number of bins
edgecolor='w'; # Color separating bars in the bargraph
#
bins=[float(carton) for carton in np.linspace(a, b,nbins+1)] # ISSUE: Should I have a and b for this problem?
h1, bin_edges = np.histogram(cartonSums,nbins,density=True) # HAD TO ADD cartonSums as a paremeter

# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] # Width of bars in the bargraphz
plt.close('all')

# Plot bar graph
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

def NormPDF(mu, sigma,x):
    f=((1/(sigma*math.sqrt(2*math.pi))*np.exp((-1*((x-mu)**2))/(2*(sigma**2)))*np.ones(np.size(x))))
    return f

# Plot PDF
f = NormPDF(mu_c, sig_c, b1)
plt.plot(b1,f,'r')
plt.title("PDF of Exponential RV's")
plt.xlabel('Lifetime of a battery in days - T')
plt.ylabel('PDF')
plt.show()

# Plot bar graph
fig2=plt.figure(2)

def CDF(carton, mu, sigma, x):
    PDFResult = NormPDF(mu, sigma, x)
    CDF = np.cumsum(barwidth * PDFResult)
    return CDF

h1 = np.cumsum(h1 * barwidth)
f = CDF(carton, mu_c, sig_c, b1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
plt.plot(b1, f, 'r')
plt.title("CDF of the Sum of Exponential RV's")
plt.xlabel('Cumulative sums of a battery lifetime in days - T')
plt.ylabel('CDF')
plt.show()
